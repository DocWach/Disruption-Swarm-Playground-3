"""Utility functions for data processing."""


def moving_average(values, window=3):
    """Compute a simple moving average."""
    if len(values) < window:
        return values[:]
    result = []
    for i in range(len(values) - window + 1):
        avg = sum(values[i:i + window]) / window
        result.append(round(avg, 2))
    return result


def normalize(values):
    """Min-max normalize a list of values to [0, 1]."""
    lo, hi = min(values), max(values)
    if lo == hi:
        return [0.5] * len(values)
    return [round((v - lo) / (hi - lo), 4) for v in values]


def detect_trend(values, window=5):
    """Detect whether recent values trend up, down, or flat."""
    if len(values) < window:
        return "insufficient data"
    recent = values[-window:]
    diffs = [recent[i+1] - recent[i] for i in range(len(recent) - 1)]
    avg_diff = sum(diffs) / len(diffs)
    if avg_diff > 0.5:
        return "increasing"
    elif avg_diff < -0.5:
        return "decreasing"
    return "stable"
