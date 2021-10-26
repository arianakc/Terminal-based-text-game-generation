from dygie.data.dataset_readers import document

if __name__ == '__main__':
    dataset = document.Dataset.from_jsonl("adventure-event.jsonl")
    print(dataset)
    doc = dataset[0]
    print(doc)
    for sent in doc:
        events = sent.predicted_events
        for event in events:
            print(event)

    #
    # sent = doc[5]
    # print(sent)
    # ner = sent.predicted_ner[0]
    # print(ner)
    # span = ner.span
    # print(span)
    # print(span.sentence)
    # print(span.start_doc)
    # print(span.end_doc)
    # ev = sent.predicted_events
    # print(ev)
    # js = doc.to_json()
    # print(js.keys())