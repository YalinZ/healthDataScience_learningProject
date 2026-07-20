# 📊 医疗与数据科学实战项目全集 (Health Data Science & Machine Learning Portfolio)

欢迎来到数据分析与机器学习项目全集仓库！本仓库收录了面向真实医疗与业务场景的数据挖掘、统计建模、机器学习算法评估及 Web 端应用部署实战案例。

---

## 🗺️ 项目全景导航 (Portfolio Navigation)

| 项目编号 | 项目名称 | 核心技术与应用领域 | 项目状态 | 跳转链接 |
| :---: | :--- | :--- | :---: | :---: |
| **01** | **01_diabetes_readmission**<br>(糖尿病 30 天再入院预测) | 特征工程 · XGBoost/随机森林 · SHAP 归因 · Streamlit 部署 | **`[已完成]`** | [查看项目](./01_diabetes_readmission) \| [结项报告](./01_diabetes_readmission/project_summary.md) |
| **02** | **02_survival_analysis**<br>(肺癌患者生存期与风险比分析) | 生存分析 (Survival Analysis) · Kaplan-Meier · 随机生存森林 (RSF) · C-index | **`[已完成]`** | [查看项目](./02_survival_analysis) \| [建模 Notebook](./02_survival_analysis/survival_analysis.ipynb) |
| **03** | **03_time_series_forecast**<br>(用户购买行为与时间序列预测) | 时间序列分析 (Time Series) · ARIMA/Prophet · 销量预测 | **`[规划中]`** | *规划中...* |

---

## 📂 项目详细介绍

### 🩺 项目 01：01_diabetes_readmission (糖尿病 30 天再入院预测)
- **业务背景**：30 天内再入院率是现代医疗质量评估的核心黄金指标。本项目基于美国 130 家医院 10 万+ 患者临床诊疗数据，构建低延迟、高召回率的再入院预警模型。
- **技术亮点**：
  - **特征工程**：ICD-9 诊断代码大类归纳、缺失值处理、性别/科室独热编码 (`One-Hot Encoding`)。
  - **模型训练与不平衡处理**：使用 **随机森林** 与 **XGBoost** 建模，配置 `scale_pos_weight` 对正样本损失进行惩罚，成功提升再入院高危拦截率（Recall 达 44.06%）。
  - **SHAP 归因**：引入 SHAP 黑盒归因，揭示历史住院次数（`number_inpatient`）与病症数是第一预测推手。
  - **概率校准与 Web 部署**：基于贝叶斯概率反校准公式解决模型输出概率膨胀 Bug，使用 **Streamlit** 搭建高颜值三色风险预警评估网页。
- **快速入口**：
  - 📖 [项目全景结项报告 (project_summary.md)](./01_diabetes_readmission/project_summary.md)
  - 📓 [完整分析与建模 Notebook (diabetes_analysis.ipynb)](./01_diabetes_readmission/diabetes_analysis.ipynb)
  - 🖥️ [Streamlit 网页部署应用代码 (app.py)](./01_diabetes_readmission/app.py)

---

### 🫁 项目 02：02_survival_analysis (肺癌患者生存期与风险比分析)
- **业务背景**：基于 NCCTG 临床肺癌数据集，针对观察生存时间（Time）与死亡/删失事件（Event）进行前沿生存分析与个体化风险预警。
- **技术亮点**：
  - **总体 Kaplan-Meier 分析**：拟合全组 228 例患者生存曲线，测算中位生存期为 **310.0 天（约 10.2 个月）**，带 95% 置信区间与删失标记。
  - **随机生存森林 (RSF) 机器学习升级**：引入非参数集成模型 `scikit-survival`，克服传统 Cox PH 模型的同比例风险假设限制，测试集 C-index 从 **0.5123** 显著提升至 **0.5603**（提升 **+9.37%**）。
  - **个体化动态生存曲线预测**：为不同体能状态（ECOG 0分 vs 2分）患者生成 0 ~ 800 天内的个性化生存衰减图表。
- **快速入口**：
  - 📓 [完整分析与建模 Notebook (survival_analysis.ipynb)](./02_survival_analysis/survival_analysis.ipynb)
  - 📊 [总体 KM 生存曲线图 (overall_km_curve.png)](./02_survival_analysis/overall_km_curve.png)
  - 📈 [个体化 RSF 生存衰减预测图 (individual_rsf_survival_curves.png)](./02_survival_analysis/individual_rsf_survival_curves.png)
  - 📋 [任务动态看板 (todo.md)](./02_survival_analysis/todo.md)

---

## 🛠️ 环境依赖与快速开始

1. **克隆本仓库**：
   ```bash
   git clone https://github.com/YalinZ/healthDataScience_learningProject.git
   cd healthDataScience_learningProject
   ```

2. **运行项目 01（糖尿病预测 Web App）**：
   ```bash
   cd 01_diabetes_readmission
   pip install pandas xgboost scikit-learn streamlit joblib shap
   streamlit run app.py
   ```

3. **运行项目 02（肺癌生存分析 Notebook）**：
   ```bash
   cd 02_survival_analysis
   pip install "numpy<2" lifelines "scikit-survival==0.23.0" matplotlib seaborn
   jupyter notebook survival_analysis.ipynb
   ```

---

## 📬 维护者与许可说明
- **维护者**：YalinZ
- **许可证**：MIT License
