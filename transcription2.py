#Import dependencies

from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from os.path import join, dirname
import os
import json
# from translate import Translator
from googletrans import Translator
from pathlib import Path

#Initialize credentials

speech_to_text = SpeechToTextV1(
    iam_apikey='3I5oGXvgRKobstOJqRdqJocu6Qbyfib0BVZ7dyRyZNDW',
    url='https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/aa0dcee3-34bb-452f-ba41-b70c4432d3a6'
)

#Read all Audio files from directory
directory_in_str = str("E:\\UG's Workspace\\College\\Project\\CODE\\audio_files")

pathlist = Path(directory_in_str).glob('**/*.mp3')

#Names of all the audio files
file_list = []

for path in pathlist:
    path_in_str = str(path)
    file_list.append(str(path_in_str[51:]))

#Iterate over all the names and store the corresponding JSON files and transcripts in their respective directories
for i in file_list:


    #Naming JSON and transcript files based on the audio file
    filename = 'json_results/'+i+'.json'
    translation_file = 'transcript_results/'+i+'.txt'
    audiofile = 'audio_files/'+i


    #Callback to the recoginze_using_sockets function to call after receiving response

    class MyRecognizeCallback(RecognizeCallback):
        def __init__(self):
            RecognizeCallback.__init__(self)
            # self.final_true = False

        def on_connected(self):
            print('Connection was successful')

        def on_listening(self):
            print('Service is listening')

        
    #Save the response JSON string in a local JSON file and local txt file; also, appending ',' after every response to treat the response as a list for easier access from the file

        def on_data(self, data):
            with open(filename, 'a+') as outfile:
                json.dump(data, outfile, indent=2)
            with open(filename, 'a+') as outfile:
                outfile.write(',')
            
            result_test = data['results']
            if(result_test[0]['final'] is True):
                with open(translation_file, 'a+') as outfile:
                    transcript_extraction = result_test[0]['alternatives']
                    transcript_text = transcript_extraction[0]['transcript']
                    json.dump(transcript_text, outfile, indent=2)
                with open(translation_file, 'a+') as outfile:
                    outfile.write(',')

    #Display the interim results
        def on_hypothesis(self, hypothesis):
            print(hypothesis)
                

        def on_error(self, error):
            print('Error received: {}'.format(error))
            print(error)#code, code_description
            # print(code, code_description)

        def on_inactivity_timeout(self, error):
            print('Inactivity timeout: {}'.format(error))

        def on_close(self):
            print("Connection closed")

            #End the list in the files
            
            with open(filename,'a+') as filehandle:
                filehandle.seek(filehandle.tell()-1, os.SEEK_SET)
                filehandle.truncate()
                filehandle.write(']')
            
            with open(translation_file,'a+') as filehandle:
                filehandle.seek(filehandle.tell()-1, os.SEEK_SET)
                filehandle.truncate()
                filehandle.write(']')


    myRecognizeCallback = MyRecognizeCallback()


    #Start the list in the files

    with open(filename,'w') as handle:
        handle.write('[')

    with open(translation_file,'w') as handle:
        handle.write('[')

    #Open file from local system and send using websockets

    with open(audiofile, 'rb') as audio_file:
        audio_source = AudioSource(audio_file)
        speech_to_text.recognize_using_websocket(audio=audio_source,
                                                content_type='audio/mp3',
                                                recognize_callback=myRecognizeCallback,
                                                model='en-US_NarrowbandModel',
                                                word_confidence=True,
                                                audio_metrics=True,
                                                smart_formatting=True,
                                                inactivity_timeout=10,
                                                speaker_labels=True,
                                                interim_results=True)

#Testing

# translate = Translator(to_lang='hi')
# translation = translate.translate(hypothesis)
# print(translation)

# translator = Translator()
# # #Language selection for translation
# destination = 'hi'
# translation = translator.translate(hypothesis, dest=destination)
# print(translation.text)