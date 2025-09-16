import numpy as np

from ccdmini.calib import (
    median_stack,
    make_master_bias,
    make_master_dark,
    make_master_flat,
    apply_calibration,
)

def test_median_stack_is_pixelwise_median():
    a = np.ones((3,3))
    b = np.ones((3,3)) * 3
    out = median_stack([a, b])
    assert np.allclose(out, 2.0) # median of {1,3} is 2 everywhere

def test_master_bias_and_dark_are_medians():
    mb = make_master_bias([np.full((2,2), 100), np.full((2,2), 102)])
    md = make_master_dark([np.full((2,2), 10),  np.full((2,2), 12)])
    assert np.allclose(mb, 101)
    assert np.allclose(md, 11)

def test_master_flat_normalization_to_unit_median():
    mf = make_master_flat([np.full((2,2), 2.0), np.full((2,2), 4.0)])
    assert np.allclose(mf, 1.0)
    assert np.allclose(np.median(mf), 1.0)

def test_apply_calibration_recovers_signal():
    true_signal = np.ones((4,4)) * 1000.0
    mb = np.ones((4,4)) * 100.0
    md = np.ones((4,4)) * 10.0
    mf = np.ones((4,4)) * 1.0

    raw = true_signal + mb + md  # construct a raw that should calibrate back to true_signal

    cal = apply_calibration(raw, mb, md, mf)    
    assert np.allclose(cal, true_signal)
