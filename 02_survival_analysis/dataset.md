# 🫁 肺癌患者生存期数据集说明 (NCCTG Lung Cancer)

## 数据来源
直接调用 Python 库 `lifelines.datasets.load_lung()` 加载。

## 核心列定义
- `time` (数值型): 观察/随访生存天数 (Survival time in days)。**【生存分析 Time 变量】**
- `status` (数值型): 1 代表删失 (Censored，患者仍存活或失访)，2 代表死亡事件 (Event)。**【生存分析 Event 变量】**
- `age`: 诊断时的患者年龄 (岁)
- `sex`: 性别 (1: 男性, 2: 女性)
- `ph.ecog`: 医师评估的 ECOG 身体状况评分 (0: 正常无症状, 1: 有症状但可走动, 2: 卧床时间 <50%, 3: 卧床时间 >50%)
- `ph.karno`: 医师评估的 Karnofsky 评分
- `pat.karno`: 患者自我评估的 Karnofsky 评分
- `meal.cal`: 吃饭时摄入的卡路里
- `wt.loss`: 过去 6 个月内体重减轻的磅数
