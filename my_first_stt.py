import speech_recognition as msr
import pyaudio

r = msr.Recognizer()

'''with msr.Microphone() as source:
    print("Speak something: ")
    audio = r.listen(source)

    p = pyaudio.PyAudio()
    try:
        print(p.get_default_input_device_info())
    except:
        print("No mics availiable")

    try:
        text = r.recognize_google(audio)
        print("This is what you just said: ")

    except:
        print("Could not recognize the voice!")'''
    
audio_test =    msr.AudioFile(r"/home/ben/Downloads/nlp test audio series/Stt_audio_test_3.wav")

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