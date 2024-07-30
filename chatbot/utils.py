from datetime import datetime

help_list = [
    "schedule appointment",
    "check appointment",
    "check appointments",
    "reschedule appointment",
    "reschedule appointments",
    "appointment",
    "common cold",
    "mild headache",
    "minor cuts and scrapes",
    "mild indigestion or heartburn",
    "mild allergies",
    "mild diarrhea or constipation",
    "muscle aches or strains",
    "mild fever",
    "minor skin irritations",
    "sore throat",
]

responses = {
    "hello": "Hello! How can I help you today?",
    "hi": "Hi there! How can I assist you?",
    "good morning": "Good morning! How can I help you?",
    "good afternoon": "Good afternoon! How can I help you?",
    "good evening": "Good evening! How can I help you?",
    "schedule appointment": "The form below is provided for you to book an appointment. You'll get an immediate response if the appointment can be possible.",
    "reschedule appointment": "Extracting your booked appointments, please hold on...",
    "reschedule appointments": "Extracting your booked appointments for rescheduling, please hold on...",
    "check appointment": "Fetching your booked appointments for rescheduling, please hold on...",
    "check appointments": "Fetching your booked appointments, please hold on...",
    "appointment": "Do you want to schedule, check, or reschedule an appointment?",
}

sickness_info = {
    "common cold": {
        "symptoms": "Runny or stuffy nose, sore throat, coughing, sneezing, mild body aches",
        "remedies": "Rest, fluids, over-the-counter cold remedies",
    },
    "mild headache": {
        "symptoms": "Stress, dehydration, tension",
        "remedies": "Drinking water, resting, over-the-counter pain relievers like ibuprofen or acetaminophen",
    },
    "minor cuts and scrapes": {
        "symptoms": "Small cuts or scrapes on the skin",
        "remedies": "Clean the wound with soap and water, apply antiseptic, cover with a bandage",
    },
    "mild indigestion or heartburn": {
        "symptoms": "Discomfort or burning sensation in the stomach or chest",
        "remedies": "Dietary adjustments, over-the-counter antacids",
    },
    "mild allergies": {
        "symptoms": "Sneezing, runny nose, itchy eyes",
        "remedies": "Over-the-counter antihistamines",
    },
    "mild diarrhea or constipation": {
        "symptoms": "Frequent loose stools or difficulty in bowel movements",
        "remedies": "Dietary changes, increased fluid intake, over-the-counter medications",
    },
    "muscle aches or strains": {
        "symptoms": "Soreness or stiffness in muscles",
        "remedies": "Rest, ice packs, compression, elevation (RICE), over-the-counter pain relievers",
    },
    "mild fever": {
        "symptoms": "Low-grade fever",
        "remedies": "Rest, fluids, fever reducers like acetaminophen or ibuprofen",
    },
    "minor skin irritations": {
        "symptoms": "Sunburn, insect bites, mild rashes",
        "remedies": "Over-the-counter creams, antihistamines, soothing lotions like aloe vera",
    },
    "sore throat": {
        "symptoms": "Pain or irritation in the throat",
        "remedies": "Rest, warm fluids, throat lozenges, over-the-counter pain relievers",
    },
}

unrecognized_message = """
I'm sorry, I didn't understand that, but here's what I can do for you.\n
<ul>
<li>Schedule appointments</li>
<li>Check appointments</li>
<li>Reschedule appointments</li>
<li>Route patients to the appropriate departments</li>
<li>Provide information on common illnesses, symptoms, and remedies</li>
</ul>
"""


def compare_processor(data) -> bool:
    for text in help_list:
        words = text.split()
        if data in words:
            return True
    return False


def chatbot_exec(data):
    data = data.lower()
    check_help_list = [word for word in data.split() if compare_processor(word)]

    if not check_help_list:
        return responses.get(data, unrecognized_message)
    elif len(check_help_list) == 1:
        text = "{}".format(check_help_list[0])
        if text in sickness_info:
            info = sickness_info[text]
            return f"{text.capitalize()}:\nSymptoms: {info['symptoms']}\nRemedies: {info['remedies']}"
        else:
            return responses.get(text, unrecognized_message)
    elif len(check_help_list) >= 2:
        text = "{} {}".format(check_help_list[0], check_help_list[1])
        if responses.get(text):
            return responses.get(text, unrecognized_message)
        else:
            print(sickness_info[text])
            return sickness_info[text]
    else:
        return None


def datetime_converter(dt):
    """
    The function `datetime_converter` takes a datetime object as input and returns a formatted date
    string in the format "Day DD Month YYYY".

    :param dt: The parameter `dt` is a datetime object that represents a specific date and time
    :return: a formatted date string in the format "Day Month Year".
    """
    try:
        dt_object = datetime.strptime(str(dt), "%Y-%m-%d %H:%M:%S.%f%z")
        formatted_date = dt_object.strftime("%a %d %b %Y")
        return formatted_date
    except:
        dt_object = datetime.strptime(str(dt), "%Y-%m-%d %H:%M:%S%z")
        formatted_date = dt_object.strftime("%a %d %b %Y")
        return formatted_date
