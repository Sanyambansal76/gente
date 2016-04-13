import requests
import json
import re

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from chatterbot import ChatBot
from bs4 import BeautifulSoup
# Create your views here.

@login_required
def gente(request):
    return render(request, 'genteai/gente.html',{})


def gente_reply(request):
    if request.is_ajax():
        a = "sa"
        chatbot = ChatBot("Robbo")
        message = request.POST["message"]
        if message[0:6]=="#info ":
            ulter_message = message[6:len(message)]
            if ulter_message != "" and ulter_message != " ":
                url = "https://en.wikipedia.org/wiki/" + ulter_message
                data = requests.get(url)
                soup = BeautifulSoup(data.content)
                send_data = soup.find("p")
                reply = send_data.text
            else:
                reply = "#info message"
        else:
            reply = chatbot.get_response(message)
        print reply

        response_data = {}
        response_data["message"] = reply
        print response_data

        return HttpResponse(json.dumps(response_data))
    else:
        return HttpResponse("Error")
        
        
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')
