# bits-and-pieces
## various cleaning/organizing utilities

[**cleansplitwikidump.py**](https://github.com/kvesik/bits-and-pieces/blob/master/cleansplitwikidump.py)
Additional cleaning to follow use of [WikiExtractor](https://github.com/attardi/wikiextractor). This script reads all of the output from WikiExtractor.py and cleans/reorganizes it by:
- removing the <doc></doc> tags (and their contents) at the beginning and end of each article
- lowercasing each word
- removing punctuation, digits, and <br> tags from the edges of each word
- omitting words altogether if they still contain any of the above
- omitting any duplicate words
- writing the remaining/cleaned words, one per line, to the file "cleanedwikiwords.txt"

This is intended to be run from within the text/ directory that is created by WikiExtractor.py (text/ should contain a series of directories AA, AB, AC, ..., each of which contains a series of text files wiki_00, wiki_01, ...).


