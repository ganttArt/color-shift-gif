from PIL import Image

IMAGE = "test.png"

def main():
    with Image.open(IMAGE) as image:
        try:
            if image.format != 'JPEG':
                image = image.convert('RGB')
        except Exception:
            print('File type not compatible')
            return
        
        image.show()

if __name__ == '__main__':
    main()
