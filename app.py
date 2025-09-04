import streamlit as st
import json

# Set page configuration
st.set_page_config(
    page_title="DigiSkills.pk FAQ Chatbot",
    page_icon="🤖",
    layout="wide"
)

# DigiSkills.pk FAQ data
DIGISKILLS_FAQS = {
    "What is DigiSkills.pk?": "DigiSkills.pk is a program initiated by the Government of Pakistan to equip the youth with necessary digital skills. It's a free online training platform that offers courses in various digital skills to help Pakistani youth become financially independent.",
    
    "How can I register for DigiSkills.pk?": "You can register by visiting the DigiSkills.pk website, clicking on the registration button, and filling out the required information including your CNIC, email, and educational background.",
    
    "Are the courses really free?": "Yes, all courses on DigiSkills.pk are completely free of charge for Pakistani citizens.",
    
    "What courses are available on DigiSkills.pk?": "Courses include Freelancing, Digital Marketing, WordPress, Graphic Design, QuickBooks, AutoCAD, Creative Writing, and many more digital skills courses.",
    
    "Can I get a certificate after completing a course?": "Yes, you receive a certificate after successfully completing each course and passing the assessment with at least 50% marks.",
    
    "How long does it take to complete a course?": "Most courses are designed to be completed in 3 months with a recommended study time of 8-10 hours per week.",
    
    "Is there any age limit for registration?": "Participants must be at least 18 years old to register for DigiSkills.pk courses.",
    
    "What are the technical requirements to take courses?": "You need a computer or smartphone with internet connection. Specific software requirements vary by course but generally include a modern web browser and basic software like PDF reader.",
    
    "Can I take multiple courses at once?": "Yes, you can enroll in multiple courses simultaneously, but it's recommended to focus on one or two at a time to ensure proper learning.",
    
    "How do I reset my password?": "You can reset your password by clicking on the 'Forgot Password' link on the login page and following the instructions sent to your registered email.",
    
    "Are the courses available in Urdu?": "Yes, most courses are available in both English and Urdu to cater to a wider audience.",
    
    "Is there any support available if I face issues during the course?": "Yes, there is a support team available through the website, and each course has dedicated instructors and teaching assistants to help students.",
    
    "Can I access the course material after completion?": "Yes, you can access the course material for a limited time (usually 30 days) after course completion.",
    
    "How often are new batches started?": "New batches typically start every 3 months. You can check the website for specific dates and registration periods.",
    
    "Do I need to have prior knowledge to enroll?": "No, most courses are designed for beginners, though some advanced courses may have prerequisites which are mentioned in the course description."
}

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
    .faq-question {
        font-weight: bold;
        color: #1E40AF;
        cursor: pointer;
        padding: 0.5rem;
        border-radius: 0.5rem;
        margin-bottom: 0.5rem;
        background-color: #f0f4f8;
    }
    .faq-question:hover {
        background-color: #e2e8f0;
    }
</style>
""", unsafe_allow_html=True)

# App header
st.markdown("<h1 class='header'>DigiSkills.pk FAQ Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<p class='subheader'>Get answers to your DigiSkills.pk questions</p>", unsafe_allow_html=True)

# Function to find the best answer for a question
def get_answer(question):
    question_lower = question.lower()
    
    # Check for exact matches
    for faq_question in DIGISKILLS_FAQS:
        if faq_question.lower() in question_lower:
            return DIGISKILLS_FAQS[faq_question]
    
    # Check for keyword matches
    keywords = {
        "register": "How can I register for DigiSkills.pk?",
        "course": "What courses are available on DigiSkills.pk?",
        "free": "Are the courses really free?",
        "certificate": "Can I get a certificate after completing a course?",
        "duration": "How long does it take to complete a course?",
        "age": "Is there any age limit for registration?",
        "requirements": "What are the technical requirements to take courses?",
        "multiple": "Can I take multiple courses at once?",
        "password": "How do I reset my password?",
        "urdu": "Are the courses available in Urdu?",
        "support": "Is there any support available if I face issues during the course?",
        "access": "Can I access the course material after completion?",
        "batch": "How often are new batches started?",
        "knowledge": "Do I need to have prior knowledge to enroll?",
        "what is": "What is DigiSkills.pk?"
    }
    
    for keyword, faq in keywords.items():
        if keyword in question_lower:
            return DIGISKILLS_FAQS[faq]
    
    # Default response for unknown questions
    return "I'm not sure about that specific question. Could you please ask about DigiSkills.pk registration, courses, certificates, or other related topics? Here are some example questions: 'How do I register?', 'What courses are available?', or 'Are the courses free?'"

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
        
        full_response = get_answer(prompt)
        message_placeholder.markdown(full_response)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": full_response})

# Sidebar with information
with st.sidebar:
    st.title("About")
    st.info("""
    This chatbot answers questions about DigiSkills.pk.
    
    DigiSkills.pk is a initiative of the Government of Pakistan to provide
    free digital skills training to the youth.
    """)
    
    st.title("Popular Questions")
    for question in list(DIGISKILLS_FAQS.keys())[:5]:
        if st.button(question, key=question):
            st.session_state.messages.append({"role": "user", "content": question})
            st.session_state.messages.append({"role": "assistant", "content": DIGISKILLS_FAQS[question]})
            st.rerun()
    
    st.title("How to Use")
    st.write("""
    1. Ask questions about DigiSkills.pk registration, courses, or certificates
    2. Type your question in the chat box below
    3. The chatbot will provide answers based on DigiSkills.pk FAQs
    """)
    
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

# Footer
st.markdown("---")
st.caption("Note: This is an AI-powered assistant. For official information, always refer to the DigiSkills.pk website.")
