#########################
#########################
# Bibliotecas para o RASA
from sys import path
path.append(".")
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import FollowupAction
from rasa_sdk.events import SlotSet
from . import *

#########################
# Outras bibliotecas
import random
import requests
import xml.etree.ElementTree as ET
import helpers.util as util
from unicodedata import normalize
##from datetime import datetime

#########################
# Scripts que serão executados ao iniciar o servidor de ações
#from scripts.cleanModels import *
#########################