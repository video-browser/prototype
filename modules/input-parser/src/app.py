import argparse
import stanza

from utils import log

POS_NOUN = "NOUN"

def checkModels():
  log("checkModels(): %s" % 1)
  stanza.download('en')

def parseInput(input):
  log("parseInput(): input: %s" % input)

  nlp = stanza.Pipeline(lang='en', processors='tokenize,mwt,pos')
  doc = nlp(input)
  log(*[f'word: {word.text}\tupos: {word.upos}\txpos: {word.xpos}\tfeats: {word.feats if word.feats else "_"}' for sent in doc.sentences for word in sent.words], sep='\n')

  parsed = { "nouns": [] }
  for sent in doc.sentences:
    for word in sent.words:
      if word.upos == POS_NOUN:
        parsed["nouns"].append(word)
  log("parseInput(): done parsing input, parsed: \n%s" % parsed)

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='later to be descripted...')
  parser.add_argument('-text', action='store', type=str, help='The text to parse.')
  args = parser.parse_args()
  log("app.py: input from command line: %s" % repr(args))

  checkModels()
  parseInput(args.text)
