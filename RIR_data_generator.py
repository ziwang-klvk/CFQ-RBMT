import os
from tqdm import tqdm

from dataset_generator import pipeline

ROOT_PATH = "pipeline/mcwq/translations"
SAVE_PATH = 'JCWQ-rir'


def translate_file(root_path: str, save_path: str, lang: str) -> None:
    """
    traverse the folder of the original dataset, find the ones in EN and create the japanese dataset in the save_path

    :param root_path: path to the original dataset folder
    :param save_path: path to a folder to save the new dataset if existing and will create the directory otherwise
    the file name should be xxx.en.txt
    """
    text_meta = {}
    for path, dir_list, file_list in os.walk(root_path):
        for file_name in file_list:
            if '.en.txt' in file_name:
                org_file_path = os.path.join(path, file_name)
                save_file_path = org_file_path.replace(root_path, save_path).replace('.en.', f'.{lang}.')
                # make the directory if not existing
                os.makedirs(os.path.dirname(save_file_path), exist_ok=True)
                num_lines = sum(1 for line in open(org_file_path, 'r'))

                with open(org_file_path, 'r') as fr, open(save_file_path, 'w') as fw:
                    print(f'Translating {org_file_path}...')
                    new_lines = []
                    for line in tqdm(fr, total=num_lines):
                        en_text = line
                        new_text, _ = pipeline(en_text, tracker=False)
                        new_text = new_text[0] + '\n'
                        new_lines.append(new_text)

                    fw.writelines(new_lines)

                    print(f'Completed {org_file_path} translation, generated {save_file_path}!\n')

            elif 'en.sparql' in file_name:
                org_file_path = os.path.join(path, file_name)
                save_file_path = org_file_path.replace(root_path, save_path).replace('.en.', f'.{lang}.')
                # make the directory if not existing
                os.makedirs(os.path.dirname(save_file_path), exist_ok=True)

                with open(org_file_path, 'r') as fr, open(save_file_path, 'w') as fw:
                    query = fr.readlines()
                    fw.writelines(query)

            else:
                continue



def generator():
    translate_file(root_path=ROOT_PATH, save_path=SAVE_PATH, lang='ja')

if __name__ == "__main__":
    generator()