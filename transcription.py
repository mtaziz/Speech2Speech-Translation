#Import dependencies

from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from os.path import join, dirname
import os
import json
from translate import Translator


filename = 'final.json'
audiofile = 'test.mp3'


#Initialize credentials

speech_to_text = SpeechToTextV1(
    iam_apikey='3I5oGXvgRKobstOJqRdqJocu6Qbyfib0BVZ7dyRyZNDW',
    url='https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/aa0dcee3-34bb-452f-ba41-b70c4432d3a6'
)


#Callback to the recoginze_using_sockets function to call after receiving response

class MyRecognizeCallback(RecognizeCallback):
    def __init__(self):
        RecognizeCallback.__init__(self)

    def on_connected(self):
        print('Connection was successful')

    def on_listening(self):
        print('Service is listening')


#Save the response JSON string in a local file named 'tran1.json' and appending ',' after every response to treat the response as a list for easier access from the file

    def on_data(self, data):
        with open(filename, 'a+') as outfile:
            json.dump(data, outfile, indent=2)
        with open(filename, 'a+') as outfile:
            outfile.write(',')


    def on_hypothesis(self, hypothesis):
        print(hypothesis+'\n')
        translate = Translator(to_lang='hi')
        translation = translate.translate(hypothesis)
        print(translation)
        print('')
        

    def on_error(self, error):
        print('Error received: {}'.format(error))
        print(error)#code, code_description
        # print(code, code_description)

    def on_inactivity_timeout(self, error):
        print('Inactivity timeout: {}'.format(error))

    def on_close(self):
        print("Connection closed")
        with open(filename,'a+') as filehandle:
            filehandle.seek(filehandle.tell()-1, os.SEEK_SET)
            filehandle.truncate()
            filehandle.write(']')


myRecognizeCallback = MyRecognizeCallback()


#Open file from local system and send using websockets

with open(filename,'w') as handle:
    handle.write('[')

with open(join(dirname(__file__), 'audio_files/mc1.mp3'),
              'rb') as audio_file:
    audio_source = AudioSource(audio_file)
    speech_to_text.recognize_using_websocket(audio=audio_source,
                                             content_type='audio/mp3',
                                             recognize_callback=myRecognizeCallback,
                                             model='en-US_NarrowbandModel',
                                             inactivity_timeout=10,
                                             speaker_labels=True,
                                             interim_results=True)