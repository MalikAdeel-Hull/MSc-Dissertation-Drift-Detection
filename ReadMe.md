# Monitoring Population Drift in Deployed Medical AI

**Author:** Malik Adeel Anjum  
**Project:** MSc AI for Healthcare Dissertation (University of Hull)  
**License:** MIT License

## 📊 Executive Summary
This project investigates **"Silent Failure"** in medical AI models due to demographic shifts (Population Drift). Using the **Pima Indians Diabetes Dataset**, it compares two anomaly detection algorithms: **Isolation Forest** vs. **One-Class SVM (OCSVM)**.

> **[View Project Presentation Slides (PDF)](docs/Drift_Detection_Presentation_Slides.pdf)**

## Key Findings (The "Trade-Off")
The experiments revealed that no single algorithm is safe for all scenarios:

1.  **Gradual Drift (Biological Shift):**
    * **Winner: Isolation Forest**
    * **Result:** Detected drift with **4.40x higher sensitivity** than OCSVM.
    * *Why:* Better at capturing correlations between features (e.g., BMI rising with Glucose).

2.  **Abrupt Drift (Systemic Shock):**
    * **Winner: One-Class SVM**
    * **Result:** Detected shock with **2.92x higher sensitivity** than Isolation Forest.
    * *Why:* Distance-based boundaries are more sensitive to sudden data displacement.

## Repository Structure
* **`data/`**: Processed Pima Indians Diabetes Dataset.
* **`notebooks/`**:
    * `01_Baseline_EDA.ipynb`: Stats & Setup.
    * `02-03`: Gradual Drift Experiments (OCSVM vs IsoForest).
    * `04-05`: Abrupt Drift Experiments (IsoForest vs OCSVM).
* **`docs/`**: Presentation Slides.

## Quick Start
1.  Clone this repo.
2.  Install dependencies: `pip install -r requirements.txt`
3.  Run `01_Baseline_EDA_and_Stats.ipynb` to initialize data.
4.  Run remaining notebooks to reproduce the drift experiments.

---
## 📞 Citation
If you use this methodology, please cite:
> **Anjum, M. A. (2025).** *Monitoring Population Drift in Deployed AI Medical Devices.* MSc Dissertation, University of Hull.
Email : malikanjum.adeel@gmail.com

**Acknowledgements:** Built using Scikit-Learn, SHAP, and NIDDK Data.