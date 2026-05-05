# Trained Models

This directory contains pre-trained drift detection models.

## Files

### ocsvm_baseline.joblib
- **Algorithm:** One-Class SVM
- **Dataset:** [Training dataset]
- **Created:** [Date]
- **Parameters:** [Your key parameters]

### ocsvm_tuned.joblib
- **Algorithm:** One-Class SVM (Hyperparameter Tuned)
- **Dataset:** [Training dataset]
- **Created:** [Date]
- **Parameters:** [Your key parameters]
- **Performance:** [Your metrics - AUC, etc.]

## Usage

```python
import joblib
model = joblib.load('ocsvm_baseline.joblib')
predictions = model.predict(X_test)
```