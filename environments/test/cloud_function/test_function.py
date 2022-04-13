import main

def test_emo_detect():
    
    #public data
    test_uri_base = 'cloud-vision-codelab'
    test_pic = 'face_surprise.jpg'

    result = main.emo_detect(test_uri_base, test_pic)

    assert result is True


