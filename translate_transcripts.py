from pathlib import Path
import ast
from translate import Translator

directory_in_str = str("E:\\UG's Workspace\\College\\Project\\CODE\\transcript_results")

pathlist = Path(directory_in_str).glob('**/*.txt')

file_list = []

for path in pathlist:
    path_in_str = str(path)
    file_list.append(str(path_in_str[39:]))

# print(file_list)
# print(type(file_list[1]))

for i in file_list:
    with open(i, 'r') as transcript:
        list_transcript = ast.literal_eval(transcript.read())
        print(type(list_transcript))
        print(len(list_transcript))