import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris


def main():
    # Load Iris dataset via sklearn
    iris = load_iris()

    # Convert to DataFrame
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

    # Task 1: Inspect data
    print("First 5 rows:")
    print(df.head())

    print("\nData types and missing values:")
    print(df.info())
    print("\nMissing values per column:")
    print(df.isnull().sum())

    # No missing values in Iris, but if there were, here is how to handle:
    # df = df.dropna()  # or df.fillna(method='ffill')

    # Task 2: Basic data analysis
    print("\nBasic statistics:")
    print(df.describe())

    # Grouping by species and compute mean sepal length
    group_means = df.groupby('species')['sepal length (cm)'].mean()
    print("\nMean sepal length per species:")
    print(group_means)

    # Task 3: Data visualization
    sns.set(style="whitegrid")

    # 1. Line chart: trend of average sepal length over species (just a simple example)
    plt.figure(figsize=(8, 5))
    group_means.plot(kind='line', marker='o')
    plt.title("Average Sepal Length by Species")
    plt.xlabel("Species")
    plt.ylabel("Average Sepal Length (cm)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # 2. Bar chart: average petal length per species
    plt.figure(figsize=(8, 5))
    sns.barplot(x='species', y='petal length (cm)', data=df, ci=None)
    plt.title("Average Petal Length per Species")
    plt.xlabel("Species")
    plt.ylabel("Petal Length (cm)")
    plt.tight_layout()
    plt.show()

    # 3. Histogram: distribution of sepal width
    plt.figure(figsize=(8, 5))
    sns.histplot(df['sepal width (cm)'], bins=15, kde=True)
    plt.title("Distribution of Sepal Width")
    plt.xlabel("Sepal Width (cm)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

    # 4. Scatter plot: sepal length vs petal length
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=df)
    plt.title("Sepal Length vs Petal Length")
    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Petal Length (cm)")
    plt.legend(title="Species")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    try:
        main()
    except FileNotFoundError:
        print("File not found error - make sure the dataset is available.")
    except Exception as e:
        print(f"An error occurred: {e}")
