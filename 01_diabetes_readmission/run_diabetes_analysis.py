import os
import sys

if sys.version_info >= (3, 7):
    sys.stdout.reconfigure(encoding='utf-8')

notebook_path = 'diabetes_analysis.ipynb'

print("="*60)
print("Diabetes Patient Readmission Prediction Project - Execution Script")
print("="*60)

# Check and install dependencies
dependencies = ['xgboost', 'sklearn', 'nbformat', 'nbconvert', 'matplotlib', 'seaborn', 'pandas', 'numpy']
missing_dep = False

for dep in dependencies:
    try:
        if dep == 'sklearn':
            import sklearn
        elif dep == 'xgboost':
            import xgboost
        elif dep == 'nbformat':
            import nbformat
        elif dep == 'nbconvert':
            from nbconvert.preprocessors import ExecutePreprocessor
        elif dep == 'matplotlib':
            import matplotlib
        elif dep == 'seaborn':
            import seaborn
        elif dep == 'pandas':
            import pandas
        elif dep == 'numpy':
            import numpy
    except ImportError:
        print(f"Dependency '{dep}' is missing. Will install all dependencies...")
        missing_dep = True
        break

if missing_dep:
    print("Installing required machine learning packages...")
    os.system('pip install xgboost scikit-learn nbformat nbconvert ipykernel matplotlib seaborn pandas numpy')
else:
    print("All dependencies are already installed.")

import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

print("Reading notebook content...")
with open(notebook_path, 'r', encoding='utf-8') as f:
    nb = nbformat.read(f, as_version=4)

ep = ExecutePreprocessor(timeout=600, kernel_name='python3')

print("Running feature engineering, training, and evaluation...")
try:
    ep.preprocess(nb, {'metadata': {'path': '.'}})
    print("Notebook executed successfully! Saving outputs...")
    with open(notebook_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)
    print("Notebook saved successfully with pre-rendered figures.")
except Exception as e:
    print("Error encountered during execution:")
    print(e)
    sys.exit(1)
print("="*60)
