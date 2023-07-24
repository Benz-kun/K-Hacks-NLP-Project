import speech_recognition as msr
import pyaudio

r = msr.Recognizer()

# audio file which is 1:51 seconds long 
audio_test =    msr.AudioFile(r"/home/ben/Downloads/nlp test audio series/test_audio_4.wav")

with audio_test as source:
    #print("heklok")
    audio =  r.record(source)   
    #print(type(audio))
    text = r.recognize_google(audio)
    try:
        print(text)
    except:
        print("Error!!")

f = open('nlp_text.txt','a')
f.write(text)
f.close()

