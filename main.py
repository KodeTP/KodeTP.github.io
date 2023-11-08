import pandas as pd

recipes = pd.read_csv("../RAW_recipes.csv")
#print(recipes.head)

ingredients = ['apples']

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
        <table>
            <tr>
                <th>Name</th>
                <th>Ingredients</th>
            </tr>"""

for index, row in recipes.iterrows():
    for ingredient in ingredients:
        if ingredient in row['ingredients']:
            o += """
            <tr>
                <td>{}</td>
                <td>{}</td>
            </tr>""".format(row['name'], row['ingredients'])
            print(row['name'])
            break



o+= """
    </body>
</html>
"""

with open(page, 'w', encoding='utf-8') as f:
    f.write(o)
