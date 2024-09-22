# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import imageio
import os
from PIL import Image, ImageDraw, ImageFont

# Define Cellular Automata class
class CellularAutomata:
    def __init__(self, width, height, rule=30):
        self.width = width
        self.height = height
        self.rule = rule
        self.grid = np.zeros((height, width), dtype=int)
        # Initialize the first row with a single active cell
        self.grid[0, width // 2] = 1

    def apply_rule(self, left, center, right):
        # Convert the neighborhood to a binary string
        neighborhood = (left << 2) | (center << 1) | right
        return (self.rule >> neighborhood) & 1

    def evolve(self):
        for i in range(1, self.height):
            for j in range(1, self.width - 1):
                left = self.grid[i-1, j-1]
                center = self.grid[i-1, j]
                right = self.grid[i-1, j+1]
                self.grid[i, j] = self.apply_rule(left, center, right)

    def visualize(self):
        # Convert the grid to ASCII art
        ascii_frame = "\n".join([''.join(['#' if cell else ' ' for cell in row]) for row in self.grid])
        return ascii_frame

    def save_gif(self, filename='cellular_automata.gif'):
        # Save ASCII frames as GIF
        images = []
        font = ImageFont.load_default()
        for i in range(self.height):
            ascii_frame = "\n".join([''.join(['#' if cell else ' ' for cell in row]) for row in self.grid[:i+1]])
            img = Image.new('RGB', (self.width * 10, (i+1) * 10), color='white')
            d = ImageDraw.Draw(img)
            d.text((0, 0), ascii_frame, font=font, fill='black')
            images.append(img)
        images[0].save(
            filename,
            save_all=True,
            append_images=images[1:],
            duration=100,
            loop=0
        )

# Main function
def main():
    width, height = 100, 100
    ca = CellularAutomata(width, height, rule=110)
    ca.evolve()
    ca.save_gif(os.path.join(os.path.dirname(__file__), 'cellular_automata.gif'))

if __name__ == "__main__":
    main()
