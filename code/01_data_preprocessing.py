# 农业废弃物资源化利用 - 数据预处理脚本
import pandas as pd
import numpy as np
import os

# 1. 创建模拟实验数据（匹配论文研究内容：土壤有效磷、作物产量）
raw_data = pd.DataFrame({
    "处理组": ["对照组", "废弃物还田1年", "废弃物还田2年", "废弃物还田3年", "废弃物还田4年"],
    "土壤有效磷(mg/kg)": [12.3, 15.7, 19.2, 23.8, 27.5],
    "作物产量(kg/hm²)": [3200, 3450, 3680, 3820, 3950],
    "碳汇增量(t CO₂/hm²)": [0, 1.2, 2.5, 3.8, 5.1]
})

# 2. 数据清洗与预处理
processed_data = raw_data.copy()
# 计算产量提升率（相对对照组）
control_yield = processed_data.loc[processed_data["处理组"] == "对照组", "作物产量(kg/hm²)"].values[0]
processed_data["产量提升率(%)"] = round((processed_data["作物产量(kg/hm²)"] - control_yield) / control_yield * 100, 1)

# 3. 确保输出目录存在
os.makedirs("../data/processed", exist_ok=True)

# 4. 保存处理后的数据
processed_data.to_csv("../data/processed/agri_waste_processed_data.csv", index=False, encoding="utf-8-sig")

print("✅ 数据预处理完成！")
print("处理后数据已保存至：data/processed/agri_waste_processed_data.csv")
print(processed_data)