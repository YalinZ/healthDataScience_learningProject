# 📊 医疗与数据科学实战项目全集 (Health Data Science & Machine Learning Portfolio)

欢迎来到数据分析与机器学习项目全集仓库！本仓库收录了面向真实医疗与业务场景的数据挖掘、统计建模、机器学习算法评估及 Web 端应用部署实战案例。

---

## 🗺️ 项目全景导航 (Portfolio Navigation)

| 项目编号 | 项目名称 | 核心技术与应用领域 | 项目状态 | 跳转链接 |
| :---: | :--- | :--- | :---: | :---: |
| **01** | **01_diabetes_readmission**<br>(糖尿病 30 天再入院预测) | 特征工程 · XGBoost/随机森林 · SHAP 归因 · Streamlit 部署 | **`[已完成]`** | [查看项目](./01_diabetes_readmission) \| [结项报告](./01_diabetes_readmission/project_summary.md) |
| **02** | **02_survival_analysis**<br>(肺癌患者生存期与风险比分析) | 生存分析 (Survival Analysis) · Kaplan-Meier · 随机生存森林 (RSF) · C-index | **`[已完成]`** | [查看项目](./02_survival_analysis) \| [建模 Notebook](./02_survival_analysis/survival_analysis.ipynb) |
| **03** | **03_time_series_forecast**<br>(中国流感趋势预测与搜索指数预警) | 时间序列分析 · ADF 检验 · STL 分解 · SARIMA/SARIMAX 外生预警 | **`[已完成]`** | [查看项目](./03_time_series_forecast) \| [分析 Notebook](./03_time_series_forecast/time_series_analysis.ipynb) |
| **04** | **04_bayesian_diagnosis**<br>(常见呼吸道传染病贝叶斯网络诊断) | 贝叶斯信念网络 (BBN) · CPT 概率表 · 变量消除法 · BernoulliNB | **`[已完成]`** | [查看项目](./04_bayesian_diagnosis) \| [分析 Notebook](./04_bayesian_diagnosis/bayesian_diagnosis.ipynb) |

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

### 🤒 项目 03：03_time_series_forecast (中国流感趋势预测与搜索指数预警)
- **业务背景**：结合中国疾控中心历史流感病例监测数据与网络“发烧/流感”百度搜索热度指数，开展季节性时间序列建模与暴发峰值预测。
- **技术亮点**：
  - **ADF 平稳性检验与 STL 分解**：原始序列存在显著上升趋势与冬春季节性（ADF $p=0.9987$），一阶差分后实现平稳（$p<0.05$）；调用 `statsmodels` 拆解出 12 个月冬春高发周期。
  - **无泄露 8:2 时间序列切分**：遵循时序切分红线（无随机打乱），划分 2018.01 - 2022.09 (57个月) 为训练集，2022.10 - 2023.12 (15个月) 为测试集。
  - **SARIMAX 外生预警建模**：引入搜索指数作为外生特征（Exogenous Regressor），增强模型对流行病暴发拐点与高峰期的前瞻性预测能力。
- **快速入口**：
  - 📓 [完整分析与建模 Notebook (time_series_analysis.ipynb)](./03_time_series_forecast/time_series_analysis.ipynb)
  - 📈 [双轴时序对比图 (ts_overview.png)](./03_time_series_forecast/ts_overview.png)
  - 📊 [STL 趋势-季节性-残差分解图 (stl_decomposition.png)](./03_time_series_forecast/stl_decomposition.png)
  - ✂️ [8:2 时间切分示意图 (train_test_split.png)](./03_time_series_forecast/train_test_split.png)
  - 📋 [任务动态看板 (todo.md)](./03_time_series_forecast/todo.md)

---

### 🧬 项目 04：04_bayesian_diagnosis (常见呼吸道传染病贝叶斯网络与朴素贝叶斯诊断对比)
- **业务背景**：探讨概率图模型（PGM）在医学临床诊断与多症状鉴别推理中的实际价值，对比基线朴素贝叶斯 (`BernoulliNB`) 与贝叶斯信念网络 (`BBN`) 的表现。
- **技术亮点**：
  - **BBN 图结构与 CPT 绑定**：基于 `pgmpy` 构建有向无环图 (DAG)，加入症状间横向依赖（`Fever -> Fatigue`），通过 `check_model()` 校验概率守恒。
  - **变量消除法精准推导**：运用 `VariableElimination` 推导后验概率 $P(\text{Disease} \mid \text{Evidence})$。
  - **证据冲击与偏见失真剖析**：当观察到 `Fever=1, LossOfTaste=1` 时，BBN 准确识别 COVID 概率（**87.89%**），而朴素贝叶斯因独立性假设稀释强标志特征概率（降至 **57.56%**）。
- **快速入口**：
  - 📓 [完整分析与建模 Notebook (bayesian_diagnosis.ipynb)](./04_bayesian_diagnosis/bayesian_diagnosis.ipynb)
  - 🕸️ [BBN 网络拓扑图 (bbn_topology.png)](./04_bayesian_diagnosis/bbn_topology.png)
  - 📊 [模型预测概率对比图 (model_comparison.png)](./04_bayesian_diagnosis/model_comparison.png)
  - 📋 [任务动态看板 (todo.md)](./04_bayesian_diagnosis/todo.md)

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

4. **运行项目 03（流感时间序列预测 Notebook）**：
   ```bash
   cd 03_time_series_forecast
   pip install akshare statsmodels pmdarima matplotlib seaborn
   jupyter notebook time_series_analysis.ipynb
   ```

5. **运行项目 04（贝叶斯诊断与 BBN 对比 Notebook）**：
   ```bash
   cd 04_bayesian_diagnosis
   pip install "numpy<2" pgmpy scikit-learn networkx matplotlib seaborn
   jupyter notebook bayesian_diagnosis.ipynb
   ```

---

## 📬 维护者与许可说明
- **维护者**：YalinZ
- **许可证**：MIT License
