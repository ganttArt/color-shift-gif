from PIL import Image, UnidentifiedImageError
from modules.create_gif import create_gif
import argparse

IMAGE = "assets/test-images/test.png"

parser = argparse.ArgumentParser(
    prog='Color Shift GIF',
    description='Python script that takes an image and turns it into a color changing GIF',
)
parser.add_argument('-nl', '--noloop', action='store_const',
                    const=True, default=False, help='turn off looping in the GIF')
parser.add_argument('-p', '--posterize', action='store_const',
                    const=True, default=False, help='posterize setting')
args = parser.parse_args()


def main():
    try:
        with Image.open(IMAGE) as image:
            if image.format != 'JPEG' and not args.posterize:
                image = image.convert('RGB')
            create_gif(image, noloop=args.noloop, posterize=args.posterize, filename=IMAGE)
    except UnidentifiedImageError:
        print('Error: file type not compatible')


if __name__ == '__main__':
    main()
