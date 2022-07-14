import cv2


def convert_to_sketch(image_to_sketch: str):
    """Converts image to sketch

    Args:
        image (str): png or jpeg file name to convert
    """
    image = cv2.imread(image_to_sketch)
    grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    invert = cv2.bitwise_not(grey_img)
    blur = cv2.GaussianBlur(invert, (21, 21), 0)
    inverted_blur = cv2.bitwise_not(blur)
    sketch = cv2.divide(grey_img, inverted_blur, scale=256.0)

    cv2.imwrite(f'sketch_{image_to_sketch}', sketch)


convert_to_sketch('car.png')