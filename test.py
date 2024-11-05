from PIL import Image

# Open an image file
with Image.open("example.jpg") as img:
    # Display the original image
    img.show()

    # Perform some operations
    # Convert the image to grayscale
    grayscale_img = img.convert("L")

    # Resize the image
    resized_img = grayscale_img.resize((100, 100))

    # Save the modified image
    resized_img.save("modified_image.jpg")


def add(a: float, b: float) -> float:
    return a + b
