fig, axes = plt.subplots(3, 3, figsize=(15, 12))

def plot_kde(x, y, ax, title, start_color=0.0):
    cmap = sns.cubehelix_palette(start=start_color, light=1, as_cmap=True)
    sns.kdeplot(x=x, y=y, cmap=cmap, fill=True, cut=5, ax=ax)  # fixed
    ax.set(title=title)

plot_kde(attrition['Age'], attrition['TotalWorkingYears'], axes[0,0], 'Age vs TotalWorkingYears', 0.0)
plot_kde(attrition['Age'], attrition['DailyRate'], axes[0,1], 'Age vs DailyRate', 0.33)
plot_kde(attrition['YearsInCurrentRole'], attrition['Age'], axes[0,2], 'YearsInRole vs Age', 0.66)
plot_kde(attrition['DailyRate'], attrition['DistanceFromHome'], axes[1,0], 'DailyRate vs DistanceFromHome', 1.0)
plot_kde(attrition['DailyRate'], attrition['JobSatisfaction'], axes[1,1], 'DailyRate vs JobSatisfaction', 1.33)
plot_kde(attrition['YearsAtCompany'], attrition['JobSatisfaction'], axes[1,2], 'YearsAtCompany vs JobSatisfaction', 1.66)
plot_kde(attrition['YearsAtCompany'], attrition['DailyRate'], axes[2,0], 'YearsAtCompany vs DailyRate', 2.0)
plot_kde(attrition['RelationshipSatisfaction'], attrition['YearsWithCurrManager'], axes[2,1], 'RelationshipSatisfaction vs YearsWithManager', 2.33)
plot_kde(attrition['WorkLifeBalance'], attrition['JobSatisfaction'], axes[2,2], 'WorkLifeBalance vs JobSatisfaction', 2.66)

fig.tight_layout()
plt.show()

