import joblib

# 1. 就像打开休眠仓一样，一键解冻并加载模型
loaded_stuff = joblib.load("best_diabetes_model.pkl")

# 2. 打印看看它的真面目（如果是 XGBoost，会输出 XGBClassifier 对象的参数）
print("成功复活的对象：", loaded_stuff)

# 3. 它已经满血复活了，现在可以直接让它干活预测
# 假设传入一行对齐好的网页测试数据
# prediction = loaded_stuff.predict(web_input_data)