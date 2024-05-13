# -*- coding: utf-8 -*-
"""
Created on Mon May 13 23:41:49 2024

@author: Sarfarazuddin
"""

import json
import requests


url = ''


input_data_for_model = {
    
    'pregnancies' : 6,
    'Glucose' : 148,
    'BloodPressure' : 72,
    'SkinThickness' : 35,
    'Insulin' : 0,
    'BMI' : 33.6,
    'DiabetesPedigreeFunction' : 0.627,
    'Age' : 50
    
    }

input_json = json.dumps(input_data_for_model)

response = requests.post(url, data=input_json)

print(response.text)