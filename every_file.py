# This file will create a html file that links all the other html files inside it that when you are
# working on different html files you switch between them easily

# importing os library
import os

# an array for html files that are going to be stored in it
html_files = []
# a loop that sees if the file ends with ".html" appends it to the array
for i in os.listdir():
    if i.endswith('.html'):
        html_files.append(i)
# opening the html file to write the data inside it
with open("directories.html", 'w') as file:
    # writing normal html things inside the file
    file.write(
        '''<!DOCTYPE html>
<html>
<head>
    <title>All the directories</title>
</head>
<body>

''')
    # A loop again to write the "a" tags and data in the body part of our html file
    for html_file in html_files:
        file.write(f'   <a href="{html_file}" target="_blank">{html_file}</a><br>\n')
    # Writing final parts of the html file
    file.write(
        '''</body>
</html>
''')
