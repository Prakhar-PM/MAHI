# MAHI
# AI Chatbot  This repository contains code for an AI-powered chatbot that uses deep learning techniques to understand and respond to user queries. The chatbot can handle a variety of intents, including greetings, farewells, asking for the time and date.
This project is an AI-powered chatbot built using deep learning and natural language processing (NLP) techniques. The chatbot is capable of understanding and responding to user queries based on predefined intents and patterns. It incorporates speech recognition to capture user input and text-to-speech to provide spoken responses, making interactions more natural and user-friendly.

The neural network model is implemented using PyTorch, and the project includes all necessary steps for data preprocessing, model training, and evaluation. The chatbot can handle various tasks such as greetings, farewells, providing the current time and date, and fetching information from Wikipedia.

Features
Neural Network: A three-layer feed-forward neural network for intent classification.
Speech Recognition: Uses the speech_recognition library to capture and recognize spoken words.
Text-to-Speech: Uses the pyttsx3 library for converting text responses into spoken words.
NLP Techniques: Tokenization, stemming, and bag-of-words for text preprocessing.
JSON Configuration: Intents, patterns, and responses are stored in a JSON file for easy modification and expansion.
Datetime Functions: Fetches and provides the current time and date.
Wikipedia Integration: Fetches summaries from Wikipedia for user queries.

Requirements
Python 3.x
PyTorch
speech_recognition
pyttsx3
nltk
wikipedia-api

Training the Model:

Run the script to train the neural network model:
python train.py
This will preprocess the data, train the model, and save the trained model to a file.
Run the main script to start the chatbot:
python main.py

