from joblib import load
import os 
from django.conf import settings

def load_model():
    file_path = os.path.join(settings.BASE_DIR, "app/car-pridiction.model")
    model = load(file_path)
    return model