from imageai.Detection import ObjectDetection
from IPython.display import Image
import os

execution_path = os.getcwd()

detector = ObjectDetection()

detector.setModelTypeAsRetinaNet()
detector.setModelPath(os.path.join(execution_path, "retinanet_resnet50_fpn_coco-eeacb38b.pth"))
detector.loadModel()

detection = detector.detectObjectsFromImage(
    input_image=os.path.join(execution_path, "1258082_720.jpg"),
    output_image_path=os.path.join(execution_path, "imagenew.jpg"),
)

for eachItem in detection:
    print(eachItem["name"], " : ", eachItem["percentage_probability"])

Image(filename='imagenew.jpg')