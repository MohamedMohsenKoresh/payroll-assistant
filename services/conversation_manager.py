conversations = {}


def save_context(employee_id, intent, topic=None, response=None):

    history = conversations.get(employee_id, [])

    history.append(
        {
            "intent": intent,
            "topic": topic,
            "response": response
        }
    )

    conversations[employee_id] = history[-10:]


def get_last_context(employee_id):

    history = conversations.get(employee_id, [])

    if not history:
        return None

    return history[-1]


def get_last_intent(employee_id):

    context = get_last_context(employee_id)

    if context is None:
        return None

    return context["intent"]


def get_last_topic(employee_id):

    context = get_last_context(employee_id)

    if context is None:
        return None

    return context["topic"]


def get_last_response(employee_id):

    context = get_last_context(employee_id)

    if context is None:
        return None

    return context["response"]


def get_history(employee_id):

    return conversations.get(employee_id, [])


def clear_context(employee_id):

    conversations.pop(employee_id, None)