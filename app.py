import pickle
from flask import Flask, request, jsonify, render_template, app
import numpy as np 
import pandas as pd 

app = Flask(__name__)