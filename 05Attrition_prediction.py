from sklearn.model_selection import train_test_split, StratifiedShuffleSplit

# Split data into train and test sets
train, test, target_train, target_val = train_test_split(
    attrition_final,   # features
    target,            # target variable
    train_size=0.8,    # 80% train, 20% test
    random_state=0,
    stratify=target    # optional: ensures class distribution is preserved
)


oversampler  = SMOTE(random_state= 0)
smote_train, smote_target = oversampler.fit_resample(train, target_train)


seed = 0

rf_params = {
    'n_jobs': -1,
    'n_estimators': 1000,
#     'warm_start': True,
    'max_depth': 4,
    'min_samples_leaf': 2,
    'max_features' : 'sqrt',
    'random_state' : seed,
    'verbose': 0
}

rf = RandomForestClassifier(**rf_params)
rf.fit(smote_train, smote_target)
rf_predictions = rf.predict(test)
print("Accuracy score: {}".format(accuracy_score(target_val, rf_predictions)))
print("="*80)
print(classification_report(target_val, rf_predictions))
