from dygie.data.dataset_readers import document

if __name__ == '__main__':
    dataset = document.Dataset.from_jsonl("adventure-relation.jsonl")
    print(dataset)
    doc = dataset[0]
    print(doc)
    sent = doc[5]
    for sent in doc:
        relations = sent.predicted_relations
        for event in relations :
            print(event)