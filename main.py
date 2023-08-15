from text_to_speech import TextToSpeech
from train_model import TrainModel

def main():
    # Initialize the classes
    tts = TextToSpeech()
    tm = TrainModel()

    # Train the model
    tm.train()

    # Convert text to speech
    tts.convert_text_to_speech()

if __name__ == "__main__":
    main()
