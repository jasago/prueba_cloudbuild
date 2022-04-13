from __future__ import print_function
from google.cloud import vision

def emo_detect(uri_base, pic):
    client = vision.ImageAnnotatorClient()
    image = vision.Image()
    image.source.image_uri = '%s/%s' % (uri_base, pic)
    response = client.face_detection(image=image)# pylint: disable=no-member
    faces = response.face_annotations

    for face in faces:
        print("Anger: " + str(face.anger_likelihood),
         " Joy: "+ str(face.joy_likelihood), " Surprice: " +
         str(face.surprise_likelihood), " Sorrow: "+ str(face.sorrow_likelihood))
    return True

def main(event , context):
    uri_base = 'gs://project1-test-346303-input' #Bucket donde esta la imagen
    pic = 'image_to_analyze.jpg' #Imagen a analizar

    emo_detect(uri_base, pic) #Detectar las emociones

    # print(event['bucket'])
    # print(event['name'])
    print(event.bucket)
    print(event.name)
