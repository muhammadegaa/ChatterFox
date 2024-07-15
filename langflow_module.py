from transformers import pipeline

# Initialize the text-generation pipeline (as a fallback)
text_generator = pipeline("text-generation", model="microsoft/DialoGPT-medium")

# Hardcoded detailed responses for demo purposes based on Spotify's account help pages
demo_responses = {
    "reset password": "To reset your Spotify password, go to the password reset page: https://www.spotify.com/password-reset/. Enter your email address and follow the instructions in the email you receive.",
    "change email": "To change your email address on Spotify, log in to your account, go to your account settings, and update your email information. Don't forget to save the changes.",
    "close account": "If you want to close your Spotify account, visit this page: https://support.spotify.com/close-account/. Follow the instructions to permanently delete your account.",
    "subscription plans": "Spotify offers several subscription plans including Individual, Duo, Family, and Student plans. Each plan has different features and pricing. Visit https://www.spotify.com/plans/ for more details.",
    "login issues": "If you are having trouble logging in, ensure that you are using the correct username and password. If you forgot your password, you can reset it at https://www.spotify.com/password-reset/. If the issue persists, try clearing your browser cache or using a different browser.",
    "premium benefits": "Spotify Premium offers ad-free music, offline listening, higher sound quality, and the ability to play any song on demand. Visit https://www.spotify.com/premium/ for more details.",
    "family plan": "The Spotify Family Plan allows up to 6 family members to enjoy Premium benefits under one plan at a discounted rate. Each member gets their own account. More information is available at https://www.spotify.com/family/."
}

def fetch_answer_from_query(query):
    query = query.lower()
    if "reset" in query and "password" in query:
        return demo_responses["reset password"]
    elif "change" in query and "email" in query:
        return demo_responses["change email"]
    elif "close" in query and "account" in query:
        return demo_responses["close account"]
    elif "subscription" in query or "plans" in query:
        return demo_responses["subscription plans"]
    elif "login" in query or "trouble logging in" in query:
        return demo_responses["login issues"]
    elif "premium" in query and ("benefits" in query or "features" in query):
        return demo_responses["premium benefits"]
    elif "family" in query and "plan" in query:
        return demo_responses["family plan"]
    else:
        return None

def generate_response(user_input):
    # Try to fetch an answer from the hardcoded responses
    kb_response = fetch_answer_from_query(user_input)
    if kb_response:
        return kb_response

    # Fallback to AI response generation if no relevant answer is found
    response = text_generator(user_input, max_length=100, num_return_sequences=1)[0]['generated_text']
    return response