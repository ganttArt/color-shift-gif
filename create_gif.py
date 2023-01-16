import numpy as np
import colorsys
from progress_bar import progress_bar
from PIL import Image
from pathlib import Path


def create_gif(image, filename='color-shifted'):
    # Create an numpy array from the image, and convert the rgb values to hsv, placing the new image array in a list
    image = np.array(image)
    images = [create_hsv_array_from_rgb(image)]

    # Create a list of numpy arrays that each have been hue shifted + .01
    for i in progress_bar(list(range(99)), prefix='Shifting hues:', length=40):
        new_image = create_hue_shifted_array(images[i])
        images.append(new_image)

    # Convert all of the hsv numpy arrays into rgb arrays, then into Image objects
    for i in progress_bar(list(range(100)), prefix='HSV to Image:', length=40):
        rgb = create_rgb_array_from_hsv_array(images[i])
        images[i] = Image.fromarray(rgb.astype(np.uint8))

    # Create a gif from all the Image objects
    gif = []
    for image in progress_bar(images, prefix='GIF synthesizing:', length=40):
        gif.append(image.convert("P", palette=Image.ADAPTIVE))
    gif[0].save(f'{Path(filename).stem}.gif', save_all=True,
                optimize=False, append_images=gif[1:], loop=0)


def create_hsv_array_from_rgb(image):
    hsv_image = np.zeros((image.shape))
    for row in range(image.shape[0]):
        for column in range(image.shape[1]):
            pixel = image[row][column]
            # Normalize rgb values to 0-1 range for colorsys conversion
            (r, g, b) = (
                pixel[0] / 255,
                pixel[1] / 255,
                pixel[2] / 255
            )
            (h, s, v) = colorsys.rgb_to_hsv(r, g, b)
            hsv_image[row][column] = [h, s, v]
    return hsv_image


def create_hue_shifted_array(image):
    shifted = np.zeros((image.shape))

    for row in range(image.shape[0]):
        for column in range(image.shape[1]):
            [h, s, v] = image[row][column]
            h += .01
            if h > 1:
                h -= 1
            shifted[row][column] = [h, s, v]

    return shifted


def create_rgb_array_from_hsv_array(image):
    rgb_image = np.zeros((image.shape))

    for row in range(image.shape[0]):
        for column in range(image.shape[1]):
            pixel = image[row][column]
            (h, s, v) = (pixel[0], pixel[1], pixel[2])
            (r, g, b) = colorsys.hsv_to_rgb(h, s, v)
            rgb_image[row][column] = [
                int(r * 255),
                int(g * 255),
                int(b * 255)
            ]

    return rgb_image
