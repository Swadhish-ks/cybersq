import cv2
def load_image(path):
    image = cv2.imread(path)
    if image is None:
        print("Error: Could not load image.")
    return image
def image_type():
    print('ENTER THE IMAGE TYPE YOU WANT TO CONVERT:')
    print('1. Grayscale')
    print('2. BINARY')
    print('3. ORGINAL IMAGE')
    choice = int(input('ENTER YOUR CHOICE (1/2/3): '))
    return choice

def convert_image(image, choice):
    if choice == 1:
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    elif choice == 2:
        _, binary_img = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
        return binary_img
    elif choice == 3:
       return image
    else:
        print("Invalid choice. Returning original image.")
        return image
    
def display_image(window_name, image):
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
path = "opencv/img.jpg"
image = load_image(path)
choice = image_type()
converted_image = convert_image(image, choice)
display_image("Converted Image", converted_image)