# MCWQ-R

Repo for the paper [On Evaluating Multilingual Compositional Generalization with Translated Datasets](https://arxiv.org/abs/2306.11420).
The introduced MCWQ-R dataset can be found in the [`data`](https://github.com/ziwang-klvk/CFQ-RBMT/tree/main/data) folder. The remaining modules are under construction.

The implementation of a Rule-Based Machine Translation (RBMT) framework (and related supportive toolkits) for questions generated as in the [CFQ paper](https://arxiv.org/pdf/1912.09713v2.pdf). This project is also largely based on the [MCWQ dataset](https://github.com/coastalcph/seq2sparql) and can be regarded as its branch.

## Requirement

#### Dataset generation

* URBANS 

  The modified URBANS is added as a submodule

* NLTK

## Structure

### Submodules

#### URBANS: 

The URBANS module was revised from the [CFG-based version](https://github.com/pyurbans/urbans), a Universal Rule-Based Machine Translation toolkit. Several new features are added to this library for practical usage. Primarily, they are:

1. Tag-Word dictionary

   ```python
   class Translator:
       def __init__(self,
                    src_grammar: str,
                    src_to_tgt_grammar: Dict,
                    src_to_tgt_dictionary: Dict):
           """         
           UPDATE: The dictionary now mapping the word based on its POS tag to avoid ambiguity
                       E.g: en_to_jp_dict = {
                                           "Vte":
                                               {
                                               "eat":"tabete",
                                               "drink":"nonnde",
                                               ...
                                               }
                                           "Vorg":
                                               {
                                               "eat":"taberu",
                                               "drink":"nomu"
                                               }
                                           }
            """
   ```

2.  Word tag parser (also for failures and ambiguities)

   ```python
   def parse_words(self, sentences: List[str] or str):
   """
   Parse the sentences to get the words and their tags that should be provided in the translation dictionary
   """
   ```

3. Post-processing for disambiguation


### Dataset generation

`pipeline`: Involves codes and related files used for grammar development, translation assessment, result analysis and etc.

​		|_______________ `mt.ipynb`: The main pipeline for grammar construction.

​        |_______________ `ambiguous_sentences.txt`: Ambiguous sentences after parsing.

​		|_______________ `ambiguity_maps.csv`: Ambiguities in translations after post-processing.

​	    |_______________ `google_translate.ipynb`: Comparison with Google translation.

​		|_______________ `analysis.ipynb`: Analytic figures, etc.




`grammar`: Involves developed EN-JP transduction grammar.

​		|_______________ `source_grammar.py`, `transduction_rule.py`, `dictionary.py`: Involves variables of the transduction grammar.

​		|_______________ `postproc.py`: Involves rules for post-processing.


`dataset_generator.py`: The main file for dataset generation. Simply run this script to traverse `*.en.txt` files in `./mcwq/official` and generate `./jcwq` correspondingly.
