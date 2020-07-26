import logging
from os import environ
environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # FATAL
logging.getLogger('tensorflow').setLevel(logging.FATAL)

from typing import Iterable
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

from numpy import argmax
from pickle import load as pkl_load


class FullyConnected_NN:
    def __init__(self):
        #Setting hyperparameters
        self.vocab_size = 20000
        self.embedding_dim = 32
        self.oov_tok = "<OOV>"
        self.trunc_type='post'
        self.max_length = 220
        self.padding_type='post'

        with open('models/tokenizer.pkl', 'rb') as f:
            self.tokenizer = pkl_load(f)
        self.model = load_model('models/basic_model')

    def prepare_input(self,X:list):
        '''Convert input X to padded sequences'''
        sequences = self.tokenizer.texts_to_sequences(X)

        padded = pad_sequences(
                            sequences,
                            maxlen=self.max_length,
                            truncating=self.trunc_type,
                            padding=self.padding_type
                            )
        return padded

    def get_rating(self,sentence:str ):
        '''Takes as input path to model and a sentence.'''
        new_sent = [sentence]
        new_data = self.prepare_input(new_sent)
        rating = argmax( self.model.predict(new_data) ) + 1
        return rating

class GRU(FullyConnected_NN):
    def __init__(self):
        #Setting hyperparameters
        self.vocab_size = 20000
        self.embedding_dim = 32
        self.oov_tok = "<OOV>"
        self.trunc_type='post'
        self.max_length = 220
        self.padding_type='post'

        with open('models/gru_tokenizer.pkl', 'rb') as f:
            self.tokenizer = pkl_load(f)
        self.model = load_model('models/GRU_model')


if __name__ == "__main__":
    sentence = 'This is a decent and average product i guess.'
    obj = GRU()
    rating = obj.get_rating(sentence)
    print('Rating given by model is:',rating)


