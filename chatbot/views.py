from django.shortcuts import render
from django.http import JsonResponse
from .models import Appointment, Inquiry, Doctor
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .utils import chatbot_exec, datetime_converter
from .forms import AppointmentForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json
from .decorators import authorized_user


def index(request):
    return render(request, "home.html", {})


@login_required
@csrf_exempt
def home(request):
    form = AppointmentForm
    if request.method == "POST":
        data = json.loads(request.body)
        message = data.get("data", "")
        response = chatbot_exec(message)
        return JsonResponse({"response": response})
    context = {
        "form": form,
    }
    return render(request, "chat_bot.html", context)


@csrf_exempt
def schedule_appointment(request):
    if request.method == "POST":
        try:
            patient = request.user
            doctor = request.POST["doctor"]
            date = request.POST["date"]
            reason = request.POST["reason"]
            get_doctor_capacity = Doctor.objects.get(id=int(doctor))
            if get_doctor_capacity.capacity < 5:
                appointment = Appointment(
                    patient=patient, doctor_id=doctor, date=date, reason=reason
                )
                appointment.save()
                get_doctor_capacity.capacity += 1
                get_doctor_capacity.save()
                return JsonResponse(
                    {"success": "Appointment scheduled successfully."}, safe=False
                )
            else:
                return JsonResponse(
                    {
                        "filled": f"Appointment with {get_doctor_capacity.name} is not possible."
                    },
                    safe=False,
                )
        except Exception as e:
            return JsonResponse({"error": str(e)}, safe=False)


def get_appointments(request):
    if request.method == "GET":
        appointments = Appointment.objects.filter(patient_id=request.user.id)
        if appointments:
            data = [
                {
                    "reason": i.reason,
                    "date": i.date,
                }
                for i in appointments
                if i.closed != True
            ]
            return JsonResponse(data, safe=False)
        else:
            return JsonResponse(
                {"not_found": "No appointment available for you."}, safe=False
            )


def handle_inquiry(request):
    if request.method == "POST":
        patient = request.user
        question = request.POST["question"]
        inquiry = Inquiry(patient=patient, question=question)
        inquiry.save()
        answer = f"Your question was: {question}"
        inquiry.answer = answer
        inquiry.save()
        return JsonResponse({"status": "success", "answer": answer})


@login_required
def dashboard(request):
    get_appointments = Appointment.objects.filter(closed=False)
    context = {"appointments": get_appointments}
    return render(request, "dashboard.html", context)


def dashboard_dataset(request):
    get_appointments = Appointment.objects.all()
    if request.method == "GET":
        data = [
            {
                "id": i.id,
                "patient": i.patient.email,
                "doctor": i.doctor.name,
                "reason": i.reason,
                "short": f"{i.reason[0:30]}...",
                "date": datetime_converter(i.date),
                "status": i.closed,
                "tel": i.get_user_info[0],
                "email": i.get_user_info[1],
            }
            for i in get_appointments
        ]
        if data:
            return JsonResponse({"appointments": data}, safe=False)
        else:
            return JsonResponse({"appointments": []}, safe=False)


def delete_appointment(request, pk):
    if request.method == "POST":
        appointment = get_object_or_404(Appointment, pk=pk)
        appointment.delete()
        return JsonResponse(
            {"success": True, "message": "Appointment deleted successfully"}
        )
    return JsonResponse({"success": False, "message": "Invalid request"}, status=400)


def toggle_appointment_status(request, appointment_id):
    if request.method == "POST":
        appointment = get_object_or_404(Appointment, id=appointment_id)
        appointment.closed = not appointment.closed
        appointment.save()
        return JsonResponse(
            {
                "success": True,
                "message": f"Appointment {'closed' if appointment.closed else 're-opened'} successfully.",
            }
        )
    return JsonResponse({"success": False, "message": "Invalid request method."})
