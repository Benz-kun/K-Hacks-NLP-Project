Project Update

After a while of research i decided to go forward with Mozilla's DeepSpeech model as my primary API. The code works and audio is recognised but the calrity and accuracy is not upto the mark. Working currently to change these faults and make it a better transcriber.

The file mic_vad_streaming is the current code which i am using to get my real time conversion. It contains the following libraries:
deepspeech, pyaudio, wave, webrtcvad, halo , scripy with other modules like Portaudio installed for Audio detection. 
The model and scorer to initiate the program was taken from the deepspeech examples github repository.
