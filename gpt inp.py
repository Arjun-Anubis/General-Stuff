# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 17:09:22 2021

@author: anubi
"""



import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# initialize tokenizer and model from pretrained GPT2 model
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')
while True: 
    seq = input("prompt : ")

    print(tokenizer.decode(model.generate(tokenizer.encode(seq, return_tensors='pt'), max_length=2000, do_sample=True)[0], skip_special_tokens=True))