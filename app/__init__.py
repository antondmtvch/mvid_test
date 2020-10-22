from flask import Flask
from app.helpers import load_dataset

app = Flask(__name__)

from app import views

app.config.from_object('config.DevelopmentConfig')
app.config.from_mapping(
    DATA=load_dataset(app.config['DATASET_PATH'])
)
