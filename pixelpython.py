import random
import sys

from PIL import Image, ImageDraw
from pypixel import generate_triangle_wallpaper, generate_hexagon_wallpaper, get_rgb_components



def generate_wallpaper(
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
	
	if output_image_path:
		# Save the image
		image.save(output_image_path)
		print(f"Wallpaper generated and saved: {output_image_path}")
	else:
		image.show()


def main():
	random.seed(0)
	args = sys.argv[1:]

	template = "DEFAULT"
	color_string = "#6496C8"
	bg_color_string = None
	size = 110
	width = 1920
	height = 1080
	padding = 0
	gap = 10
	output_image_path = None

	for arg in args:
		if "=" in arg:
			key, value = arg.split("=")
			key = key.strip().upper()
			match key:
				case 'COLOR' | 'C': color_string = value
				case 'BACKGROUND' | 'BG': bg_color_string = value
				case 'SIZE' | 'S': size = int(value)
				case 'HEIGHT' | 'H': height = int(value)
				case 'WIDTH' | 'W': width = int(value)
				case 'SQUARE' | 'SQ': height = width = int(value)
				case 'PADDING': padding = int(value)
				case 'GAP': gap = int(value)
				case 'OUT': output_image_path = value
				case _:
					print(f"Unknown key: '{key}'")
		elif arg.isnumeric():
			height = int(arg)
			width = height
		else:
			command = arg.upper()
			match command:
				case '4K':
					height, width = 2160, 3840
				case 'SQUARE':
					height = max(height, width)
					width = height
				case 'TRIANGLE':
					template = 'TRIANGLE'
				case 'HEXAGON':
					template = 'HEXAGON'
				case _:
					print(f"Unknown command: '{command}'")

	bg_color_string = bg_color_string or color_string
	match template:
		case 'DEFAULT':
			generate_wallpaper(
				color_string, bg_color_string=bg_color_string,
				size=size, width=width, height=height,
				padding=padding, gap=gap,
				output_image_path=output_image_path
			)
		case 'TRIANGLE':
			generate_triangle_wallpaper(image_size=(width, height), triangle_size=size, color_string=color_string)
		case 'HEXAGON':
			generate_hexagon_wallpaper(image_size=(width, height), hex_size=size, color_string=color_string)
		case _:
			print(f"Unknown template: '{template}'")


if __name__ == "__main__":
	main()
