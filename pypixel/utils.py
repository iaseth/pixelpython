import json



with open('colors.json') as f:
	colors_json = json.load(f)
	colors = colors_json['colors']


def get_rgb_components(color_string):
	if color_string.startswith("#"):
		color_string = color_string.lstrip("#")
		return tuple(int(color_string[i:i+2], 16) for i in (0, 2, 4))
	else:
		for color in colors:
			if color['name'].upper() == color_string.upper():
				return get_rgb_components(color['code'])


