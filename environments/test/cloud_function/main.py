import emotion_detection

def main(event , context):

    uri_base = event['bucket'] #Bucket donde esta la imagen
    pic = event['name']        #Nombre de la imagen a analizar

    emotion_detection.emo_detect(uri_base, pic) #Detectar las emociones
