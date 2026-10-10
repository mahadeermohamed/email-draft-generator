 Email Draft Generator

Converts rough bullet points into a polished, professional email using an LLM.

## Why I built this
To practice prompt engineering — getting consistent, well-structured 
output from an LLM, not just random text.

## Tech stack
Python, requests, Gemini API, python-dotenv

## How to run
1. Clone this repo
2. Create a `.env` file with your API key (see `.env.example`)
3. Install dependencies: `pip install -r requirements.txt`
4. Run: `python main.py`

## Example

Enter bullet points: missed the meeting, want to reschedule, suggest Friday
Enter tone: apologetic

Subject: Apologies for Missing Today’s Meeting

Hi [Name],
I’m sorry I wasn’t able to join today’s meeting. Would Friday work
to reschedule and catch up on what was discussed?
Thanks for understanding.


## What I learned
How prompt specificity (tone, length, structure) directly changes 
output quality, and how to chain user input into a dynamic prompt.
