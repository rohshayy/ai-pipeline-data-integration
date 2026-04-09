# ai-pipeline-data-integration
A data engineering pipeline simulating multi-branch university data integration, featuring merging, imputation, and feature scaling.

# AI Data Integration Pipeline

## **Project Overview**
This project simulates a real-world AI data engineering task: consolidating fragmented datasets from multiple regional branches into a unified, ML-ready master file. The pipeline handles data concatenation, relational merging, and statistical imputation, concluding with feature scaling (normalization) for future Deep Learning applications.

## **Core Technical Implementations**

### **1. Data Consolidation (Concatenation)**
* **Method:** `pd.concat(axis=0)`
* **Logic:** The pipeline stacks data from Branch A and Branch B. 
* **Technical Note:** In this implementation, we use **Axis 0**, which refers to the **Row-wise** concatenation (stacking one branch on top of the other). Conversely, **Axis 1** would be used for **Column-wise** concatenation if we were adding new features to the same students.

### **2. Relational Data Merging**
* **Method:** `pd.merge()`
* **Logic:** Performed a left-join between the master university records and a secondary "City" dataset using `Student_ID` as the primary key. This mimics how AI engineers pull metadata from disparate SQL tables.

### **3. Statistical Imputation (Math-Logic)**
As a Mathematics MPhil, I have implemented two specific strategies to preserve data integrity:
* **Global Mean Imputation:** Used for Math scores to maintain the overall average of the population.
* **Median Imputation:** Used for Physics scores to ensure the distribution is not skewed by outliers.

### **4. Feature Scaling for AI**
* **Total_Score_Normalized:** Calculated as `(Math + Physics) / 200`.
* **Rationale:** Scaling data to a range of [0, 1] is a critical pre-processing step for Neural Networks. It ensures that the loss function surface is more spherical, allowing Gradient Descent to converge significantly faster.

## **Technical Stack**
* **Language:** Python
* **Library:** Pandas
* **IDE:** PyCharm

## **Usage Instructions**
1. Ensure Python and Pandas are installed.
2. Run the pipeline script.
   python Data_Integration_Pipeline.py
