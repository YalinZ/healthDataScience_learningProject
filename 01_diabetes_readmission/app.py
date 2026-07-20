import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# 设置网页基本配置 (高颜值第一步)
st.set_page_config(
    page_title="糖尿病患者再入院风险评估系统",
    page_icon="🩺",
    layout="centered",
    initial_sidebar_state="expanded"
)

# 注入自定义 CSS 样式，打造 Premium/Aesthetic 视觉效果
st.markdown("""
<style>
    /* 全局背景和字体微调 */
    .stApp {
        background-color: #f9fbfd;
    }
    /* 渐变标题横幅 */
    .header-banner {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        color: white;
        margin-bottom: 25px;
        box-shadow: 0 4px 15px rgba(30, 60, 114, 0.15);
    }
    .header-banner h1 {
        color: white !important;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-weight: 700;
        margin-bottom: 10px;
    }
    .header-banner p {
        font-size: 1.1rem;
        opacity: 0.9;
        margin: 0;
    }
    /* 卡片布局样式 */
    .card-panel {
        background-color: white;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.02), 0 1px 3px rgba(0, 0, 0, 0.05);
        border: 1px solid #eef2f6;
        margin-bottom: 20px;
    }
    /* 核心指标卡片 */
    .metric-box {
        text-align: center;
        padding: 15px;
        border-radius: 8px;
        font-weight: bold;
    }
    /* 绿色低风险 */
    .risk-low {
        background-color: #e8f5e9;
        color: #2e7d32;
        border: 1px solid #c8e6c9;
    }
    /* 黄色中风险 */
    .risk-medium {
        background-color: #fff3e0;
        color: #ef6c00;
        border: 1px solid #ffe0b2;
    }
    /* 红色高风险 */
    .risk-high {
        background-color: #ffebee;
        color: #c62828;
        border: 1px solid #ffcdd2;
    }
</style>
""", unsafe_allow_html=True)

# 页面顶部横幅
st.markdown("""
<div class="header-banner">
    <h1>🩺 糖尿病患者 30 天再入院风险评估系统</h1>
    <p>基于 XGBoost 机器学习模型的临床决策辅助工具</p>
</div>
""", unsafe_allow_html=True)

# 侧边栏：提供医学背景知识与帮助
st.sidebar.markdown("### 📋 评估系统医学背景")
st.sidebar.info("""
本系统利用机器学习算法（XGBoost），对糖尿病患者出院后 **30天内快速再入院** 的风险进行预测。

**基准线参考**：
本数据集的平均再入院率为 **8.97%**。

**关键预测指标解释**：
- **历史住院次数 (Inpatient Visits)**：反映患者身体的脆弱度与疾病慢性化程度，是最核心的影响特征。
- **确诊病症总数 (Number of Diagnoses)**：反映患者的合并症复杂程度。
- **住院天数与化验次数**：间接对应患者本次发定义的急性程度和治疗调整密度。
""")

# 加载保存的 .pkl 模型组件
@st.cache_resource
def load_model_artifacts():
    pkl_path = "best_diabetes_model.pkl"
    if not os.path.exists(pkl_path):
        st.error(f"❌ 未找到模型文件 '{pkl_path}'，请确保已在 Notebook 中成功运行模型保存步骤。")
        return None
    return joblib.load(pkl_path)

artifacts = load_model_artifacts()

if artifacts is not None:
    model = artifacts['model']
    feature_columns = artifacts['columns']
    feature_medians = artifacts['medians']

    # 主表单卡片
    st.markdown('<div class="card-panel">', unsafe_allow_html=True)
    st.markdown("### ✍️ 请输入患者的临床关键特征")
    
    # 采用两列布局，界面更整洁美观
    col1, col2 = st.columns(2)
    
    with col1:
        number_inpatient = st.number_input(
            "⏳ 历史住院次数 (过去一年)",
            min_value=0, max_value=20, value=0, step=1,
            help="患者在过去一年中因各种原因住院的总次数。"
        )
        
        time_in_hospital = st.slider(
            "🏥 本次住院天数 (天)",
            min_value=1, max_value=14, value=3, step=1,
            help="患者本次因糖尿病或并发症住院的总天数。"
        )
        
        num_lab_procedures = st.slider(
            "🧪 本次住院化验次数 (次)",
            min_value=1, max_value=120, value=40, step=1,
            help="住院期间进行的血液、尿液等化验检测的总次数。"
        )

    with col2:
        gender = st.selectbox(
            "👤 性别",
            options=["女 (Female)", "男 (Male)"],
            index=0,
            help="患者的生理性别。"
        )
        
        number_diagnoses = st.slider(
            "🩺 确诊病症总数 (个)",
            min_value=1, max_value=16, value=6, step=1,
            help="患者出院时病历上记录的诊断病症总数。"
        )

    st.markdown('</div>', unsafe_allow_html=True)

    # 评估按钮
    if st.button("🚀 开始评估再入院风险", use_container_width=True):
        # 1. 构造基础数据框，默认全部使用训练集中位数填充
        input_dict = feature_medians.copy()
        
        # 2. 覆盖用户输入的 5 个最核心特征
        input_dict['number_inpatient'] = number_inpatient
        input_dict['time_in_hospital'] = time_in_hospital
        input_dict['num_lab_procedures'] = num_lab_procedures
        input_dict['number_diagnoses'] = number_diagnoses
        
        # 处理性别 One-Hot 编码 (训练集只有 'gender_Male' 列，Female 为 0，Male 为 1)
        if "男 (Male)" in gender:
            input_dict['gender_Male'] = 1
        else:
            input_dict['gender_Male'] = 0

        # 3. 将字典转为 DataFrame，并确保特征顺序与训练时严格一致
        input_df = pd.DataFrame([input_dict])
        input_df = input_df[feature_columns]

        # 4. 进行模型预测
        # 预测概率 (XGBoost 训练时使用了 scale_pos_weight=10.15 导致输出的概率被拉高，需要进行数学校准)
        uncalibrated_prob = model.predict_proba(input_df)[0][1]
        
        # 概率校准公式: p = p' / (p' + (1 - p') * w)
        w = 10.15
        pred_prob = uncalibrated_prob / (uncalibrated_prob + (1 - uncalibrated_prob) * w)
        
        # 5. 显示评估结果卡片
        st.markdown("### 📊 评估结果")
        
        # 将概率转换为百分比
        prob_pct = pred_prob * 100
        uncalibrated_pct = uncalibrated_prob * 100
        
        # 根据校准后的真实概率评估风险等级（本数据集真实基准再入院率约 8.97%）
        # 我们设定：小于 9% 为低风险，9%~20% 为中度风险，大于 20%（接近均值2.5倍以上）为高风险
        if pred_prob < 0.09:
            risk_class = "risk-low"
            risk_desc = "🟢 低风险患者"
            risk_advice = "该患者的30天内再入院风险低于或接近临床基准线。出院后建议按常规方案进行社区随访与药物管理。"
        elif 0.09 <= pred_prob < 0.20:
            risk_class = "risk-medium"
            risk_desc = "🟡 中度风险患者"
            risk_advice = "该患者的再入院风险超出基准线。建议在出院前加强用药指导，并在出院后第一周内进行电话或门诊随访。"
        else:
            risk_class = "risk-high"
            risk_desc = "🔴 高危风险患者"
            risk_advice = "警告：该患者30天内快速再入院风险极高！建议临床医生重新评估其出院指征，出院后建立绿色通道并进行密集的日间医疗跟踪。"

        # 渲染漂亮的评估卡片
        st.markdown(f"""
        <div class="metric-box {risk_class}">
            <h2 style="margin:0; color:inherit;">{risk_desc}</h2>
            <p style="font-size: 1.5rem; margin: 10px 0 0 0; color:inherit;">预测 30天内再入院概率: {prob_pct:.2f}%</p>
            <p style="font-size: 0.9rem; margin: 5px 0 0 0; opacity: 0.8;">(临床基准发生率: 8.97% | 模型原始未校准得分: {uncalibrated_pct:.1f}%)</p>
        </div>
        """, unsafe_allow_html=True)
        
        # 显示临床建议
        st.markdown(f"**💡 临床干预建议**：{risk_advice}")
        
        # 视觉进度条
        st.progress(pred_prob)

else:
    st.info("💡 请先完成数据建模和模型保存（best_diabetes_model.pkl 文件生成后，刷新网页即可使用）。")
