import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox

def detect_emotion_from_image(image):
    try:
        faces, confidences = cv.detect_face(image)

        if not faces:
            return image, "No Face Detected"

        for face in faces:
            (startX, startY) = face[0], face[1]
            (endX, endY) = face[2], face[3]

            face_crop = image[startY:endY, startX:endX]
            label, confidence = cv.detect_gender(face_crop)

            # Just using gender detection to simulate response; replace with real emotion model if needed
            emotion = "Happy" if label[0] == "male" else "Surprised"

            cv.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)
            cv.putText(image, emotion, (startX, startY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

            return image, emotion

        return image, "Face Detected"
    except Exception as e:
        print(f"Error: {e}")
        return image, "Error"
