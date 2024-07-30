from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("chatbot/", views.home, name="chatbot"),
    path("dashboard/", views.dashboard),
    path("api/dashboard/", views.dashboard_dataset),
    path("api/appointment/", views.schedule_appointment),
    path("api/get-appointments/", views.get_appointments),
    path(
        "api/reschedule-appointment/",
        views.reschedule_appointment,
        name="reschedule-appointment",
    ),
    path(
        "appointments/<int:pk>/delete/",
        views.delete_appointment,
        name="delete_appointment",
    ),
    path(
        "appointments/<int:appointment_id>/toggle-status/",
        views.toggle_appointment_status,
        name="toggle_appointment_status",
    ),
]
