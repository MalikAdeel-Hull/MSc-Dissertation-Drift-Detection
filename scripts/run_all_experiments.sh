#!/bin/bash
set -e

echo "Running all drift detection experiments..."

cd notebooks

echo "1. Running baseline EDA..."
jupyter nbconvert --to notebook --execute 01_Baseline_EDA_and_Stats.ipynb

echo "2. Running Gradual Drift OCSVM experiment..."
jupyter nbconvert --to notebook --execute 02_Gradual_Drift_Experiment_OCSVM.ipynb

echo "3. Running Gradual Drift IsoForest experiment..."
jupyter nbconvert --to notebook --execute 03_Gradual_Drift_Experiment_IsoForest.ipynb

echo "4. Running Abrupt Drift IsoForest experiment..."
jupyter nbconvert --to notebook --execute 04_Abrupt_Drift_Experiment_IsoForest.ipynb

echo "5. Running Abrupt Drift OCSVM experiment..."
jupyter nbconvert --to notebook --execute 05_Abrupt_Drift_Experiment_OCSVM.ipynb

echo "✅ All experiments completed!"