import plotly.graph_objs as go

# Encode target
attrition["Attrition_numerical"] = attrition["Attrition"].map({'Yes':1, 'No':0})

# Numerical columns (including target for correlation)
numerical = [
    'Age', 'DailyRate', 'DistanceFromHome', 'Education', 'EmployeeNumber',
    'EnvironmentSatisfaction', 'HourlyRate', 'JobInvolvement', 'JobLevel',
    'JobSatisfaction', 'MonthlyIncome', 'MonthlyRate', 'NumCompaniesWorked',
    'PercentSalaryHike', 'PerformanceRating', 'RelationshipSatisfaction',
    'StockOptionLevel', 'TotalWorkingYears', 'TrainingTimesLastYear',
    'WorkLifeBalance', 'YearsAtCompany', 'YearsInCurrentRole',
    'YearsSinceLastPromotion', 'YearsWithCurrManager', 'Attrition_numerical'
]

# Compute correlation
corr_matrix = attrition[numerical].corr()

# Create heatmap
heatmap = go.Heatmap(
    z=corr_matrix.values,
    x=corr_matrix.columns,
    y=corr_matrix.columns,
    colorscale='Viridis',
    reversescale=False,
    opacity=1.0
)

# Layout
layout = go.Layout(
    title='Pearson Correlation of Numerical Features',
    xaxis=dict(ticks='', nticks=len(numerical)),
    yaxis=dict(ticks=''),
    width=900, height=700
)

# Figure
fig = go.Figure(data=[heatmap], layout=layout)
py.iplot(fig, filename='labelled-heatmap')

