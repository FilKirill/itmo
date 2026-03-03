import colorsys


def rgb_hsv(r, g, b):
    h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
    return h * 360, s * 100, v * 100


def hsv_rgb(h, s, v):
    r, g, b = colorsys.hsv_to_rgb(h / 360, s / 100, v / 100)
    return r * 255, g * 255, b * 255


for h in [60, 120, 180, -60, -120]:
    for s in [-33, -67]:
        h1, s1, v1 = (rgb_hsv(255, 5, 5))
        h2, s2, v2 = (rgb_hsv(250, 128, 5))
        h3, s3, v3 = (rgb_hsv(250, 250, 5))
        h4, s4, v4 = (rgb_hsv(128, 250, 5))
        print(hsv_rgb(h1 + h, s1 + s, v1))
        print(hsv_rgb(h2 + h, s2 + s, v2))
        print(hsv_rgb(h3 + h, s3 + s, v3))
        print(hsv_rgb(h4 + h, s4 + s, v4))
        print(s, h)
        print('')

