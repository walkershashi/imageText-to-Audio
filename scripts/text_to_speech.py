# import the packages required
import IPython
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

apikey = '' # your apikey
url = '' # Your url endpoint

# instantiate the TextToSpeech with apikey and set the service url
T2S = TextToSpeechV1(IAMAuthenticator(apikey))
T2S.set_service_url(url)

def speak_text(text):
    
    with open('./audio/temp.mp3', 'wb') as audio_file:
        response = T2S.synthesize(text, accept = 'audio/mp3', voice = 'en-US_AllisonV3Voice').get_result()
        audio_file.write(response.content)
        
    return IPython.display.Audio('./audio/temp.mp3', autoplay = True)

