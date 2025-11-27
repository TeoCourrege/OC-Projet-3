import pandas as pd


building_consumption = pd.read_csv("2016_Building_Energy_Benchmarking.csv")


# On separe les colonnes numeriques et qualitatives
num_cols = building_consumption.select_dtypes(include=['float64', 'int64']).columns
cat_cols = building_consumption.select_dtypes(include=['object']).columns


print("=== Colonnes numériques ===")
for col in num_cols:
    print(f"\nColonne: {col}")
    print("Type:", building_consumption[col].dtype)
    print("Valeurs manquantes:", building_consumption[col].isna().sum())
    print("Valeurs uniques:", building_consumption[col].nunique())
    print("Statistiques descriptives:")
    print(building_consumption[col].describe())


print("\n=== Colonnes catégorielles ===")
for col in cat_cols:
    print(f"\nColonne: {col}")
    print("Type:", building_consumption[col].dtype)
    print("Valeurs manquantes:", building_consumption[col].isna().sum())
    print("Nombre de valeurs uniques:", building_consumption[col].nunique())
    print("Top 5 valeurs les plus fréquentes:")
    print(building_consumption[col].value_counts().head(5))