import json
import nltk


def read_stories(stories_file):
    stories = []
    with open(stories_file, "r") as f:
        lines = f.readlines()
        for line in lines:
            stories.append(line.strip("\n"))
    return stories


def process_stories(stories):
    processed_stories = []
    for sid, story in enumerate(stories):
        processed_sentences = []
        sentences = nltk.sent_tokenize(story)
        for sentence in sentences:
            processed_sentences.append(nltk.word_tokenize(sentence))
        processed_story ={"doc_key": "short_stories_"+str(sid),
                          "dataset": "ace05",
                          "sentences": processed_sentences}
        processed_stories.append(processed_story)
    return processed_stories


def write_to_json(processed_stories, story_json_file):
    with open(story_json_file, "a+") as f:
        for processed_story in processed_stories:
            json.dump(processed_story, f)
            f.write("\n")





if __name__ == '__main__':
    stories = read_stories("adventure.txt")
    processed_stories = process_stories(stories)
    write_to_json(processed_stories, "adventure-ace05.json")



