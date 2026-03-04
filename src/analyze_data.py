"""Sensor data analysis script — contains a deliberate bug for practice."""

import csv
import statistics


def load_data(filepath):
    """Load sensor readings from CSV."""
    readings = []
    with open(filepath, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            readings.append({
                "timestamp": row["timestamp"],
                "sensor_id": row["sensor_id"],
                "value": float(row["value"]),
                "unit": row["unit"],
            })
    return readings


def filter_by_sensor(readings, sensor_id):
    """Return readings for a specific sensor."""
    return [r for r in readings if r["sensor_id"] == sensor_id]


def compute_statistics(readings):
    """Compute basic statistics for a list of readings.

    BUG: There is an off-by-one error in the outlier detection.
    """
    values = [r["value"] for r in readings]
    mean = statistics.mean(values)
    stdev = statistics.stdev(values)

    # Outlier detection — readings beyond 2 standard deviations
    # BUG: should be >= not > for the absolute value check,
    # and the threshold comparison is inverted
    outliers = [v for v in values if abs(v - mean) < 2 * stdev]

    return {
        "count": len(values),
        "mean": round(mean, 2),
        "stdev": round(stdev, 2),
        "min": min(values),
        "max": max(values),
        "outliers": outliers,
    }


def main():
    readings = load_data("data/sensor_readings.csv")
    print(f"Loaded {len(readings)} readings")

    for sid in ["S001", "S002", "S003"]:
        subset = filter_by_sensor(readings, sid)
        stats = compute_statistics(subset)
        print(f"\nSensor {sid}:")
        print(f"  Count: {stats['count']}")
        print(f"  Mean:  {stats['mean']} ± {stats['stdev']}")
        print(f"  Range: [{stats['min']}, {stats['max']}]")
        print(f"  Outliers: {len(stats['outliers'])}")


if __name__ == "__main__":
    main()
