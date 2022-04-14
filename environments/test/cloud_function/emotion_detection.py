from __future__ import print_function
from google.cloud import vision

def get_most_likely(face):
    anger = str(face.anger_likelihood)
    joy = str(face.joy_likelihood)
    suprice = str(face.surprise_likelihood)
    return True

def emo_detect(uri_base, pic):

    client = vision.ImageAnnotatorClient()
    image = vision.Image()
    image.source.image_uri = 'gs://%s/%s' % (uri_base, pic)

    response = client.face_detection(image=image)# pylint: disable=no-member
    face = response.face_annotations[0]

    return get_most_likely(face)

    # for face in faces:
    #     print("Anger: " + str(face.anger_likelihood),
    #      " Joy: "+ str(face.joy_likelihood), " Surprice: " +
    #      str(face.surprise_likelihood), " Sorrow: "+ str(face.sorrow_likelihood))