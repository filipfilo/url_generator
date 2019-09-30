import json
import sys
import time
import webbrowser


# enter path to valid json file
path_to_json = r''

all_langs = ['ar-ae', 'bg-bg', 'ca-es', 'cs-cz', 'da-dk', 'de-de',
             'el-gr', 'en-us', 'es-es', 'es-mx', 'fi-fi', 'fr-fr',
             'hr-hr', 'hu-hu', 'id-id', 'it-it', 'ja-jp', 'ko-kr',
             'ms-my', 'nb-no', 'nl-nl', 'pl-pl', 'pt-br', 'pt-pt',
             'ro-ro', 'ru-ru', 'sk-sk', 'sv-se', 'th-th', 'tl-ph',
             'tr-tr', 'uk-ua', 'vi-vn', 'zh-cn', 'zh-tw']


def get_json():
    try:
        with open(path_to_json) as f:
            mydict = json.load(f)
            return mydict
    except FileNotFoundError:
        sys.exit('File not found')


obj_dict = get_json()

language = input('select language (like "bg-bg")\n')
counter = 0

if language in all_langs:
    for section in obj_dict:
        input('hit ENTER to continue opening URLs')
        locations = obj_dict[section]
        for a, string_loc in enumerate(locations, start=1):
            url = f'https://asd.dummyurl.net/{language}/{section}/translated/#search={string_loc}&sfields=source,target,locations&soptions=exact'
            print(a, "\n", url)
            webbrowser.open_new_tab(url)
            time.sleep(0.2)
            counter += 1
    print(f'{counter} links opened')
else:
    print('invalid language')
