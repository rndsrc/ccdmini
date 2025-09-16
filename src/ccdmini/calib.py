import numpy as np

def median_stack(arrays):
    """Median-combine a list of 2D arrays (H, W) to (H, W)."""
    return np.median(np.stack(arrays, axis=0), axis=0)

def make_master_bias(biases):
    """Master bias via median combine."""
    return median_stack(biases)

def make_master_dark(darks):
    """Master dark via median combine (assumes matching exposure)."""
    return median_stack(darks)

def make_master_flat(flats):
    """Master flat via median combine, then normalize to unit median."""
    mf  = median_stack(flats)
    med = float(np.median(mf))
    if med <= 0:
        raise ValueError("Flat median must be positive to normalize.")
    return mf / med


def apply_calibration(raw, mbias, mdark, mflat):
    """Apply CCD calibration: (raw - mbias - mdark) / mflat."""
    denom = np.where(mflat==0, 1.0, mflat)
    return (raw - mbias - mdark) / denom
