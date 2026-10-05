"""Keep the Gradient - Hard-Margin SVM (Episode 3) (specified, not yet implemented)

Solve min 1/2||w||^2 s.t. y_i (w^T x_i + w_0) >= 1 (e.g. through its dual QP) and return w, w_0 and the multipliers mu_i; support vectors are the points with mu_i > 0. Needed by the SVM scenes of Episode 3.
"""
from __future__ import annotations


def hard_margin_svm(X, y, *args, **kwargs):
    """See the module docstring for the specification."""
    raise NotImplementedError("hard_margin_svm: see gradkit/algorithms/svm.py for the specification")
