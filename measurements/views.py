from django.shortcuts import render

from .logic import measurements_logic as ml
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def measurements_view(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        if id is not None:
            measurement_dto = ml.get_measurement(id)
            measurement = serializers.serialize('json', [measurement_dto,])
            return HttpResponse(measurement, content_type='application/json')
        else:
            measurements_dto = ml.get_measurements()
            measurements = serializers.serialize('json', measurements_dto)
            return HttpResponse(measurements, content_type='application/json')
    elif request.method == 'POST':
        data = json.loads(request.body)
        measurement_dto = ml.create_measurement(data)
        measurement = serializers.serialize('json', [measurement_dto,])
        return HttpResponse(measurement, content_type='application/json')

@csrf_exempt
def measurement_view(request, id):
    if request.method == 'GET':
        measurement_dto = ml.get_measurement(id)
        measurement = serializers.serialize('json', [measurement_dto,])
        return HttpResponse(measurement, content_type='application/json')

    elif request.method == 'PUT':
        measurement_dto = ml.update_measurement(id, json.loads(request.body))
        measurement = serializers.serialize('json', [measurement_dto,])
        return HttpResponse(measurement, content_type='application/json')

    elif request.method == 'DELETE':
        measurement_dto = ml.delete_measurement(id)
        measurement = serializers.serialize('json', [measurement_dto,])
        return HttpResponse(measurement, content_type='application/json')

