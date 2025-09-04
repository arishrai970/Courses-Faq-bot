import streamlit as st
import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set page configuration
st.set_page_config(
    page_title="DigiSkills.pk FAQ Chatbot",
    page_icon="🤖",
    layout="wide"
)

# Initialize DeepSeek API
def get_deepseek_response(prompt):
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        return "DeepSeek API key not found. Please set the DEEPSEEK_API_KEY environment variable."
    
    url = "https://api.deepseek.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    # Predefined DigiSkills.pk context
    digiskills_context = """
    DigiSkills.pk is a program initiated by the Government of Pakistan to equip the youth with 
    necessary digital skills. Here are some frequently asked questions:

    1. What is DigiSkills.pk?
    DigiSkills.pk is a free online training platform that offers courses in various digital skills to help Pakistani youth become financially independent.

    2. How can I register for DigiSkills.pk?
    You can register by visiting the DigiSkills.pk website, clicking on the registration button, and filling out the required information.

    3. Are the courses really free?
    Yes, all courses on DigiSkills.pk are completely free of charge for Pakistani citizens.

    4. What courses are available on DigiSkills.pk?
    Courses include Freelancing, Digital Marketing, WordPress, Graphic Design, QuickBooks, and many more.

    5. Can I get a certificate after completing a course?
    Yes, you receive a certificate after successfully completing each course and passing the assessment.

    6. How long does it take to complete a course?
    Most courses are designed to be completed in 3 months with a recommended study time of 8-10 hours per week.

    7. Is there any age limit for registration?
    Participants must be at least 18 years old to register for DigiSkills.pk courses.

    8. What are the technical requirements to take courses?
    You need a computer or smartphone with internet connection. Specific software requirements vary by course.

    9. Can I take multiple courses at once?
    Yes, you can enroll in multiple courses simultaneously, but it's recommended to focus on one or two at a time.

    10. How do I reset my password?
    You can reset your password by clicking on the "Forgot Password" link on the login page and following the instructions.

    11. Are the courses available in Urdu?
    Yes, most courses are available in both English and Urdu to cater to a wider audience.

    12. Is there any support available if I face issues during the course?
    Yes, there is a support team available through the website, and each course has dedicated instructors and teaching assistants.

    13. Can I access the course material after completion?
    Yes, you can access the course material for a limited time after course completion.

    14. How often are new batches started?
    New batches typically start every 3 months. You can check the website for specific dates.

    15. Do I need to have prior knowledge to enroll?
    No, most courses are designed for beginners, though some advanced courses may have prerequisites.
    """
    
    # Create a prompt that includes the FAQ context
    full_prompt = f"""
    You are a helpful assistant specialized in answering questions about DigiSkills.pk. 
    Use the following information to answer questions:
    
    {digiskills_context}
    
    Please answer the following question about DigiSkills.pk:
    {prompt}
    
    If the question is not related to DigiSkills.pk, politely decline to answer and suggest asking about DigiSkills.pk instead.
    Keep your response concise and informative.
    """
    
    data = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant specialized in DigiSkills.pk FAQs."},
            {"role": "user", "content": full_prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 1000
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        return result['choices'][0]['message']['content']
    except requests.exceptions.RequestException as e:
        return f"Error connecting to DeepSeek API: {str(e)}"
    except KeyError:
        return "Error parsing response from DeepSeek API."

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Custom CSS for better styling
st.markdown("""
<style>
    .stChatMessage {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    .stChatMessage [data-testid="stMarkdownContainer"] {
        font-size: 1.1rem;
    }
    .header {
        text-align: center;
        color: #1E40AF;
    }
    .subheader {
        text-align: center;
        color: #6B7280;
        margin-bottom: 2rem;
    }
    .sidebar .sidebar-content {
        background-color: #f0f2f6;
    }
</style>
""", unsafe_allow_html=True)

# App header
st.markdown("<h1 class='header'>DigiSkills.pk FAQ Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<p class='subheader'>Powered by DeepSeek AI • Get answers to your DigiSkills.pk questions</p>", unsafe_allow_html=True)

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask about DigiSkills.pk..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate assistant response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("Thinking...")
        
        full_response = get_deepseek_response(prompt)
        message_placeholder.markdown(full_response)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": full_response})

# Sidebar with information
with st.sidebar:
    st.title("About")
    st.info("""
    This chatbot answers questions about DigiSkills.pk using DeepSeek AI.
    
    DigiSkills.pk is a initiative of the Government of Pakistan to provide
    free digital skills training to the youth.
    """)
    
    st.title("How to Use")
    st.write("""
    1. Ask questions about DigiSkills.pk registration, courses, or certificates
    2. Type your question in the chat box below
    3. The AI will provide answers based on DigiSkills.pk FAQs
    """)
    
    st.title("Example Questions")
    st.write("""
    - How do I register for DigiSkills.pk?
    - What courses are available?
    - Are the courses free?
    - How do I get a certificate?
    - What is the duration of courses?
    """)
    
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

# Footer
st.markdown("---")
st.caption("Note: This is an AI-powered assistant. For official information, always refer to the DigiSkills.pk website.")
