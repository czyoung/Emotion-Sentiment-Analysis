#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 14:18:46 2018

"""

messageNum = 0

from socket import *
import toneAnalyzer
import time

def sendMessage(message):
    global messageNum
    
    #Create a UDP socket
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    
    #Set a timeout value of 1 second
    clientSocket.settimeout(1)
    
    addr = ("127.0.0.1", 11000)
    
    message = "t:" + str(messageNum) + ";s:127.0.0.1;p:10000;d:" + message
    
    #Send message
    clientSocket.sendto(message.encode(), addr)
    
    messageNum += 1
    
    #If data is received back from server, print
    try:
        data, server = clientSocket.recvfrom(1024)
        print (data)
        
    except timeout:
        print ("REQUEST TIMED OUT")

#sendMessage("arousal=54")

'''
message= input('Give a command:')

while(message != "q"):
    sendMessage(message)
    
    message = input('Give a command:')
'''
'''
response = input("Type a Message!:\n")
sendMessage("message=" + response)
'''
response = input("Type a sentence:\n")
'''
results = analyze_tone(response) 
display_results(results)
'''

while(response != "q"):
    results = analyze_tone(response)
    tone = highest_tone(results)
    message = display_results(results)
    if tone == 'Joy':
        sendMessage("arousal=27")
        sendMessage("pleasure=100")
        sendMessage("talking=true")
        sendMessage("message= I'm glad to hear you are happy!")
        time.sleep(3)
    elif tone == 'Anger':
        sendMessage("arousal=100")
        sendMessage("pleasure=-100")
        sendMessage("talking=true")
        sendMessage("message= I think you should just take a deep breath and count to ten.")
        time.sleep(3)
    elif tone == 'Sadness':
        sendMessage("arousal=-36")
        sendMessage("pleasure=-71")
        sendMessage("talking=true")
        sendMessage("message= I'm sorry. Is there anything I can do to help?")
        time.sleep(3)
    elif tone == 'Fear':
        sendMessage("arousal=100")
        sendMessage("pleasure=0")
        sendMessage("talking=true")
        sendMessage("message= It'll be alright.")
        time.sleep(3)
    elif tone == 'Disgust':
        sendMessage("arousal=50")
        sendMessage("pleasure=-60")
        sendMessage("talking=true")
        sendMessage("message= I suggest you think of the sweet smell of fresh beautiful roses.")
        time.sleep(3)
  
    sendMessage("talking=false")
    sendMessage("message=" + message)

    response = input("Type a sentence:\n")  
    
    
    
    
    
    
    
    