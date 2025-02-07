import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


with open("events.json", encoding="utf8") as file:
    date = (json.load(file))
df1 = pd.DataFrame(date["events"])
df = pd.DataFrame(date["events"])["signature"].value_counts()
print(df)

plt.figure(figsize=(10, 8))
plt.bar(df.index, df.values)
plt.xlabel('Типы атак')
plt.ylabel('Колличество атак')
plt.title("Распределение типов событий безопасности")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()
