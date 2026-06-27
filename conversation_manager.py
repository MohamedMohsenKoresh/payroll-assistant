last_intent = None
last_topic = None
last_response = None


def save_context(intent, topic=None, response=None):

    global last_intent
    global last_topic
    global last_response

    last_intent = intent
    last_topic = topic
    last_response = response


def get_last_intent():

    return last_intent


def get_last_topic():

    return last_topic


def get_last_response():

    return last_response