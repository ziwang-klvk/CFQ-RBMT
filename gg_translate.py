import os
import json
import sys
from tqdm import tqdm
from google.cloud import translate_v2 as gg_translate

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/mac/Downloads/friendly-drake-365016-5060bb0f2dff.json"

translate_client = gg_translate.Client()

def translate_with_qmark(q, target):
    q = q if q[-1] == "?" else q + "?"
    q_trans = translate_client.translate(q, target_language=target)["translatedText"]
    return q_trans[:-1] if q_trans[-1] == "?" else q_trans

def translate_questions(path, path_map, lang):
    map = dict()
    with open(path, 'r') as fr:
        lines = fr.readlines()

    lines = list(set(lines))
    for line in tqdm(lines):
        trans = translate_with_qmark(line, lang)
        map[line] = trans

    with open(os.path.join(path_map, 'map.json'), 'w') as fw:
        json.dump(map, fw)

    return map


def generate_file_with_map(map, root_path, save_path, lang):
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
                        new_line = map[line]
                        new_lines.append(new_line)
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


if __name__ == "__main__":
    map = translate_questions("pipeline/Questions.txt", "pipeline", 'ja')
    generate_file_with_map(map, root_path="pipeline/mcwq/translations", save_path="gt_data", lang='ja')
