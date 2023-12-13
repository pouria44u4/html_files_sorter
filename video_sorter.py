from os import listdir

with open('videos.html', 'w') as file:
    file.write(
'''<!DOCTYPE html>
<html>
<head>
    <title>videos</title>
</head>
<body>
    ''')
    for file_ in listdir():
        if file_.lower().endswith('.mp4') or file_.lower().endswith('.wmv') or file_.lower().endswith('.webm') or file_.lower().endswith('.mkv') or file_.lower().endswith('.avi'):
            file.write(f'    <video src="{file_}"></video>\n')
    file.write(
'''</body>
</html>''')