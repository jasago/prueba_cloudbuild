from __future__ import print_function
from google.cloud import vision

def emo_detect():
    uri_base = 'gs://project1-test-346303-input'
    
    pics = ('image_to_analyze.jpg')



    client = vision.ImageAnnotatorClient()
    image = vision.Image()

    for pic in pics:
        print("entro")
        image.source.image_uri = '%s/%s' % (uri_base, pic)
        response = client.face_detection(image=image)

        # print('=' * 30)
        # print('File:', pic)
        for face in response.face_annotations:
            print("entro 2")
            print(face.anger_likelihood, "    ", face.joy_likelihood, "   ",
              face.surprise_likelihood, "     ", face.sorrow_likelihood)
            print("paso")
    print("termino")
def main(event , context):
    print("image num       anger       joy      surprice     sorrow")
    emo_detect()
