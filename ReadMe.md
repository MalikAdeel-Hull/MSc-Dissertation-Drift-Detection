# Monitoring Population Drift in Deployed Medical AI

**Author:** Malik Adeel Anjum  
**Project:** MSc AI for Healthcare Dissertation (University of Hull)

## 📊 Executive Summary & Slides
This repository contains the experimental pipeline for investigating **"Silent Failure"** in medical AI models. Using the **Pima Indians Diabetes Dataset**, the research simulates how patient demographic shifts (Population Drift) degrade model reliability.

> **[📄 View Project Presentation Slides (PDF)](docs/Drift_Detection_Presentation_Slides.pdf)** > *A visual summary of the research gap, methodology, and the "Trade-off" conclusion.*

---

## 📌 Research Objective
To evaluate the safety trade-offs between **Partitioning methods (Isolation Forest)** and **Distance-based methods (One-Class SVM)** when monitoring clinical data. The study validates performance across two distinct failure modes:
1.  **Gradual Drift:** Simulating slow biological changes (e.g., rising population BMI).
2.  **Abrupt Drift:** Simulating sudden systemic shocks (e.g., sensor calibration errors).

## 📂 Repository Structure

```text
├── data/                               <-- Pima Indians Diabetes Dataset
├── docs/
│   └── Drift_Detection_Presentation_Slides.pdf  <-- Executive Summary Slides
├── notebooks/
│   ├── 01_Baseline_EDA_and_Stats.ipynb           <-- Statistical baselining & imputation
│   ├── 02_Gradual_Drift_Experiment_OCSVM.ipynb   <-- Gradual drift sensitivity (OCSVM)
│   ├── 03_Gradual_Drift_Experiment_IsoForest.ipynb <-- Gradual drift sensitivity (IsoForest)
│   ├── 04_Abrupt_Drift_Experiment_IsoForest.ipynb  <-- Abrupt drift sensitivity (IsoForest)
│   └── 05_Abrupt_Drift_Experiment_OCSVM.ipynb    <-- Abrupt drift sensitivity (OCSVM)
├── requirements.txt
└── README.md