# import the packages required
import IPython
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

apikey = '3PcEPv1M3BoE7HwCDrfgHfz-dgE_sa_BLrL6pSihFjN2' # your apikey
url = 'https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/90007e7b-9aef-49b1-825c-98767191dfae' # Your url endpoint

# instantiate the TextToSpeech with apikey and set the service url
T2S = TextToSpeechV1(IAMAuthenticator(apikey))
T2S.set_service_url(url)

def speak_text(text):
    
    with open('./audio/temp.mp3', 'wb') as audio_file:
        response = T2S.synthesize(text, accept = 'audio/mp3', voice = 'en-US_AllisonV3Voice').get_result()
        audio_file.write(response.content)
        
    return IPython.display.Audio('./audio/temp.mp3', autoplay = True)

