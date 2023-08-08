from dataprocessor import DataProcessor
from modeltrainer import ModelTrainer
from predictor import Predictor

def main():
    # Load and preprocess data
    dp = DataProcessor('data.csv')
    dp.load_data()
    dp.preprocess_data()

    # Train model
    mt = ModelTrainer(dp.data)
    mt.train_model()
    mt.save_model('model.pkl')

    # Make predictions
    pred = Predictor('model.pkl')
    pred.load_model()
    predictions = pred.predict(dp.data)

    print(predictions)

if __name__ == "__main__":
    main()
