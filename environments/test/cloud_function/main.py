from __future__ import print_function
from google.cloud import vision


def emo_detect():
    
    uri_base = 'gs://project1-test-346303-input'
    pic = ('image_to_analyze.jpg')
    
    client = vision.ImageAnnotatorClient()
    image = vision.Image()

           
    image.source.image_uri = '%s/%s' % (uri_base, pic)
    response = client.face_detection(image=image)

    faces = response.face_annotations
        
    for face in faces:
        print("Anger: " + str(face.anger_likelihood), " Joy: "+ str(face.joy_likelihood), " Surprice: " +
         str(face.surprise_likelihood), " Sorrow: "+ str(face.sorrow_likelihood))
    
def main(event , context):
    emo_detect()
