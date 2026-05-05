# Data Drift Detection in Healthcare: MSc Dissertation

<!-- Badges -->
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## 📋 Overview

This repository contains the code, data, and analysis for an MSc dissertation on **detecting and analyzing data drift in healthcare datasets**. The project explores two complementary approaches to drift detection:

- **One-Class SVM (OCSVM)** - A density-based anomaly detection method
- **Isolation Forest (IsoForest)** - An ensemble-based outlier detection method

The dissertation evaluates these methods on both **gradual drift** and **abrupt drift** scenarios using two datasets: the Pima Indian Diabetes dataset and the Framingham Heart Study Heart Diseases (FGHD) dataset.

## 🔑 Key Research Findings: The "Detection Trade-off"
The study reveals that no single algorithm is universally superior. A strategic choice is required based on the expected drift:

| Drift Archetype | Sensitivity Winner | Key Result |
| :--- | :--- | :--- |
| **Gradual (Multi-factor)** | **Isolation Forest** | **4.40x** higher sensitivity than OCSVM |
| **Abrupt (Systemic Shock)** | **One-Class SVM** | **2.92x** higher reactivity than IF |
## 📁 Project Structure

```
.
├── README.md                          # This file
├── LICENSE                            # MIT License
├── CITATION.cff                       # Citation metadata
├── requirements.txt                   # Python dependencies
├── setup.py                           # Package setup
│
├── data/
│   ├── raw/                          # Original datasets (do not modify)
│   │   ├── diabetes.csv              # Pima Indian Diabetes dataset
│   │   └── README.md
│   ├── processed/                    # Cleaned and processed data
│   │   ├── pima_step1_clean.csv
│   │   ├── pima_step2_imputed.csv
│   │   ├── fhgd_step1_clean.csv
│   │   └── fhgd_step2_imputed.csv
│   └── .gitkeep
│
├── notebooks/                        # Jupyter notebooks (execution order)
│   ├── 01_Baseline_EDA_and_Stats.ipynb
│   ├── 02_Gradual_Drift_Experiment_OCSVM.ipynb
│   ├── 03_Gradual_Drift_Experiment_IsoForest.ipynb
│   ├── 04_Abrupt_Drift_Experiment_IsoForest.ipynb
│   ├── 05_Abrupt_Drift_Experiment_OCSVM.ipynb
│   ├── archive/                     # Earlier iterations (reference only)
│   │   ├── FGHD_eda.ipynb
│   │   ├── FGHD_IF_Gradual.ipynb
│   │   └── ...
│   └── reports/                     # Generated reports from notebooks
│       └── drafts/
│
├── src/                             # Python package code
│   ├── __init__.py
│   ├── drift_detection/
│   │   ├── __init__.py
│   │   ├── ocsvm.py                # OCSVM implementation
│   │   ├── isoforest.py            # Isolation Forest implementation
│   │   └── utils.py                # Utility functions
│   ├── data/
│   │   ├── __init__.py
│   │   ├── loaders.py              # Data loading functions
│   │   └── preprocessors.py        # Data preprocessing pipeline
│   └── evaluation/
│       ├── __init__.py
│       └── metrics.py              # Evaluation metrics
│
├── models/                          # Trained models
│   ├── ocsvm_baseline.joblib
│   ├── ocsvm_tuned.joblib
│   └── README.md
│
├── docs/
│   ├── manuscripts/                # Dissertation manuscripts
│   │   ├── Population_Drift_Manuscript_FINAL.docx
│   │   └── ...
│   └── Drift_Detection_Presentation_Slides.pdf
│
├── scripts/                         # Utility scripts
│   ├── setup_environment.sh         # Environment setup
│   └── run_all_experiments.sh       # Run all experiments
│
└── .gitignore                       # Git ignore rules
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip or conda

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/MalikAdeel-Hull/MSc-Dissertation-Drift-Detection.git
cd MSc-Dissertation-Drift-Detection
```

2. **Create and activate a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Install the package (optional, for development):**
```bash
pip install -e .
```

### Running the Experiments

**To reproduce all results:**
```bash
bash scripts/run_all_experiments.sh
```

**To run notebooks individually:**
Follow the numbered order:
```bash
jupyter notebook notebooks/01_Baseline_EDA_and_Stats.ipynb
jupyter notebook notebooks/02_Gradual_Drift_Experiment_OCSVM.ipynb
jupyter notebook notebooks/03_Gradual_Drift_Experiment_IsoForest.ipynb
# ... and so on
```

## 📊 Datasets

### Pima Indian Diabetes Dataset
- **Source:** UCI Machine Learning Repository
- **Size:** X samples, Y features
- **Target:** Diabetes diagnosis (binary classification)
- **Preprocessing:** Handles missing values, feature scaling applied

### Framingham Heart Study Heart Diseases (FGHD)
- **Source:** [Source URL]
- **Size:** X samples, Y features
- **Target:** Heart disease prediction
- **Preprocessing:** [Describe preprocessing steps]

See `data/raw/README.md` for detailed dataset information.

## 🔬 Methodology

### Approach 1: One-Class SVM (OCSVM)
- Learns a boundary around normal data
- Detects points outside this boundary as drift
- Parameters: [mention key hyperparameters]

### Approach 2: Isolation Forest (IsoForest)
- Isolates anomalies using random trees
- More computationally efficient than OCSVM
- Parameters: [mention key hyperparameters]

### Evaluation Metrics
- Drift detection rate (sensitivity)
- False positive rate (specificity)
- Area under ROC curve (AUC)
- [Other metrics you used]

## 📈 Results

### Summary of Key Findings
| Metric | OCSVM | IsoForest |
|--------|-------|-----------|
| AUC (Gradual Drift) | X | Y |
| AUC (Abrupt Drift) | X | Y |
| Runtime (sec) | X | Y |

For detailed results, see the generated reports in `notebooks/reports/` or the dissertation manuscript in `docs/manuscripts/`.

## 📖 Documentation

- **Full Dissertation:** See `docs/manuscripts/Population_Drift_Manuscript_FINAL.docx`
- **Presentation Slides:** See `docs/Drift_Detection_Presentation_Slides.pdf`
- **Detailed Analysis:** Check individual notebooks with results and visualizations

## 🛠️ Development

### Adding New Features
1. Create a branch: `git checkout -b feature/your-feature`
2. Make changes and commit: `git commit -am 'Add your feature'`
3. Push to branch: `git push origin feature/your-feature`
4. Submit a pull request

See `CONTRIBUTING.md` for guidelines.

### Code Quality
This project uses:
- **Black** for code formatting
- **Pylint** for linting
- **Pytest** for testing (when applicable)

## 📝 Citation

If you use this code in your research, please cite it as:

```bibtex
@misc{Adeel2026,
  author = {Adeel, Malik},
  title = {Data Drift Detection in Healthcare: An MSc Dissertation},
  year = {2026},
  howpublished = {\url{https://github.com/MalikAdeel-Hull/MSc-Dissertation-Drift-Detection}},
  note = {MSc Dissertation, University of Hull}
}
```

Or use the CITATION.cff file for automated citation generation.

## 📄 License

This project is licensed under the MIT License - see the `LICENSE` file for details.

## ✍️ Author

**Malik Adeel**
- Email: malikanjum.adeel@gmail.com
- University: University of Hull

## 🙏 Acknowledgments

- Supervisors and advisors
- Dataset sources
- Open-source libraries used (scikit-learn, pandas, matplotlib, etc.)

## 🔗 Resources

- [Scikit-learn Documentation](https://scikit-learn.org/)
- [Pandas Documentation](https://pandas.pydata.org/)
- [Jupyter Notebooks Guide](https://jupyter.org/)

## 🐛 Issues & Questions

Please file issues for bugs or feature requests on the [GitHub Issues page](https://github.com/MalikAdeel-Hull/MSc-Dissertation-Drift-Detection/issues).

For questions about the research, please contact the author directly.

---

**Last Updated:** May 2026  
**Status:** Completed (MSc Dissertation)
