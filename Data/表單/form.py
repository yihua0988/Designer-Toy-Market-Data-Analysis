import pandas as pd
df = pd.read_csv('潮玩市場調查_csv.csv')
df = df.rename(columns={
    '請問您是否有聽說過潮流玩具?': '聽說過潮玩嗎?',
    '選擇潮牌玩具注重因素': '注重因素',
    '接觸潮玩主要來源': '接觸來源',
    '購買潮玩產品預算': '購買預算',
    '購買潮玩主要原因': '購買原因',
    '是否有意願 購買 / 重複購買': '有意願購買/重複購買',
    '是否有購買過潮流玩具': '曾購買潮玩',
    '是否購買分類': '購買分類' # 這個欄位看起來已經是處理過的分類
})

df['注重因素'] = df['注重因素'].fillna('')
all_factors = df['注重因素'].str.split(',').explode().str.strip()
factors_counts = all_factors.value_counts()

df['接觸來源'] = df['接觸來源'].fillna('')
all_sources = df['接觸來源'].str.split(',').explode().str.strip()
source_counts = all_sources.value_counts()

df['購買原因'] = df['購買原因'].fillna('')
all_reasons = df['購買原因'].str.split(',').explode().str.strip()
reason_counts = all_reasons.value_counts()

df['品牌'] = df['品牌'].fillna('')
all_main_brands = df['品牌'].str.split(',').explode().str.strip()
main_brand_counts = all_main_brands.value_counts()

brand_columns = ['POPMART', 'Disney', 'Pok\'emon']
for col in brand_columns:
    # 使用 str() 確保處理的是字串，避免TypeError，並替換 NaN
    df[col] = df[col].astype(str).fillna('')
    # 這裡處理方式類似，將多個 IP 拆開，並移除空白
    all_ips = df[col].str.split(', ').explode().str.strip()
    # 移除空字串 (來自 NaN 填充)
    all_ips = all_ips[all_ips != '']
    if not all_ips.empty:
        ip_counts = all_ips.value_counts()
        print(f"\n'{col}' 下的 IP 統計：")
        print(ip_counts)



# 將 '聽說潮玩', '有意願購買/重複購買', '曾購買潮玩' 轉換為布林值或數值
df['聽說過潮玩嗎?'] = df['聽說過潮玩嗎?'].map({'是': True, '否': False})
df['有意願購買/重複購買'] = df['有意願購買/重複購買'].map({'是': True, '否': False})
df['曾購買潮玩'] = df['曾購買潮玩'].map({'是': True, '否': False})



# 定義預算區間到數值的映射
budget_mapping = {
    '500元以下': 250,
    '500–1000元': 750,
    '1000–3000元': 2000,
    '超過3000元': 3500 # 取一個代表值
}
df['購買預算_數值'] = df['購買預算'].map(budget_mapping)

# 儲存清洗後的資料到新的 CSV 檔案
df.to_csv('潮玩市場調查_清洗後.csv', index=False, encoding='utf-8-sig')

