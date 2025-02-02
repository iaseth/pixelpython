from PIL import Image, ImageDraw
import random

from .utils import get_rgb_components



def generate_hexagon_wallpaper(image_size=(1080, 1080), hex_size=100, color_string="red"):
	base_color = get_rgb_components(color_string)
	img = Image.new("RGB", image_size, base_color)
	draw = ImageDraw.Draw(img)

	hex_height = int(hex_size * 1.732)  # sqrt(3) * hex_size
	rows = image_size[1] // hex_height
	cols = image_size[0] // (hex_size * 3 // 2)

	for row in range(rows + 1):
		for col in range(cols + 1):
			# Generate random brightness variation for the base color
			shade_factor = random.uniform(0.6, 1.2)
			color = tuple(min(255, max(0, int(c * shade_factor))) for c in base_color)

			x = col * (hex_size * 3 // 2)
			y = row * hex_height
			if col % 2 == 1:
				y += hex_height // 2

			# Define hexagon vertices
			hexagon = [
				(x, y), (x + hex_size // 2, y - hex_height // 2), (x + hex_size * 3 // 2, y - hex_height // 2),
				(x + hex_size * 2, y), (x + hex_size * 3 // 2, y + hex_height // 2), (x + hex_size // 2, y + hex_height // 2)
			]

			# Draw the hexagon
			draw.polygon(hexagon, fill=color)

	img.show()
	img.save("hexagon_wallpaper.png")


