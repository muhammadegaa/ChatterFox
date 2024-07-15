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
    "premium benefits": "Spotify Premium offers ad-free music, offline listening, higher sound quality, an