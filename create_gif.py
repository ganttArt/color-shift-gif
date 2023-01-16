import numpy as np
import colorsys

# Order:
# Convert original image array to hsv
# Create a bunch of hsv images, each being hue shifted, use colorsys, .01
# convert all of those to rgb
# Create video with those in opencv


def create_gif(image):
    image = np.array(image)
    images = [create_hsv_array_from_rgb(image)]

    for i in range(99):
        new_image = create_hue_shifted_array(images[i])
        images.append(new_image)


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

# def shift_hue(image):
#     new_image = np.zeros((image.shape))
#     for row in range(image.shape[0]):
#         for column in range(image.shape[1]):
#             pixel = shift_pixel_hue(image[row][column])
#             new_image[row][column] = pixel

#     return new_image


# def shift_pixel_hue(pixel):
#     print('rgb input', pixel)
#     hls = colorsys.rgb_to_hls(pixel[0], pixel[1], pixel[2])
#     print('hls', hls)
#     hue = hls[0]
#     hue += 1
#     if hue >= 360:
#         hue -= 360
#     print('hue', hue)
#     rgb = colorsys.hls_to_rgb(hue, hls[1], hls[2])
#     print('rgb', rgb)
#     return rgb

# print(shift_pixel_hue([10,150,80]))
