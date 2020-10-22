import pandas as pd
from flask import Flask

app = Flask(__name__)

from app import views

app.config.from_object('app.config.DevelopmentConfig')
app.config.from_mapping(
    DATA=pd.read_feather(app.config['HD5_PATH'], columns=app.config['DATASET_COLS'])
)
