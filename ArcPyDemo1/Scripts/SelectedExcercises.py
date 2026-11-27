# Name: Select_Example2.py
# Description: Select roads of Class 4 from major roads tin the gnatcatcher habitat study area
   
# Import system modules
import arcpy
   
# Set workspace
arcpy.env.workspace = "V:/ArcPyDemo1/Data/SanDiego"
   
# Set local variables
in_features = "majorrds.shp"
out_feature_class = "V:/ArcPyDemo1/Scratch/majorrdsClass4.shp"
where_clause = '"CLASS" = \'4\''
   
# Execute Select
arcpy.Select_analysis(in_features, out_feature_class, where_clause)

# Buffer the results
buffRoads = "V:/ArcPyDemo1/Scratch/BufferedRoads.shp"
buffDist = "500 meters"
arcpy.Buffer_analysis(out_feature_class, buffRoads, buffDist, "", "", "ALL")

#%% ArcPy Functions
# Use Exists function to return a boolean if V:\ArcPyDemo1/data/SanDiego/climate.shp exists
arcpy.Exists("V:/ArcPyDemo1/Data/SanDiego/climate.shp")

# Use ListFields function to generate a list of all the fields in the same filepath above, saving the output variable as "myFields"
myFields = arcpy.ListFields("V:/ArcPyDemo1/Data/SanDiego/climate.shp")
type(myFields)
len(myFields)
myField = myFields[0]
type(myField)

# Generate a list of just String type fields in filepath dataset
 stringFields = arcpy.ListFields('V:/ArcPyDemo1/Data/SanDiego/climate.shp','','String')
  # or
  stringFields = arcpy.ListFields(
      dataset = 'V:/ArcPyDemo1/Data/SanDiego/climate.shp',
      field_type = 'String'
  )

#%% ArcPy Classes
# 1. Create an ArcPy point object:
myPoint = arcpy.Point()

# 2. Assign values to the X, Y and ID properties of the point object:
myPoint.X = 6266956
myPoint.Y = 1876781
myPoint.ID = 1

# 3. Extract the first polygon from the San_Diego study_quads.shp feature class:
myPoly = arcpy.SearchCursor('V:/ArcPyDemo1/Data/SanDiego/study_quads.shp').next().Shape

# Use the Point’s within method to see whether our point is within the polygon.
print (myPoint.within(myPoly))

# List some properties (Area? How many points?) of the myPoly polygon object:
print("Area: {0}".format(myPoly.area))
print("Points: {0}".format(myPoly.pointCount))

#%% Using ArcPy environment settings in Python
# Import ArcPy and set the current workspace to “V:\ArcPyDemo1\data\SanDiego”
import arcpy
arcpy.env.workspace = "V:/ArcPyDemo1/Data/SanDiego"

# Set the outputCoordinateSystem value to force our processes to create output in a specific coordinate system:
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984")

# Another environment setting allows us to overwrite the output, if it exists:
arcpy.env.overwriteOutput = True

# Now, let’s re-run the remaining code we did in Exercise 1b…
     # Set local variables
in_features = "majorrds.shp"
out_feature_class = "majorrdsClass4.shp"
where_clause = '"CLASS" = \'4\''
     # Execute Select
arcpy.Select_analysis(in_features, out_feature_class, where_clause)
