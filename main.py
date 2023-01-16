from PIL import Image
from create_gif import create_gif

IMAGE = "test.png"

def main():
    with Image.open(IMAGE) as image:
        try:
            if image.format != 'JPEG':
                image = image.convert('RGB')
        except Exception:
            print('File type not compatible')
            return
        
        create_gif(image)

if __name__ == '__main__':
    main()
