import numpy as np
import colorsys
from modules.progress_bar import progress_bar
from PIL import Image
from pathlib import Path


def duration_to_milliseconds_per_frame(duration):
    frames_per_second = 100 / float(duration)  # 100 frames in output gif
    seconds_per_frame = 1 / frames_per_second * 1000
    return seconds_per_frame


def create_gif(image, noloop, posterize, filename, duration):
    # Create an numpy array from the image, and convert the rgb values to hsv, placing the new image array in a list
    image_array = np.array(image)
    hsv_array, transparency_detected = create_hsv_array_from_rgb(image_array)
    images = [hsv_array]

    # Create a list of numpy arrays that each have been hue shifted + .01
    for i in progress_bar(list(range(99)), prefix='Shifting hues:', length=40):
        new_image = create_hue_shifted_array(images[i])
        images.append(new_image)

    # Convert all of the hsv numpy arrays into rgb arrays, then into Image objects
    for i in progress_bar(list(range(100)), prefix='HSV to Image:', length=40):
        rgb = create_rgb_array_from_hsv_array(images[i])
        images[i] = Image.fromarray(rgb.astype(np.uint8))

    # For posterized gif, end with a frame of the input image that is not posterized
    if posterize and noloop:
        image = image.convert('RGB')
        images.append(image)

    # Create a gif from all the Image objects
    file_settings = {}
    if not noloop:
        file_settings['loop'] = 0
    if transparency_detected:
        file_settings['transparency'] = 0

    milliseconds_per_frame = duration_to_milliseconds_per_frame(duration)

    gif = []
    for image in progress_bar(images, prefix='GIF synthesizing:', length=40):
        gif.append(image.convert("P", palette=Image.ADAPTIVE))

    gif[0].save(f'{Path(filename).stem}.gif', save_all=True,
                optimize=False, append_images=gif[1:], duration=milliseconds_per_frame, **file_settings)


def create_hsv_array_from_rgb(image):
    transparency_detected = False
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
            try:
                alpha = pixel[3]
                if (alpha < 255):
                    transparency_detected = True
                    alpha = 0
                hsv_image[row][column] = [h, s, v, alpha]
            except IndexError:
                hsv_image[row][column] = [h, s, v]

    if transparency_detected:
        print('Transparency detected in image. All semi-transparent pixel will turn fully transparent')

    return hsv_image, transparency_detected


def create_hue_shifted_array(image):
    shifted = np.zeros((image.shape))

    for row in range(image.shape[0]):
        for column in range(image.shape[1]):
            hue = image[row][column][0]
            saturation = image[row][column][1]
            value = image[row][column][2]

            hue += .01
            if hue > 1:
                hue -= 1

            try:
                alpha = image[row][column][3]
                shifted[row][column] = [hue, saturation, value, alpha]
            except IndexError:
                shifted[row][column] = [hue, saturation, value]

    return shifted


def create_rgb_array_from_hsv_array(image):
    rgb_image = np.zeros((image.shape))

    for row in range(image.shape[0]):
        for column in range(image.shape[1]):
            pixel = image[row][column]
            (h, s, v) = (pixel[0], pixel[1], pixel[2])
            (r, g, b) = colorsys.hsv_to_rgb(h, s, v)

            try:
                alpha = pixel[3]
                rgb_image[row][column] = [
                    int(r * 255),
                    int(g * 255),
                    int(b * 255),
                    alpha
                ]
            except IndexError:
                rgb_image[row][column] = [
                    int(r * 255),
                    int(g * 255),
                    int(b * 255)
                ]

    return rgb_image
