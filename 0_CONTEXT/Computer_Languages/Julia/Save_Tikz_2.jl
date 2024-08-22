using PGFPlotsX

# Define a simple TikZ code
tikz_code = raw"""
\begin{tikzpicture}
    % Draw a blue circle
    \draw[fill=blue!20, draw=blue, very thick] (0,0) circle (2cm);
    
    % Draw a red square
    \draw[fill=red!20, draw=red, very thick] (-1,-1) rectangle (1,1);
    
    % Add some text
    \node at (0,0) {Simple TikZ Example};
    
    % Draw an arrow
    \draw[->, thick] (2,2) -- (1,1) node[above right] {Arrow};
\end{tikzpicture}
"""

# Create a TikzPicture object
tikz_picture = TikzPicture(tikz_code)

# Save the TikzPicture as a PNG file
pgfsave("simple_tikz_example.png", tikz_picture; dpi=300)

println("Image saved as 'simple_tikz_example.png'")