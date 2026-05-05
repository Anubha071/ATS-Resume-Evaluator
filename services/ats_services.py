from utils.prompts import ats_prompt
from services.openai_services import get_completion

def get_ats_analysis(resume_text, job_description, job_profile):
    prompt = ats_prompt(resume_text, job_description, job_profile)
    response = get_completion(prompt)
    return response