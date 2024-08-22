# Import necessary modules
using Pkg
using TikzPictures
import Cairo
using Rsvg

# Function to convert .tex file to multiple formats
function convert_tex_to_formats(tex_file::String, output_folder::String)
    # Read the .tex file content
    tex_content = read(tex_file, String)
    
    # Check if the content already has a documentclass
    has_documentclass = occursin("\\documentclass", tex_content)
    
    # If there's no documentclass, add one
    if !has_documentclass
        tex_content = "\\documentclass{standalone}\n" * tex_content
    end
    
    # Extract the preamble and document content
    preamble, document_content = split_tex_content(tex_content)
    
    # Create a TikzPicture object with the document content only
    tikz_picture = TikzPicture(document_content, preamble=preamble)
    
    # Define output formats and their corresponding save functions
    formats = [
        ("pdf", save_pdf),
        ("svg", save_svg),
        ("png", save_png)
    ]
    
    # Iterate over each format and attempt to save
    for (ext, save_func) in formats
        try
            output_file = joinpath(output_folder, replace(basename(tex_file), ".tex" => ".$ext"))
            save_func(output_file, tikz_picture)
            println("File saved to: $output_file")
        catch e
            println("Failed to save $ext: $e")
        end
    end
end

# Helper function to split the TeX content into preamble and document content
function split_tex_content(tex_content::String)
    parts = split(tex_content, "\\begin{document}")
    if length(parts) != 2
        error("Invalid TeX file structure. Cannot find \\begin{document}")
    end
    preamble = parts[1]
    document_content = "\\begin{document}" * parts[2]
    
    # Remove any existing \documentclass from the preamble
    preamble = replace(preamble, r"\\documentclass\{.*?\}" => "")
    
    return preamble, document_content
end

# Helper functions for saving in different formats
function save_pdf(output_file, tikz_picture)
    TikzPictures.save(PDF(output_file), tikz_picture)
end

function save_svg(output_file, tikz_picture)
    TikzPictures.save(SVG(output_file), tikz_picture)
end

function save_png(output_file, tikz_picture)
    # First save as SVG
    temp_svg = tempname() * ".svg"
    TikzPictures.save(SVG(temp_svg), tikz_picture)
    
    # Then convert SVG to PNG using Rsvg
    r = Rsvg.handle_new_from_file(temp_svg)
    d = Rsvg.dimension_data(r)
    cs = Cairo.CairoImageSurface(d.width, d.height, Cairo.FORMAT_ARGB32)
    c = Cairo.CairoContext(cs)
    Rsvg.render_cairo(c, r)
    Cairo.write_to_png(cs, output_file)
    
    # Clean up temporary SVG file
    rm(temp_svg)
end

# Example usage
convert_tex_to_formats("myoutput.tex", "output_folder")