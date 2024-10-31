import spacy

# Load spaCy model for intent and entity recognition
nlp = spacy.load("en_core_web_sm")

def process_transcription(text):
    doc = nlp(text)
    
    # Example intent recognition (customize as needed)
    intent = "recommendation" if "recommend" in text else "general_inquiry"
    
    # Extract named entities
    entities = {ent.label_: ent.text for ent in doc.ents}
    
    return intent, entities
