import re
import os
from tqdm import tqdm

import urbans
from grammar.dictionary import dic_en2jp
from grammar.source_grammar import EN_source_transduction_grammar as src_grammar
from grammar.transduction_rule import src_to_target_grammar
from grammar.postproc import post_processing, pref_pattern


ROOT_PATH = "mcwq/official"
SAVE_PATH = "jcwq"

def pipeline(sentences: list or str) -> list:
    post_processor = post_processing()

    e2j_translator = urbans.Translator(src_grammar=src_grammar,
                                       src_to_tgt_grammar=src_to_target_grammar,
                                       src_to_tgt_dictionary=dic_en2jp,
                                       )

    translation, trans_map = e2j_translator.translate(sentences, remove_space=True, prefered_pattern=pref_pattern)
    translation = post_processor.replace(translation)
    return translation


def splitIO(line: str) -> list:
    """
    Split a line in the format of
    IN: [text]  OUT: [sparql]\n
    """
    splitter = re.compile('IN:\s|\s\sOUT:\s')
    spl = splitter.split(line)
    assert len(spl) == 3
    text2sparql = spl[1:3]
    return text2sparql


def translate_file_en2jp(root_path: str, save_path: str) -> None:
    """
    traverse the folder of the original dataset, find the ones in EN and create the japanese dataset in the save_path

    :param root_path: path to the original dataset folder
    :param save_path: path to a folder to save the new dataset if existing and will create the directory otherwise
    the file name should be xxx.en.txt
    """

    for path, dir_list, file_list in os.walk(root_path):
        for file_name in file_list:
            if '.en.' in file_name:
                org_file_path = os.path.join(path, file_name)
                save_file_path = org_file_path.replace(root_path, save_path).replace('.en.', '.ja.')
                # make the directory if not existing
                os.makedirs(os.path.dirname(save_file_path), exist_ok=True)

                num_lines = sum(1 for line in open(org_file_path, 'r'))
                with open(org_file_path, 'r') as fr, open(save_file_path, 'w') as fw:
                    print(f'Translating {org_file_path}...')
                    for line in tqdm(fr, total=num_lines):
                        text2sparql = splitIO(line)
                        jp_text = pipeline(text2sparql[0])[0]
                        jp_text2sparql = [jp_text, text2sparql[1]]
                        jp_line = 'IN: ' + jp_text2sparql[0] + '  OUT: ' + jp_text2sparql[1]
                        fw.write(jp_line)
                    print(f'Completed {org_file_path} translation, generated {save_file_path}!\n')
            else:
                continue


def generator():
    translate_file_en2jp(root_path=ROOT_PATH, save_path=SAVE_PATH)

if __name__ == "__main__":
    generator()