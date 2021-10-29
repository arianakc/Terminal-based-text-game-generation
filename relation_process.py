from dygie.data.dataset_readers import document

character_ignore_list = ["'s", 'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're",
                         "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', "who", "her", "he",
                         "his", "him",
                         "she", "they", "their", "them", "it", "one", "someone", "person", "man", "men", "that", "this",
                         "anyone",
                         "people", "everyone", "guys", "nobody", "mine", "family", "mans", "friends",
                         "woman", "boy", "girl", "friend", "buddy", "dear", "accent", "teens", "human", "all", "kind",
                         "circle"]
location_ignore_list = ["this", "that", "here", "building", "side", "wall", "rest", "it", "them", "we","some","there",
                        "place"]

vehicle_ignore_list = ["one", "car", "them", "it", "they", "what", "that", "seat", "black"]

def extract_characters(doc):
    # NER labeled PER
    characters = []
    for sent in doc:
        ners = sent.predicted_ner
        for ner in ners:
            if ner.label == "PER":
                character = " ".join(ner.span.text)
                if character not in characters and character.lower() not in character_ignore_list and character.lower()[-1]!='s':
                    characters.append(character)
    return characters


def extract_locations(doc):
    # NER labeled LOC, GPE, FAC
    locations = []
    for sent in doc:
        ners = sent.predicted_ner
        for ner in ners:
            if ner.label == "LOC" or ner.label == "GPE" or ner.label == "FAC":
                location = " ".join(ner.span.text)
                if location not in locations and location.lower() not in location_ignore_list and location.lower()[-1]!='s':
                    locations.append(location)
    return locations


def extract_vehicles(doc):
    # NER labeled VEH
    vehicles = []
    for sent in doc:
        ners = sent.predicted_ner
        for ner in ners:
            if ner.label == "VEH":
                vehicle = " ".join(ner.span.text)
                if vehicle not in vehicles and vehicle.lower() not in vehicle_ignore_list and vehicle.lower()[-1]!='s':
                    vehicles.append(vehicle)
    return vehicles


def extract_relations(doc):
    for sent in doc:
        relations = sent.predicted_relations
        for relation in relations:
            print(relation)


if __name__ == '__main__':
    dataset = document.Dataset.from_jsonl("adventure-relation.jsonl")
    print(dataset)
    doc = dataset[9]
    print(doc)
    for sent in doc:
        relations = sent.predicted_relations
        for relation in relations:
            print(relation)
    print(extract_characters(doc))
    print(extract_locations(doc))
    print(extract_vehicles(doc))
