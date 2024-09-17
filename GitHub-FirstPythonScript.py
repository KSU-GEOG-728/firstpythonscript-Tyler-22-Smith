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

# Listing Regions Avalible To Choose From
regions_array = arcpy.da.TableToNumPyArray('ks_ecoregions', ['US_L3NAME'])
regions_list = regions_array['US_L3NAME']
print("Select an Ecoregion:")
ecoregion = input(regions_list) #when running type in terminal after list[]

# Concatenation of selected ecoregion from input() function
input_selection = "US_L3NAME = " + "'" + ecoregion +  "'"
selected_ecoregion = arcpy.SelectLayerByAttribute_management('ks_ecoregions', 'NEW_SELECTION', input_selection)

# Buffering Selected Ecoregion by 10 Km
buffer_ecoregion = arcpy.analysis.Buffer(selected_ecoregion, 'ecoregion_buffered', '10 Kilometers')

# Clipping Rivers Within the Buffered Ecoregion
clipped_rivers = arcpy.analysis.Clip('ks_major_rivers', buffer_ecoregion, 'clipped_rivers')

# Extracting Answer
river_array = arcpy.da.TableToNumPyArray(clipped_rivers, ["Shape_Length"])
answer = str(round(river_array["Shape_Length"].sum(), ndigits = 0))

# Print Statements for terminal
print(" ")
print(" ")
print("....Selecting Ecoregion")
print(" ")
print(" ")
print("........Buffering Selection")
print(" ")
print(" ")
print("............Clipping Rivers")
print(" ")
print(" ")
print("########################################################")
print(" ")
print("Total Length of Rivers in the {0} = {1} ft".format(ecoregion, answer))
print(" ")
print("########################################################")

# Final Output when using "Flint Hills": 
# Total Length of Rivers in the Flint Hills = 812213.0 ft