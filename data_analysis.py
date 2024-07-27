import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

# Replace with your actual DataFrame loading
df = pd.read_csv('Breast_Cancer.csv')

# Distribution of Ages
plt.figure(figsize=(12,6))
median_age = df.Age.median()
sns.histplot(df.Age, color='pink', kde=True, bins=12, stat='density', line_kws={'color': 'red', 'linewidth': 2})
plt.axvline(median_age, color='red', linewidth=2, label='Median Age')
plt.xlabel('Age', fontsize=15)
plt.ylabel('Density', fontsize=15)
#plt.title("Distribution of Ages of Women with Breast Cancer", fontsize=20)
plt.legend()
plt.savefig('static/age_distribution.png')
plt.close()

# Size of the Tumor Based on Grade
plt.figure(figsize=(12,7))
sns.boxplot(x='Tumor Size', y='Grade', data=df, palette='pastel')
plt.xlabel('Tumor Size', fontsize=15)
plt.ylabel('Grade', fontsize=15)
#plt.title("Size of the Tumor Based on Grade", fontsize=20)
plt.savefig('static/tumor_size_grade.png')
plt.close()


# Define custom colors
palette_estrogen = {'Positive': '#ff66b2', 'Negative': '#ff1a66'}  # Light pink and dark pink
palette_progesterone = {'Positive': '#ff66b2', 'Negative': '#ff1a66'}  # Light pink and dark pink

# Create subplots
fig, axes = plt.subplots(1, 2, figsize=(16, 8))

# Plot Estrogen Status
sns.countplot(x='Grade', hue='Estrogen Status', data=df, palette=palette_estrogen, ax=axes[0])
axes[0].set_title("Estrogen Status for Different Grades of Breast Cancer", fontweight="bold", fontsize=15)

# Plot Progesterone Status
sns.countplot(x='Grade', hue='Progesterone Status', data=df, palette=palette_progesterone, ax=axes[1])
axes[1].set_title("Progesterone Status for Different Grades of Breast Cancer", fontweight="bold", fontsize=15)

# Save figure
plt.savefig('static/hormone_status.png')
plt.close()

# 4. Tumor Sizes for Different Ages and Survival Months
plt.figure(figsize=(14,10))
plt.scatter(df.Age, df['Survival Months'], s=df['Tumor Size'], c=df['Tumor Size'], cmap='pink', alpha=0.5, edgecolor='k')
plt.colorbar().set_label('Tumor Size')
plt.xlabel("Age", fontsize=15)
plt.ylabel("Survival Months", fontsize=15)
#plt.title("Tumor Sizes for Different Ages and Survival Months", fontsize=20, fontweight="bold")
plt.savefig('static/tumor_survival.png')
plt.close()

# 5. Patient Dead or Alive Based on Differentiation Status
# Define custom colors
palette_status = {'Dead': '#ff1a66', 'Alive': '#ff66b2'}  # Dark pink and light pink

# Plot
plt.figure(figsize=(14, 6))
ax = sns.countplot(x='differentiate', hue='Status', data=df, palette=palette_status)

# Annotate bars
for p in ax.patches:
    ax.annotate('{:.1f}'.format(p.get_height()), (p.get_x() + p.get_width() / 2, p.get_height()), 
                ha='center', va='center', fontsize=12, color='black', xytext=(0, 10), textcoords='offset points')

plt.xticks(rotation=30)
plt.xlabel("Differentiation Status", fontsize=15)
plt.ylabel("Count", fontsize=15)
#plt.title("Patient Dead or Alive Based on Differentiation Status", fontsize=20, fontweight="bold")

# Save figure
plt.savefig('static/differentiation_status.png')
plt.close()

# 6. Distribution Between Regional Node Examined and Regional Node Positive
plt.figure(figsize=(10,10))
sns.kdeplot(x=df['Regional Node Examined'], y=df['Reginol Node Positive'], cmap='Reds', shade=True, bw_adjust=0.5)
plt.xlabel('Regional Node Examined', fontsize=15)
plt.ylabel('Reginol Node Positive', fontsize=15)
#plt.title("Distribution Between Regional Node Examined and Regional Node Positive", fontsize=20, fontweight="bold")
plt.savefig('static/regional_node.png')
plt.close()