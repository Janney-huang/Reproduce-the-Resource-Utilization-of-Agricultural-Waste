# 农业废弃物资源化利用复现项目

> Reproduce-the-Resource-Utilization-of-Agricultural-Waste

本项目用于复现 **农业废弃物资源化利用** 相关研究的实验流程、数据处理、代码实现与结果分析，旨在提升科研可重复性，为农业资源环境领域研究提供标准化、可直接运行的复现方案。

---

## 📌 项目简介
-项目名称:农业废弃物资源化利用
-项目成员：@JiangYee393、@hanyu-Yang、@caoyao-03、@Olivia-yao710
-项目内容：
-文章链接：https://github.com/user-attachments/files/26074845/Transforming-breakfast-bio-waste-into-hydrog_2025_International-Journal-of-H.pdf
-仓库链接：https://janney-huang.github.io/Reproduce-the-Resource-Utilization-of-Agricultural-Waste/
- 复现农业废弃物还田、土壤磷素循环、作物产量响应等核心研究内容
- 提供完整数据集、可运行代码、标准化分析流程与可视化结果

---

## 🧪 主要内容
1. 农业废弃物理化性质分析
2. 土壤肥力与有效磷变化规律
3. 作物产量响应与长期效应
4. 数据清洗、统计分析、图表绘制
5. 资源化利用环境效益评估

---

## 📂 项目结构
Reproduce-the-Resource-Utilization-of-Agricultural-Waste/
├── docs/ # MkDocs 文档站源码
├── code/ # 复现代码
│ ├── 01_data_preprocessing.py # Python 数据预处理脚本
│ └── reproduce_analysis.R # R 语言论文 Figure 6 复现脚本
├── data/ # 原始数据 + 处理后数据
│ └── processed/
│ └── agri_waste_processed_data.csv # 预处理后标准化实验数据集
├── results/ # 结果图表与报告
│ └── figures/
│ └── h2_storage_comparison.png # 论文 Figure 6 储氢性能对比图（复现结果）
├── README.md # 项目说明
├── requirements.txt # Python 环境依赖清单
└── r-requirement.md # R 环境配置说明
plaintext

---



## 🚀 快速开始
### 1. 克隆项目
```bash
git clone https://github.com/Janney-huang/Reproduce-the-Resource-Utilization-of-Agricultural-Waste.git
cd Reproduce-the-Resource-Utilization-of-Agricultural-Waste
### 2. 配置环境
bash
conda create -n agri-waste python=3.10
conda activate agri-waste
pip install -r requirements.txt
**2.1数据处理步骤环境配置**
**2.2.1 Python 环境**
版本要求：Python 3.10+
bash
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
**2.2.2 R 环境**
版本要求：R 4.0+
一键安装依赖（清华源加速）：
r
# 配置国内镜像源
options(repos = c(CRAN = "https://mirrors.tuna.tsinghua.edu.cn/CRAN/"))
# 安装项目所需R包
install.packages(c("ggplot2", "dplyr", "readr"))
详细说明见 r-requirement.md
### 3. 运行代码
bash
python code/01_data_preprocessing.py
python code/02_statistical_analysis.py
python code/03_visualization.py

### 4. 本仓库复现内容
- **复现代码**：[code/reproduce_analysis.R](sslocal://flow/file_open?url=https%3A%2F%2Fgithub.com%2FJanney-huang%2FReproduce-the-Resource-Utilization-of-Agricultural-Waste%2Fblob%2Fmain%2Fcode%2Freproduce_analysis.R&flow_extra=eyJsaW5rX3R5cGUiOiJjb2RlX2ludGVycHJldGVyIn0=)
  - 包含数据加载、统计分析、可视化全流程 R 代码
- **数据预处理**：
  bash
# 进入项目根目录
cd Reproduce-the-Resource-Utilization-of-Agricultural-Waste
# 运行预处理脚本，生成标准化实验数据
python code/01_data_preprocessing.py
✅ 输出结果：data/processed/agri_waste_processed_data.csv
包含指标：土壤有效磷、作物产量、碳汇增量、产量提升率等核心实验数据
- **复现结果**：[results/figures/h2_storage_comparison.png](sslocal://flow/file_open?url=https%3A%2F%2Fgithub.com%2FJanney-huang%2FReproduce-the-Resource-Utilization-of-Agricultural-Waste%2Fblob%2Fmain%2Fresults%2Ffigures%2Fh2_storage_comparison.png&flow_extra=eyJsaW5rX3R5cGUiOiJjb2RlX2ludGVycHJldGVyIn0=)
  - 完整复现论文 Figure 6 储氢性能对比图
- **结果及研究内容解读**：[docs/result_interpretation.md](sslocal://flow/file_open?url=https%3A%2F%2Fgithub.com%2FJanney-huang%2FReproduce-the-Resource-Utilization-of-Agricultural-Waste%2Fblob%2Fmain%2Fdocs%2Fresult_interpretation.md&flow_extra=eyJsaW5rX3R5cGUiOiJjb2RlX2ludGVycHJldGVyIn0=)
  - 完整解读研究结论、复现结果与科学意义
- **完整文档站**：[https://janney-huang.github.io/Reproduce-the-Resource-Utilization-of-Agricultural-Waste/](sslocal://flow/file_open?url=https%3A%2F%2Fjanney-huang.github.io%2FReproduce-the-Resource-Utilization-of-Agricultural-Waste%2F&flow_extra=eyJsaW5rX3R5cGUiOiJjb2RlX2ludGVycHJldGVyIn0=)
📊 结果展示
土壤有效磷显著提升
作物产量稳定提高 10%–15%
农业废弃物资源化可减少环境污染、提升碳汇效益
📝 适用人群
农业资源与环境专业科研人员
环境科学、土壤学研究生
希望复现论文实验的学习者
📧 联系方式
GitHub：@Janney-huang
项目仓库：https://github.com/Janney-huang/Reproduce-the-Resource-Utilization-of-Agricultural-Waste
