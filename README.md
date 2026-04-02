# Assignment 7 – Data Visualization with Matplotlib

## Project Purpose

The purpose of this project is to use **Matplotlib** to create meaningful data visualizations from real-world datasets and identify patterns that may not be obvious in raw data alone.

Two different datasets were analyzed:

1. **Fisher’s Iris dataset** using sepal and petal measurements  
2. **Loan dataset** containing borrower and loan information  

The goal was to generate multiple visualizations that communicate differences, trends, and possible relationships within the data.

This assignment focuses on:
- Importing and organizing data into a workable form  
- Creating clear visualizations using Matplotlib  
- Comparing groups within datasets  
- Interpreting trends and patterns from charts  
Only allowed libraries were used:

- `matplotlib`
- `pandas`
- `numpy`
- standard Python modules

---

## Datasets Used

### Iris Dataset

The Iris dataset contains physical measurements of iris flowers from different species.
The visualizations compare species using:
- Sepal length  
- Sepal width  
- Petal length  
- Petal width  
The goal is to visually show how species differ based on physical traits.

---

### Loan Dataset

The loan dataset contains borrower financial information and loan details.
The visualizations explore:
- Loan amount patterns  
- Default rates  
- Borrower income relationships  

The goal is to identify useful trends that may help explain borrowing behavior and default risk.

---

## Class Design and Implementation

The program is organized using a class-based structure so that data loading, visualization, and analysis are separated into clear sections.

### Main Class

`DataVisualizationAnalyzer`

This class handles:

- loading both datasets  
- cleaning and organizing data  
- creating all required charts  
- printing analysis conclusions  
---
## Class Attributes

`iris_sepal_data`  
Stores the sepal measurement dataset.

`iris_petal_data`  
Stores the petal measurement dataset.

`loan_data`  
Stores the loan dataset.

`species_groups`  
Groups iris measurements by species for easier comparison.

`default_flag`  
Stores whether each loan record represents a default or non-default case.

---
## Class Methods

`load_data()`  
Loads all CSV files into pandas DataFrames.

`create_iris_visualizations()`  
Creates three visualizations for the Iris dataset:

- sepal length vs sepal width scatter plot  
- petal length vs petal width scatter plot  
- grouped boxplots for all physical measurements  

These plots help compare physical traits between iris species.

`create_loan_visualizations()`  
Creates three visualizations for the loan dataset:

- median loan amount by loan grade  
- default rate by loan purpose  
- borrower income vs loan amount scatter plot  

These plots help identify trends in lending behavior and risk.

`analyze_loan_data()`  
Prints written conclusions based on the loan visualizations.

`save_plots()`  
Saves each generated chart as image files for review.

---
## Visualizations Created
### Iris Visualizations

1. **Sepal Scatter Plot**  
   Compares sepal length and width across species.

2. **Petal Scatter Plot**  
   Compares petal length and width across species.

3. **Boxplots by Species**  
   Shows spread and median values of all four measurements.

These charts make species differences visually clear.

---
### Loan Visualizations

1. **Median Loan Amount by Grade**  
   Shows how loan size changes across credit grades.

2. **Default Rate by Loan Intent**  
   Shows which loan purposes have higher default frequency.

3. **Income vs Loan Amount Scatter Plot**  
   Compares borrower income and requested loan amount while highlighting defaults.

---

## Analysis Summary

The loan visualizations revealed several trends:

- Loan amounts generally increase as loan grade changes.
- Certain loan purposes such as **medical** and **debt consolidation** showed higher default rates.
- Defaults occur across many income levels, not only among lower-income borrowers.

These conclusions are supported by comparing grouped values and scatter distributions across the charts.

---

## Limitations

Some limitations of this project include:

- Visual conclusions depend on data quality and available variables  
- The datasets may contain missing or simplified values  
- Charts show correlation but do not prove causation  
- Some patterns may require deeper statistical analysis beyond visualization  

Despite these limitations, the visualizations successfully highlight important differences and trends in both datasets.

---
## Output Files

The program saves generated charts as image files, including:

- `iris_sepal_scatter.png`
- `iris_petal_scatter.png`
- `iris_boxplots.png`
- `loan_median_amount_by_grade.png`
- `loan_default_rate_by_intent.png`
- `loan_income_vs_amount_default.png`
