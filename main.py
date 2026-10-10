import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found. Check your .env file.")


def generate_email(bullet_point, tone):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent?key={api_key}"

    prompt = f"""Tone: {tone}
Convert these bullet points into a polished email.
Include a greeting, 2-3 short paragraphs, and a sign-off.
Keep it under 150 words.

Bullet points:
{bullet_point}
"""

    try:
        payload = {"contents": [{"parts": [{"text": prompt}]}]}
        response = requests.post(url, json=payload, timeout=30)
        response.raise_for_status()
        data = response.json()
        email_text = data["candidates"][0]["content"]["parts"][0]["text"]
        return email_text
    except requests.exceptions.Timeout:
        print("The request took too long. Please try again.")
    except requests.exceptions.RequestException as e:
        print(f"Something went wrong while generating the email: {e}")
    except (KeyError, IndexError):
        print("Couldn't read the generated email. Please try again.")

    return None


def get_valid_bullets():
    while True:
        bullets = input("Enter your bullet points (or 'exit' to quit):\n").strip()
        if bullets.lower() == "exit":
            return bullets
        if not bullets:
            print("Please enter at least one bullet point.\n")
        elif len(bullets.split()) < 3:
            print("That looks too short. Try adding more detail.\n")
        else:
            return bullets


def main():
    print("Email Draft Generator (type 'exit' anytime to quit)\n")

    while True:
        bullets = get_valid_bullets()
        if bullets.lower() == "exit":
            print("Goodbye!")
            break

        tone = input("Enter tone (formal, casual, apologetic, etc.):\n").strip()
        if tone.lower() == "exit":
            print("Goodbye!")
            break

        result = generate_email(bullets, tone)
        if result:
            print("\n--- Generated Email ---\n")
            print(result)
            save_email(result)

        print("\n" + "-" * 40)

def save_email(email_text):
    save = input("\nSave this email to a file? (y/n): ").strip().lower()
    if save == "y":
        filename = input("Filename (default: generated_email.txt): ").strip()
        filename = filename if filename else "generated_email.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(email_text)
        print(f"Saved to {filename}")

if __name__ == "__main__":
    main()