# Test to see if creating a cache for the hue shift algorithm (rgb to hsv, shift hue, back to rgb) to improve run time would make sense.
# Conclusion. Too memory intensive and dubiously quicker. The cache would be .5gb and takes a long time to load from json in Python.

import colorsys
import json
from progress_bar import progress_bar


def shift_rgb_hue(r, g, b):
    [hue, s, v] = colorsys.rgb_to_hsv(r/255, g/255, b/255)
    hue += .01
    if hue > 1:
        hue -= 1
    (red, green, blue) = colorsys.hsv_to_rgb(hue, s, v)
    return red, green, blue


def create_cache():
    cache = {}

    for r in progress_bar(list(range(256)), prefix='r', length=64):
        for g in range(256):
            for b in range(256):
                red, green, blue = shift_rgb_hue(r, g, b)
                cache[f'[{r}, {g}, {b}]'] = [int(red), int(green), int(blue)]

    return cache


CACHE = create_cache()
print('cache created')
with open("cache.json", "w") as outfile:
    json.dump(CACHE, outfile)
