def chatbot_response(message):
    message = message.lower()

    responses = {
        "hello": "Hi there! How can I help you with your career today?",
        "what is career compass": "Career Compass is a tool to help you discover suitable careers, courses, and colleges based on your interests.",
        "how does this work": "You take a quiz based on your interests. Based on your responses, we suggest careers, courses, and colleges that fit you.",
        "thank you": "You're welcome! 😊",
        "bye": "Goodbye! Wish you success in your career journey!"
    }

    for keyword in responses:
        if keyword in message:
            return responses[keyword]

    return "I'm not sure how to respond to that. Try asking about careers, courses, or how the quiz works!"
