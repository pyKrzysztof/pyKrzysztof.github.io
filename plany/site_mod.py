import os

files = [file for file in os.listdir(".") if file.startswith("o")]

for file in files:
    print(file)
    with open(file, 'r', encoding="ISO-8859-2") as f:
        code = f.read()
        code = code.replace('href="../css/plan.css"', 'href="plan.css"')
        code = code.replace('src="../scripts/plan.js""', 'href="plan.js"')

    with open(file, 'w') as f:
        f.write(code)
