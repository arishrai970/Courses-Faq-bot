# DigiSkills.pk FAQ Chatbot

A Streamlit-based chatbot that answers frequently asked questions about DigiSkills.pk using DeepSeek AI.

## Features

- Answers questions about DigiSkills.pk registration, courses, and certificates
- Powered by DeepSeek AI
- Clean and responsive Streamlit interface
- Chat history maintained during session

## Setup

1. Clone this repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set your DeepSeek API key as environment variable:
   - Create a `.env` file in the root directory
   - Add: `DEEPSEEK_API_KEY=your_api_key_here`
4. Run the app: `streamlit run app.py`

## Deployment

### GitHub Setup
1. Create a new repository on GitHub
2. Push the code to your repository

### Streamlit Deployment
1. Create a free account on [Streamlit Cloud](https://streamlit.io/cloud)
2. Connect your GitHub repository
3. Add your DeepSeek API key as a secret in Streamlit Cloud:
   - Go to your app settings → Secrets
   - Add: `DEEPSEEK_API_KEY = "your_actual_api_key"`
4. Deploy the app

## Usage

1. Open the deployed Streamlit app
2. Type your question about DigiSkills.pk in the chat input
3. The AI will respond with relevant information based on DigiSkills.pk FAQs

## Note

This chatbot uses predefined DigiSkills.pk FAQ information combined with DeepSeek's AI capabilities to provide accurate answers.
