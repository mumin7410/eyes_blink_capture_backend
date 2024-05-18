from PIL import Image
from io import BytesIO
import base64
from deepface import DeepFace
import os
import tempfile


class FaceRecognition:
    def __init__(self):
        self.result = ''
    
    def decode_base64(self, base64_string):
        image_data = base64.b64decode(base64_string)
        image = Image.open(BytesIO(image_data))

        # Create a temporary file to save the image
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.jpg')
        image.save(temp_file.name)

        return temp_file.name
    
    def run_Facerecognition(self, base64_image):

        image_path = self.decode_base64(base64_image)
        result = DeepFace.find(
            img_path=image_path,
            db_path="./api/faces",
            model_name='VGG-Face',
            enforce_detection=False
        )
        if len(result[0]) == 0:
            os.remove(image_path)
            print("not found")
            return "not found"
        else:
            os.remove(image_path)
            print("found")
            return "found"
        
    

if __name__ == "__main__":
    fr = FaceRecognition()
    fr.run_recognition()