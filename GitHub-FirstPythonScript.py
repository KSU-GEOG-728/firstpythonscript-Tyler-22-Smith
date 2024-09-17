#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: GitHub-FirstPythonScript.py
    Author: Tyler Smith
    Description:  ARC GIS tool to calculate stream area in a selected eco region
    Date created: 09/12/2024
    Python Version: 3.9.16
"""

# Import arcpy module and allow overwrites
import arcpy
arcpy.env.overwriteOutput = True

# Set current workspace
#arcpy.env.workspace = "c:/Users/Tyler Smith/Documents/GitHub/firstpythonscript-Tyler-22-Smith/GitHub-FirstPythonScript.gdb"
arcpy.env.workspace = "c:/Users/Tyler Smith/Documents/GitHub/firstpythonscript-Tyler-22-Smith/ExerciseData.gdb"

# Geoprocessing

# Selecting Appropriate Ecoregion
select_ecoregion = arcpy.SelectLayerByAttribute_management('ks_ecoregions', 'NEW_SELECTION', "US_L3NAME = 'Flint Hills'")

# Buffering Selected Ecoregion by 10 Km
buffer_ecoregion = arcpy.analysis.Buffer(select_ecoregion, 'ecoregion_buffered', '10 Kilometers')

# Clipping Rivers Within the Buffered Ecoregion
clipped_rivers = arcpy.analysis.Clip('ks_major_rivers', buffer_ecoregion, 'clipped_rivers')
   
# Selecting the "Shape_Length" Field Within the clipped_rivers Feature Class and Summing Their Lengths
total_river_length = 0
with arcpy.da.SearchCursor('clipped_rivers', "Shape_Length") as cursor:
    for row in cursor:
        total_river_length = total_river_length + row[0]


# Printing Final Answer
print("Total Length of Rivers in Selected Ecoregion {0}".format(round(total_river_length, 0)))