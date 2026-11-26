import os

ENTRY = "It's you from 2040. The 'no regrets' tattoo got infected, we lost the arm, and the surgeon kept it as a souvenir. He named it Kevin."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
