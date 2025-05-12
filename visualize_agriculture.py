# visualize_agriculture.py

from qgis.core import QgsRasterLayer, QgsRasterCalculatorEntry, QgsRasterCalculator
from qgis.utils import iface
import os

def calculate_ndvi(nir_path, red_path, output_path):
    # Load the NIR and Red bands
    nir = QgsRasterLayer(nir_path, "NIR")
    red = QgsRasterLayer(red_path, "Red")

    if not nir.isValid() or not red.isValid():
        print("Invalid raster layers.")
        return

    # Define raster calculator entries
    entries = []

    nir_entry = QgsRasterCalculatorEntry()
    nir_entry.ref = 'nir@1'
    nir_entry.raster = nir
    nir_entry.bandNumber = 1
    entries.append(nir_entry)

    red_entry = QgsRasterCalculatorEntry()
    red_entry.ref = 'red@1'
    red_entry.raster = red
    red_entry.bandNumber = 1
    entries.append(red_entry)

    # NDVI formula: (NIR - Red) / (NIR + Red)
    expression = '(nir@1 - red@1) / (nir@1 + red@1)'

    calculator = QgsRasterCalculator(
        expression,
        output_path,
        'GTiff',
        nir.extent(),
        nir.width(),
        nir.height(),
        entries
    )

    result = calculator.processCalculation()

    if result == 0:
        iface.addRasterLayer(output_path, "NDVI")
        print("NDVI calculated and added to map.")
    else:
        print("NDVI calculation failed.")

# Example usage
# Provide full paths to your Red and NIR band files (e.g., Sentinel Band 4 and Band 8)
nir_band_path = "/path/to/NIR.tif"
red_band_path = "/path/to/RED.tif"
output_ndvi_path = "/path/to/output_ndvi.tif"

calculate_ndvi(nir_band_path, red_band_path, output_ndvi_path)
