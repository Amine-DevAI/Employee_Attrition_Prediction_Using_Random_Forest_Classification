# Map target variable
target_map = {'Yes':1, 'No':0}
target = attrition["Attrition"].apply(lambda x: target_map[x])

# Separate categorical and numerical columns
categorical = attrition.select_dtypes(include='object').columns.tolist()
categorical.remove('Attrition')  # remove target
numerical = attrition.select_dtypes(exclude='object').columns.tolist()

# One-hot encode categorical variables
attrition_cat = pd.get_dummies(attrition[categorical])

# Keep numerical variables
attrition_num = attrition[numerical]

# Combine numerical + encoded categorical features
attrition_final = pd.concat([attrition_num, attrition_cat], axis=1)

