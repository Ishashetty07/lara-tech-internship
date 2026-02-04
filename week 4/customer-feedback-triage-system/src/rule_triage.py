def rule_based_triage(feedback):

    text = feedback.lower()

    if any(w in text for w in ["crash", "error", "not working", "fail", "bug"]):
        category = "Complaint"
        urgency = "High"
        action = "Escalate"

    elif any(w in text for w in ["add", "feature", "support", "enable", "request"]):
        category = "Feature Request"
        urgency = "Medium"
        action = "Forward"

    elif any(w in text for w in ["love", "great", "thanks", "awesome"]):
        category = "Praise"
        urgency = "Low"
        action = "Ignore"

    elif any(w in text for w in ["how", "what", "where", "can i"]):
        category = "Question"
        urgency = "Low"
        action = "Respond"

    else:
        category = "Question"
        urgency = "Low"
        action = "Respond"

    return {
        "category": category,
        "urgency": urgency,
        "action": action,
        "reasoning": "Rule-based keyword matching."
    }
