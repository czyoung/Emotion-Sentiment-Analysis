#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 13:34:41 2018

"""

import requests
import json
 
def analyze_tone(text):
    username = 'ENTER USERNAME HERE'
    password = 'ENTER PASSWORD HERE'
    watsonUrl = 'https://gateway.watsonplatform.net/tone-analyzer/api/v3/tone?version=2016-05-19'
    headers = {"content-type": "text/plain"}
    data = text
    try:
        r = requests.post(watsonUrl, auth=(username,password),headers = headers,
         data=data)
        return r.text
    except:
        return False
 
def welcome():
    message = "Welcome to the IBM Watson Tone Analyzer\n"
    print(message + "-" * len(message) + "\n")
    message = "How it works"
    print(message)
    message = "Perhaps a bit too aggressive in your emails? Are your blog posts a little too friendly? Tone Analyzer might be able to help. The service uses linguistic analysis to detect and interpret emotional, social, and writing cues found in text."
    print(message)
    print()
    print("Have fun!\n")
 
def display_results(data):
    data = json.loads(str(data))
    tempResults = ""
    print(data)
    for i in data['document_tone']['tone_categories']:
        print(i['category_name'])
        tempResults += i['category_name'] + "\n"
        print("-" * len(i['category_name']))
        tempResults += "-" * len(i['category_name']) + "\n"
        for j in i['tones']:
            print(j['tone_name'].ljust(20),(str(round(j['score'] * 100,1)) + "%").rjust(10))
            tempResults += j['tone_name'] + "\t" + str(round(j['score'] * 100,1)) + "%" + "\n"
        print()
        tempResults += "\n"
    print()
    tempResults += "\n"
    return tempResults
 
def highest_tone(data):
    data = json.loads(str(data))
    tempScore = 0
    highestTone = "None"
    for tone in data['document_tone']['tone_categories'][0]['tones']:
        if tone['score'] > tempScore:
            tempScore = tone['score']
            highestTone = tone['tone_name']
    
    print("{}: {}".format(highestTone,tempScore))
    return highestTone
        
def main():
    welcome()
     
    data = input("Enter some text to be analyzed for tone analysis by IBM Watson (Q to quit):\n")
    if len(data) >= 1:
        if data == 'q'.lower():
            exit
        results = analyze_tone(data)
        if results != False:
            display_results(results)
            exit
        else:
            print("Something went wrong")
 