
# PixelPython

This Python script generates a wallpaper with evenly sized rectangular patterns. The rectangles are all shades of a specified base color and are arranged to cover the entire image with optional padding and gaps.

![Red-4k](https://github.com/iaseth/pixelpython/blob/master/samples/red-4k.png?raw=true)

## Requirements
- Python 3.x
- Pillow (PIL)

To install dependencies, run:
```sh
pip install pillow
```

## Usage
Run the script with a specified hex color and rectangle size:
```sh
python pixelpython.py
```

The script accepts the following arguments:
- `color`: Base color in hex/name format (e.g., `"#6496C8"` or `"red"`)
- `background`: Background color in hex/name format
- `size`: Size of each rectangle (default: 110)
- `width`: Width of the wallpaper (default: 1920)
- `height`: Height of the wallpaper (default: 1080)
- `padding`: Padding around the edges (default: 0)
- `gap`: Gap between rectangles (default: 10)

## Output
The generated wallpaper is saved as `wallpaper.png` in the same directory.

## License
This project is open-source and available under the MIT License.

