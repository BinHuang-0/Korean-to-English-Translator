import tensorflow as tf

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

import unicodedata
import re
import numpy as np
import os
import io
import time

current_path = os.getcwd()
corpus_path = current_path + "/kor.txt"

#preprocessing text
def preprocess_sentence(w):
    w = re.sub(r"([?.!,])", r" \1 ", w)
    w = re.sub(r'[" "]+', " ", w)
    #w = re.sub(r"[^a-zA-Z?.!,]+", " ", w)
    w = w.strip()
    w = '<start>' + w + ' <end>'
    return w

ko_sentence = u"안녕하세요!"
en_sentence = u"Hello!"

print(preprocess_sentence(ko_sentence))
print(preprocess_sentence(en_sentence))

exit()
