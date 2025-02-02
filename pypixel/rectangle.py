from PIL import Image, ImageDraw
import random

from .utils import get_rgb_components, save_or_show_image



def generate_rectangle_wallpaper(
	color_string, bg_color_string,
	size=110, width=1920, height=1080,
	padding=10, gap=5,
	output_image_path="wallpaper.png"
):
	# Create a blank white image
	color = get_rgb_components(color_string)
	bg_color = get_rgb_components(bg_color_string)
	image = Image.new("RGB", (width, height), bg_color)
	draw = ImageDraw.Draw(image)

	# Calculate number of rectangles in each row and column
	cols = (width - 2 * padding + gap) // (size + gap)
	rows = (height - 2 * padding + gap) // (size + gap)

	# Adjust width and height to fit full rectangles
	total_width = cols * (size + gap) - gap
	total_height = rows * (size + gap) - gap
	start_x = (width - total_width) // 2
	start_y = (height - total_height) // 2

	for i in range(rows):
		for j in range(cols):
			x1 = start_x + j * (size + gap)
			y1 = start_y + i * (size + gap)
			x2 = x1 + size
			y2 = y1 + size
			
			# Generate a shade of the given color
			shade_factor = random.uniform(0.2, 0.8)
			shaded_color = (
				int(color[0] * shade_factor),
				int(color[1] * shade_factor),
				int(color[2] * shade_factor)
			)
			
			draw.rectangle([x1, y1, x2, y2], fill=shaded_color, outline=None)

	save_or_show_image(image, output_image_path)


