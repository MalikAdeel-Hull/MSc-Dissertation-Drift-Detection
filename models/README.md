# Models Directory

## Overview

This directory is for storing trained drift detection models generated during experiment execution.

## Generated Models

Models are **automatically created during notebook execution** and are not included in the repository (excluded via `.gitignore`).

### Model Files Generated

During the drift detection experiments, the following models are trained and saved:

- **One-Class SVM (OCSVM) Models**
  - Trained on Pima dataset baseline
  - Trained on FHGD dataset baseline
  - Parameters: `kernel='rbf'`, `nu=0.05`

- **Isolation Forest Models**
  - Trained on Pima dataset baseline
  - Trained on FHGD dataset baseline
  - Parameters: `n_estimators=100`, `contamination=0.05`

## Reproducibility

To regenerate all models, run the experiment scripts:

```bash
# Run all experiments (generates models)
bash scripts/run_all_experiments.sh

# Or run dataset-specific experiments
bash scripts/run_pima_experiments.sh    # Pima models only
bash scripts/run_fhgd_experiments.sh    # FHGD models only
```

Each notebook automatically trains and evaluates models on its respective dataset.

## Model Persistence

Models are trained fresh in each notebook run. If you wish to save trained models:

```python
import joblib

# Save a model
joblib.dump(model, 'models/model_name.joblib')

# Load a model
model = joblib.load('models/model_name.joblib')
```

Note: Saved models (`.joblib` files) are gitignored to keep repository size small.