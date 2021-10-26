import json
import nltk
import spacy
import neuralcoref
nlp = spacy.load('en_core_web_sm')
neuralcoref.add_to_pipe(nlp)


def replace_pronouns(text, is_replace_processive=True):
  doc = nlp(text)
  tokens = [str(token) for token in doc]
  for coref in doc._.coref_clusters:
    coref_mention = str(coref.main)
    coref_mention = " ".join([str(t) for t in nlp(coref_mention)])
    for mention in coref.mentions:
      for id in range(mention.start, mention.end):
        if id == mention.start:
          if is_replace_processive:
            if ((mention.end - mention.start)==1) and (tokens[id].lower() in ["my", "mine", "your", "her", "his", "its", "our", "their"]) and ("'s" not in coref_mention):
                tokens[id] = coref_mention+" 's"
            else:
                tokens[id] = coref_mention
          else:
            tokens[id] = coref_mention
        else:
          tokens[id] = ""
  return " ".join(filter(None, tokens))


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
        coref_story = replace_pronouns(story)
        sentences = nltk.sent_tokenize(coref_story)
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



