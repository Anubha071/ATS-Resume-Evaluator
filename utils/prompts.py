def ats_prompt(resume_text, job_description, job_profile):
    prompt = f"""
    ✨ You are an expert career coach and resume strategist. Your mission is to analyze the provided resume and job description, then craft a tailored resume that is fully optimized for Applicant Tracking Systems (ATS) and highlights the candidate's most relevant skills and experiences for the specified job profile. 🚀

    📄 Resume Text:
    {resume_text}

    📑 Job Description:
    {job_description}

    🎯 Job Profile:
    {job_profile}
    
    Please provide your evaluation in the following format:

    ⭐ Score: [Your Score out of 100]  
    📝 Explanation: [A concise explanation of the score, highlighting strengths and weaknesses of the resume in relation to the job description and profile.]  

     🚀Strengths: [List specific areas where the resume effectively matches the job description and profile, such as relevant skills, experience, or keywords that align well with the job requirements.]  

    ⚠️ Weaknesses: [List specific areas where the resume could be improved to better match the job description and profile, such as missing keywords, lack of relevant experience, or formatting issues.]  
    
    ✅Suitable Jobs: [Based on the analysis, suggest other job roles or industries that the candidate's resume may be well-suited for, in case the current job profile is not the best fit.]

    ✍️ Finally, create a tailored resume that incorporates the necessary improvements to enhance the candidate's chances of passing through ATS and catching the attention of hiring managers. The tailored resume should be concise, well-structured, and focused on the most relevant skills and experiences for the specified job profile.
    """
    return prompt

def ask_resume_questions(resume_text, user_question):
    prompt = f"""
    You are an expert career coach and resume strategist. Your task is to analyze the provided resume and answer the user's question based on the content of the resume. 

    📄 Resume Text:
    {resume_text}

    ❓ User Question:
    {user_question}

    Please provide a clear and concise answer to the user's question based on the information available in the resume. If the resume does not contain enough information to answer the question, please indicate that as well.
    """
    return prompt

# pass this pormpt to (LLM) openai_services.get_completion(ats_prompt(resume_text, job_description, job_profile)) to get the evaluation and tailored resume.