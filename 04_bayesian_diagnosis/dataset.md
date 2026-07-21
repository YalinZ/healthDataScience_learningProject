# 🩺 常见呼吸道与传染病贝叶斯网络节点字典

## 1. 疾病节点 (Target Disease Nodes - 互斥或关联)
- `Flu` (流感): 先验概率 P(Flu) = 0.08
- `COVID` (新冠): 先验概率 P(COVID) = 0.05
- `Cold` (普通感冒): 先验概率 P(Cold) = 0.15

## 2. 症状观察节点 (Symptom Nodes - 证据 Evidence)
- `Fever` (发热): 受 Flu, COVID, Cold 共同影响
- `Cough` (咳嗽): 受 Flu, COVID, Cold 共同影响
- `LossOfTaste` (味觉/嗅觉丧失): 主要受 COVID 驱动 (条件概率差异显著)
- `SoreThroat` (喉咙痛): 常见于 Cold 和 COVID
- `Fatigue` (极度疲劳): 常见于 Flu 和 COVID

## 3. 概率表 (CPT - Conditional Probability Tables)
- 各疾病节点对症状节点的激活概率矩阵（见 Python 代码结构配置）。

## 4. 模型对比维度 (Baseline vs Evolution)
- **伯努利朴素贝叶斯 (Bernoulli Naive Bayes)**：作为基线模型，假设发热、咳嗽、味觉丧失、疲劳等所有症状在给定疾病条件下相互独立。
- **贝叶斯信念网络 (Bayesian Belief Network, BBN)**：作为演进模型，显式建模症状间的条件依赖（如：发热可能诱发疲劳，COVID 强驱动味觉丧失与发热的协同出现）。
