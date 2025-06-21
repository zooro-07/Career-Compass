career_map = {
    "math": ["Data Analyst", "Accountant"],
    "tech": ["Software Engineer", "Cybersecurity Analyst"],
    "social": ["Teacher", "Psychologist"],
    "art": ["Graphic Designer", "Animator"],
    "science": ["Research Scientist", "Lab Technician"],
}

college_map = {
    "Data Analyst": ["MIT", "Stanford"],
    "Accountant": ["Harvard", "UPenn"],
    "Software Engineer": ["Caltech", "CMU"],
    "Cybersecurity Analyst": ["Georgia Tech"],
    "Teacher": ["NYU", "UConn"],
    "Psychologist": ["UCLA", "UC Berkeley"],
    "Graphic Designer": ["RISD", "Parsons"],
    "Animator": ["CalArts"],
    "Research Scientist": ["Oxford", "Cambridge"],
    "Lab Technician": ["Johns Hopkins"],
}

def match_careers(answers):
    matched = {}
    for val in answers:
        for career in career_map.get(val, []):
            matched[career] = college_map.get(career, [])
    return matched
