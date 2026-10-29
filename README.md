# Image Cartoonification Using Python and OpenCV

A Python desktop application that converts photographs into cartoon-style images using image-processing techniques.

This project reconstructs a Cartoonify application originally documented as part of a Machine Learning internship.

## Features

- Select a JPG, JPEG, or PNG image using a file dialog.
- Convert images between BGR, RGB, and grayscale formats.
- Reduce noise using median filtering.
- Generate a black-and-white edge mask using adaptive thresholding.
- Smooth colors using bilateral filtering.
- Combine the edge mask with the smoothed image to produce a cartoon effect.
- Display the original and cartoonified images side by side.
- Save the processed image as PNG or JPEG.

## Technologies Used

- **Python** — Programming language
- **OpenCV** — Image processing
- **Tkinter** — Desktop interface and file dialogs
- **Matplotlib** — Image visualization
- **NumPy** — Array-based image representation through OpenCV

## How to Run

1. Clone this repository.
2. Open the project folder in PyCharm or another Python development environment.
3. Create and activate a Python virtual environment.
4. Install the required packages using `pip install -r requirements.txt`.
5. Run `python main.py`.
6. Click **Cartoonify an Image**, select a photograph, and view the result.
7. Choose a location to save the cartoonified image.

## Image Processing Workflow

Image Upload → BGR-to-RGB Conversion → Grayscale Conversion → Median Blurring → Adaptive Thresholding

In parallel, bilateral filtering smooths the original RGB image. The resulting color image and edge mask are combined using `cv2.bitwise_and()`.

## Project Background

The original application was documented during a Machine Learning internship at Intrainz. This version was reconstructed to revisit Python programming, computer vision, image processing, and desktop application development.

The provided implementation uses traditional image-processing techniques rather than a trained machine learning model.
