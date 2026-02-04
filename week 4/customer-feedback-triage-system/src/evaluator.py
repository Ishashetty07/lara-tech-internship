def compare(ai_result, rule_result):

    return {
        "category_match": ai_result["category"] == rule_result["category"],
        "urgency_match": ai_result["urgency"] == rule_result["urgency"]
    }
