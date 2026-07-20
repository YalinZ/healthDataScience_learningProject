# 📋 任务动态看板

- [x] 任务 1: 读取 `lifelines.datasets.load_lung` 数据，检查缺失值并转换 `status` 列为标准的二进制 (0=Censored, 1=Event)
- [x] 任务 2: 计算全局中位生存时间 (Median Survival Time) 并绘制总体 Kaplan-Meier 生存曲线
- [ ] 任务 3: 按性别 (Sex) 与 ECOG 评分拆分患者，绘制分层次 KM 曲线并进行 Log-Rank 差异检验
- [ ] 任务 4: 构建多因素 Cox 回归模型，分析 age、sex、ph.ecog、wt.loss 等特征对生存期的影响
- [ ] 任务 5: 绘制 Cox 模型的风险比森林图 (Forest Plot) 并导出文本分析结论
- [x] 任务 6: 自动安装并导入 `scikit-survival` (`sksurv`) 库，完成数据的训练集/测试集切分
- [x] 任务 7: 训练随机生存森林 (RSF) 模型，计算并对比 Cox 模型与 RSF 模型在测试集上的 C-index 得分
- [x] 任务 8: 为测试集中特定的一位患者，绘制并对比 Cox 与 RSF 预测的个体化生存概率曲线 (Individual Survival Curves)