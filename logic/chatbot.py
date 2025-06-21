def chatbot_response(message):
    message = message.lower()
    if "engineer" in message:
        return "Engineering is a versatile career — you can choose from mechanical, civil, computer, or electrical!"
    elif "ai" in message or "artificial" in message:
        return "AI is a booming field. Top careers include ML engineer, AI researcher, and data scientist."
    elif "biology" in message:
        return "If you love biology, consider careers like doctor, biologist, or geneticist."
    elif "college" in message:
        return "Top colleges include MIT, Harvard, Stanford, IITs and NITs depending on the field."
    else:
        return "I'm here to help! Ask me about careers, colleges, or subjects you love."
