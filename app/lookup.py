import spacy
import os
import glob
import pandas as pd

class LookUpService:
    def __init__(self):
        # Use chinese since it can handle whitespace and
        # non whitespace tokens
        self.nlp = spacy.blank("zh")
        ruler = self.nlp.add_pipe("entity_ruler")
        lookup_files = glob.glob("./rules/*")
        patterns = []
        for file in lookup_files:
            ent_type = os.path.basename(file).split(".")[0].upper()
            ents = list(pd.read_csv(file, header=None)[0])
            patterns += [{"label": ent_type, "pattern": ent} for ent in ents]
        with self.nlp.select_pipes(enable="tagger"):
            ruler.add_patterns(patterns)

    def lookup(self, sentence):
        doc = self.nlp(sentence)
        return [(ent.text, ent.label_) for ent in doc.ents]
