# 🌾 Agriculture Visualizer in QGIS

This is a QGIS Python script that calculates NDVI from satellite imagery (Sentinel or Landsat) and visualizes **agricultural or vegetated areas** only.

## Features

- Visualize agricultural land using NDVI.
- Works with any multispectral image (e.g., Sentinel-2, Landsat).
- Lightweight and beginner-friendly.

## Requirements

- QGIS (3.x recommended)
- Satellite images (e.g., Sentinel-2 Band 4 and Band 8)

## How to Use

1. Open QGIS.
2. Open Python Console (Plugins → Python Console).
3. Paste the code from `visualize_agriculture.py`.
4. Edit paths to your Red and NIR bands.
5. Run and visualize the result!

## NDVI Formula

\[
NDVI = \frac{(NIR - RED)}{(NIR + RED)}
\]

## Sample Output

High NDVI = Green fields  
Low NDVI = Bare soil or buildings

## License

MIT License
