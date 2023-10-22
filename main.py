import sqlite3

sql = sqlite3.connect("file.db")
cursor = sql.cursor()

page = "index.html"

o = """
<!DOCTYPE html>
<html>
    <head>
        <title>My Website</title>
    </head>
    <body>
        <h1>My Website</h1>
        <p>This is my website.</p>
    </body>
</html>
"""

with open(page, 'w', encoding='utf-8') as f:
    f.write(o)