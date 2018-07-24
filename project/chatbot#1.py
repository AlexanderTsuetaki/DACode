# chatbot.py
# Example of XML parsing.
# 01-27-2016
__author__="Alexander Tsuetaki"
import sys
import string
import xml.etree.ElementTree as ET
import random

import xml.etree.ElementTree as ET

def remove_punctuation(input):
    s = input # Sample string
    out = s.translate(string.maketrans("",""), string.punctuation)
    return out
def split_example(split_phrase):
    phrase = split_phrase.split(" ")
    return(phrase)
def destroy_plurals(word):
    if word[-1]=="s":
        word = word[0:len(word)-1]
    return word

def interact_with_user(replies, comp_says, comp_replies):
    reply = raw_input(comp_says).lower()
    reply = remove_punctuation(reply)
    user_reply = split_example(reply)
    user_reply = destroy_plurals(user_reply)
    #matches = [i for i in user_reply if i in replies]
    counter=0
    for word in user_reply:
        for i in range(0,len(replies)):
            if word == replies[i]:
                print comp_replies[i]

            else:
                counter+=1
    if counter== len(user_reply)*len(replies):
        comp_replies[len(comp_replies)-1]



def main():
    test = ET.parse('chatbot.xml')
    root = test.getroot()
    for item in root:
        replies = []
        comp_says = ""
        comp_replies = []
        for element in item:
            if element.tag == 'say':
                comp_says = element.text
            elif element.tag == 'responses':
                replies = element.text.split(", ")
            elif element.tag == 'option':
                comp_replies.append(element.text)
        interact_with_user(replies, comp_says, comp_replies)
    print('Thank you for your time! I hope to see you again')

if __name__ == "__main__":
    main()


