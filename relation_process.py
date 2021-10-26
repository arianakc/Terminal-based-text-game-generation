from dygie.data.dataset_readers import document


if __name__ == '__main__':
    dataset = document.Dataset.from_jsonl("adventure-relation.jsonl")
    print(dataset)
    doc = dataset[1]
    print(doc)
    for sent in doc:
        ners = sent.predicted_ner
        for ner in ners:
            print(ner)
    for sent in doc:
        relations = sent.predicted_relations
        for relation in relations :
            print(relation)