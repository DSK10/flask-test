import cv2
import mediapipe as mp
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils


class Detect():

  def process(self,filename):
    file = filename
    with mp_face_detection.FaceDetection(
        model_selection=1, min_detection_confidence=0.5) as face_detection:

      image = cv2.imread(file)
      # Convert the BGR image to RGB and process it with MediaPipe Face Detection.
      results = face_detection.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

      # Draw face detections of each face.
      if not results.detections:
        return None
      
      annotated_image = image.copy()
      bb = []

      for detection in results.detections:
        bbc = detection.location_data.relative_bounding_box
       
        x,y,w,h = bbc.xmin,bbc.ymin,bbc.width,bbc.height
        bb.append({"x":x,"y":y,"w":w,"h":h})
      return bb
print(Detect().process('2.jpg'))