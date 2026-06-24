# Video Cartoonizer Tool (Image Processing)
A Python-based Digital Image Processing application that transforms standard video files into stylized cartoon animations. Built using **OpenCV** and **NumPy**, the project processes video frames in real-time, executing sequential pipeline steps: edge detection, color quantization, and mask compositing.

## Key Highlights
- **Custom Color Quantization:** Developed an independent quantization function using NumPy vectorization (`np.digitize` and `np.clip`) to map 256 color spaces into distinct step levels without heavy ML clustering.
- **Edge Extraction Pipeline:** Utilizes Canny Edge Detection coupled with Morphological Dilation to produce thick, bold cartoonish outlines.
- **Frame-by-Frame Video Processing:** Streamlines standard MP4 streams into highly optimized AVI container sequences via `cv2.VideoWriter`.

## How the Algorithm Works (Pipeline)
1. **Grayscale Conversion:** Reduces the input frame color dimensionality to prepare for gradient analysis.
2. **Canny Edge Detection:** Computes intensity gradients to capture sharp structural borders.
3. **Morphological Dilation:** Extends edge pixels to increase line thickness (`edge_thickness`).
4. **Color Levels Reduction:** Bins pixel intensities down to customized buckets (e.g., 6 levels) to create flat shading.
5. **Mask Masking & Compositing:** Inverts the black-and-white edge map and merges it with the quantized frame using a bitwise AND operation (`cv2.bitwise_and`).

## Requirements
- Python 3
- OpenCV (`opencv-python`)
- NumPy

## How to Run
1. Place your target video file in the project directory and name it `my_video.mp4` (or update the filename path inside `main.py`).
2. Install the necessary libraries:
   ```bash
   pip install opencv-python numpy
