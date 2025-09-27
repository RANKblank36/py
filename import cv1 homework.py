import cv2

image_path = 'dog.jpeg'
image = cv2.imread(image_path)

if image is None:
    print(f"Error: Unable to load image at {image_path}")
    exit()

sizes = {
    'small': (200, 200),
    'medium': (400, 400),
    'large': (600, 600)
}

for label, dimensions in sizes.items():
    resized = cv2.resize(image, dimensions)
    
    window_name = f"{label.capitalize()} Image"
    cv2.imshow(window_name, resized)

    output_filename = f"input_image_{label}.jpeg"
    cv2.imwrite(output_filename, resized)
    print(f"Saved: {output_filename}")

cv2.waitKey(0)
cv2.destroyAllWindows()
