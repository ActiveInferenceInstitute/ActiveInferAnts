using TikzPictures
using LaTeXStrings
import Cairo
using Rsvg

function render_tex_to_pdf(tex_file::String, output_folder::String)
    if !isfile(tex_file)
        error("File not found: $tex_file")
    end
    
    # Read the .tex file content
    tex_content = read(tex_file, String)
    
    # Remove \DeclareUnicodeCharacter commands
    tex_content = replace(tex_content, r"\\DeclareUnicodeCharacter\{.*?\}\{.*?\}" => "")
    
    # Split the content into preamble and document
    preamble, document_content = split_tex_content(tex_content)
    
    # Check if \documentclass is already present
    if !occursin(r"\\documentclass", preamble)
        # Add necessary packages and commands to the preamble
        preamble = """
        \\documentclass{standalone}
        $preamble
        \\usepackage[T1]{fontenc}
        \\usepackage{textcomp}
        \\usepackage{amsmath}
        \\usepackage{amssymb}
        \\usepackage[utf8]{inputenc}
        
        % Define Greek letters and other Unicode characters
        \\newcommand{\\uniθ}{\\ensuremath{\\theta}}
        \\newcommand{\\uniγ}{\\ensuremath{\\gamma}}
        % Add more Unicode character definitions as needed
        """
    else
        # Add necessary packages and commands to the preamble without \documentclass
        preamble = """
        $preamble
        \\usepackage[T1]{fontenc}
        \\usepackage{textcomp}
        \\usepackage{amsmath}
        \\usepackage{amssymb}
        \\usepackage[utf8]{inputenc}
        
        % Define Greek letters and other Unicode characters
        \\newcommand{\\uniθ}{\\ensuremath{\\theta}}
        \\newcommand{\\uniγ}{\\ensuremath{\\gamma}}
        % Add more Unicode character definitions as needed
        """
    end

    # Create a TikzPicture object with the document content only
    tikz_picture = TikzPicture(document_content, preamble=preamble)
    
    # Define the output file path
    output_file = joinpath(output_folder, replace(basename(tex_file), ".tex" => ".pdf"))
    
    # Save the TikzPicture as a PDF file
    try
        save(PDF(output_file), tikz_picture)
        println("PDF successfully saved to: $(abspath(output_file))")
        return true
    catch e
        if isa(e, ErrorException) && occursin("LaTeX error", e.msg)
            println("LaTeX error occurred. Check your TeX content for syntax errors.")
            println("Error details: ", e.msg)
            println("Preamble:")
            println(preamble)
            println("Document content:")
            println(document_content)
        else
            println("An unexpected error occurred: ", e)
        end
        return false
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

# Example usage
tex_file_path = joinpath(@__DIR__, "coin_toss.tex")
output_folder = "output_folder"

if !isdir(output_folder)
    mkdir(output_folder)
end

success = render_tex_to_pdf(tex_file_path, output_folder)
if success
    println("PDF generated successfully!")
else
    println("Failed to generate PDF. Please check the error messages above.")
end