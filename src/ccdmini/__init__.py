"""
ccdmini: Minimal CCD calibration primitives for ASTR 501.

This package intentionally stays tiny to keep the focus on
workflow/automation, while still representing real calibration steps.
"""

from .calib import (
    median_stack,
    make_master_bias,
    make_master_dark,
    make_master_flat,
    apply_calibration,
)
