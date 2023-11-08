import pandas as pd

recipes = pd.read_csv("../RAW_recipes.csv")
#print(recipes.head)

ingredients = ['bok choy']

page = "index.html"
o = """
<!DOCTYPE html>
<html>
    <head>
        <title>Recipie Finder</title>
    </head>
    <div style="width: 397px; height: 62px; padding: 16px; background: white; border-radius: 16px; border: 1px #EFEFEF solid; justify-content: flex-start; align-items: center; gap: 10px; display: inline-flex">
        <div style="color: #C5C5C5; font-size: 20px; font-family: Poppins; font-weight: 400; word-wrap: break-word">Search...</div>
    </div>
    <body>
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
