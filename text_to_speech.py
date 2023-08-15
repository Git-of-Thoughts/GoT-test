from gtts import gTTS

class TextToSpeech:
    def __init__(self):
        pass

    def convert_text_to_speech(self, text):
        # Convert the text to speech
        speech = gTTS(text=text, lang='en', slow=False)

        # Save the speech audio into a file
        speech.save("output.mp3")
