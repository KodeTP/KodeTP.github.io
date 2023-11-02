import pandas as pd

recipes = pd.read_csv("../RAW_recipes.csv")
print(recipes.head)

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