from django import forms
from .models import Appointment, Inquiry, Doctor


class AppointmentForm(forms.ModelForm):
    date = forms.DateTimeField(
        input_formats=["%Y-%m-%dT%H:%M"],
        widget=forms.DateTimeInput(
            attrs={
                "type": "datetime-local",
            },
            format="%Y-%m-%dT%H:%M",
        ),
    )

    class Meta:
        model = Appointment
        fields = ["doctor", "date", "reason"]
        widgets = {
            "date": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "reason": forms.Textarea(attrs={"rows": 3}),
        }


class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ["patient", "question", "answer"]
        widgets = {
            "question": forms.Textarea(attrs={"rows": 3}),
            "answer": forms.Textarea(attrs={"rows": 3}),
        }


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ["name", "specialty", "capacity"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Doctor Name"}),
            "specialty": forms.TextInput(attrs={"placeholder": "Specialty"}),
            "capacity": forms.NumberInput(attrs={"min": 0}),
        }
