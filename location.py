import spacy

spc = spacy.load("en_core_web_sm")


def extract_loc(text):
    doc = spc(text)
    locations = [ent.text for ent in doc.ents if ent.label_ in ["GPE", "LOC", "FAC"]]
    
    if not locations:
        print("Could not detect location automatically")
        manual = input("Please enter your location: ")
        locations = [manual]

    return locations


