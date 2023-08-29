from django.shortcuts import render
from .forms import CarPredictionForm
from .machineLearningModel import load_model
import numpy as np

def maxMin(input):
    minVal = 0
    maxVal = 400
    result = (input - minVal)/(maxVal - minVal)
    return result


def z_Score(input):
    mean = 19.405247616118118
    std = 3.9714218411022917
    result = (input - mean)/std
    return result

def mock_model_predict(data):

    mileage = z_Score(data['mileage'])

    maxPower = maxMin(data['max_power'])
    
    year = maxMin(data['year'])

    data_array = np.array([year,maxPower,mileage]).reshape(1, -1)
    model_instance = load_model()
    result = model_instance.predict(data_array)
    return f"Predicted price is about {int(np.exp(result[0]))} $"

def predict_car(request):
    prediction = ''

    if request.method == 'POST':
        form = CarPredictionForm(request.POST)
        if form.is_valid():
            mileage = form.cleaned_data['mileage']
            max_power = form.cleaned_data['max_power']
            year = form.cleaned_data['year']
            input_data = {'mileage': mileage, 'max_power': max_power,'year':year}
            prediction = mock_model_predict(input_data)
    else:
        form = CarPredictionForm()

    return render(request, 'car_input_page.html', {'form': form, 'prediction': prediction})
