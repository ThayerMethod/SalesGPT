import yaml
from src.listener import listen_and_transcribe
from src.nlp_processing import process_transcription
from src.llm_responder import generate_response
from src.real_time_ui import display_response

def main():
    # Load config settings
    with open("config/config.yaml", "r") as f:
        config = yaml.safe_load(f)
    
    print("SalesGPT is now listening to the conversation...")
    
    while True:
        # Listen and transcribe real-time conversation
        transcription = listen_and_transcribe(config['listener'])
        
        # Process transcription to identify intent and entities
        intent, entities = process_transcription(transcription)
        
        # Generate LLM response
        response = generate_response(transcription, intent, entities, config['llm'])
        
        # Display the response in real-time UI
        display_response(transcription, response)

if __name__ == "__main__":
    main()
