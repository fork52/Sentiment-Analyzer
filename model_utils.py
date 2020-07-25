import logging
from os import environ
environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # FATAL
logging.getLogger('tensorflow').setLevel(logging.FATAL)

from typing import Iterable
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

from numpy import argmax
from pickle import load as pkl_load

#Setting hyperparameters
vocab_size = 20000
embedding_dim = 32
oov_tok = "<OOV>"
trunc_type='post'
max_length = 220
padding_type='post'

def prepare_input(X:list):
    '''Convert input to'''
    with open('models/tokenizer.pkl', 'rb') as f:
        tokenizer = pkl_load(f)

    sequences = tokenizer.texts_to_sequences(X)

    padded = pad_sequences(
                           sequences,
                           maxlen=max_length,
                           truncating=trunc_type,
                           padding=padding_type
                        )
    return padded

def get_rating(model_path:str , sentence:str ):
    '''Takes as input path to model and a sentence.'''
    model = load_model(model_path)
    new_sent = [sentence]
    new_data = prepare_input(new_sent)
    rating = argmax( model.predict(new_data) ) + 1
    return rating

if __name__ == "__main__":
    sentence = 'This is a decent and average product i guess.'
    rating = get_rating('models/basic_model',sentence)
    print('Rating given by model is:',rating)


