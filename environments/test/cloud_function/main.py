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
        print(face.anger_likelihood, " ",face.joy_likelihood, " ",
         face.surprise_likelihood, " ", face.sorrow_likelihood)
    
def main(event , context):
    #print("Ira       Alegria      Sorpresa     Pena")
    emo_detect()
