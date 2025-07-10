import pandas as pd
df = pd.read_csv('潮玩市場調查_csv.csv')
df["是否購買分類"] = df["請問您是否有購買過潮流玩具?"].apply(lambda x: "有購買" if x == "是" else "未購買")
df.to_csv("潮玩市場調查_csv.csv", index=False,encoding='utf-8-sig')
df[""]