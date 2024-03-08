from ultralytics import YOLO

# load a pretrained YOLOv9 model
model = YOLO('yolov9c.pt')

# Run inference on an image
results = model.predict('img1.jpg')

# Display results to screen
results[0].show()