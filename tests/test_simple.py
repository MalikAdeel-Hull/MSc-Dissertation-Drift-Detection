#!/usr/bin/env python
"""Simple diagnostic test for drift detection modules"""

import sys
from pathlib import Path

# Add src to path - go up one level from tests/
src_path = Path(__file__).parent.parent / 'src'
sys.path.insert(0, str(src_path))

print("Python path: " + str(sys.path[0]))
print("Current dir: " + str(Path.cwd()))

# Test imports
try:
    from drift_detection import load_raw_data, PIMA_COLS_WITH_MISSING
    print("[OK] Imports successful")
except Exception as e:
    print("[FAIL] Import failed: " + str(e))
    sys.exit(1)

# Test data loading
try:
    df = load_raw_data('data/processed/pima_step1_clean.csv')
    print("[OK] Data loaded: " + str(df.shape))
except Exception as e:
    print("[FAIL] Load failed: " + str(e))
    sys.exit(1)

# Test missingness flags
try:
    from drift_detection import create_missingness_flags
    df = create_missingness_flags(df, PIMA_COLS_WITH_MISSING)
    print("[OK] Missingness flags created: " + str(df.shape))
except Exception as e:
    print("[FAIL] Flags failed: " + str(e))
    sys.exit(1)

# Test split
try:
    from drift_detection import temporal_train_test_split
    features = [col for col in df.columns if col != 'Outcome']
    X_base, X_test, y_base, y_test, split = temporal_train_test_split(
        df, features, target_col='Outcome', test_fraction=0.30
    )
    print("[OK] Split successful: base=" + str(X_base.shape) + ", test=" + str(X_test.shape))
except Exception as e:
    print("[FAIL] Split failed: " + str(e))
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Test preprocessing
try:
    from drift_detection import PreprocessingPipeline, identify_feature_types
    continuous_cols, indicator_cols = identify_feature_types(X_base)
    pipeline = PreprocessingPipeline()
    X_base_prep = pipeline.fit_transform(X_base, continuous_cols, indicator_cols)
    X_test_prep = pipeline.transform(X_test)
    print("[OK] Preprocessing successful: base=" + str(X_base_prep.shape) + ", test=" + str(X_test_prep.shape))
except Exception as e:
    print("[FAIL] Preprocessing failed: " + str(e))
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Test OCSVM
try:
    from drift_detection import fit_ocsvm, get_outlier_rate
    ocsvm = fit_ocsvm(X_base_prep, gamma=0.1)
    baseline_rate = get_outlier_rate(ocsvm, X_base_prep)
    print("[OK] OCSVM trained: baseline_rate=" + str(round(baseline_rate, 4)))
except Exception as e:
    print("[FAIL] OCSVM failed: " + str(e))
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Test gradual drift
try:
    from drift_detection import simulate_gradual_drift
    X_drifted = simulate_gradual_drift(X_test, 'Glucose', drift_percentage=0.40)
    print("[OK] Gradual drift successful: " + str(X_drifted.shape))
except Exception as e:
    print("[FAIL] Gradual drift failed: " + str(e))
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Test abrupt drift
try:
    from drift_detection import apply_minmax_drift

    # Compute baseline stats
    X_clean = X_base.dropna()
    X_base_stats = {
        'Glucose': {
            'f_min': X_clean['Glucose'].min(),
            'f_range': X_clean['Glucose'].max() - X_clean['Glucose'].min()
        }
    }

    X_drifted_abrupt = apply_minmax_drift(
        X_test,
        X_base_stats,
        features=['Glucose'],
        shift_f=0.4,
        range_f=1.5,
        verbose=False
    )
    print("[OK] Abrupt drift successful: " + str(X_drifted_abrupt.shape))
except Exception as e:
    print("[FAIL] Abrupt drift failed: " + str(e))
    import traceback
    traceback.print_exc()
    sys.exit(1)

print("\n" + "="*70)
print("ALL DIAGNOSTICS PASSED")
print("="*70)
