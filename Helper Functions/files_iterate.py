from pathlib import Path

directory_in_str = str("E:\\UG's Workspace\\College\\Project\\CODE\\audio_files")

pathlist = Path(directory_in_str).glob('**/*.mp3')

file_list = []

for path in pathlist:
    path_in_str = str(path)
    file_list.append(str(path_in_str[51:]))

print(file_list)
print(type(file_list[1]))