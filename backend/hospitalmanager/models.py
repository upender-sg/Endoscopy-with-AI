from django.db import models
from generic.models import UUIDModel, TimeStampedModel

class HospitalModel(UUIDModel, TimeStampedModel):
    hid = models.CharField(max_length= 200)
    name = models.CharField(max_length= 200)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    adderess = models.TextField()
    status = models.IntegerField(default=1)
class DepertmentModel(UUIDModel, TimeStampedModel):
    hospital_id = models.ForeignKey(HospitalModel, on_delete=models.CASCADE)
    depertment_name = models.CharField(max_length=200)
    status = models.IntegerField(default=1)

class StaffModel(UUIDModel, TimeStampedModel):
    COLOR_CHOICES = (
    ('doctor','DOCTOR'),
    ('anesthesia', 'ANESTHESIA'),
    ('nurse','NURSE'), )
    profession = models.CharField(max_length=12, choices=COLOR_CHOICES, default='doctor')
    hospital_id = models.ForeignKey(HospitalModel, on_delete=models.CASCADE)
    department_id = models.ForeignKey(DepertmentModel, on_delete=models.CASCADE)
    acount_id=  models.CharField(max_length= 200, default='')
    name =  models.CharField(max_length= 200)
    phone = models.CharField(max_length=20, default='')
    speciality =  models.TextField(default='')
    status = models.IntegerField(default=1)



