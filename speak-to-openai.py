import openai
import speech_recognition as sr
import pyttsx3
import os
# Initialize the speech recognition and text-to-speech engines
r = sr.Recognizer()
engine = pyttsx3.init()
LISTEN = True

# Set up the OpenAI API credentials and configuration
openai.api_key = os.environ.get('OPENAI_API_KEY', '')
openai_model = "text-davinci-002"
openai_completion = {
    "model": openai_model,
    "temperature": 0.5,
    "max_tokens": 1024,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0
}

# Define a function to process the speech input using OpenAI's GPT-3
def process_input(text):
    # Use the OpenAI API to generate a response text
    openai_completion = {
        "max_tokens": 60,
        "temperature": 0.7,
    }
    response = openai.Completion.create(model=openai_model, prompt=text, **openai_completion)
    response_text = response.choices[0].text.strip()

    # Return the response text
    return response_text


# Define a function to generate speech output
def generate_output(text):
    # Set the text-to-speech engine properties
    engine.setProperty('rate', 150)   # Speed percent (can go over 100)
    engine.setProperty('volume', 1)  # Volume 0-1

    # Say the text using the text-to-speech engine
    engine.say(text)
    engine.runAndWait()

# Start the speech recognition loop
while LISTEN:
    # Listen for audio input
    with sr.Microphone() as source:
        print("Speak now...")
        audio = r.listen(source)

    # Convert audio to text using speech recognition
    try:
        text = r.recognize_google(audio)
        print("You said: " + text)

        # Process the input text using OpenAI's GPT-3
        response_text = process_input(text)

        # Generate speech output from the response text
        generate_output(response_text)
        input_text = text.lower()
        if 'thank you' in input_text:
            LISTEN = False
            exit()

    except sr.UnknownValueError:
        print("Sorry, I didn't understand that. Please try again.")
    except sr.RequestError as e:
        print("Sorry, I'm having trouble connecting to the speech recognition service. Please try again later.")
