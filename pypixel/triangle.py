from PIL import Image, ImageDraw
import random

from .utils import get_rgb_components, save_or_show_image



def generate_triangle_wallpaper(
	image_size=(3840, 2160), triangle_size=100, color_string="red",
	output_image_path="wallpaper.png"
):
	base_color = get_rgb_components(color_string)
	img = Image.new("RGB", image_size, base_color)
	draw = ImageDraw.Draw(img)

	rows = image_size[1] // triangle_size
	cols = image_size[0] // triangle_size

	for row in range(rows + 1):
		for col in range(cols + 1):
			# Generate random brightness variation for the base color
			shade_factor = random.uniform(0.6, 1.2)
			color = tuple(min(255, max(0, int(c * shade_factor))) for c in base_color)
			shade_factor = random.uniform(0.6, 1.2)
			color2 = tuple(min(255, max(0, int(c * shade_factor))) for c in base_color)

			x = col * triangle_size
			y = row * triangle_size

			# Define two triangles per grid cell
			triangle1 = [(x, y), (x + triangle_size, y), (x + triangle_size // 2, y + triangle_size)]
			triangle2 = [(x, y), (x + triangle_size // 2, y + triangle_size), (x - triangle_size // 2, y + triangle_size)]

			# Draw the triangles
			draw.polygon(triangle1, fill=color)
			draw.polygon(triangle2, fill=color2)

	save_or_show_image(img, output_image_path)


