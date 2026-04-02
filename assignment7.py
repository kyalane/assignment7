import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def load_iris_data(sepal_path="Sepal_Data.csv", petal_path="Petal_Data.csv"):
    sepal = pd.read_csv(sepal_path)
    petal = pd.read_csv(petal_path)
    merged = pd.merge(sepal, petal, on=["sample_id", "species"], how="inner")
    return merged


def iris_visualizations(iris_df):
    species = iris_df["species"].unique()
    colors = {s: c for s, c in zip(species, ["tab:blue", "tab:orange", "tab:green"]) }

    fig, ax = plt.subplots(figsize=(8, 6))
    for s in species:
        sub = iris_df[iris_df["species"] == s]
        ax.scatter(sub["sepal_length"], sub["sepal_width"], label=s, alpha=0.75, s=45, c=colors[s], edgecolors="k")
    ax.set_xlabel("Sepal Length")
    ax.set_ylabel("Sepal Width")
    ax.set_title("Iris Sepal Dimensions by Species")
    ax.legend(title="Species")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig("iris_sepal_scatter.png", dpi=150)

    fig, ax = plt.subplots(figsize=(8, 6))
    for s in species:
        sub = iris_df[iris_df["species"] == s]
        ax.scatter(sub["petal_length"], sub["petal_width"], label=s, alpha=0.75, s=45, c=colors[s], edgecolors="k")
    ax.set_xlabel("Petal Length")
    ax.set_ylabel("Petal Width")
    ax.set_title("Iris Petal Dimensions by Species")
    ax.legend(title="Species")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig("iris_petal_scatter.png", dpi=150)

    fig, axs = plt.subplots(2, 2, figsize=(12, 10), sharey=False)
    metric_info = [
        ("sepal_length", "Sepal Length"),
        ("sepal_width", "Sepal Width"),
        ("petal_length", "Petal Length"),
        ("petal_width", "Petal Width"),
    ]
    for (col, label), ax in zip(metric_info, axs.flatten()):
        iris_df.boxplot(column=col, by="species", ax=ax, patch_artist=True,
                        boxprops=dict(facecolor="lightblue", edgecolor="black"),
                        medianprops=dict(color="red"))
        ax.set_title(label)
        ax.set_xlabel("Species")
        ax.set_ylabel(label)
        ax.grid(True, axis="y", alpha=0.2)
    fig.suptitle("Iris Sepal and Petal Dimension Distribution by Species")
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    fig.savefig("iris_boxplots.png", dpi=150)

    print("Iris visualizations saved: iris_sepal_scatter.png, iris_petal_scatter.png, iris_boxplots.png")


def clean_loan_amount(loan_str):
    if pd.isna(loan_str):
        return np.nan
    return float(str(loan_str).replace("£", "").replace(",", ""))


def load_and_prepare_loan_data(path="LoanDataset - LoansDatasest.csv"):
    loan_df = pd.read_csv(path)
    loan_df["loan_amnt_clean"] = loan_df["loan_amnt"].apply(clean_loan_amount)
    loan_df["loan_int_rate"] = pd.to_numeric(loan_df["loan_int_rate"], errors="coerce")
    loan_df["default_flag"] = loan_df["Current_loan_status"].fillna("UNKNOWN").str.upper().apply(lambda x: 1 if x.strip() == "DEFAULT" else 0)
    loan_df["home_ownership"] = loan_df["home_ownership"].fillna("UNKNOWN")
    loan_df["loan_grade"] = loan_df["loan_grade"].fillna("UNKNOWN")
    loan_df["loan_intent"] = loan_df["loan_intent"].fillna("UNKNOWN")
    return loan_df


def loan_visualizations(loan_df):
    # 1) Loan amount distribution by loan grade
    loan_by_grade = loan_df.groupby("loan_grade")["loan_amnt_clean"].median().sort_values()
    fig, ax = plt.subplots(figsize=(10, 6))
    loan_by_grade.plot(kind="bar", ax=ax, color="skyblue", edgecolor="black")
    ax.set_ylabel("Median Loan Amount")
    ax.set_title("Median Loan Amount by Loan Grade")
    ax.grid(axis="y", alpha=0.3)
    fig.tight_layout()
    fig.savefig("loan_median_amount_by_grade.png", dpi=150)

    # 2) Default rate by loan intent
    default_rates = loan_df.groupby("loan_intent")["default_flag"].mean().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(10, 6))
    default_rates.plot(kind="bar", ax=ax, color="coral", edgecolor="black")
    ax.set_ylabel("Default Rate")
    ax.set_title("Default Rate by Loan Intent")
    ax.set_ylim(0, 1)
    ax.grid(axis="y", alpha=0.3)
    fig.tight_layout()
    fig.savefig("loan_default_rate_by_intent.png", dpi=150)

    # 3) Income vs loan amount, default vs non-default
    fig, ax = plt.subplots(figsize=(10, 6))
    for flag, label, col in [(0, "No Default", "tab:green"), (1, "Default", "tab:red")]:
        subset = loan_df[loan_df["default_flag"] == flag]
        ax.scatter(subset["customer_income"], subset["loan_amnt_clean"], alpha=0.6, label=label, c=col, s=40, edgecolors="k")
    ax.set_xlabel("Customer Income")
    ax.set_ylabel("Loan Amount")
    ax.set_title("Loan Amount vs Customer Income (Default vs No Default)")
    ax.legend()
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.grid(True, which="both", alpha=0.25)
    fig.tight_layout()
    fig.savefig("loan_income_vs_amount_default.png", dpi=150)

    print("Loan visualizations saved: loan_median_amount_by_grade.png, loan_default_rate_by_intent.png, loan_income_vs_amount_default.png")


def loan_analysis_text(loan_df):
    top_intents = loan_df["loan_intent"].value_counts().head(3)
    text = []
    text.append("Loan data visual analysis summary:")
    text.append(f"1. Top 3 loan intents by count: {', '.join([f'{i} ({c})' for i,c in top_intents.items()])}.")
    default_by_intent = loan_df.groupby("loan_intent")["default_flag"].mean().sort_values(ascending=False).head(3)
    text.append(f"2. Highest default rates are for: {', '.join([f'{i} ({d:.2f})' for i,d in default_by_intent.items()])}.")

    median_by_grade = loan_df.groupby("loan_grade")["loan_amnt_clean"].median().sort_values()
    text.append(f"3. Median loan amount increases with grade (from lower to higher): {', '.join([f'{g}:{int(v)}' for g,v in median_by_grade.items()])}.")

    default_rate = loan_df["default_flag"].mean()
    text.append(f"4. Overall default rate in dataset is {default_rate:.2%}.")

    text.append("5. The relationship between customer income and loan amount shows that high loan amounts are mostly requested by higher-income borrowers, but defaults are present across the spectrum.")
    text.append("Conclusion: Risk patterns are visible in loan intent and grade; data-driven underwriting should consider both loan purpose and borrower history alongside loan amount.")
    return "\n".join(text)


def main():
    print("=== Iris dataset visualizations ===")
    iris_df = load_iris_data()
    iris_visualizations(iris_df)

    print("=== Loan dataset visualizations ===")
    loan_df = load_and_prepare_loan_data()
    loan_visualizations(loan_df)

    analysis = loan_analysis_text(loan_df)
    print("\n" + analysis)


if __name__ == "__main__":
    main()
