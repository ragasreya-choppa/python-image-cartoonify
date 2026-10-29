import tkinter as tk
from tkinter import filedialog

import cv2
import matplotlib.pyplot as plt

top = tk.Tk()
top.geometry("400x400")
top.title("Cartoonify Your Image !")
top.configure(background="white")

def cartoonify(image_path):
    original_image = cv2.imread(image_path)

    if original_image is None:
        print("Error: Unable to read the selected image.")
        return
    print("Image Loaded SuccessFully!")

    height, width, channels = original_image.shape
    print("Image Height:", height)
    print("Image Width:", width)
    print("Image Channels:", channels)

    rgb_image = cv2.cvtColor(
        original_image, cv2.COLOR_BGR2RGB
    )
    print("BGR to RGB conversion successful")
    print("RGB image shape: ", rgb_image.shape)

    gray_scale_image = cv2.cvtColor(
        rgb_image, cv2.COLOR_RGB2GRAY
    )
    print("Grayscale conversion successful!")
    print("Grayscale image shape: ", gray_scale_image.shape)

    smooth_gray_scale = cv2.medianBlur(
        gray_scale_image, 5
    )
    print("Median Blurring Successful!")
    print("Smoothed Grayscale image shape: ", smooth_gray_scale.shape)

    edge_mask = cv2.adaptiveThreshold(
        smooth_gray_scale,
        255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY,
        9,
        9
    )

    print("Adaptive Thresholding Successful!")
    print("Edge mask shape: ", edge_mask.shape)


    color_image = cv2.bilateralFilter(
        rgb_image,
        9,
        300,
        300
    )

    print("Bilateral Filtering Successful!")
    print("Smoothed Color Image shape: ", color_image.shape)

    cartoon_image = cv2.bitwise_and(
        color_image,
        color_image,
        mask=edge_mask
    )
    print("Cartoon image created successfully!")
    print("Cartoon image shape: ", cartoon_image.shape)

    fig, axes = plt.subplots(1,2, figsize=(12, 6))

    axes[0].imshow(rgb_image)
    axes[0].set_title("Original Image")
    axes[0].axis('off')

    axes[1].imshow(cartoon_image)
    axes[1].set_title("Cartoonified Image")
    axes[1].axis('off')

    plt.tight_layout()
    plt.show()
    save_cartoon(cartoon_image)



def save_cartoon(cartoon_image):
    save_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[
            ("PNG Image", "*.png"),
            ("JPEG Image", "*.jpg")
        ],
        initialfile = "cartoonified_image.png"
    )

    if not save_path:
        print("Image Saving Cancelled")
        return

    bgr_cartoon = cv2.cvtColor(
        cartoon_image,
        cv2.COLOR_RGB2BGR
    )

    success = cv2.imwrite(save_path, bgr_cartoon)

    if success:
        print("Cartoon Image Saved SuccessFully!")
        print("Saved at:", save_path)
    else:
        print("Error! Unable to save the cartoon Image!")


def upload():
    image_path = filedialog.askopenfilename(
        title = "Select an Image",
        filetypes=[("Image Files", ("*.jpg", "*.jpeg", "*.png")), ("All Files", "*.*")],
    )

    if image_path:
        print("Selected Image: ", image_path)
        cartoonify(image_path)
    else:
        print("No Image Selected!")


upload_button = tk.Button(
    top,
    text="Cartoonify an Image",
    command=upload,
    padx=10,
    pady=5,
    bg="#364156",
    fg="white",
    font=("Calibri", 10, "bold")
)

upload_button.pack(side=tk.TOP, pady=50)

top.mainloop()
