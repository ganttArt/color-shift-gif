from PIL import Image
from modules.create_gif import create_gif
import argparse

IMAGE = "test.png"

parser = argparse.ArgumentParser(
    prog='Color Shift GIF',
    description='Python script that takes an image and turns it into a color changing GIF',
)
parser.add_argument('-nl', '--noloop', action='store_const',
                    const=True, default=False, help='turn off looping in the GIF')
args = parser.parse_args()


def main():
    with Image.open(IMAGE) as image:
        try:
            if image.format != 'JPEG':
                image = image.convert('RGB')
        except Exception:
            print('File type not compatible')
            return

        create_gif(image, noloop=args.noloop, filename=IMAGE)


if __name__ == '__main__':
    main()
