def match_careers(answers):
    career_map = {
        "Engineering": ["technical", "math", "computer"],
        "Doctor": ["medical", "science"],
        "Graphic Designer": ["creative", "computer"],
        "Journalist": ["communication", "creative"],
        "Software Developer": ["computer", "math"],
        "Agriculturist": ["outdoor", "science"],
        "Chemist": ["science", "math"],
        "Teacher": ["communication", "math"]
    }

    result = []
    for career, tags in career_map.items():
        score = sum(1 for tag in tags if tag in answers)
        if score > 0:
            result.append((career, score))

    # Sort results by score
    result.sort(key=lambda x: x[1], reverse=True)
    return result

