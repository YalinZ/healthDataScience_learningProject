# 💊 罕见药物不良反应 (FAERS/DrugBank) 数据集说明

## 1. 核心特征 (Features)
- `drug_primary` (string): 主治疗药物名称（如 Aspirin, Metformin, Warfarin）
- `drug_concomitant` (string): 联合合并用药名称
- `patient_age`: 患者年龄
- `patient_gender`: 性别 (0: 女性, 1: 男性)
- `dosage_mg`: 药物剂量（毫克）

## 2. 预测目标 (Target & Rare Event)
- `adverse_event_rare` (binary): 是否发生罕见严重不良反应（如 Acute_Liver_Failure 肝衰竭），正样本占比约为 1%~2% (极端不平衡)。
