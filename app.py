# work with streamlit to create a web application for the ATS system -> frontend.

import streamlit as st
from services.ats_services import get_ats_analysis
from utils.pdf_utils import extract_text_from_pdf
from utils.prompts import ask_resume_questions
from services.openai_services import get_completion, get_qa_answer

st.title("AI Powered ATS Resume Evaluator and Tailor")

job_role = st.text_input("Enter the job profile you are applying for (e.g., Software Engineer, Data Scientist, etc.):")
job_description = st.text_area("Enter the job description for the position you are applying to:")
uploaded_file = st.file_uploader("Upload your resume (PDF format only):", type=["pdf"])

resume_text = " "  # Initialize resume_text variable to store the extracted text from the uploaded PDF resume, which will be used for further processing and analysis in the application.

if st.button("Evaluate and Tailor Resume"):
    if uploaded_file is None:
        st.warning("Please upload your resume in PDF format.")
    elif job_role.strip() == "" or job_description.strip() == "":
        st.warning("Please enter both the job profile and job description.")
    else:
        with st.spinner("Processing your resume..."):
            # pass
            resume_text = extract_text_from_pdf(uploaded_file)      # Extract text from the uploaded PDF resume using the utility function.
            ats_result = get_ats_analysis(resume_text, job_description, job_role)       # Get the ATS analysis and tailored resume by calling the service function with the extracted resume text, job description, and job profile.
            # Display the ATS analysis and tailored resume in the Streamlit app.
            st.subheader("ATS Analysis and Tailored Resume:")
            st.write(ats_result)



if "messages" not in st.session_state:
    st.session_state.messages = []

# Display past messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
if question := st.chat_input("Ask about your resume or job fit..."):
    # Show user message
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)
        
        # Build prompt for backend
    prompt = f"""
    Resume:
    {resume_text}

    Job Description:
    {job_description}

    Question:
    {question}
    """

    # Call your ATS backend (Groq/OpenAI)
    answer = get_qa_answer(resume_text, job_description, question)

    # Show assistant reply
    st.session_state.messages.append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.markdown(answer)