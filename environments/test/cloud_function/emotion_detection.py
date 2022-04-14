from __future__ import print_function
from google.cloud import vision

def emo_detect(uri_base, pic):

    client = vision.ImageAnnotatorClient()
    image = vision.Image()
    image.source.image_uri = 'gs://%s/%s' % (uri_base, pic)

    response = client.face_detection(image=image)# pylint: disable=no-member
    faces = response.face_annotations

    print(type(faces))
    print(faces[0])
    # for face in faces:
    #     print("Anger: " + str(face.anger_likelihood),
    #      " Joy: "+ str(face.joy_likelihood), " Surprice: " +
    #      str(face.surprise_likelihood), " Sorrow: "+ str(face.sorrow_likelihood))
    return True