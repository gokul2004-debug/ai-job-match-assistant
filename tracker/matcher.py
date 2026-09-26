SKILL_ALIASES = {
    'js': 'javascript',
    'javascript': 'javascript',
    'postgres': 'postgresql',
    'postgresql': 'postgresql',
    'py': 'python',
    'python': 'python',
}

def normalize(skill):
    skill = skill.strip().lower()
    return SKILL_ALIASES.get(skill, skill)

def calculate_match(my_skills, job_description):
    skills_list = [normalize(s) for s in my_skills.split(',')]
    job_text = job_description.lower()

    matched = [s for s in skills_list if s in job_text or normalize(s) in job_text]
    missing = [s for s in skills_list if s not in matched]

    score = int((len(matched) / len(skills_list)) * 100) if skills_list else 0

    return {
        'score': score,
        'matched_skills': matched,
        'missing_skills': missing
    }