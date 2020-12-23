from textblob import TextBlob
import pandas as pd
def senti(purposes):
    purpose_max = -100#Store a max value
    purpose_min = 100#Store a min value
    purpose_max_str = " " #Create an empty str for max
    purpose_min_str = " " #Create an empty str for min
    for sentence in purposes:
        sentence = sentence.replace("[", '').replace("]", '').replace("'", '').replace(",", '')
        if "Purpose" in sentence:
            blob = TextBlob(sentence)
            sent_pos = blob.sentiment[0]
            sent_neg = blob.sentiment[0]
            if sent_pos > purpose_max:
                purpose_max = sent_pos
                purpose_max_str = sentence
            if sent_neg < purpose_min:
                purpose_min = sent_neg
                purpose_min_str = sentence
    print("The best idea is:",purpose_max_str,purpose_max)
    print('\n')
    print("The worst idea is:",purpose_min_str,purpose_min)

if __name__ == "__main__":
    with open("combine.txt")as c:
        senti(c)