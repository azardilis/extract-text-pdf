import aspell
from typing import *
from functools import partial
import os
                      
def get_first_suggestion(speller, word):
    if speller.check(word):
        return word
    
    suggestions = speller.suggest(word)
    if suggestions:
        return suggestions[0]
    else:
        return word

def go():
    fn = "test-data/cyprob-page-000.txt"
    nm, ext = os.path.splitext(fn)
    new_fn = "{nm}-auto-corrected{ext}".format(nm=nm, ext=ext)
    
    greek_speller = aspell.Speller('lang', 'el')
    get_first_suggestion_ = partial(get_first_suggestion, speller=greek_speller)
    
    new_lines = list()
    
    with open(fn, "r") as fin:
        for ln in fin:
            nln = " ".join([get_first_suggestion_(word=word) for word in ln.split()])
            new_lines.append(nln)

    with open(new_fn, "w") as fout:
        fout.write("\n".join(new_lines))
            

    
    
