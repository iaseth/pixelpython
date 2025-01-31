import json
import random
import sys

from PIL import Image, ImageDraw



with open('colors.json') as f:
	colors_json = json.load(f)
	colors = colors_json['colors']


def get_rgb_components(hex_color):
	if hex_color.startswith("#"):
		hex_color = hex_color.lstrip("#")
		return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
	else:
		for color in colors:
			if color['name'].upper() == hex_color.upper():
				return get_rgb_components(color['code'])


def generate_wallpaper(
	hex_color, size, width=1920, height=1080,
	padding=10, gap=5,
	output_image_path="wallpaper.png"
):
	# Create a blank white image
	color = get_rgb_components(hex_color)
	image = Image.new("RGB", (width, height), color)
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
	
	# Save the image
	image.save(output_image_path)
	print(f"Wallpaper generated and saved: {output_image_path}")


def main():
	args = sys.argv[1:]

	hex_color = "#6496C8"
	size = 110
	width=1920
	height=1080
	padding = 0
	gap = 10

	for arg in args:
		if "=" in arg:
			key, value = arg.split("=")
			key = key.strip().upper()
			match key:
				case 'COLOR' | 'C': hex_color = value
				case 'SIZE' | 'S': size = int(value)
				case 'HEIGHT' | 'H': height = int(value)
				case 'WIDTH' | 'W': width = int(value)
				case 'SQUARE' | 'SQ': height = width = int(value)
				case 'PADDING': padding = int(value)
				case 'GAP': gap = int(value)
				case _:
					print(f"Unknown key: '{key}'")
		else:
			command = arg.upper()
			match command:
				case '4K':
					height, width = 2160, 3840
				case 'SQUARE':
					height = max(height, width)
					width = height
				case _:
					print(f"Unknown command: '{command}'")


	generate_wallpaper(
		hex_color, size,
		width=width, height=height,
		padding=padding, gap=gap
	)


if __name__ == "__main__":
	main()
