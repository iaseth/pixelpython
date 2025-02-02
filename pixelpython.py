import random
import sys

from PIL import Image, ImageDraw
from pypixel import generate_rectangle_wallpaper, generate_triangle_wallpaper, generate_hexagon_wallpaper



def main():
	random.seed(0)
	args = sys.argv[1:]

	template = "RECTANGLE"
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

				case 'RECTANGLE': template = 'RECTANGLE'
				case 'TRIANGLE': template = 'TRIANGLE'
				case 'HEXAGON': template = 'HEXAGON'

				case _:
					print(f"Unknown command: '{command}'")

	bg_color_string = bg_color_string or color_string
	match template:
		case 'RECTANGLE':
			generate_rectangle_wallpaper(
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
