#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return None
    a = len(sentence)
    b = sentence[0]
    return a, b
