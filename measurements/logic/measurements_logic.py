from ..models import Measurement
from ..models import Variable

def get_measurements():
    return Measurement.objects.all()

def get_measurement(id):
    return Measurement.objects.get(pk=id)

def update_measurement(id, data):
    measurement = get_measurement(id)
    measurement.variable = Variable.objects.get(pk=data['variable'])
    measurement.value = data['value']
    measurement.unit = data['unit']
    measurement.place = data['place']
    measurement.save()
    return measurement

def create_measurement(data):
    measurement = Measurement(
        variable = Variable.objects.get(pk=data['variable']),
        value = data['value'],
        unit = data['unit'],
        place = data['place'],
    )
    measurement.save()
    return measurement

def delete_measurement(id):
    measurement = get_measurement(id)
    measurement.delete()
    return measurement

