# Preliminary Analysis of Environmental Sensor Data

## Abstract

This paper presents a preliminary analysis of environmental sensor data collected from a building monitoring system. We examine temperature, pressure, and humidity readings over a single day to identify patterns and anomalies.

## Introduction

Building environment monitoring is critical for occupant comfort and energy efficiency. Modern sensor networks generate large volumes of time-series data that require automated analysis to extract actionable insights.

This study analyzes data from three sensors deployed in a university research building. The sensors measure temperature (Sensor S001), barometric pressure (Sensor S002), and relative humidity (Sensor S003).

## Methodology

Data was collected at hourly intervals from 08:00 to 17:00 on March 1, 2026. Each sensor reported a single scalar value per reading. We compute descriptive statistics and apply outlier detection using a threshold of two standard deviations from the mean.

## Results

Initial analysis reveals a clear diurnal pattern in temperature readings, with values rising through midday and declining in the afternoon. Humidity shows an inverse relationship with temperature, as expected.

The final reading at 17:00 shows anomalous values across all three sensors, suggesting a possible sensor malfunction or environmental event.

## Discussion

The anomalous readings at 17:00 warrant further investigation. Possible explanations include sensor calibration drift, power supply issues, or a genuine environmental event. Cross-referencing with building HVAC logs would help disambiguate these hypotheses.

## Conclusion

This preliminary analysis demonstrates the value of automated anomaly detection in building sensor networks. Future work should incorporate longer time series, additional sensor modalities, and more sophisticated detection algorithms.
