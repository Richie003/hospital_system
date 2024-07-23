from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from auth_bot.models import UserBio


class Appointment(models.Model):
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    doctor = models.ForeignKey("Doctor", on_delete=models.CASCADE)
    date = models.DateTimeField()
    reason = models.TextField()
    closed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.patient)

    @property
    def get_user_info(self):
        try:
            bio = UserBio.objects.get(for_user_id=self.patient.id)
            return [bio.tel, bio.for_user.email]
        except:
            return [None, None]


class Inquiry(models.Model):
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question = models.TextField()
    answer = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.patient


class Doctor(models.Model):
    name = models.CharField(max_length=100, default="", blank=True)
    specialty = models.CharField(max_length=100, default="", blank=True)
    capacity = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return str(self.name)
