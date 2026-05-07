# Test Suite

Test files for the drift detection framework.

## Test Files

### `test_abrupt_drift.py` (PRIMARY)
Comprehensive test suite for abrupt drift functionality.

**Tests**:
1. Single feature abrupt drift (OCSVM)
2. Multivariate abrupt drift (Isolation Forest)
3. NaN value preservation
4. Clinical range clipping
5. Gradual vs Abrupt drift comparison

**Status**: ✓ All 5 tests passing
**Runtime**: ~2-3 minutes
**Coverage**: apply_minmax_drift(), get_outlier_rate(), calculate_detection_ratio()

**Run**:
```bash
python -m pytest tests/test_abrupt_drift.py -v
```

### `test_modules.py`
General module import and functionality tests.

**Tests**:
- Module imports
- Function signatures
- Basic data loading

**Run**:
```bash
python -m pytest tests/test_modules.py -v
```

### `test_simple.py`
Diagnostic test for all major components.

**Tests**:
- Data loading
- Missingness flags
- Temporal split
- Preprocessing
- OCSVM training
- Gradual drift
- Abrupt drift

**Status**: ✓ All tests passing
**Runtime**: ~30 seconds

**Run**:
```bash
python test_simple.py
```

## Running All Tests

### Using pytest (recommended)
```bash
pytest tests/ -v
```

### Using individual scripts
```bash
python tests/test_abrupt_drift.py
python test_simple.py
```

## Test Results

### Latest Results (May 7, 2026)

```
test_abrupt_drift.py:
✓ TEST 1: Abrupt Drift - Single Feature        PASSED
✓ TEST 2: Abrupt Drift - Multivariate          PASSED
✓ TEST 3: NaN Preservation                     PASSED
✓ TEST 4: Clinical Range Clipping              PASSED
✓ TEST 5: Gradual vs Abrupt Comparison         PASSED

OVERALL: 5/5 TESTS PASSED ✓
```

## Performance Metrics

### Detection Ratios Achieved

**Single Feature (Glucose)**:
- OCSVM: **3.00x** ⭐ (Strong signal)
- Isolation Forest: **1.29x** (Moderate)

**Multivariate (4 features)**:
- OCSVM: **3.00x** ⭐ (Strong)
- Isolation Forest: **4.22x** ⭐⭐ (Very strong)

## Test Data

Tests use the Pima Indians Diabetes dataset:
- **Location**: `data/processed/pima_step1_clean.csv`
- **Samples**: 768
- **Features**: 8
- **Train/Test**: 70/30 split

## Adding New Tests

1. Create a new file: `test_*.py`
2. Use pytest conventions
3. Import from `drift_detection` package:

```python
from drift_detection import (
    load_raw_data,
    create_missingness_flags,
    fit_ocsvm,
    # ... etc
)

def test_your_feature():
    """Test description"""
    # Test code here
    assert result == expected
```

4. Run: `pytest tests/test_*.py -v`

## Troubleshooting

**Import errors?**
- Ensure `conftest.py` is in `tests/` directory
- Check that `src/drift_detection/` exists
- Run from repo root: `cd /path/to/MSc-Dissertation-Drift-Detection`

**Module not found?**
```bash
pip install -e .
# or
pip install scikit-learn pandas numpy scipy
```

**Tests hanging?**
- OCSVM can be slow on first run
- Increase timeout if needed
- Check system RAM

---

For more details, see:
- `REPOSITORY_AUDIT.md` - Complete audit report
- `IMPLEMENTATION_STATUS.md` - Implementation details
- `src/drift_detection/MODULE_USAGE.md` - API documentation
