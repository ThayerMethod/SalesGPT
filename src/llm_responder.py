import openai
import json

# Load custom prompts
with open("config/prompts.json", "r") as f:
    prompts = json.load(f)

def generate_response(transcription, intent, entities, settings):
    openai.api_key = settings['api_key']
    
    # Select appropriate prompt based on intent
    prompt = prompts.get(intent, prompts['default'])
    prompt = prompt.format(transcription=transcription, entities=entities)
    
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    
    return response.choices[0].text.strip()
