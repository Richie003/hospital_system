from datetime import datetime

help_list = ["schedule appointment", "check appointment", "appointment"]

responses = {
    "hello": "Hello! How can I help you today?",
    "hi": "Hi there! How can I assist you?",
    "good morning": "Good morning! How can I help you?",
    "good afternoon": "Good afternoon! How can I help you?",
    "good evening": "Good evening! How can I help you?",
    "schedule appointment": "The form below is provided for you to book an appointment, you'll get an immediate response if the appointment can be possible.",
    "check appointment": "Fetching your booked appointments, please hold on...",
    "appointment": "Do you want schedule, check or reschedule an appointment",
}

unrecognized_message = """
I'm sorry, I didn't understand that, but here's what I can do for you.\n
<ul>
<li>Schedule appointments</li>
<li>Check appointments</li>
<li>Rescheduling appointments</li>
<li>Routing patients to the appropriate departments</li>
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
    elif len(check_help_list) >= 2:
        text = "{} {}".format(check_help_list[0], check_help_list[1])
        return responses.get(text, unrecognized_message)
    elif len(check_help_list) == 1:
        text = "{}".format(check_help_list[0])
        return responses.get(text, unrecognized_message)
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
