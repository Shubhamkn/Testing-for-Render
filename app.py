import pandas as pd
import numpy as np
from flask import Flask, render_template, requests

app = Flask(__name__) 

@app.route('/', methods = ['GET'])
def index():
        return render_template('index.html')
