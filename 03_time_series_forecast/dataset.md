# 🤒 中国流行性感冒发病数与百度搜索指数时间序列数据集

## 1. 核心时间序列
- `date` (datetime64): 采样日期（建议按月 `MS` 或按周 `W` 聚合）。**【时间索引列】**
- `flu_cases` (numeric): 中国疾控中心 (CDC) 或开源数据集公布的全国/各省流感确诊发病人数。**【主预测目标 Y】**

## 2. 外生特征 (External Regressors / X)
- `search_index_fever` (numeric): “发烧”关键字的百度/微博搜索热度指数。
- `search_index_flu` (numeric): “流感”关键字的搜索热度指数。
- `avg_temp` (numeric): 全国/省份月平均气温（气温骤降通常引发呼吸道疾病）。
