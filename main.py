from PIL import Image, UnidentifiedImageError
from modules.create_gif import create_gif
import argparse

parser = argparse.ArgumentParser(
    prog='Color Shift GIF',
    description='Python script that takes an image and turns it into a color changing GIF',
)
parser.add_argument('-nl', '--noloop', action='store_const',
                    const=True, default=False, help='Turn off looping in the GIF')
parser.add_argument('-p', '--posterize', action='store_const',
                    const=True, default=False, help='Posterize setting')
parser.add_argument('-t', '--transparent', action='store_const',
                    const=True, default=False, help='Maintain transparency in image')
parser.add_argument(
    '-f', '--file', help='Input image file name. Include relative path if not in root directory')
parser.add_argument('-d', '--duration', default=10,
                    help='gif duration in seconds')
parser.add_argument('-dm', '--delaymotion', default=False,
                    help='delay motion in the gif by _ seconds (show first frame)')
args = parser.parse_args()

IMAGE = "assets/test-images/test.png"

if args.file:
    IMAGE = args.file


def main():
    try:
        with Image.open(IMAGE) as image:
            if image.format != 'JPEG' and not args.posterize and not args.transparent:
                image = image.convert('RGB')
            create_gif(
                image,
                noloop=args.noloop,
                posterize=args.posterize,
                filename=IMAGE,
                duration=args.duration,
                delay_motion=args.delaymotion
            )
    except UnidentifiedImageError:
        print('Error: file type not compatible')


if __name__ == '__main__':
    main()
