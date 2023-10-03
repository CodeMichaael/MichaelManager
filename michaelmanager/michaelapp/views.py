from rest_framework.decorators import api_view as app
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import serializers
from rest_framework import status

@app(["POST"])
def connections():
    pass






