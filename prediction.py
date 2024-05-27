categorical_columns = ['BusinessTravel', 'Department', 'EducationField']
for column in categorical_columns:
    if column in df.columns:
        label_encoder = LabelEncoder()
        df[column] = label_encoder.fit_transform(df[column])
    else:
        print(f"Column '{column}' not found in the DataFrame")

features = ['Age', 'DailyRate', 'DistanceFromHome', 'Education', 'EnvironmentSatisfaction', 'HourlyRate',
            'JobInvolvement', 'JobLevel', 'JobSatisfaction', 'MonthlyIncome', 'NumCompaniesWorked',
            'PercentSalaryHike', 'PerformanceRating', 'RelationshipSatisfaction', 'StockOptionLevel',
            'TotalWorkingYears', 'TrainingTimesLastYear', 'WorkLifeBalance', 'YearsAtCompany',
            'YearsInCurrentRole', 'YearsSinceLastPromotion', 'YearsWithCurrManager', 'BusinessTravel',
            'Department', 'EducationField']

missing_features = [feature for feature in features if feature not in df.columns]
if missing_features:
    print(f"Missing features: {missing_features}")
    features = [feature for feature in features if feature in df.columns]

X = df[features]
y = df['Attrition']

scaler = StandardScaler()
X = scaler.fit_transform(X)

# Apply SMOTE to balance the classes
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X, y)

X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.2, random_state=42)

initial_model = RandomForestClassifier(random_state=42)
initial_model.fit(X_train, y_train)
initial_feature_importances = pd.Series(initial_model.feature_importances_, index=features)
top_features = initial_feature_importances.nlargest(10).index.tolist()

# Use only the top features for training
X_train_top = X_train[:, [features.index(f) for f in top_features]]
X_test_top = X_test[:, [features.index(f) for f in top_features]]

# Hyperparameter tuning using RandomizedSearchCV with class weights
param_distributions = {
    'n_estimators': [100, 200, 300],
    'max_features': ['sqrt', 'log2'],  # Avoid 'auto' due to deprecation
    'max_depth': [4, 6, 8, 10],
    'criterion': ['gini', 'entropy'],
    'class_weight': ['balanced', 'balanced_subsample']
}

random_search = RandomizedSearchCV(estimator=RandomForestClassifier(random_state=42),
                                   param_distributions=param_distributions,
                                   n_iter=20,  # Number of parameter settings sampled
                                   cv=3,  # Number of cross-validation folds
                                   n_jobs=-1,  # Use all available CPUs
                                   random_state=42,
                                   scoring='precision')
random_search.fit(X_train_top, y_train)

# Best parameters from RandomizedSearchCV
best_params = random_search.best_params_
print("Best parameters:", best_params)

model = RandomForestClassifier(**best_params, random_state=42)
model.fit(X_train_top, y_train)

y_pred = model.predict(X_test_top)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

precision = precision_score(y_test, y_pred, average=None)
print("Precision for class 0:", precision[0])
print("Precision for class 1:", precision[1])

# Feature Importances
feature_importances = pd.Series(model.feature_importances_, index=top_features)
plt.figure(figsize=(10, 6))
feature_importances.nlargest(10).plot(kind='barh')
plt.title('Top 10 Feature Importance')
plt.xlabel('Importance')
plt.ylabel('Feature')
plt.show()
