import cv2
import numpy as np

def quantize_color(img, levels=8):
    bins = np.linspace(0, 255, levels).astype(np.uint8)
    out = np.zeros_like(img)
    for i in range(3): 
        inds = np.digitize(img[:, :, i], bins, right=True)
        inds = np.clip(inds, 0, len(bins) - 1)
        out[:, :, i] = bins[inds]
    return out

def cartoonize_frame(frame, edge_thickness=1, color_levels=8):
    # 1. Detect edges
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    edges = cv2.dilate(edges, np.ones((edge_thickness, edge_thickness), np.uint8))

    # 2. Reduce colors
    quant = quantize_color(frame, levels=color_levels)

    edges_inv = cv2.bitwise_not(edges)
    edges_color = cv2.cvtColor(edges_inv, cv2.COLOR_GRAY2BGR)
    cartoon = cv2.bitwise_and(quant, edges_color)

    return cartoon

def cartoonize_video(input_file, output_file, color_levels=8, edge_thickness=1):
    cap = cv2.VideoCapture(input_file)
    if not cap.isOpened():
        print("Can't open video:", input_file)
        return

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height= int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

    print("Processing video...")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cartoon = cartoonize_frame(frame, edge_thickness, color_levels)
        out.write(cartoon)

    cap.release()
    out.release()
    print("Done! Saved as", output_file)

if __name__ == "__main__":
    cartoonize_video('my_video.mp4', 'cartoon_output.avi', color_levels=6, edge_thickness=2)
