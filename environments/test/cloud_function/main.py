from __future__ import print_function
from google.cloud import vision

def emo_detect():
    uri_base = 'gs://project1-test-346303-input'
    
    pics = ('image_to_analyze.jpg')



    client = vision.ImageAnnotatorClient()
    image = vision.Image()

    for pic in pics:
        image.source.image_uri = '%s/%s' % (uri_base, pic)
        response = client.face_detection(image=image)

        # print('=' * 30)
        # print('File:', pic)
        for face in response.face_annotations:
            print(face.anger_likelihood, "    ", face.joy_likelihood, "   ",
              face.surprise_likelihood, "     ", face.sorrow_likelihood)
            # likelihood = vision.Likelihood(face.surprise_likelihood)
            # vertices = ['(%s,%s)' % (v.x, v.y) for v in face.bounding_poly.vertices]
            # print('Face surprised:', likelihood.name)
            # print('Face bounds:', ",".join(vertices))

def main(event , context):
    print("image num       anger       joy      surprice     sorrow")
    emo_detect()
