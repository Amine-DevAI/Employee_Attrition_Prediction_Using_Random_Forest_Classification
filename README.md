# Employee Attrition Prediction Using Random Forest

A comprehensive machine learning project that predicts employee attrition using Random Forest classification with advanced data preprocessing and visualization techniques.

## 📊 Project Overview

This project analyzes employee data to predict which employees are likely to leave the company, enabling HR departments to take proactive retention measures. The model achieves **86.05% accuracy** with excellent performance in identifying employees who will stay (97% recall).

## 🎯 Key Results

- **Overall Accuracy**: 86.05%
- **Staying Employees**: 97% recall, 88% precision
- **At-Risk Employees**: 64% precision when flagged
- **Dataset**: 1,470 employees from IBM HR Analytics dataset

## 🛠️ Technologies Used

- **Python 3.x**
- **Data Analysis**: `pandas`, `numpy`
- **Visualization**: `matplotlib`, `seaborn`, `plotly`
- **Machine Learning**: `scikit-learn`, `imblearn`
- **Key Algorithm**: Random Forest Classifier with SMOTE for class imbalance

## 📁 Repository Structure

```
├── 01_necessary_Python_libraries.py    # Required libraries and imports
├── 02_data_exploration.py              # EDA and visualization code
├── 03Finding_Correlation.py            # Correlation analysis
├── 04Feature_Engineering.py            # Data preprocessing pipeline
├── 05Attrition_prediction.py          # Model training and evaluation
├── Employee_Attrition-2.pdf           # Complete project documentation
└── README.md                          # This file
```

## 🔄 Code Organization

This project follows a **modular approach** with separate Python files for each analysis phase:

### **01_necessary_Python_libraries.py**
- All required imports and library dependencies
- Environment setup and configuration

### **02_data_exploration.py** 
- 9 KDE plots for bivariate relationship analysis
- Data distribution and statistical summaries
- Initial data quality assessment

### **03Finding_Correlation.py**
- Correlation matrix generation and visualization
- Feature relationship analysis
- Interactive Plotly heatmap creation

### **04Feature_Engineering.py**
- Target variable encoding (Yes/No → 1/0)
- Categorical/numerical feature separation
- One-hot encoding implementation
- Train/test split with stratification

### **05Attrition_prediction.py**
- SMOTE implementation for class imbalance
- Random Forest model training
- Performance evaluation and metrics
- Results interpretation

## 🔍 Analysis Pipeline

### 1. Exploratory Data Analysis
- **9 KDE plots** analyzing bivariate relationships
- **Correlation matrix** of 25 numerical features
- Interactive visualizations with Plotly

### 2. Data Preprocessing
- Target variable encoding (Yes/No → 1/0)
- Categorical and numerical feature separation
- One-hot encoding for categorical variables
- Stratified train/test split (80/20)

### 3. Class Imbalance Handling
- **SMOTE** (Synthetic Minority Oversampling Technique)
- Applied only to training data to prevent data leakage
- Balanced minority class (attrition cases)

### 4. Model Training
- **Random Forest Classifier** with optimized hyperparameters:
  - 1000 estimators
  - Max depth: 4
  - Min samples per leaf: 2
  - Feature sampling: sqrt

### 5. Evaluation
- Comprehensive metrics: accuracy, precision, recall, F1-score
- Tested on original (unbalanced) data for realistic assessment

### Key Visualizations

The analysis generates several key visualizations:
- **KDE relationship plots** (from `02_data_exploration.py`)
- **Correlation heatmap** (from `03Finding_Correlation.py`) 
- **Performance metrics visualization** (from `05Attrition_prediction.py`)

## 💼 Business Impact

### For HR Departments:
- **High-confidence retention insights**: 97% accuracy in identifying stable employees
- **Targeted interventions**: 64% accuracy when flagging at-risk employees
- **Cost-effective approach**: Minimizes false-positive interventions
- **Strategic workforce planning**: Understanding natural attrition rates

### Operational Recommendations:
- Prioritize retention efforts on flagged cases (64% accuracy)
- Implement secondary screening for at-risk employees
- Maintain engagement programs for predicted stable employees
- Monitor missed cases for model improvement

## 🚀 Getting Started

### Prerequisites
```bash
pip install numpy pandas seaborn matplotlib plotly scikit-learn imbalanced-learn
```

### Running the Analysis

The project is designed to run sequentially:

```bash
# 1. Set up environment
python 01_necessary_Python_libraries.py

# 2. Explore the data
python 02_data_exploration.py

# 3. Analyze correlations
python 03Finding_Correlation.py

# 4. Engineer features
python 04Feature_Engineering.py

# 5. Train and evaluate model
python 05Attrition_prediction.py
```

Or run individual modules based on your needs:

## 📊 Model Performance Details

| Metric | No Attrition (0) | Attrition (1) | Overall |
|--------|------------------|---------------|---------|
| **Precision** | 0.88 | 0.64 | 0.84 |
| **Recall** | 0.97 | 0.30 | 0.86 |
| **F1-Score** | 0.92 | 0.41 | 0.84 |
| **Support** | 247 employees | 47 employees | 294 total |

## 🎓 Methodology Highlights

- **Proper ML Pipeline**: No data leakage, stratified sampling
- **Class Imbalance Handling**: SMOTE applied correctly
- **Feature Engineering**: Smart encoding and preprocessing
- **Comprehensive EDA**: Multi-dimensional relationship analysis
- **Business-Focused Evaluation**: Realistic performance assessment

## 📋 Dataset Information

**Source**: IBM HR Analytics Employee Attrition & Performance Dataset  
**Size**: 1,470 employees  
**Features**: Demographics, compensation, satisfaction, tenure, performance metrics  
**Target**: Binary classification (Stay/Leave)  
**Class Distribution**: ~84% staying, ~16% attrition

## 🔗 Connect

- **GitHub**: [Amine-DevAI](https://github.com/Amine-DevAI)
- **LinkedIn**: [Mohamed Amine](https://www.linkedin.com/in/mohamed-amine-mammar-el-hadj-715a41295)

## 📄 Documentation

For detailed methodology, mathematical formulations, and comprehensive analysis, see the complete [project documentation](Employee_Attrition-2.pdf).

## 🤝 Contributing

Feel free to fork this repository and submit pull requests for improvements. Issues and feature requests are welcome!

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

---

*This project demonstrates end-to-end machine learning methodology with focus on business applicability and professional documentation standards.*
