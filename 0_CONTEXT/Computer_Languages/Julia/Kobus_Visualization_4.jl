# https://learnableloop.com/posts/FFGViz4_KE.html
using InteractiveUtils
versioninfo() ## Julia version

import Pkg; Pkg.instantiate(); Pkg.activate()
Pkg.add(Pkg.PackageSpec(;name="RxInfer", version="3.5.1"))
Pkg.add(Pkg.PackageSpec(;name="MetaGraphsNext", version="0.7.0"))
Pkg.add(Pkg.PackageSpec(;name="GraphPlot", version="0.5.2"))
using RxInfer, MetaGraphsNext

using GraphPlot
Pkg.status()

"""
Takes the tikz string given by generate_tikz() and 
writes it to a .tex file to produce a TikZ visualisation. 
"""
function show_tikz(tikz_code_graph::String)
    ## eval(Meta.parse(dot_code_graph)) ## for GraphViz

    ## see problem in ^v1 under TikzPictures section 
    ## tikz_picture = TikzPicture(tikz_code_graph)
    ## return tikz_picture
    file_path = "myoutput.tex" ## write to file rather than show in notebook
    open(file_path, "w") do file
        write(file, tikz_code_graph)
    end
end


show_tikz


"""
Given a unsanitized string, provides a sanitized equivalent.
"""
function sanitized(vertex::String)
    if haskey(_san_node_ids, vertex)
        return _san_node_ids[vertex]
    else
        return vertex
    end
end

"""
Given a label string, provides its looked up latex value.
"""
function lup(label::String)
    if _lup_enabled
        lup_label = get(_lup_dict, label, replace(label, "_" => "\\_"))
    else
        return replace(label, "_" => "\\_")
    end
end
function print_meta_graph(meta_graph) ## just for info
    println("============== NODES ==============")
    for node in MetaGraphsNext.vertices(meta_graph)
        label = MetaGraphsNext.label_for(meta_graph, node)
        println("$node: $label")
    end
    println("\n============== LINKS ==============")
    for link in MetaGraphsNext.edges(meta_graph)
        source_node = MetaGraphsNext.label_for(meta_graph, link.src)
        dest_node = MetaGraphsNext.label_for(meta_graph, link.dst)
        println("$(source_node) -> $(dest_node)")
    end
end

function retain_can(s::String) ## retain canonical chars of a label string
    m = match(r"^[a-zA-Zγθs₀\*]*", s)
    return m.match
end
"""
Given a user specified canonical factor label string, 
returns all the GraphPPL associated labels from the context's factor_nodes.
"""
function str_facs(gppl_model, factor::String)
    context = GraphPPL.getcontext(gppl_model)
    vec = []
    for (factor_ID, factor_label) in pairs(context.factor_nodes)
        ## println("$(factor_ID), $(factor_label)")
        ## println("$(typeof(factor_ID)), $(typeof(factor_label))")
        node_data = gppl_model[factor_label]
        ## println("$(node_data.properties.fform)\n")
        if retain_can(string(node_data.properties.fform)) == factor
            append!(vec, factor_label)
        end
    end
    result = string.(vec)
    return result
end
"""
Given a user specified canonical variable label string, 
returns all the GraphPPL associated labels from the context's individual_variables.
"""
function str_individual_vars(gppl_model, var::String)
    context = GraphPPL.getcontext(gppl_model)
    vec = []
    for (node_ID, node_label) in pairs(context.individual_variables)
        ## println("$(node_ID), $(node_label)")
        ## println("$(typeof(node_ID)), $(typeof(node_label))")
        if occursin(var, string(node_ID))
            append!(vec, node_label)
        end
    end
    result = string.(vec)
    return result
end
"""
Given a user specified canonical variable label string, 
returns all the GraphPPL associated labels from the context's vector_variables.
"""
function str_vector_vars(gppl_model, var::String)
    context = GraphPPL.getcontext(gppl_model)
    vec = []
    for (node_ID, node_label) in pairs(context.vector_variables)
        ## println("$(node_ID), $(node_label)")
        ## println("$(typeof(node_ID)), $(typeof(node_label))")
        if string(node_ID) == var
            append!(vec, node_label)
        end
    end
    result = string.(vec)
    return result
end

"""
Given a GraphPPL model, provides a `kobus_graph` which also contains neighbours
for variable nodes (i.e. not only for factor nodes). It also contains some other
useful properties.
"""
function create_kobus_graph(gppl_model)
    kobus_graph = Dict{String, Dict{Symbol, Any}}()
    meta_graph = gppl_model.graph
    for (i,vertex) in enumerate(MetaGraphsNext.vertices(meta_graph))
        node_label = MetaGraphsNext.label_for(meta_graph, vertex)
        node_label_str = sanitized(string(node_label))
        println("$(i): $(node_label_str)")
        if !haskey(kobus_graph, node_label_str)
            kobus_graph[node_label_str] = Dict{Symbol, Any}()
            kobus_graph[node_label_str][:neighbours] = []  
            kobus_graph[node_label_str][:node_label] = node_label

            node_code = code_for(meta_graph, node_label)
            kobus_graph[node_label_str][:node_code] = node_code

            node_lup = lup(node_label_str)
            kobus_graph[node_label_str][:node_lup] = node_lup

            node_global_counter = node_label.global_counter
            kobus_graph[node_label_str][:node_global_counter] = node_global_counter

            node_data = gppl_model[node_label] ## GraphPPL.NodeData
            kobus_graph[node_label_str][:node_data] = node_data

            properties = node_data.properties ## GraphPPL.Factor|VariableNodeProperties
            ##
            # kobus_graph[node_label_str][:properties] = Dict{Symbol, Any}()
            # for prop in properties
            #     value = getproperty(properties, prop)
            #     # println("field: $(field), value: $(value)")
            #     kobus_graph[node_label_str][:properties][prop] = value
            # end
            kobus_graph[node_label_str][:properties] = properties

            fields = fieldnames(typeof(properties)) ## Tuple{Symbol, Symbol}
            kobus_graph[node_label_str][:fields] = Dict{Symbol, Any}()
            for field in fields
                value = getfield(properties, field)
                kobus_graph[node_label_str][:fields][field] = value
            end
        end
    end
    ## populate the :neighbours key
    for (i,edge) in enumerate(MetaGraphsNext.edges(meta_graph))
        src_node = MetaGraphsNext.label_for(meta_graph, edge.src)
        dst_node = MetaGraphsNext.label_for(meta_graph, edge.dst)
        san_src_node = sanitized(string(src_node)); #println(typeof(san_src_node))
        san_dst_node = sanitized(string(dst_node))
        ## println("$(i): $(san_src_node) -- $(san_dst_node)")
        push!(kobus_graph[san_src_node][:neighbours], san_dst_node)
        push!(kobus_graph[san_dst_node][:neighbours], san_src_node)
    end
    return kobus_graph
end
"""
Given a user name of a variable node, provides the `inifac` node connected to it.
"""
function find_inifac_node(kobus_graph, out_neighbor_uname, gppl_model)
    inifac_out_neighbor_str = str_individual_vars(gppl_model, out_neighbor_uname)[1]
    var_neighbours = kobus_graph[inifac_out_neighbor_str][:neighbours]
    for i in 1:length(var_neighbours)
        neighbors = kobus_graph[var_neighbours[i]][:properties].neighbors
        println("    var_neighbours[$(i)]: $(var_neighbours[i])")
        in_neighbor_label = neighbors[2][1]; println("        in_neighbor_label: $(in_neighbor_label)")
        out_neighbor_label = neighbors[1][1]; println("        out_neighbor_label: $(out_neighbor_label)")
        if string(out_neighbor_label)==inifac_out_neighbor_str
            println("inifac_out_neighbor_str: $(inifac_out_neighbor_str)")
            println("inifac_str: $(var_neighbours[i])")
            return var_neighbours[i]
        end
    end
end
"""
Given a user name of a `sysvar` variable node, provides the `cntrl` nodes connected to it.
"""
function find_cntrl_nodes(kobus_graph, uname, gppl_model)
    cntrl_var_label_strs = str_vector_vars(gppl_model, uname)
    println("cntrl_var_label_strs: $(cntrl_var_label_strs)")
    sysvars = Vector{String}()
    facs = Vector{String}()
    parvars = Vector{Vector{String}}()
    for i in 1:length(cntrl_var_label_strs)
        var_neighbours = kobus_graph[cntrl_var_label_strs[i]][:neighbours]
        println("cntrl_var_label_strs[i]: $(cntrl_var_label_strs[i])")
        for j in 1:length(var_neighbours)
            neighbors = kobus_graph[var_neighbours[j]][:properties].neighbors
            println("    var_neighbours[j]: $(var_neighbours[j])")
            in_neighbor_label = neighbors[2][1]
            println("        in_neighbor_label: $(in_neighbor_label)")
            out_neighbor_label = neighbors[1][1]
            println("        out_neighbor_label: $(out_neighbor_label)")
            if (string(out_neighbor_label) in cntrl_var_label_strs)
                push!(facs, var_neighbours[j])
                push!(sysvars, cntrl_var_label_strs[i])
                parvar_nodes = find_parvar_nodes(kobus_graph, var_neighbours[j], gppl_model)
                append!(parvars, [parvar_nodes])
            end
        end
    end
    return sysvars, facs, parvars
end
"""
Given a `inifac` label string, provides the `iniparvar` nodes connected to it.
"""
function find_iniparvar_nodes(kobus_graph, inifac_label_str, gppl_model)
    neighbors = kobus_graph[inifac_label_str][:properties].neighbors
    println("neighbors: $(neighbors)")
    out_var = string(neighbors[1][1]); println("        out_var: $(out_var)")
    iniparvars = Vector{String}()
    for i in 2:length(neighbors)
        push!(iniparvars, string(neighbors[i][1]))
    end    
    return out_var, iniparvars
end
"""
Given a `fac` label string, provides the `parvar` nodes connected to it.
"""
function find_parvar_nodes(kobus_graph, fac_label_str, gppl_model)
    state_var_label_strs = str_vector_vars(gppl_model, "s")
    neighbors = kobus_graph[fac_label_str][:properties].neighbors
    println("neighbors: $(neighbors)")
    parvars = Vector{String}()
    for i in 2:length(neighbors)
        in_neighbor_label = neighbors[i][1]
        if !(string(in_neighbor_label) in state_var_label_strs)
            push!(parvars, string(in_neighbor_label))
        end
    end    
    return parvars
end
"""
Given a `fac` label string, provides the next variable in the `state0` sequence.
"""
function next_var(kobus_graph, fac_label_str)
    neighbors = kobus_graph[fac_label_str][:properties].neighbors
    var = neighbors[1]
    println("var: $(var)")
    var_label = var[1]
    println("=== NEXT var node is: $(var_label)")
    return var_label
end
"""
Given a `var` label, provides the next factor in the `state0` sequence.
"""
function next_fac(kobus_graph, var_label, state_var_label_strs, gppl_model)
    println("var_label: $(var_label)")
    try
        var_index = gppl_model[var_label].properties.index
    catch
        var_index = 0
        println("Exception: Setting var_index to 0")
    end
    if var_index == nothing var_index = 0 end ## for s_0  
    println("var_index: $(var_index)")
    var_neighbours = kobus_graph[string(var_label)][:neighbours]
    println("var_neighbours: $(var_neighbours)")
    for i in 1:length(var_neighbours)
        neighbors = kobus_graph[var_neighbours[i]][:properties].neighbors
        println("    var_neighbours[$(i)]: $(var_neighbours[i])")
        ## in_neighbor is this var node && out_neighbor is the next s 
        in_neighbor_label = neighbors[2][1]; println("        in_neighbor_label: $(in_neighbor_label)")
        out_neighbor_label = neighbors[1][1]; println("        out_neighbor_label: $(out_neighbor_label)")
        if in_neighbor_label==var_label
            if var_index+1 <= length(state_var_label_strs)
                if string(out_neighbor_label)==state_var_label_strs[var_index + 1]
                    fac_label_str = var_neighbours[i]
                    println("        === NEXT fac node is: $(fac_label_str)")
                    return fac_label_str
                elseif length(var_neighbours) == 2
                    println("        Take this var_label as next fac because we ONLY have 2 var_neighbours")
                    fac_label_str = var_neighbours[i]
                    println("        === NEXT fac node is: $(fac_label_str)")
                    return fac_label_str
                end
            else
                return "END"
            end
        end
    end
end
"""
Given a `inifac` label string, provides the `state0` nodes.
"""
function find_state0_nodes(kobus_graph, inifac_label_str, gppl_model)
    state_var_label_strs = str_vector_vars(gppl_model, "s")
    vars = Vector{String}() ## may contain non-sysvars too
    facs = Vector{String}()
    node_lab_strs = [inifac_label_str]
    fac_str = node_lab_strs[1]
    while fac_str != "END"
        var = next_var(kobus_graph, fac_str)
        push!(node_lab_strs, string(var))
        push!(vars, string(var))
        fac_str = next_fac(kobus_graph, var, state_var_label_strs, gppl_model)
        if fac_str == "END" || fac_str == nothing
            return node_lab_strs, vars, facs
        else
            push!(node_lab_strs, fac_str)
            push!(facs, fac_str)
        end
    end
end
"""
Given a user name, provides the `obser` nodes.
"""
function find_obser_nodes(kobus_graph, uname, gppl_model)
    obser_var_label_strs = str_vector_vars(gppl_model, uname)
    state_var_label_strs = str_vector_vars(gppl_model, "s")
    println("obser_var_label_strs: $(obser_var_label_strs)")
    sysvars = Vector{String}()
    facs = Vector{String}()
    parvars = Vector{Vector{String}}()
    for i in 1:length(obser_var_label_strs)
        var_neighbours = kobus_graph[obser_var_label_strs[i]][:neighbours]
        println("obser_var_label_strs[i]: $(obser_var_label_strs[i])")
        for j in 1:length(var_neighbours)
            neighbors = kobus_graph[var_neighbours[j]][:properties].neighbors
            println("    var_neighbours[j]: $(var_neighbours[j])")
            in_neighbor_label = neighbors[2][1]
            println("        in_neighbor_label: $(in_neighbor_label)")
            out_neighbor_label = neighbors[1][1]
            println("        out_neighbor_label: $(out_neighbor_label)")
            if length(state_var_label_strs) > 0
                if (string(out_neighbor_label) in obser_var_label_strs) && (string(in_neighbor_label) in state_var_label_strs)
                    push!(facs, var_neighbours[j])
                    push!(sysvars, obser_var_label_strs[i])
                    parvar_nodes = find_parvar_nodes(kobus_graph, var_neighbours[j], gppl_model)
                    append!(parvars, [parvar_nodes])
                end
            elseif isempty(state_var_label_strs) ## no state vars avail
                if string(out_neighbor_label) in obser_var_label_strs
                    push!(facs, var_neighbours[j])
                    push!(sysvars, obser_var_label_strs[i])
                    parvar_nodes = find_parvar_nodes(kobus_graph, var_neighbours[j], gppl_model)
                    append!(parvars, [parvar_nodes])
                end
            else
                println("find_obser_nodes(): UNHANDLED CASE")
            end
        end
    end
    return sysvars, facs, parvars
end
"""
Given a user name, provides the `prefr` nodes.
"""
function find_prefr_nodes(kobus_graph, uname, gppl_model)
    obser_var_label_strs = str_vector_vars(gppl_model, uname)
    state_var_label_strs = str_vector_vars(gppl_model, "s")
    println("obser_var_label_strs: $(obser_var_label_strs)")
    facs = Vector{String}()
    parvars = Vector{Vector{String}}()
    for i in 1:length(obser_var_label_strs)
        var_neighbours = kobus_graph[obser_var_label_strs[i]][:neighbours]
        println("obser_var_label_strs[i]: $(obser_var_label_strs[i])")
        for j in 1:length(var_neighbours)
            neighbors = kobus_graph[var_neighbours[j]][:properties].neighbors
            println("    var_neighbours[j]: $(var_neighbours[j])")
            in_neighbor_label = neighbors[2][1]
            println("        in_neighbor_label: $(in_neighbor_label)")
            out_neighbor_label = neighbors[1][1]
            println("        out_neighbor_label: $(out_neighbor_label)")
            if (string(out_neighbor_label) in obser_var_label_strs) && !(string(in_neighbor_label) in state_var_label_strs)
                push!(facs, var_neighbours[j])
                parvar_nodes = find_parvar_nodes(kobus_graph, var_neighbours[j], gppl_model)
                append!(parvars, [parvar_nodes])
            end
        end
    end
    return facs, parvars
end


"""
Provides equal spaces to be used on the sides of factor nodes.
"""
function spaces(n::Int)
    d = 1/(n + 1)
    return [i*d for i in 1:n]
end
"""
Setup a table of equal spaces to be used on the sides of factor nodes. 
"""
function setup_divn(n)
    divn = Dict()
    for i in 1:n
        divn[i] = spaces(i)
    end
    return divn
end
"""
Calculate the arc radius to be used for `CFFG`s
"""
function radius(constrained::Bool)
    if constrained
        return "\\ar" ## arc radius of a fac node
    else
        return "\\nr" ## node radius of a fac node
    end
end

_ytop = 30 #18 ## grid y-value at the top of picture
_show_grid = false ## displays a grid with the FFG if true
_node_size = "10mm" #"15mm" ## the length of the sides of factor node boxes (in millimeters)
## _show_var_points = false ## draws the var circles if true

_xsep = 2
# _xsep = 2.5

_tsep = 6*_xsep
# _tsep = 7*_xsep
# _tsep = 7.5*_xsep
# _tsep = 8*_xsep
# _tsep = 9*_xsep

_ysep = 3

_divn = setup_divn(15)

function get_preamble_and_postamble(heading)
    iob = IOBuffer() ## preamble
    write(iob, "\\documentclass{standalone}\n")
    write(iob, "\\usepackage{tikz}\n")
    write(iob, "\\usetikzlibrary{calc}\n")    
    write(iob, "\\usepackage{amsmath}\n")
    write(iob, "\\usepackage{bm}\n") ## for BOLD calligraphic
    ## write(iob, "\\newcommand\\ns{10mm} %% define node (minimum) size\n")
    write(iob, "\\newcommand\\ns{$(_node_size)} %% define node (minimum) size\n")
    write(iob, "\\newcommand\\nr{.5*\\ns} %% define node radius\n")
    write(iob, "\\newcommand\\ar{.4*\\ns} %% define arc radius\n")
    write(iob, "\\newcommand\\br{.19*\\ns} %% define bead radius\n")
    write(iob, "\\DeclareUnicodeCharacter{03B8}{\\theta}\n")
    write(iob, "\\DeclareUnicodeCharacter{03B3}{\\gamma}\n")
    ## write(iob, "\\DeclareUnicodeCharacter{2080}{\\0}\n") ## theta_0
    write(iob, "\\DeclareUnicodeCharacter{209C}{\\0}\n") ## for sₜ₋₁_1: does not work
    write(iob, "\\DeclareUnicodeCharacter{208B}{\\0}\n") ## 
    write(iob, "\\DeclareUnicodeCharacter{2081}{\\0}\n") ## 
    write(iob, "\\begin{document}\n")
    write(iob, "\\begin{tikzpicture}[\n")
    write(iob, "    scale=1, \n")
    write(iob, "    draw=black, \n")
    write(iob, "    fac/.style={rectangle, draw=black!100, fill=black!0, minimum size=\\ns, inner sep=0pt},\n")
    write(iob, "    dlt/.style={rectangle, draw=black!100, fill=black!100, minimum size=.2*\\ns},\n")
    write(iob, "    var/.style={circle, draw=gray!100, fill=gray!100, minimum size=1mm, inner sep=0pt},\n")
    write(iob, "    bus/.style={rectangle, draw=black!100, fill=black!100, minimum width=30mm, minimum height=.5mm, inner sep=0pt},\n")
    write(iob, "    eql/.style={rectangle, draw=black!100, fill=black!0, minimum size=.5*\\ns},\n")
    ## write(iob, "    text=gray,\n")
    write(iob, "    text=black,\n")
    write(iob, "    ]\n")
    write(iob, "\\node[font=\\Large] at (4,$(_ytop-1)) {\\textbf{$(heading)}};\n")
    if _show_grid write(iob, "\\draw[lightgray] (0,0) grid ($(_ytop), $(_ytop));\n") end
    preamble = String(take!(iob))
    print(preamble)
    println("⋮"); println("⋮"); println("⋮") ## [\]vdots[tab]

    iob = IOBuffer() ## postamble
    ## Adjust bounding box. Must be here, i.e. after the drawing
    write(iob, "\\path[use as bounding box] ([xshift=-1cm, yshift=-1cm]current bounding box.south west) rectangle ([xshift=1cm, yshift=2cm]current bounding box.north east);\n")
    write(iob, "\\end{tikzpicture}\n")
    write(iob, "\\end{document}\n")
    postamble = String(take!(iob))
    print(postamble)

    return preamble, postamble
end

"""
Given the name of a layer, draws the nodes in that layer. Used for all layers
containing system variables (`sysvar`s). These are typically:
`cntrl`, `stateM4`, `stateM3`, `stateM2`, `stateM1`, `stateP1`, `stateP2`, `obser`, `prefr`
"""
function draw_sysvar_layer(layers2, name, divn, y, iob)
    anchor = layers2[name].anchor
    y_cntrl = y
    facs = layers2[name].facs
    for k in 1:length(facs)
        if length(facs[k]) > 0
            x = anchor + (k-1)*_xsep ##anchor for this fac_grp
            for (i,v) in enumerate(facs[k]) ##for each fac in this fac_grp
                write(iob, "\\node($(v))[fac] at ($(x), $(y)) {\$$(lup(v))\$};\n")
                if _CFFG
                    ## write(iob, "\\draw ($(v))++(\\ar,0mm) arc[start angle=0, end angle=180, radius=\\ar];\n") ##TOP
                    ## write(iob, "\\draw ($(v))++(\\ar,0mm) arc[start angle=0, end angle=-180, radius=\\ar];\n") ##BOTTOM
                    write(iob, "\\draw ($(v))++(\\ar,0mm) arc[start angle=0, end angle=-180, radius=\\ar];\n") ##BOTTOM
                end
                x += _tsep ##move to next t
            end
        end
    end
    parvars = layers2[name].parvars
    if length(parvars) > 0
        for k in 1:length(parvars)
            if length(parvars[k]) > 0
                for (i,v) in enumerate(parvars[k])
                    for (j, w) in enumerate(v)
                        write(iob, "\\node($(w))[var] at (\$ ($(facs[k][i]).south west) + (-.5*\\ns, $(divn[length(v)][j])*\\ns) \$) {};\n")
                        write(iob, "\\node[above] at ($(w)) {\$$(lup(w))\$};\n") ## label
                        if _deltas_enabled write(iob, "\\node($(w))[dlt] at (\$ ($(w).center) + (-.4*\\ns, 0) \$) {};\n") end
                    end
                end
            end
        end
    end
    x = anchor
    sysvars = layers2[name].sysvars
    for (i,v) in enumerate(sysvars)
        write(iob, "\\node($(v))[var] at ($(x), $(y-1.5)) {};\n")
        write(iob, "\\node[above right] at ($(v)) {\$$(lup(v))\$};\n") ## label
        ## write(iob, "\\node($(v))[dlt] at (\$ ($(obser_facs[i]).center) + (0, -2.0*\\ns) \$) {};\n")
        if _deltas_enabled write(iob, "\\node($(v))[dlt] at (\$ ($(v).center) + (0, -.4*\\ns) \$) {};\n") end
        x += _tsep
    end
end
"""
Given the name of a layer, draws the nodes in that layer. Used for all layers
containing parameter variables (`parvar`s). These are typically:
`paramB1`, `paramB2`, `paramA`
"""
function draw_param_layer(layers2, name, divn, y, iob)
    anchor = layers2[name].anchor
    y_paramB1 = y
    inifac = layers2[name].inifac
    if !isempty(inifac)
        x = anchor
        write(iob, "\\node($(inifac))[fac] at ($(x), $(y)) {\$$(lup(inifac))\$};\n")
    end
    iniparvars = layers2[name].iniparvars
    if length(iniparvars) > 0
        n = length(iniparvars)
        for (i,v) in enumerate(iniparvars)
            write(iob, "\\node($(v))[var] at (\$ ($(inifac).south west) + (-.5*\\ns, $(divn[n][i])*\\ns) \$) {};\n")
            write(iob, "\\node[above] at ($(v)) {\$$(lup(v))\$};\n") ## label
            if _deltas_enabled write(iob, "\\node($(v))[dlt] at (\$ ($(v).center) + (-.4*\\ns, 0) \$) {};\n") end
        end
    end
    parvar = layers2[name].parvar
    if !isempty(parvar)
        x = anchor + 1*_xsep
        write(iob, "\\node($(parvar))[eql] at ($(x), $(y)) {\$=\$};\n")
        write(iob, "\\node[xshift=.4*\\ns, yshift=.4*\\ns] at ($(parvar)) {\$$(lup(parvar))\$};\n") ## label
    end
end
"""
Given the name of a layer, draws the nodes in that layer. Used for the `state0` layer.
This is the layer containing factors (sometimes interleafed with variables) associated
with the state transition sequence.
"""
function draw_state_layer(layers2, name, divn, y, iob)
    anchor = layers2[name].anchor
    y_state0 = y
    inifac = layers2[name].inifac
    if !isempty(inifac)
        x = anchor - 2*_xsep
        write(iob, "\\node($(inifac))[fac] at ($(x), $(y)) {\$$(lup(inifac))\$};\n")
    end
    iniparvars = layers2[name].iniparvars
    if length(iniparvars) > 0
        n = length(iniparvars)
        for (i,v) in enumerate(iniparvars)
            write(iob, "\\node($(v))[var] at (\$ ($(inifac).south west) + (-.5*\\ns, $(divn[n][i])*\\ns) \$) {};\n")
            write(iob, "\\node[above] at ($(v)) {\$$(lup(v))\$};\n") ## label
            if _deltas_enabled write(iob, "\\node($(v))[dlt] at (\$ ($(v).center) + (-.4*\\ns, 0) \$) {};\n") end
        end
    end
    sysvars = layers2[name].sysvars
    if length(sysvars) > 0
        x = anchor - 1*_xsep;
        write(iob, "\\node($(sysvars[1]))[var] at ($(x), $(y)) {};\n")
        write(iob, "\\node[above] at ($(sysvars[1])) {\$$(lup(sysvars[1]))\$};\n") ## label
        x += _tsep
        for (i,v) in enumerate(sysvars[2:end])
            if i < length(sysvars) - 1
                write(iob, "\\node($(v))[eql] at ($(x), $(y)) {\$=\$};\n")
                write(iob, "\\node[xshift=.4*\\ns, yshift=.4*\\ns] at ($(v)) {\$$(lup(v))\$};\n") ## label
            else
                write(iob, "\\node($(v))[var] at ($(x), $(y)) {};\n")
                write(iob, "\\node[above] at ($(v)) {\$$(lup(v))\$};\n") ## label
            end
            x += _tsep
        end
    end
    facs = layers2[name].facs
    for k in 1:length(facs)
        if length(facs[k]) > 0
            x = anchor + (k-1)*_xsep
            for (i,v) in enumerate(facs[k])
                if k % 2  == 1 ## for facs
                    write(iob, "\\node($(v))[fac] at ($(x), $(y)) {\$$(lup(v))\$};\n")
                    if _CFFG
                        ## write(iob, "\\draw ($(v))++(\\ar,0mm) arc[start angle=0, end angle=180, radius=\\ar];\n") ##TOP
                        write(iob, "\\draw ($(v))++(\\ar,0mm) arc[start angle=0, end angle=-180, radius=\\ar];\n") ##BOTTOM
                    end
                else ## for vars
                    write(iob, "\\node($(v))[var] at ($(x), $(y)) {};\n")
                    write(iob, "\\node[above] at ($(v)) {\$$(lup(v))\$};\n") ## label    
                end
                x += _tsep
            end
        end
    end
    ## to have parvars in state layer at north, this needs to be adjusted
    parvars = layers2[name].parvars
    if length(parvars) > 0
        for k in 1:length(parvars)
            if length(parvars[k]) > 0
                for (i,v) in enumerate(parvars[k])
                    for (j, w) in enumerate(v)
                        write(iob, "\\node($(w))[var] at (\$ ($(facs[k][i]).south west) + (-.5*\\ns, $(divn[length(v)][j])*\\ns) \$) {};\n")
                        write(iob, "\\node[above] at ($(w)) {\$$(lup(w))\$};\n") ## label
                        if _deltas_enabled write(iob, "\\node($(w))[dlt] at (\$ ($(w).center) + (-.4*\\ns, 0) \$) {};\n") end
                    end
                end
            end
        end
    end
end

"""
Given the name of a layer, draws the links for that layer. Links are usually:
    from `iniparvar`s or `parvars` (parameter variable nodes) to `fac`s (factor nodes)
    from the `sysvar`s (system variable nodes) to the linked `fac`s (factor nodes) 
        in the layer below
Used for all layers containing system variables (`sysvar`s). These are typically:
`cntrl`, `stateM4`, `stateM3`, `stateM2`, `stateM1`, `stateP1`, `stateP2`, `obser`, `prefr`
"""
function draw_sysvar_links(layers2, name, divn, y, iob) ## for cntrl & obser
    parvars = layers2[name].parvars
    if length(parvars) > 0
        for k in 1:length(parvars)
            if length(parvars[k]) > 0
                facs = layers2[name].facs
                for (i,v) in enumerate(parvars[k])
                    for (j, w) in enumerate(v)
                        ## write(iob, "\\draw ($(w)) -- ([shift={(0, $(divn[length(v)][j])*\\ns)}]$(facs[1][i]).south west);\n")
                        ## can also have CFFG when using .center:
                        write(iob, "\\draw ($(w)) -- ([shift={(-$(radius(_CFFG)), ($(divn[length(v)][j])-.5)*\\ns)}]$(facs[1][i]).center);\n")
                    end
                end
            end
        end
    end
    sysvars = layers2[name].sysvars
    facs = layers2[name].facs
    for (i,v) in enumerate(sysvars)
        write(iob, "\\draw ($(facs[1][i])) -- ($(sysvars[i]));\n")
    end
    link_facs = layers2[name].links
    if link_facs !== nothing
        for (i,v) in enumerate(link_facs[1])
            write(iob, "\\draw ($(sysvars[i])) -- ($(v));\n") ## ignore s_0
            # write(iob, "\\draw ($(sysvars[i+1][1])) -- ($(v));\n") ## ignore s_0
            # write(iob, "\\draw ($(sysvars[2][i])) -- ($(v));\n") ## ignore s_0
        end
    end
end

"""
Given the name of a layer, draws the links for that layer. Links are usually:
    from `iniparvar`s or `parvars` (parameter variable nodes) to `fac`s (factor nodes)
    from the `parvar` (parameter variable node) to the linked `fac`s (factor nodes)
Used for all layers containing parameter variables (`parvar`s). These are typically:
`paramB1`, `paramB2`, `paramA`
"""
function draw_param_links(layers2, name, divn, y, iob)
    iniparvars = layers2[name].iniparvars
    n = length(iniparvars)
    inifac = layers2[name].inifac
    for (i,v) in enumerate(iniparvars)
        ## write(iob, "\\draw[blue, line width=3pt] ($(v)) -- ([shift={(0, $(divn[length(iniparamA_vars)][i]))}]$(iniparamA_fac).south west);\n")
        write(iob, "\\draw ($(v)) -- ([shift={(0, $(divn[n][i])*\\ns)}]$(inifac).south west);\n")
    end  
    parvar = layers2[name].parvar
    write(iob, "\\draw ($(inifac)) -| ($(parvar));\n")
    linked_facs = layers2[name].links
    parvar = layers2[name].parvar
    link_fac_side = layers2[name].link_fac_side
    link_fac_offset = layers2[name].link_fac_offset
    for k in 1:length(linked_facs)
        if length(linked_facs[k]) > 0
            if link_fac_side == "west"
                for i in linked_facs[k]
                    write(iob, "\\draw ($(parvar)) -| ([shift={(-\\nr,0)}]$(i).west) -- ([shift={(-$(radius(_CFFG)),0)}]$(i).center);\n")
                    ## write(iob, "\\draw ($(parvar)) -| ([shift={(-.5*\\ns,0)}]$(i).west) -- ([shift={(-$(radius(_CFFG)),$(link_fac_offset))}]$(i).center);\n")
                end
            elseif link_fac_side == "north"
                for i in linked_facs[k]
                    write(iob, "\\draw ($(parvar)) -| ([shift={(-$(link_fac_offset)*\\ns, 0)}]$(i).north east);\n")
                end
            else
                println("ERROR: Invalid link_fac_side $link_fac_side")
            end
        end
    end
end
"""
Given the name of a layer, draws the links for that layer. Links are usually:
    from `iniparvar`s or `parvars` (parameter variable nodes) to `fac`s (factor nodes)
    from each `fac`/`var` to the next one in the `state0`` sequence.
Used for the `state0` layer. This is the layer containing factors (sometimes interleafed with variables) associated
with the state transition sequence.
"""
function draw_state_links(layers2, name, divn, y, iob)
    inifac = facs = layers2[name].inifac
    sysvars = layers2[name].sysvars
    facs = layers2[name].facs
    if !isempty(inifac)
        iniparvars = layers2[name].iniparvars
        n = length(iniparvars)
        for (i,v) in enumerate(iniparvars)
            write(iob, "\\draw ($(v)) -- ([shift={(0, $(divn[n][i])*\\ns)}]$(inifac).south west);\n")
        end
        write(iob, "\\draw ($(inifac)) -| ($(sysvars[1]));\n")
    end
    if length(sysvars) > 0
        for k in 1:length(facs[1]) ## for each column
            seq = [row[k] for row in facs] ## seq k, col k
            println("seq: $seq")
            if length(seq) > 1
                ## println("\\draw ($(sysvars[k])) -- ([shift={(-$(radius(_CFFG)),0)}]$(seq[1]).center);\n")
                write(iob, "\\draw ($(sysvars[k])) -- ([shift={(-$(radius(_CFFG)),0)}]$(seq[1]).center);\n")
                for i in 1:length(seq) - 1
                    ## if i % 2  == 1 ## for facs
                        ## write(iob, "\\draw ($(seq[i])) -- ($(seq[i+1]));\n")
                    ## else ## for vars
                        ## println("\\draw ([shift={($(radius(_CFFG)),0)}]$(seq[i]).center) -- ([shift={(-$(radius(_CFFG)),0)}]$(seq[i+1]).center);\n")
                        write(iob, "\\draw ([shift={($(radius(_CFFG)),0)}]$(seq[i]).center) -- ([shift={(-$(radius(_CFFG)),0)}]$(seq[i+1]).center);\n")
                        ## write(iob, "\\draw ($(seq[i])) -- ($(seq[i+1]));\n")
                    ## end
                end
                ## println("\\draw ([shift={($(radius(_CFFG)),0)}]$(fac_seq[end]).center) -- ([shift={(-$(radius(_CFFG)),0)}]$(sysvars[k+1]).center);\n")
                write(iob, "\\draw ([shift={($(radius(_CFFG)),0)}]$(seq[end]).center) -- ($(sysvars[k+1]));\n")
                ## write(iob, "\\draw ($(seq[end])) -- ($(sysvars[k+1]));\n")
            else
                println("... doing the else ...")
                for (i,v) in enumerate(facs[1])
                    ## println("\\draw ([shift={($(radius(_CFFG)),0)}]$(v).center) -- ($(sysvars[i+1]).west);\n")
                    write(iob, "\\draw ([shift={($(radius(_CFFG)),0)}]$(v).center) -- ($(sysvars[i+1]).west);\n")
                    ## write(iob, "\\draw ($(v)) -- ($(sysvars[i+1]).west);\n")
                end
                for (i,v) in enumerate(facs[1])
                    ## println("\\draw ([shift={(-$(radius(_CFFG)),0)}]$(v).center) -- ($(sysvars[i]).east);\n")
                    write(iob, "\\draw ([shift={(-$(radius(_CFFG)),0)}]$(v).center) -- ($(sysvars[i]).east);\n")
                    ## write(iob, "\\draw ($(v)) -- ($(sysvars[i]).east);\n")
                end
            end
        end
    end
    link_facs = layers2[name].links
    for (i,v) in enumerate(link_facs[1])
        write(iob, "\\draw ($(sysvars[i+1])) -- ($(v));\n") ## ignore s_0
    end
end

"""
Given a GraphPPL.Model and a definition of layers, generates the `tikz` code.
"""
function generate_tikz(;
heading::String,
Model::GraphPPL.Model,
layers2::Dict)    
    preamble, postamble = get_preamble_and_postamble(heading)
    tikz = preamble
    divn = setup_divn(15)
    iob = IOBuffer() ## graph
    ytop = _ytop
    y = ytop
    write(iob, "%% --------------------------- NODES ---------------------------\n")
    if haskey(layers2, "cntrl")
        y -= _ysep
        draw_sysvar_layer(layers2, "cntrl", divn, y, iob)
    end
    if haskey(layers2, "paramB1")
        y -= _ysep
        draw_param_layer(layers2, "paramB1", divn, y, iob)
    end
    if haskey(layers2, "paramB2")
        y -= _ysep
        draw_param_layer(layers2, "paramB2", divn, y, iob)
    end
    if haskey(layers2, "stateM4")
        y -= _ysep
        draw_sysvar_layer(layers2, "stateM4", divn, y, iob)
    end
    if haskey(layers2, "stateM3")
        y -= _ysep
        draw_sysvar_layer(layers2, "stateM3", divn, y, iob)
    end
    if haskey(layers2, "stateM2")
        y -= _ysep
        draw_sysvar_layer(layers2, "stateM2", divn, y, iob)
    end
    if haskey(layers2, "stateM1")
        y -= _ysep
        draw_sysvar_layer(layers2, "stateM1", divn, y, iob)
    end
    if haskey(layers2, "state0")
        y -= _ysep
        draw_state_layer(layers2, "state0", divn, y, iob)
    end
    if haskey(layers2, "stateP1")
        y -= _ysep
        draw_sysvar_layer(layers2, "stateP1", divn, y, iob)
    end
    if haskey(layers2, "stateP2")
        y -= _ysep
        draw_sysvar_layer(layers2, "stateP2", divn, y, iob)
    end
    if haskey(layers2, "obser")
        y -= _ysep
        draw_sysvar_layer(layers2, "obser", divn, y, iob)
    end
    if haskey(layers2, "prefr")
        y -= _ysep
        draw_sysvar_layer(layers2, "prefr", divn, y, iob)
    end
    if haskey(layers2, "paramA")
        y -= _ysep
        draw_param_layer(layers2, "paramA", divn, y, iob)
    end
    write(iob, "%% --------------------------- LINKS ---------------------------\n")
    y = ytop
    if haskey(layers2, "cntrl")
        draw_sysvar_links(layers2, "cntrl", divn, y, iob)
    end
    if haskey(layers2, "paramB1")
        draw_param_links(layers2, "paramB1", divn, y, iob)
    end
    if haskey(layers2, "paramB2")      
        y -= _ysep
        draw_param_links(layers2, "paramB2", divn, y, iob)
    end
    if haskey(layers2, "stateM4")
        draw_sysvar_links(layers2, "stateM4", divn, y, iob)
    end
    if haskey(layers2, "stateM3")
        draw_sysvar_links(layers2, "stateM3", divn, y, iob)
    end
    if haskey(layers2, "stateM2")
        draw_sysvar_links(layers2, "stateM2", divn, y, iob)
    end
    if haskey(layers2, "stateM1")
        draw_sysvar_links(layers2, "stateM1", divn, y, iob)
    end
    if haskey(layers2, "state0")
        draw_state_links(layers2, "state0", divn, y, iob)
    end
    if haskey(layers2, "stateP1")
        draw_sysvar_links(layers2, "stateP1", divn, y, iob)
    end
    if haskey(layers2, "stateP2")
        draw_sysvar_links(layers2, "stateP2", divn, y, iob)
    end
    if haskey(layers2, "obser")
        draw_sysvar_links(layers2, "obser", divn, y, iob)
    end
    if haskey(layers2, "prefr")
        draw_sysvar_links(layers2, "prefr", divn, y, iob)
    end
    if haskey(layers2, "paramA")
        draw_param_links(layers2, "paramA", divn, y, iob)
    end

    ## DRAW ALL RAW LINKS FOR REFERENCE
    if _raw_links_enabled
        meta_graph = Model.graph
        for edge in MetaGraphsNext.edges(meta_graph)
            source_vertex = MetaGraphsNext.label_for(meta_graph, edge.src)
            dest_vertex = MetaGraphsNext.label_for(meta_graph, edge.dst)
            write(iob, "\\draw[dotted, red, line width=1pt] ($(sanitized(string(source_vertex)))) -- ($(sanitized(string(dest_vertex))));\n")
        end
    end
    ## WRITE EQUAL NODES AGAIN
    if haskey(layers2, "paramB1")
        write(iob, "\\node($(layers2["paramB1"].parvar))[eql] at ($(layers2["paramB1"].parvar)) {\$=\$};\n")
    end
    if haskey(layers2, "paramB2")
        write(iob, "\\node($(layers2["paramB2"].parvar))[eql] at ($(layers2["paramB2"].parvar)) {\$=\$};\n")
    end
    if haskey(layers2, "paramA")
        write(iob, "\\node($(layers2["paramA"].parvar))[eql] at ($(layers2["paramA"].parvar)) {\$=\$};\n")
    end
    ## OVERLAY BEADS
    if _CFFG
        if haskey(layers2, "paramB1") write(iob, "\\draw ($(layers2["paramB1"].inifac).east) circle(\\br)[fill=white];\n") end
        if haskey(layers2, "paramB2") write(iob, "\\draw ($(layers2["paramB2"].inifac).east) circle(\\br)[fill=white];\n") end
        if haskey(layers2, "state0") write(iob, "\\draw ($(layers2["state0"].inifac).east) circle(\\br)[fill=white];\n") end
        if haskey(layers2, "paramA") write(iob, "\\draw ($(layers2["paramA"].inifac).east) circle(\\br)[fill=white];\n") end
        anchor = 8*_xsep
        obser_facs = layers2["obser"].facs
        for k in 1:length(obser_facs)
            if length(obser_facs[k]) > 0
                x = anchor + (k-1)*_xsep
                for (i,v) in enumerate(obser_facs[k])
                    if _CFFG
                        write(iob, "\\draw ($(v).north) circle(\\br)[fill=white];\n")
                        write(iob, "\\draw ($(v).south)++(-1*\\br,-1*\\br) rectangle([shift={(\\br,\\br)}]$(v).south)[fill=white];\n")
                    end
                    x += _tsep
                end
            end
        end
    end

    graph = String(take!(iob))
    tikz *= graph
    tikz *= postamble
    return tikz
end

Base.@kwdef mutable struct Layer
    name::String
    anchor::Float64
    iniparvars::Vector{String}
    inifac::String
    parvar::String
    sysvars::Vector{String}
    facs::Vector{Vector{String}}
    parvars::Vector{Vector{Vector{String}}}
    links = nothing
    link_fac_side = nothing
    link_fac_offset = nothing
end

# Coin Toss


@model function coin_model(y, a, b)
    ## We endow θ parameter of our model with some prior
    θ ~ Beta(a, b)

    ## We assume that outcome of each coin flip is governed by the Bernoulli distribution
    for i in eachindex(y)
        y[i] ~ Bernoulli(θ)
    end
end

coin_conditioned = coin_model(a = 2.0, b = 7.0) | (y = [ true, false, true ], )
coin_rxi_model = RxInfer.create_model(coin_conditioned)
coin_gppl_model = RxInfer.getmodel(coin_rxi_model)
coin_meta_graph = coin_gppl_model.graph

print_meta_graph(coin_meta_graph)

meta_graph = coin_meta_graph

## Shorten some labels to make graph more readable
# str_labels = [string(lab) for lab in labels(meta_graph)]
# replacements = 
#     Pair("MvNormalMeanCovariance", "Nmc"), 
#     Pair("MvNormalMeanPrecision", "Nmp"), 
#     Pair("constvar", "cv"),
#     Pair("x", "XXXXX") ## make more obvious
# short_labels = [replace(s, replacements...) for s in str_labels]

GraphPlot.gplot( ## existing plotting functionality
    meta_graph,
    layout=spring_layout,
    nodelabel=collect(labels(meta_graph)),
    ## nodelabel=short_labels,
    nodelabelsize=0.1,
    NODESIZE=0.02, ## diameter of the nodes
    NODELABELSIZE=1.5,
    # nodelabelc="white",
    nodelabelc="green",
    nodelabeldist=0.0,
    nodefillc=nothing, ## "cyan"
    edgestrokec="red",
    ## ImageSize = (800, 800) ##- does not work
)

_san_node_ids = Dict("dummy" => "dummy")
_lup_enabled = true
_lup_agc = false ## append global_counter values
_raw_links_enabled = false
_CFFG = true
_deltas_enabled = true
_tsep = 3*_xsep
_lup_dict = Dict{String, String}(
    "constvar_2_3" => _lup_agc ? "a\\_2\\_3" : "a",
    "constvar_4_5" => _lup_agc ? "b\\_4\\_5" : "b",
    "Beta_6" => _lup_agc ? "\\mathcal{B}eta\\_6" : "\\mathcal{B}eta",
    "Bernoulli_8" => _lup_agc ? "\\mathcal{B}er\\_6" : "\\mathcal{B}er",
    "Bernoulli_10" => _lup_agc ? "\\mathcal{B}er\\_10" : "\\mathcal{B}er",
    "Bernoulli_12" => _lup_agc ? "\\mathcal{B}er\\_12" : "\\mathcal{B}er",
    "θ_1" => _lup_agc ? "\\theta\\_1" : "\\theta",
    "y_7" => _lup_agc ? "y_1\\_7" : "y_1",
    "y_9" => _lup_agc ? "y_2\\_9" : "y_2",
    "y_11" => _lup_agc ? "y_3\\_11" : "y_3",
);
coin_kobus_graph = create_kobus_graph(coin_gppl_model)

layers2 = Dict()
kobus_graph = coin_kobus_graph
gppl_model = coin_gppl_model

obser_sysvars, obser_facs, obser_parvars = find_obser_nodes(kobus_graph, "y", gppl_model)
layers2["obser"] = Layer(
    name="obser",
    anchor=3*_xsep,
    iniparvars = [],
    inifac = "",
    parvar="",
    ## sysvars = ["y_7", "y_9", "y_11"],
    ## sysvars = str_vector_vars(gppl_model, "y"),
    sysvars = obser_sysvars,
    ## facs = [["Bernoulli_8", "Bernoulli_10", "Bernoulli_12"]],
    ## facs = [str_facs(gppl_model, "Bernoulli")],
    facs = [obser_facs],
    parvars = []
    ## parvars = [obser_parvars]
    )

## paramA_inifac = str_facs(gppl_model, "Beta")[1]
paramA_inifac = find_inifac_node(kobus_graph, "θ", gppl_model)
paramA_out_var, paramA_iniparvars = find_iniparvar_nodes(kobus_graph, paramA_inifac, gppl_model)    
layers2["paramA"] = Layer(
    name="paramA",
    anchor=0*_xsep,
    ## iniparvars = ["constvar_2_3", "constvar_4_5"],
    iniparvars = paramA_iniparvars,
    ## inifac = "Beta_6",
    inifac = paramA_inifac,
    ## parvar="θ_1",
    parvar=paramA_out_var,
    sysvars = [],
    facs = [],
    parvars = [],
    link_fac_side = "west")
## layers2["paramA"].links = layers2["obser"].facs    

layers2["paramA"].links = layers2["obser"].facs

coin_tikz = generate_tikz(
    heading = "Coin Toss",
    Model = coin_gppl_model,
    layers2 = layers2) ## fac layers, i.e. not var (vars are handled with assoced layer)
## print(coin_tikz)
show_tikz(coin_tikz); ## write to file rather than show in notebook

# HMM with control

@model function hidden_markov_model(x)
    B ~ MatrixDirichlet(ones(3, 3))
    A ~ MatrixDirichlet([10.0 1.0 1.0; 
                         1.0 10.0 1.0; 
                         1.0 1.0 10.0 ])
    d = fill(1.0/3.0, 3)
    s₀ ~ Categorical(d)
    
    sₖ₋₁ = s₀
    for k in eachindex(x)
        s[k] ~ Transition(sₖ₋₁, B)
        x[k] ~ Transition(s[k], A)
        sₖ₋₁ = s[k]
    end
end

hmm_conditioned = hidden_markov_model() | (x = [[1.0, 0.0, 0.0], [0.0, 0.0, 1.0]],)
hmm_rxi_model = RxInfer.create_model(hmm_conditioned)
hmm_gppl_model = RxInfer.getmodel(hmm_rxi_model)
hmm_meta_graph = hmm_gppl_model.graph
meta_graph = hmm_meta_graph

## Shorten some labels to make graph more readable
# str_labels = [string(lab) for lab in labels(meta_graph)]
# replacements = 
#     Pair("MvNormalMeanCovariance", "Nmc"), 
#     Pair("MvNormalMeanPrecision", "Nmp"), 
#     Pair("constvar", "cv"),
#     Pair("x", "XXXXX") ## make more obvious
# short_labels = [replace(s, replacements...) for s in str_labels]

GraphPlot.gplot( ## existing plotting functionality
    meta_graph,
    layout=spring_layout,
    nodelabel=collect(labels(meta_graph)),
    ## nodelabel=short_labels,
    nodelabelsize=0.1,
    NODESIZE=0.02, ## diameter of the nodes
    NODELABELSIZE=1.5,
    # nodelabelc="white",
    nodelabelc="green",
    nodelabeldist=0.0,
    nodefillc=nothing, ## "cyan"
    edgestrokec="red",
    ## ImageSize = (800, 800) ##- does not work
)
## _san_node_ids = Dict("dummy" => "dummy")
_san_node_ids = Dict("Categorical{P} where P<:Real_12" => "Categorical_12")
_lup_enabled = true
_lup_agc = false ## append global_counter values
_raw_links_enabled = false
_CFFG = true
_deltas_enabled = true
_tsep = 3*_xsep
_lup_dict = Dict{String, String}(
    "MatrixDirichlet_4" => _lup_agc ? "\\mathcal{M}Dir\\_4" : "\\mathcal{M}Dir",
    "B_1" => _lup_agc ? "\\mathbf{B}\\_1" : "\\mathbf{B}",
    "constvar_10_11" => _lup_agc ? "\\mathbf{d}\\_10\\_11" : "\\mathbf{d}",
    "Categorical_12" => _lup_agc ? "\\mathcal{C}at\\_12" : "\\mathcal{C}at",
    "Transition_14" => _lup_agc ? "\\mathcal{T}\\_14" : "\\mathcal{T}",
    "Transition_18" => _lup_agc ? "\\mathcal{T}\\_18" : "\\mathcal{T}",
    "Transition_16" => _lup_agc ? "\\mathcal{T}\\_16" : "\\mathcal{T}",
    "Transition_20" => _lup_agc ? "\\mathcal{T}\\_20" : "\\mathcal{T}",
    "MatrixDirichlet_8" => _lup_agc ? "\\mathcal{M}Dir\\_8" : "\\mathcal{M}Dir",
    "A_5" => _lup_agc ? "\\mathbf{A}\\_5" : "\\mathbf{A}",
    "constvar_2_3" => _lup_agc ? "\\mathbf{B_0}\\_2\\_3" : "\\mathbf{B_0}",
    "constvar_6_7" => _lup_agc ? "\\mathbf{A_0}\\_6\\_7" : "\\mathbf{A_0}",
    ## "s₀_9" => "s_0", ## s₀ must always be in _lup_dict
    "s₀_9" => _lup_agc ? "\\mathbf{s}_0\\_9" : "\\mathbf{s}_0",
    "s_13" => _lup_agc ? "\\mathbf{s}_1\\_13" : "\\mathbf{s}_1",
    "s_17" => _lup_agc ? "\\mathbf{s}_2\\_17" : "\\mathbf{s}_2",
    "x_15" => _lup_agc ? "\\mathbf{x}_1\\_15" : "\\mathbf{x}_1",
    "x_19" => _lup_agc ? "\\mathbf{x}_2\\_19" : "\\mathbf{x}_2",
);
hmm_kobus_graph = create_kobus_graph(hmm_gppl_model)
layers2 = Dict()
kobus_graph = hmm_kobus_graph
gppl_model = hmm_gppl_model

## paramB1_inifac = "MatrixDirichlet_4"
paramB1_inifac = find_inifac_node(kobus_graph, "B", gppl_model)
paramB1_out_var, paramB1_iniparvars = find_iniparvar_nodes(kobus_graph, paramB1_inifac, gppl_model)
layers2["paramB1"] = Layer(
    name="paramB1",
    anchor=1*_xsep,
    ## iniparvars=["constvar_2_3"],
    iniparvars=paramB1_iniparvars,
    ## inifac="MatrixDirichlet_4",
    inifac=paramB1_inifac,
    ## parvar="B_1",
    parvar=paramB1_out_var,
    sysvars = [],
    facs = [],
    parvars = [],
    link_fac_side="north", link_fac_offset=_divn[1][1])
## layers2["paramB1"].links = layers2["state0"].facs

state0_inifac = find_inifac_node(kobus_graph, "s₀", gppl_model)
_, state0_vars, state0_facs = find_state0_nodes(kobus_graph, state0_inifac, gppl_model)
state0_out_var, state0_iniparvars = find_iniparvar_nodes(kobus_graph, state0_inifac, gppl_model)
layers2["state0"] = Layer(
    name="state0",
    anchor=3*_xsep,
    ## iniparvars = ["constvar_10_11"],
    iniparvars = state0_iniparvars,
    inifac = state0_inifac,
    parvar="",
    ## sysvars = ["s₀_9", "s_13", "s_17"],
    sysvars = state0_vars, ## contains only sysvars
    ## facs = [["Transition_14", "Transition_18"]],
    facs = [state0_facs],
    parvars = [])
## layers2["state0"].links = layers2["obser"].facs

obser_sysvars, obser_facs, obser_parvars = find_obser_nodes(kobus_graph, "x", gppl_model)
layers2["obser"] = Layer(
    name="obser",
    anchor=5*_xsep,
    iniparvars = [],
    inifac = "",
    parvar="",
    ## sysvars = ["x_15", "x_19"],
    sysvars = obser_sysvars,
    ## facs = [["Transition_16", "Transition_20"]],
    facs = [obser_facs],
    parvars = []
    ## parvars = [obser_parvars]
    )

paramA_inifac = find_inifac_node(kobus_graph, "A", gppl_model)
paramA_out_var, paramA_iniparvars = find_iniparvar_nodes(kobus_graph, paramA_inifac, gppl_model)
layers2["paramA"] = Layer(
    name="paramA",
    anchor=1*_xsep,
    ## iniparvars=["constvar_6_7"],
    iniparvars=paramA_iniparvars,
    ## inifac="MatrixDirichlet_8",
    inifac=paramA_inifac,
    ## parvar="A_5",
    parvar=paramA_out_var,
    sysvars = [],
    facs = [],
    parvars = [],
    link_fac_side="west")
## layers2["paramA"].links = layers2["obser"].facs

layers2["paramB1"].links = layers2["state0"].facs
layers2["state0"].links = layers2["obser"].facs
layers2["paramA"].links = layers2["obser"].facs
hmm_tikz = generate_tikz(
    heading = "Hidden Markov Model",
    Model = hmm_gppl_model,
    layers2 = layers2) ## fac layers, i.e. not var (vars are handled with assoced layer)
## print(hmm_tikz)
show_tikz(hmm_tikz); ## write to file rather than show in notebook

## Sales Forecasting with Time-Varying Autoregressive Models (Part 4)
@model function lar_model(
    x, ##. data/observations 
    𝚃ᴬᴿ, ##. Uni/Multi variate 
    Mᴬᴿ, ##. AR order
    vᵤ, ##. unit vector
    τ) ##. observation precision     
        ## Priors
        γ  ~ Gamma(α = 1.0, β = 1.0) ##. for transition precision    
        if 𝚃ᴬᴿ === Multivariate
            θ  ~ MvNormal(μ = zeros(Mᴬᴿ), Λ = diageye(Mᴬᴿ)) ##.kw μ,Λ only work inside macro
            s₀ ~ MvNormal(μ = zeros(Mᴬᴿ), Λ = diageye(Mᴬᴿ)) ##.kw μ,Λ only work inside macro
        else ## Univariate
            θ  ~ Normal(μ = 0.0, γ = 1.0)
            s₀ ~ Normal(μ = 0.0, γ = 1.0)
        end
        sₜ₋₁ = s₀
        for t in eachindex(x)
            s[t] ~ AR(sₜ₋₁, θ, γ) #.Eq (2b)
            if 𝚃ᴬᴿ === Multivariate
                x[t] ~ Normal(μ = dot(vᵤ, s[t]), γ = τ) #.Eq (2c)
            else
                x[t] ~ Normal(μ = vᵤ*s[t], γ = τ) #.Eq (2c)
            end
            sₜ₋₁ = s[t]
        end
    end

    𝚃ᴬᴿ = Univariate
m = 1
τ̃ = 0.001 ## assumed observation precision
lar_conditioned = lar_model(
    𝚃ᴬᴿ=𝚃ᴬᴿ, 
    Mᴬᴿ=m, 
    vᵤ=ReactiveMP.ar_unit(𝚃ᴬᴿ, m), 
    τ=τ̃
) | (x = [266.0, 145.0, 183.0],)
lar_rxi_model = RxInfer.create_model(lar_conditioned)
lar_gppl_model = RxInfer.getmodel(lar_rxi_model)
lar_meta_graph = lar_gppl_model.graph
print_meta_graph(lar_meta_graph)

meta_graph = lar_meta_graph

## Shorten some labels to make graph more readable
# str_labels = [string(lab) for lab in labels(meta_graph)]
# replacements = 
#     Pair("MvNormalMeanCovariance", "Nmc"), 
#     Pair("MvNormalMeanPrecision", "Nmp"), 
#     Pair("constvar", "cv"),
#     Pair("x", "XXXXX") ## make more obvious
# short_labels = [replace(s, replacements...) for s in str_labels]

GraphPlot.gplot( ## existing plotting functionality
    meta_graph,
    layout=spring_layout,
    nodelabel=collect(labels(meta_graph)),
    ## nodelabel=short_labels,
    nodelabelsize=0.1,
    NODESIZE=0.02, ## diameter of the nodes
    NODELABELSIZE=1.5,
    # nodelabelc="white",
    nodelabelc="green",
    nodelabeldist=0.0,
    nodefillc=nothing, ## "cyan"
    edgestrokec="red",
    ## ImageSize = (800, 800) ##- does not work
)

_san_node_ids = Dict("dummy" => "dummy")
_lup_enabled = true
_lup_agc = false ## append global_counter values
_raw_links_enabled = false
_CFFG = true
_deltas_enabled = true
_tsep = 2*_xsep
_lup_dict = Dict{String, String}(
    "θ_7" => _lup_agc ? "\\theta\\_7" : "\\theta",
    "constvar_8_9" => _lup_agc ? "\\mu\\_8\\_9" : "\\mu",
    "constvar_10_11" => _lup_agc ? "\\gamma\\_10\\_11" : "\\gamma",
    "NormalMeanPrecision_12" => _lup_agc ? "\\mathcal{N}\\_12" : "\\mathcal{N}",

    "constvar_2_3" => _lup_agc ? "\\alpha\\_2\\_3" : "\\alpha",
    "constvar_4_5" => _lup_agc ? "\\beta\\_4\\_5" : "\\beta",
    "GammaShapeRate_6" => _lup_agc ? "\\mathcal{G}am\\_6" : "\\mathcal{G}am",
    "γ_1" => _lup_agc ? "\\gamma\\_1" : "\\gamma",

    "constvar_14_15" => _lup_agc ? "\\mu\\_14\\_15" : "\\mu",
    "constvar_16_17" => _lup_agc ? "\\gamma\\_16\\_17" : "\\gamma",
    "NormalMeanPrecision_18" => _lup_agc ? "\\mathcal{N}\\_18" : "\\mathcal{N}",
    ## "s₀_13" => "s_0", ## s₀ must always be in _lup_dict
    "s₀_13" => _lup_agc ? "\\mathbf{s}_0\\_13" : "\\mathbf{s}_0",
    "s_19" => _lup_agc ? "\\mathbf{s}_1\\_19" : "\\mathbf{s}_1",
    "s_29" => _lup_agc ? "\\mathbf{s}_2\\_29" : "\\mathbf{s}_2",
    "s_39" => _lup_agc ? "\\mathbf{s}_3\\_39" : "\\mathbf{s}_3",

    "AR_20" => _lup_agc ? "AR\\_20" : "AR",
    "AR_30" => _lup_agc ? "AR\\_30" : "AR",
    "AR_40" => _lup_agc ? "AR\\_40" : "AR",

    "constvar_22_23" => _lup_agc ? "\\mathbf{B}\\_22\\_23" : "\\mathbf{B}",
    "constvar_32_33" => _lup_agc ? "\\mathbf{B}\\_32\\_33" : "\\mathbf{B}",
    "constvar_42_43" => _lup_agc ? "\\mathbf{B}\\_42\\_43" : "\\mathbf{B}",

    "*_24" => _lup_agc ? "*\\_24" : "*",
    "*_34" => _lup_agc ? "*\\_34" : "*",
    "*_44" => _lup_agc ? "*\\_44" : "*",
    
    "anonymous_var_graphppl_21" => _lup_agc ? "\\mathbf{v}_u\\_21" : "\\mathbf{v}_u",
    "anonymous_var_graphppl_31" => _lup_agc ? "\\mathbf{v}_u\\_31" : "\\mathbf{v}_u",
    "anonymous_var_graphppl_41" => _lup_agc ? "\\mathbf{v}_u\\_41" : "\\mathbf{v}_u",

    "constvar_26_27" => _lup_agc ? "\\tau\\_26\\_27" : "\\tau",
    "constvar_36_37" => _lup_agc ? "\\tau\\_36\\_37" : "\\tau",
    "constvar_46_47" => _lup_agc ? "\\tau\\_46\\_47" : "\\tau",

    "NormalMeanPrecision_28" => _lup_agc ? "\\mathcal{N}\\_28" : "\\mathcal{N}",
    "NormalMeanPrecision_38" => _lup_agc ? "\\mathcal{N}\\_38" : "\\mathcal{N}",
    "NormalMeanPrecision_48" => _lup_agc ? "\\mathcal{N}\\_48" : "\\mathcal{N}",

    "x_25" => _lup_agc ? "x_1\\_25" : "x_1",
    "x_35" => _lup_agc ? "x_2\\_35" : "x_2",
    "x_45" => _lup_agc ? "x_3\\_45" : "x_3",
);
lar_kobus_graph = create_kobus_graph(lar_gppl_model)
layers2 = Dict()
kobus_graph = lar_kobus_graph
gppl_model = lar_gppl_model

paramB1_inifac = find_inifac_node(kobus_graph, "θ", gppl_model)
paramB1_out_var, paramB1_iniparvars = find_iniparvar_nodes(kobus_graph, paramB1_inifac, gppl_model)
layers2["paramB1"] = Layer(
    name="paramB1",
    anchor=0*_xsep,
    ## iniparvars=["constvar_8_9", "constvar_10_11"],
    iniparvars=paramB1_iniparvars,
    ## inifac="NormalMeanPrecision_12",
    inifac=paramB1_inifac,
    ## parvar="θ_7",
    parvar=paramB1_out_var,
    sysvars = [],
    facs = [],
    parvars = [],
    link_fac_side="north", link_fac_offset=_divn[3][1])
## layers2["paramB1"].links = layers2["state0"].facs

paramB2_inifac = find_inifac_node(kobus_graph, "γ", gppl_model)
paramB2_out_var, paramB2_iniparvars = find_iniparvar_nodes(kobus_graph, paramB2_inifac, gppl_model)
layers2["paramB2"] = Layer(
    name="paramB2",
    anchor=0*_xsep,
    ## iniparvars = ["constvar_2_3", "constvar_4_5"],
    iniparvars = paramB2_iniparvars,
    ## inifac = "GammaShapeRate_6",
    inifac = paramB2_inifac,
    ## parvar = "γ_1",
    parvar = paramB2_out_var,
    sysvars = [],
    facs = [],
    parvars = [],
    link_fac_side="north", link_fac_offset=_divn[3][3])
## layers2["paramB2"].links = layers2["state0"].facs

state0_inifac = find_inifac_node(kobus_graph, "s₀", gppl_model)
_, state0_vars, state0_facs = find_state0_nodes(kobus_graph, state0_inifac, gppl_model)
state0_out_var, state0_iniparvars = find_iniparvar_nodes(kobus_graph, state0_inifac, gppl_model)
layers2["state0"] = Layer(
    name="state0",
    anchor=3*_xsep,
    ## iniparvars = ["constvar_14_15", "constvar_16_17"],
    iniparvars = state0_iniparvars,
    ## inifac = "NormalMeanPrecision_18",
    inifac = state0_inifac,
    parvar="",
    ## sysvars = ["s₀_13", "s_19", "s_29", "s_39"],
    sysvars = state0_vars, ## contains only sysvars
    ## facs = [["AR_20", "AR_30", "AR_40"]],
    facs = [state0_facs],
    parvars = [])
## layers2["state0"].links = layers2["stateP1"].facs

layers2["stateP1"] = Layer(
    name="stateP1",
    anchor=4*_xsep,
    iniparvars = [],
    inifac = "",
    parvar="",
    sysvars = ["anonymous_var_graphppl_21", "anonymous_var_graphppl_31", "anonymous_var_graphppl_41"],
    facs = [["*_24", "*_34", "*_44"]],
    parvars = [
        [["constvar_22_23"], ["constvar_32_33"], ["constvar_42_43"]] ],
    link_fac_side="north", link_fac_offset=_divn[1][1]
)
## layers2["stateP1"].links = layers2["obser"].facs

obser_sysvars, obser_facs, obser_parvars = find_obser_nodes(kobus_graph, "x", gppl_model)
layers2["obser"] = Layer(
    name="obser",
    anchor=4*_xsep,
    iniparvars = [],
    inifac = "",
    parvar="",
    ## MANUAL:  ## state vars not directly connected to obser facs
    # sysvars = obser_sysvars,
    sysvars = ["x_25", "x_35", "x_45"],
    ## MANUAL:  ## state vars not directly connected to obser facs
    ## facs = [obser_facs], 
    facs = [["NormalMeanPrecision_28", "NormalMeanPrecision_38", "NormalMeanPrecision_48"]],
    ## MANUAL: sysvars = obser_sysvars, ## state vars not directly connected to obser facs
    ## parvars = [obser_parvars],
    parvars = [
        [["constvar_26_27"], ["constvar_36_37"], ["constvar_46_47"]] ])

layers2["paramB1"].links = layers2["state0"].facs
layers2["paramB2"].links = layers2["state0"].facs
layers2["state0"].links = layers2["stateP1"].facs
layers2["stateP1"].links = layers2["obser"].facs
lar_tikz = generate_tikz(
    heading = "Time-Varying Autoregressive Model (Univariate)",
    Model = lar_gppl_model,
    layers2 = layers2) ## fac layers, i.e. not var (vars are handled with assoced layer)
## print(lar_tikz)
show_tikz(lar_tikz); ## write to file rather than show in notebook

# Fly a Drone to a Target using Active Inference
@model function dronenav_model(x, mᵤ, Vᵤ, mₓ, Vₓ, mₛ₍ₜ₋₁₎, Vₛ₍ₜ₋₁₎, T, Rᵃ)
    ## Transition function
    g = (sₜ₋₁::AbstractVector) -> begin
        sₜ = similar(sₜ₋₁) ## Next state
        sₜ = Aᵃ(sₜ₋₁, 1.0) + sₜ₋₁
        return sₜ
    end
    
    ## Function for modeling turn/yaw control
    h = (u::AbstractVector) -> Rᵃ(u[1])
    
    Γ = _γ*diageye(4) ## Transition precision
    𝚯 = _ϑ*diageye(4) ## Observation variance
    
    ## sₜ₋₁ ~ MvNormal(mean=mₛ₍ₜ₋₁₎, cov=Vₛ₍ₜ₋₁₎)
    s₀ ~ MvNormal(mean=mₛ₍ₜ₋₁₎, cov=Vₛ₍ₜ₋₁₎)
    ## sₖ₋₁ = sₜ₋₁
    sₖ₋₁ = s₀
    
    local s

    for k in 1:T
        ## Control
        u[k] ~ MvNormal(mean=mᵤ[k], cov=Vᵤ[k])
        hIuI[k] ~ h(u[k]) where { meta=DeltaMeta(method=Unscented()) }

        ## State transition
        gIsI[k] ~ g(sₖ₋₁) where { meta=DeltaMeta(method=Unscented()) }
        ghSum[k] ~ gIsI[k] + hIuI[k]#.
        s[k] ~ MvNormal(mean=ghSum[k], precision=Γ)

        ## Likelihood of future observations
        x[k] ~ MvNormal(mean=s[k], cov=𝚯)

        ## Target/Goal prior
        x[k] ~ MvNormal(mean=mₓ[k], cov=Vₓ[k])

        sₖ₋₁ = s[k]
    end
    return (s, )
end
_Fᴱⁿᵍᴸⁱᵐⁱᵗ = 0.1
function Rᵃ(a::Real) ## turn/yaw rate
    b = [ 0.0, 0.0, 1.0, 0.0 ]
    return b*_Fᴱⁿᵍᴸⁱᵐⁱᵗ*tanh(a)
end
## Rᵃ(0.25)

_γ = 1e4 ## transition precision (system noise)
_ϑ = 1e-4 ## observation variance (observation noise)

## T =_Tᵃⁱ,
## T =100
T =3
Rᵃ=Rᵃ

mᵤ = Vector{Float64}[ [0.0] for k=1:T ] ##Set control priors
ξ = 0.1
Ξ  = fill(ξ, 1, 1) ##Control prior variance
Vᵤ = Matrix{Float64}[ Ξ for k=1:T ]
mₓ      = [zeros(4) for k=1:T]
x₊ = [0.0, 0.0, 0.0*π, 0.1] ## Target/Goal state
mₓ[end] = x₊ ##Set prior mean to reach target/goal at t=T
Vₓ      = [huge*diageye(4) for k=1:T]
σ = 1e-4
Σ       = σ*diageye(4) ##Target/Goal prior variance
Vₓ[end] = Σ ##Set prior variance to reach target/goal at t=T
s₀ = [8.0, 8.0, -0.1, 0.1] ## initial state
mₛ₍ₜ₋₁₎ = s₀
Vₛ₍ₜ₋₁₎ = tiny*diageye(4)

drone_conditioned = dronenav_model(
    mᵤ= mᵤ, 
    Vᵤ= Vᵤ, 
    mₓ= mₓ, 
    Vₓ= Vₓ,
    mₛ₍ₜ₋₁₎= mₛ₍ₜ₋₁₎,
    Vₛ₍ₜ₋₁₎= Vₛ₍ₜ₋₁₎,
    T=T, 
    Rᵃ=Rᵃ
) | (x = [ [8.099, 7.990, -0.109, 0.1],  [8.198, 7.979, -0.119, 0.1],  [8.298, 7.967, -0.129, 0.1]],)
## ) | (x = [ [8.099, 7.990, -0.109],  [8.198, 7.979, -0.119],  [8.298, 7.967, -0.129]],)
drone_rxi_model = RxInfer.create_model(drone_conditioned)
drone_gppl_model = RxInfer.getmodel(drone_rxi_model)
drone_meta_graph = drone_gppl_model.graph
##
## fieldnames(GraphPPL.Context)
# drone_gppl_model_context = GraphPPL.getcontext(drone_gppl_model)
# drone_gppl_model_context.individual_variables
# drone_gppl_model_context.vector_variables
# drone_gppl_model_context.factor_nodes
print_meta_graph(drone_meta_graph)

meta_graph = drone_meta_graph

## Shorten some labels to make graph more readable
str_labels = [string(lab) for lab in labels(meta_graph)]
replacements = 
    Pair("MvNormalMeanCovariance", "Nmc"), 
    Pair("MvNormalMeanPrecision", "Nmp"), 
    Pair("constvar", "cv"),
    Pair("x", "XXXXX") ## make more obvious
short_labels = [replace(s, replacements...) for s in str_labels]

GraphPlot.gplot( ## existing plotting functionality
    meta_graph,
    layout=spring_layout,
    ## nodelabel=collect(labels(meta_graph)),
    nodelabel=short_labels,
    nodelabelsize=0.1,
    NODESIZE=0.02, ## diameter of the nodes
    NODELABELSIZE=1.5,
    # nodelabelc="white",
    nodelabelc="green",
    nodelabeldist=0.0,
    nodefillc=nothing, ## "cyan"
    edgestrokec="red",
    ## ImageSize = (800, 800) ##- does not work
)
_cntrl_hash_prefix = "70"
_state_hash_prefix = "69"
_san_node_ids = Dict(
    ## "#45_14" => "HX_14",
    "#$(_cntrl_hash_prefix)_14" => "CH_14",
    ## "#45_39" => "HX_39",
    "#$(_cntrl_hash_prefix)_39" => "CH_39",
    ## "#45_64" => "HX_64",
    "#$(_cntrl_hash_prefix)_64" => "CH_64",

    "#$(_state_hash_prefix)_16" => "SH_16",
    "#$(_state_hash_prefix)_41" => "SH_41",
    "#$(_state_hash_prefix)_66" => "SH_66",
)
_lup_enabled = true
_lup_agc = false ## append global_counter values
_raw_links_enabled = false
_CFFG = false
_deltas_enabled = false
_tsep = 6*_xsep
_lup_dict = Dict{String, String}(
    "constvar_8_9" => _lup_agc ? "\\mathbf{m}_u\\_8\\_9" : "\\mathbf{m}_u", 
    "constvar_10_11" => _lup_agc ? "\\mathbf{V}_u\\_10\\_11" : "\\mathbf{V}_u", 
    "MvNormalMeanCovariance_12" => _lup_agc ? "\\mathcal{N}\\_12" : "\\mathcal{N}",
    "u_7" => _lup_agc ? "\\mathbf{u}_1\\_7" : "\\mathbf{u}_1",

    "constvar_33_34" => _lup_agc ? "\\mathbf{m}_u\\_33\\_34" : "\\mathbf{m}_u", 
    "constvar_35_36" => _lup_agc ? "\\mathbf{V}_u\\_35\\_36" : "\\mathbf{V}_u", 
    "MvNormalMeanCovariance_37" => _lup_agc ? "\\mathcal{N}\\_37" : "\\mathcal{N}",
    "u_32" => _lup_agc ? "\\mathbf{u}_2\\_32" : "\\mathbf{u}_2",

    "constvar_58_59" => _lup_agc ? "\\mathbf{m}_u\\_58\\_59" : "\\mathbf{m}_u", 
    "constvar_60_61" => _lup_agc ? "\\mathbf{V}_u\\_60\\_61" : "\\mathbf{V}_u", 
    "MvNormalMeanCovariance_62" => _lup_agc ? "\\mathcal{N}\\_62" : "\\mathcal{N}",
    "u_57" => _lup_agc ? "\\mathbf{u}_3\\_57" : "\\mathbf{u}_3",

    "hIuI_13" => _lup_agc ? "h(\\mathbf{u})\\_13" : "h(\\mathbf{u})",
    "hIuI_38" => _lup_agc ? "h(\\mathbf{u})\\_38" : "h(\\mathbf{u})",
    "hIuI_63" => _lup_agc ? "h(\\mathbf{u})\\_63" : "h(\\mathbf{u})",
    "+_18" => _lup_agc ? "+\\_18" : "+",
    "+_43" => _lup_agc ? "+\\_43" : "+",
    "+_68" => _lup_agc ? "+\\_68" : "+",

    "gIsI_15" => _lup_agc ? "g(\\mathbf{s})\\_15" : "g(\\mathbf{s})",
    "gIsI_40" => _lup_agc ? "g(\\mathbf{s})\\_40" : "g(\\mathbf{s})",
    "gIsI_65" => _lup_agc ? "g(\\mathbf{s})\\_65" : "g(\\mathbf{s})",
    "ghSum_17" => _lup_agc ? "g(\\mathbf{s}) {+} h(\\mathbf{u})\\_17" : "g(\\mathbf{s}) {+} h(\\mathbf{u})",
    "ghSum_42" => _lup_agc ? "g(\\mathbf{s}) {+} h(\\mathbf{u})\\_42" : "g(\\mathbf{s}) {+} h(\\mathbf{u})",
    "ghSum_67" => _lup_agc ? "g(\\mathbf{s}) {+} h(\\mathbf{u})\\_67" : "g(\\mathbf{s}) {+} h(\\mathbf{u})",
    # "ghSum_17" => _lup_agc ? "g {+} h" : "g {+} h", ## to compress space surrounding +; better than \\!+\\! & \\mathrel{+}
    # "ghSum_42" => _lup_agc ? "g {+} h" : "g {+} h",
    # "ghSum_67" => _lup_agc ? "g {+} h" : "g {+} h",

    "MvNormalMeanPrecision_22" => _lup_agc ? "\\mathcal{N}\\_22" : "\\mathcal{N}",
    "constvar_20_21" => _lup_agc ? "\\vartheta\\_20\\_21" : "\\vartheta", 
    "MvNormalMeanPrecision_47" => _lup_agc ? "\\mathcal{N}\\_47" : "\\mathcal{N}",
    "constvar_45_46" => _lup_agc ? "\\vartheta\\_45\\_46" : "\\vartheta", 
    "MvNormalMeanPrecision_72" => _lup_agc ? "\\mathcal{N}\\_72" : "\\mathcal{N}",
    "constvar_70_71" => _lup_agc ? "\\vartheta\\_70\\_71" : "\\vartheta", 

    "MvNormalMeanCovariance_6" => _lup_agc ? "\\mathcal{N}\\_6" : "\\mathcal{N}",
    "constvar_4_5" => _lup_agc ? "10^{12}\\_4\\_5" : "10^{12}",
    "constvar_2_3" => _lup_agc ? "\\mathbf{0}\\_2\\_3" : "\\mathbf{0}",
    "s₀_1" => _lup_agc ? "\\mathbf{s}_0\\_1" : "\\mathbf{s}_0", ## s₀ must always be in _lup_dict
    "s_19" => _lup_agc ? "\\mathbf{s}_1\\_19" : "\\mathbf{s}_1",
    "s_44" => _lup_agc ? "\\mathbf{s}_2\\_44" : "\\mathbf{s}_2",
    "s_69" => _lup_agc ? "\\mathbf{s}_3\\_69" : "\\mathbf{s}_3",
    
    "MvNormalMeanCovariance_26" => _lup_agc ? "\\mathcal{N}\\_26" : "\\mathcal{N}",
    "constvar_24_25" => _lup_agc ? "\\mathbf\\Theta\\_24\\_25" : "\\mathbf\\Theta",
    "MvNormalMeanCovariance_51" => _lup_agc ? "\\mathcal{N}\\_51" : "\\mathcal{N}",
    "constvar_49_50" => _lup_agc ? "\\mathbf\\Theta\\_49\\_50" : "\\mathbf\\Theta",
    "MvNormalMeanCovariance_76" =>  _lup_agc ? "\\mathcal{N}\\_76" : "\\mathcal{N}",
    "constvar_74_75" => _lup_agc ? "\\mathbf\\Theta\\_74\\_75" : "\\mathbf\\Theta",
    "x_23" => _lup_agc ? "\\mathbf{x}_1\\_23" : "\\mathbf{x}_1",
    "x_48" => _lup_agc ? "\\mathbf{x}_2\\_48" : "\\mathbf{x}_2",
    "x_73" => _lup_agc ? "\\mathbf{x}_3\\_73" : "\\mathbf{x}_3",

    "MvNormalMeanCovariance_31" => _lup_agc ? "\\mathcal{N}\\_31" : "\\mathcal{N}",
    "constvar_29_30" => _lup_agc ? "\\mathbf{V}_x\\_29\\_30" : "\\mathbf{V}_x", 
    "constvar_27_28" => _lup_agc ? "\\mathbf{m}_x\\_27\\_28" : "\\mathbf{m}_x", 
    "MvNormalMeanCovariance_56" => _lup_agc ? "\\mathcal{N}\\_56" : "\\mathcal{N}",
    "constvar_54_55" => _lup_agc ? "\\mathbf{V}_x\\_54\\_55" : "\\mathbf{V}_x", 
    "constvar_52_53" => _lup_agc ? "\\mathbf{m}_x\\_52\\_53" : "\\mathbf{m}_x", 
    "MvNormalMeanCovariance_81" => _lup_agc ? "\\mathcal{N}\\_81" : "\\mathcal{N}",
    "constvar_79_80" => _lup_agc ? "\\mathbf{V}_x\\_79\\_80" : "\\mathbf{V}_x", 
    "constvar_77_78" => _lup_agc ? "\\mathbf{m}_x\\_77\\_78" : "\\mathbf{m}_x", 

    # "MvNormalMeanCovariance_36" => _lup_agc ? "\\bm{\\mathcal{N}}\\_36" : "",
    # "MvNormalMeanPrecision_76" => _lup_agc ? "\\bm{\\mathcal{N}}\\_76" : "",
    # "MvNormalMeanCovariance_31" =>  _lup_agc ? "\\bm{\\mathcal{N}}\\_31" : "",
);
drone_kobus_graph = create_kobus_graph(drone_gppl_model)
layers2 = Dict()
kobus_graph = drone_kobus_graph
gppl_model = drone_gppl_model

cntrl_sysvars, cntrl_facs, cntrl_parvars = find_cntrl_nodes(kobus_graph, "u", gppl_model)
layers2["cntrl"] = Layer(
    name="cntrl",
    anchor=3*_xsep,
    iniparvars = [],
    inifac = "",
    parvar="",
    ## sysvars = ["u_7", "u_32", "u_57"],
    sysvars = cntrl_sysvars,
    ## facs = [["MvNormalMeanCovariance_12", "MvNormalMeanCovariance_37", "MvNormalMeanCovariance_62"]],
    facs = [cntrl_facs],
    ## parvars = [
    #     [
    #         ["constvar_8_9", "constvar_10_11"], 
    #         ["constvar_33_34", "constvar_35_36"],
    #         ["constvar_58_59", "constvar_60_61"]
    #     ] ]
    parvars = [cntrl_parvars]    
    )
## layers2["cntrl"].links = layers2["stateM2"].facs

layers2["stateM1"] = Layer(
    name="state2",
    anchor=3*_xsep,
    iniparvars = [],
    inifac = "",
    parvar="",
    sysvars = ["hIuI_13", "hIuI_38", "hIuI_63"],
    facs = [
        [
            sanitized("#$(_cntrl_hash_prefix)_14"), 
            sanitized("#$(_cntrl_hash_prefix)_39"), 
            sanitized("#$(_cntrl_hash_prefix)_64")
        ]
    ],    
    parvars = [],
    link_fac_side="north", link_fac_offset=_divn[1][1])
## layers2["stateM1"].links = [layers2["state0"].facs[3]]

state0_inifac = find_inifac_node(kobus_graph, "s₀", gppl_model)
## _, state0_sysvars, state0_facs = find_state0_nodes(kobus_graph, state0_inifac, gppl_model)
_, state0_vars, state0_facs = find_state0_nodes(kobus_graph, state0_inifac, gppl_model)
state0_out_var, state0_iniparvars = find_iniparvar_nodes(kobus_graph, state0_inifac, gppl_model)
layers2["state0"] = Layer(
    name="state0",
    anchor=1*_xsep,
    ## iniparvars = ["constvar_2_3", "constvar_4_5"],
    iniparvars = state0_iniparvars,
    ## inifac = "MvNormalMeanCovariance_6",
    inifac = state0_inifac,
    parvar="",
    sysvars = ["s₀_1", "s_19", "s_44", "s_69"], ## state0_vars only return first seq, so hand-configure
    facs = [ ## in general, facs could be interleafed with vars; first & last layers must be facs
        [sanitized("#$(_state_hash_prefix)_16"), sanitized("#$(_state_hash_prefix)_41"), sanitized("#$(_state_hash_prefix)_66")],
        ["gIsI_15", "gIsI_40", "gIsI_65"], 
        ["+_18", "+_43", "+_68"],
        ["ghSum_17", "ghSum_42", "ghSum_67"], 
        ["MvNormalMeanPrecision_22", "MvNormalMeanPrecision_47", "MvNormalMeanPrecision_72"]
    ],
    parvars = [
        [],
        [], 
        [],
        [], 
        [["constvar_20_21"], ["constvar_45_46"], ["constvar_70_71"]] ])
## layers2["state0"].links = layers2["obser"].facs

obser_sysvars, obser_facs, obser_parvars = find_obser_nodes(kobus_graph, "x", gppl_model)
layers2["obser"] = Layer(
    name="obser",
    anchor=6*_xsep,
    iniparvars = [],
    inifac = "",
    parvar="",
    ## sysvars = ["x_23", "x_48", "x_73"], 
    sysvars = obser_sysvars,
    ## facs = [["MvNormalMeanCovariance_26", "MvNormalMeanCovariance_51", "MvNormalMeanCovariance_76"]],
    facs = [obser_facs],
    ## parvars = [
    #     [["constvar_24_25"], ["constvar_49_50"], ["constvar_74_75"]] ]
    parvars = [obser_parvars]
    )
## layers2["obser"].links = layers2["prefr"].facs

prefr_facs, prefr_parvars = find_prefr_nodes(kobus_graph, "x", gppl_model)
layers2["prefr"] = Layer(
    name="prefr",
    anchor=6*_xsep,
    iniparvars = [],
    inifac = "",
    parvar="",
    sysvars = [], 
    ## facs = [["MvNormalMeanCovariance_31", "MvNormalMeanCovariance_56", "MvNormalMeanCovariance_81"]],
    facs = [prefr_facs],
    ## parvars = [
    #     [
    #         ["constvar_27_28", "constvar_29_30"], 
    #         ["constvar_52_53", "constvar_54_55"], 
    #         ["constvar_77_78", "constvar_79_80"]
    #     ] ]
    parvars = [prefr_parvars]
    )

layers2["cntrl"].links = layers2["stateM1"].facs
layers2["stateM1"].links = [layers2["state0"].facs[3]]
layers2["state0"].links = layers2["obser"].facs
layers2["obser"].links = layers2["prefr"].facs
drone_tikz = generate_tikz(
    heading = "Drone Flying to Target",
    Model = drone_gppl_model,
    layers2 = layers2) ## fac layers, i.e. not var (vars are handled with assoced layer)
## print(drone_tikz)
show_tikz(drone_tikz); ## write to file rather than show in notebook