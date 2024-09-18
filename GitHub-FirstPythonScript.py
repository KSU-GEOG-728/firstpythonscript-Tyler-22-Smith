#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: GitHub-FirstPythonScript.py
    Author: Tyler Smith
    Description:  ARC GIS tool to calculate stream area in a selected eco region
    Date created: 09/12/2024
    Python Version: 3.11.8
"""

# Import arcpy module and allow overwrites
import arcpy
arcpy.env.overwriteOutput = True

# Set current workspace (file path to geo database in local repo)
arcpy.env.workspace = "c:/Users/Tyler Smith/Documents/GitHub/firstpythonscript-Tyler-22-Smith/ExerciseData.gdb"

# Geoprocessing

# Concatenation of selected ecoregion from input() function
selected_ecoregion = arcpy.SelectLayerByAttribute_management('ks_ecoregions', 'NEW_SELECTION', "US_L3NAME = 'Flint Hills'")

# Buffering Selected Ecoregion by 10 Km
arcpy.analysis.Buffer(selected_ecoregion, 'ecoregion_buffered', '10 Kilometers')

# Clipping Rivers Within the Buffered Ecoregion
arcpy.analysis.Clip('ks_major_rivers', 'ecoregion_buffered', 'clipped_rivers')

# Compute stream length in miles and sum new length in output table
arcpy.AddGeometryAttributes_management("clipped_rivers", "LENGTH", "MILES_US")
arcpy.Statistics_analysis("clipped_rivers", "outStats", [["LENGTH", "SUM"]])
