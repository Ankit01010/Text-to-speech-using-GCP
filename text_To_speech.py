from google.cloud import speech




client = speech.SpeechClient.from_service_account_file('key.json')




file name= "myaudio.mp3"


with open(file_name, 'rb') as f :
    mp3_data=f.read()


audi_file=speech.RecognitionAudio(content=mp3_data)


config= speech.RecognitionAudio(
    sample_rate_hertz=44100,
    enable_automatic_punctuation=True,
    language_code='en-US' 
) 



response=client.recognize(
    config=config,
    audio=audio_file
)


for result in response.results:
    print("Transcript : {} ".format(result.alternative[0].transcript))

