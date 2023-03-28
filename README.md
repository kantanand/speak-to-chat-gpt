# speak-to-chat-gpt
This code listens for audio input using the microphone, 
converts the audio to text using the Google Speech-to-Text API, 
sends the text to the Chat GPT API endpoint (which requires an API key), 
and generates speech output from the response text using the pyttsx3 text-to-speech library.  

Note that this is just a basic example, and you'll need to customize it for your specific use case. You may also want to add error handling, adjust the speech recognition and text-to-speech engine settings, and modify the Chat GPT processing function to fit your specific Chat GPT implementation.

GET openai api key from 
https://platform.openai.com/


# setup python env
- python -m venv env
- source env/bin/activate
- export OPENAI_API_KEY="your api key need to go ghere"


# install python libs 
pip install -r requirements 

# run 
python speak-to-openai.py

# exampls 
say: tell me about python 

For exiting this applicatoin  
say: thank you 
