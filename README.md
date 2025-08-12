# OpenStreetMap Extraction and RoadRunner Workflow
This repository provides a step-by-step guide to extract OpenStreetMap (OSM) data for a specific area, process it with RoadRunner, and verify the map output.

##Steps to Extract and Process OpenStreetMap Data

### 1- Extract OpenStreetMap Data:

Visit BBBike Extracts.
Use the Add points to polygon option to define a custom polygon for your area of interest. This helps reduce the number of nodes, lowering complexity and resource usage during processing.
Select the output format: OSM XML 7z (xz).
Follow the interface steps to finalize your selection and extract the data. The OSM extract will be sent to your email.

### 2-Import in RoadRunner:
Import the downloaded OpenStreetMap file into RoadRunner.
Build the mesh from the imported data.
Review and resolve any errors found in the mesh. It is recommended to delete problematic roads or junctions and rebuild them from scratch to avoid persistent errors.

### 3-Export OpenDrive Map:
When exporting, make sure to enable the "Elevate by layers" option to ensure proper elevation layering in the output.

### 4-Verify Your Map:
To validate your map, select a random point (with coordinates x, y, z) on a road.
Use the offset values from the exported OpenDRIVE (XODR) file along with the Python script provided in this repository to convert (x, y, z) coordinates to latitude and longitude.
Cross-check the corresponding location dimensions with Google Maps for confirmation.

