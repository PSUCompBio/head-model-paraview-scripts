# trace generated using paraview version 5.8.1-RC1
#
# To ensure correct image size when batch processing, please search
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
import os.path
import glob

folder_id = 1595511788889
save_images = 1

read_path_brain = 'C:\\Users\\rhk12\\Downloads\\%s (1)\\' % folder_id
read_ply = 'C:\\Users\\rhk12\\Downloads\\%s\\avatars\\*\\face\\model.ply' % folder_id
for item in glob.glob(read_ply):
    read_ply_path = item


brainfile = '%s_brain_rotated.vtk' % folder_id
fiberfile = '%s_fiber_rotated.vtk' % folder_id

brainfile_path = read_path_brain + brainfile
fiberfile_path = read_path_brain + fiberfile

print (read_path_brain)
print (read_ply_path)
print (brainfile)
print (fiberfile)
print (brainfile_path)
print (fiberfile_path)


#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'Legacy VTK Reader'
#a1595505301165_brain_rotatedvtk = LegacyVTKReader(FileNames=['C:\\Users\\rhk12\\Downloads\\1595505301165 (1)\\1595505301165_brain_rotated.vtk'])
a1595505301165_brain_rotatedvtk = LegacyVTKReader(FileNames=[brainfile_path])

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1435, 767]

# get layout
layout1 = GetLayout()

# show data in view
a1595505301165_brain_rotatedvtkDisplay = Show(a1595505301165_brain_rotatedvtk, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
a1595505301165_brain_rotatedvtkDisplay.Representation = 'Surface'
a1595505301165_brain_rotatedvtkDisplay.ColorArrayName = [None, '']
a1595505301165_brain_rotatedvtkDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
a1595505301165_brain_rotatedvtkDisplay.SelectOrientationVectors = 'None'
a1595505301165_brain_rotatedvtkDisplay.ScaleFactor = 0.015763229876756667
a1595505301165_brain_rotatedvtkDisplay.SelectScaleArray = 'None'
a1595505301165_brain_rotatedvtkDisplay.GlyphType = 'Arrow'
a1595505301165_brain_rotatedvtkDisplay.GlyphTableIndexArray = 'None'
a1595505301165_brain_rotatedvtkDisplay.GaussianRadius = 0.0007881614938378334
a1595505301165_brain_rotatedvtkDisplay.SetScaleArray = [None, '']
a1595505301165_brain_rotatedvtkDisplay.ScaleTransferFunction = 'PiecewiseFunction'
a1595505301165_brain_rotatedvtkDisplay.OpacityArray = [None, '']
a1595505301165_brain_rotatedvtkDisplay.OpacityTransferFunction = 'PiecewiseFunction'
a1595505301165_brain_rotatedvtkDisplay.DataAxesGrid = 'GridAxesRepresentation'
a1595505301165_brain_rotatedvtkDisplay.PolarAxes = 'PolarAxesRepresentation'
a1595505301165_brain_rotatedvtkDisplay.ScalarOpacityUnitDistance = 0.009708305760487314

# reset view to fit data
renderView1.ResetCamera()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Legacy VTK Reader'
a1595505301165_fiber_rotatedvtk = LegacyVTKReader(FileNames=[fiberfile_path])

# show data in view
a1595505301165_fiber_rotatedvtkDisplay = Show(a1595505301165_fiber_rotatedvtk, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
a1595505301165_fiber_rotatedvtkDisplay.Representation = 'Surface'
a1595505301165_fiber_rotatedvtkDisplay.ColorArrayName = [None, '']
a1595505301165_fiber_rotatedvtkDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
a1595505301165_fiber_rotatedvtkDisplay.SelectOrientationVectors = 'None'
a1595505301165_fiber_rotatedvtkDisplay.ScaleFactor = 0.014230580255389215
a1595505301165_fiber_rotatedvtkDisplay.SelectScaleArray = 'None'
a1595505301165_fiber_rotatedvtkDisplay.GlyphType = 'Arrow'
a1595505301165_fiber_rotatedvtkDisplay.GlyphTableIndexArray = 'None'
a1595505301165_fiber_rotatedvtkDisplay.GaussianRadius = 0.0007115290127694606
a1595505301165_fiber_rotatedvtkDisplay.SetScaleArray = [None, '']
a1595505301165_fiber_rotatedvtkDisplay.ScaleTransferFunction = 'PiecewiseFunction'
a1595505301165_fiber_rotatedvtkDisplay.OpacityArray = [None, '']
a1595505301165_fiber_rotatedvtkDisplay.OpacityTransferFunction = 'PiecewiseFunction'
a1595505301165_fiber_rotatedvtkDisplay.DataAxesGrid = 'GridAxesRepresentation'
a1595505301165_fiber_rotatedvtkDisplay.PolarAxes = 'PolarAxesRepresentation'
a1595505301165_fiber_rotatedvtkDisplay.ScalarOpacityUnitDistance = 0.004379420226767524

# update the view to ensure updated data information
renderView1.Update()

# create a new 'PLY Reader'
modelply = PLYReader(FileNames=[read_ply_path])
#modelply = PLYReader(FileNames=[read_ply])



# show data in view
modelplyDisplay = Show(modelply, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
modelplyDisplay.Representation = 'Surface'
modelplyDisplay.ColorArrayName = [None, '']
modelplyDisplay.OSPRayScaleArray = 'TCoords'
modelplyDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
modelplyDisplay.SelectOrientationVectors = 'None'
modelplyDisplay.ScaleFactor = 0.02359660714864731
modelplyDisplay.SelectScaleArray = 'None'
modelplyDisplay.GlyphType = 'Arrow'
modelplyDisplay.GlyphTableIndexArray = 'None'
modelplyDisplay.GaussianRadius = 0.0011798303574323654
modelplyDisplay.SetScaleArray = ['POINTS', 'TCoords']
modelplyDisplay.ScaleTransferFunction = 'PiecewiseFunction'
modelplyDisplay.OpacityArray = ['POINTS', 'TCoords']
modelplyDisplay.OpacityTransferFunction = 'PiecewiseFunction'
modelplyDisplay.DataAxesGrid = 'GridAxesRepresentation'
modelplyDisplay.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
modelplyDisplay.ScaleTransferFunction.Points = [0.011202685534954071, 0.0, 0.5, 0.0, 0.5774843692779541, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
modelplyDisplay.OpacityTransferFunction.Points = [0.011202685534954071, 0.0, 0.5, 0.0, 0.5774843692779541, 1.0, 0.5, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# change solid color
modelplyDisplay.AmbientColor = [0.8666666666666667, 0.7529411764705882, 0.5490196078431373]
modelplyDisplay.DiffuseColor = [0.8666666666666667, 0.7529411764705882, 0.5490196078431373]

# change solid color
modelplyDisplay.AmbientColor = [0.9254901960784314, 0.803921568627451, 0.5882352941176471]
modelplyDisplay.DiffuseColor = [0.9254901960784314, 0.803921568627451, 0.5882352941176471]

# Properties modified on modelplyDisplay
modelplyDisplay.Opacity = 0.45

# Properties modified on modelplyDisplay
modelplyDisplay.Opacity = 0.52

# Properties modified on modelplyDisplay
modelplyDisplay.Opacity = 0.6

# set active source
SetActiveSource(a1595505301165_brain_rotatedvtk)

# Properties modified on a1595505301165_brain_rotatedvtkDisplay
a1595505301165_brain_rotatedvtkDisplay.Opacity = 0.9

# Properties modified on a1595505301165_brain_rotatedvtkDisplay
a1595505301165_brain_rotatedvtkDisplay.Opacity = 0.8

# Properties modified on a1595505301165_brain_rotatedvtkDisplay
a1595505301165_brain_rotatedvtkDisplay.Opacity = 0.35

# Properties modified on a1595505301165_brain_rotatedvtkDisplay
a1595505301165_brain_rotatedvtkDisplay.Opacity = 0.27

# Properties modified on a1595505301165_brain_rotatedvtkDisplay
a1595505301165_brain_rotatedvtkDisplay.Opacity = 0.3

# set active source
SetActiveSource(modelply)

# Properties modified on modelplyDisplay
modelplyDisplay.Opacity = 0.41

# Properties modified on modelplyDisplay
modelplyDisplay.Opacity = 0.33

# Properties modified on modelplyDisplay
modelplyDisplay.Opacity = 0.29

# Properties modified on modelplyDisplay
modelplyDisplay.Opacity = 0.4

# set active source
SetActiveSource(a1595505301165_brain_rotatedvtk)

# Properties modified on a1595505301165_brain_rotatedvtkDisplay
a1595505301165_brain_rotatedvtkDisplay.Opacity = 0.2

# Properties modified on a1595505301165_brain_rotatedvtkDisplay
a1595505301165_brain_rotatedvtkDisplay.Opacity = 0.1

# Properties modified on a1595505301165_brain_rotatedvtkDisplay
a1595505301165_brain_rotatedvtkDisplay.Opacity = 0.14

# Properties modified on a1595505301165_brain_rotatedvtkDisplay
a1595505301165_brain_rotatedvtkDisplay.Specular = 0.1

# Properties modified on a1595505301165_brain_rotatedvtkDisplay
a1595505301165_brain_rotatedvtkDisplay.Specular = 0.03

# set active source
SetActiveSource(a1595505301165_fiber_rotatedvtk)

# change solid color
a1595505301165_fiber_rotatedvtkDisplay.AmbientColor = [0.0, 0.0, 0.0]
a1595505301165_fiber_rotatedvtkDisplay.DiffuseColor = [0.0, 0.0, 0.0]

# set active source
SetActiveSource(modelply)

# Properties modified on modelplyDisplay
modelplyDisplay.Opacity = 0.45

# current camera placement for renderView1
renderView1.CameraPosition = [0.00886309493333668, -0.015200096834484027, 0.6853924699131546]
renderView1.CameraFocalPoint = [0.00886309493333668, -0.015200096834484027, -0.02110375091433525]
renderView1.CameraParallelScale = 0.12489220493348169

# save screenshot
if save_images == 1:
    SaveScreenshot('1.png', renderView1, ImageResolution=[1435, 767])



# set active source
SetActiveSource(a1595505301165_brain_rotatedvtk)

# set active source
SetActiveSource(modelply)

# create a new 'Clip'
clip1 = Clip(Input=modelply)
clip1.ClipType = 'Plane'
clip1.HyperTreeGridClipper = 'Plane'
clip1.Scalars = [None, '']

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [0.00036820024251937866, -0.011663608253002167, -0.007976904511451721]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip1.HyperTreeGridClipper.Origin = [0.00036820024251937866, -0.011663608253002167, -0.007976904511451721]

# Properties modified on clip1
clip1.Scalars = ['POINTS', '']

# show data in view
clip1Display = Show(clip1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
clip1Display.Representation = 'Surface'
clip1Display.ColorArrayName = [None, '']
clip1Display.OSPRayScaleArray = 'TCoords'
clip1Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip1Display.SelectOrientationVectors = 'None'
clip1Display.ScaleFactor = 0.023594978451728824
clip1Display.SelectScaleArray = 'None'
clip1Display.GlyphType = 'Arrow'
clip1Display.GlyphTableIndexArray = 'None'
clip1Display.GaussianRadius = 0.001179748922586441
clip1Display.SetScaleArray = ['POINTS', 'TCoords']
clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
clip1Display.OpacityArray = ['POINTS', 'TCoords']
clip1Display.OpacityTransferFunction = 'PiecewiseFunction'
clip1Display.DataAxesGrid = 'GridAxesRepresentation'
clip1Display.PolarAxes = 'PolarAxesRepresentation'
clip1Display.ScalarOpacityUnitDistance = 0.02141350151052093

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip1Display.ScaleTransferFunction.Points = [0.011202685534954071, 0.0, 0.5, 0.0, 0.5772579908370972, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip1Display.OpacityTransferFunction.Points = [0.011202685534954071, 0.0, 0.5, 0.0, 0.5772579908370972, 1.0, 0.5, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# hide data in view
Hide(modelply, renderView1)

# change solid color
clip1Display.AmbientColor = [1.0, 0.8313725490196079, 0.592156862745098]
clip1Display.DiffuseColor = [1.0, 0.8313725490196079, 0.592156862745098]

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=clip1.ClipType)

# set active source
SetActiveSource(a1595505301165_brain_rotatedvtk)

# create a new 'Threshold'
threshold1 = Threshold(Input=a1595505301165_brain_rotatedvtk)
threshold1.Scalars = ['CELLS', 'PartID']
threshold1.ThresholdRange = [0.0, 9.0]

# Properties modified on threshold1
threshold1.ThresholdRange = [0.0, 0.0]

# show data in view
threshold1Display = Show(threshold1, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
threshold1Display.Representation = 'Surface'
threshold1Display.ColorArrayName = [None, '']
threshold1Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold1Display.SelectOrientationVectors = 'None'
threshold1Display.ScaleFactor = 0.015763229876756667
threshold1Display.SelectScaleArray = 'None'
threshold1Display.GlyphType = 'Arrow'
threshold1Display.GlyphTableIndexArray = 'None'
threshold1Display.GaussianRadius = 0.0007881614938378334
threshold1Display.SetScaleArray = [None, '']
threshold1Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold1Display.OpacityArray = [None, '']
threshold1Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold1Display.DataAxesGrid = 'GridAxesRepresentation'
threshold1Display.PolarAxes = 'PolarAxesRepresentation'
threshold1Display.ScalarOpacityUnitDistance = 0.015711899211189064

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(a1595505301165_brain_rotatedvtk)

# create a new 'Threshold'
threshold2 = Threshold(Input=a1595505301165_brain_rotatedvtk)
threshold2.Scalars = ['CELLS', 'PartID']
threshold2.ThresholdRange = [0.0, 9.0]

# Properties modified on threshold2
threshold2.ThresholdRange = [1.0, 1.0]

# show data in view
threshold2Display = Show(threshold2, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
threshold2Display.Representation = 'Surface'
threshold2Display.ColorArrayName = [None, '']
threshold2Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold2Display.SelectOrientationVectors = 'None'
threshold2Display.ScaleFactor = 0.015244810283184052
threshold2Display.SelectScaleArray = 'None'
threshold2Display.GlyphType = 'Arrow'
threshold2Display.GlyphTableIndexArray = 'None'
threshold2Display.GaussianRadius = 0.0007622405141592026
threshold2Display.SetScaleArray = [None, '']
threshold2Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold2Display.OpacityArray = [None, '']
threshold2Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold2Display.DataAxesGrid = 'GridAxesRepresentation'
threshold2Display.PolarAxes = 'PolarAxesRepresentation'
threshold2Display.ScalarOpacityUnitDistance = 0.016325696047454742

# update the view to ensure updated data information
renderView1.Update()

# hide data in view
Hide(threshold1, renderView1)

# hide data in view
Hide(threshold2, renderView1)

# set active source
SetActiveSource(a1595505301165_brain_rotatedvtk)

# create a new 'Threshold'
threshold3 = Threshold(Input=a1595505301165_brain_rotatedvtk)
threshold3.Scalars = ['CELLS', 'PartID']
threshold3.ThresholdRange = [0.0, 9.0]

# Properties modified on threshold3
threshold3.ThresholdRange = [2.0, 9.0]

# show data in view
threshold3Display = Show(threshold3, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
threshold3Display.Representation = 'Surface'
threshold3Display.ColorArrayName = [None, '']
threshold3Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold3Display.SelectOrientationVectors = 'None'
threshold3Display.ScaleFactor = 0.01479274034500122
threshold3Display.SelectScaleArray = 'None'
threshold3Display.GlyphType = 'Arrow'
threshold3Display.GlyphTableIndexArray = 'None'
threshold3Display.GaussianRadius = 0.0007396370172500611
threshold3Display.SetScaleArray = [None, '']
threshold3Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold3Display.OpacityArray = [None, '']
threshold3Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold3Display.DataAxesGrid = 'GridAxesRepresentation'
threshold3Display.PolarAxes = 'PolarAxesRepresentation'
threshold3Display.ScalarOpacityUnitDistance = 0.010615530254364737

# update the view to ensure updated data information
renderView1.Update()

# hide data in view
Hide(a1595505301165_brain_rotatedvtk, renderView1)

# set active source
SetActiveSource(threshold1)

# rename source object
RenameSource('skull', threshold1)

# set active source
SetActiveSource(threshold2)

# rename source object
RenameSource('csf', threshold2)

# set active source
SetActiveSource(threshold3)

# rename source object
RenameSource('brain', threshold3)

# set scalar coloring
ColorBy(threshold3Display, ('CELLS', 'PartID'))

# hide color bar/color legend
threshold3Display.SetScalarBarVisibility(renderView1, False)

# rescale color and/or opacity maps used to include current data range
threshold3Display.RescaleTransferFunctionToDataRange(True, False)


# get color transfer function/color map for 'PartID'
partIDLUT = GetColorTransferFunction('PartID')

# get opacity transfer function/opacity map for 'PartID'
partIDPWF = GetOpacityTransferFunction('PartID')

# create a new 'Clip'
clip2 = Clip(Input=threshold3)
clip2.ClipType = 'Plane'
clip2.HyperTreeGridClipper = 'Plane'
clip2.Scalars = ['CELLS', 'PartID']
clip2.Value = 5.5

# init the 'Plane' selected for 'ClipType'
clip2.ClipType.Origin = [-3.5099685192108154e-05, 0.039759501814842224, -0.020281001925468445]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip2.HyperTreeGridClipper.Origin = [-3.5099685192108154e-05, 0.039759501814842224, -0.020281001925468445]

# show data in view
clip2Display = Show(clip2, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
clip2Display.Representation = 'Surface'
clip2Display.ColorArrayName = ['CELLS', 'PartID']
clip2Display.LookupTable = partIDLUT
clip2Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip2Display.SelectOrientationVectors = 'None'
clip2Display.ScaleFactor = 0.014791753888130189
clip2Display.SelectScaleArray = 'None'
clip2Display.GlyphType = 'Arrow'
clip2Display.GlyphTableIndexArray = 'None'
clip2Display.GaussianRadius = 0.0007395876944065094
clip2Display.SetScaleArray = [None, '']
clip2Display.ScaleTransferFunction = 'PiecewiseFunction'
clip2Display.OpacityArray = [None, '']
clip2Display.OpacityTransferFunction = 'PiecewiseFunction'
clip2Display.DataAxesGrid = 'GridAxesRepresentation'
clip2Display.PolarAxes = 'PolarAxesRepresentation'
clip2Display.ScalarOpacityFunction = partIDPWF
clip2Display.ScalarOpacityUnitDistance = 0.011394588606481506

# hide data in view
Hide(threshold3, renderView1)

# show color bar/color legend
clip2Display.SetScalarBarVisibility(renderView1, False)

# update the view to ensure updated data information
renderView1.Update()

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=clip2.ClipType)

# set active source
SetActiveSource(threshold1)

# show data in view
threshold1Display = Show(threshold1, renderView1, 'UnstructuredGridRepresentation')

# Properties modified on threshold1Display
threshold1Display.Opacity = 0.39

# Properties modified on threshold1Display
threshold1Display.Opacity = 0.27

# set active source
SetActiveSource(threshold2)

# show data in view
threshold2Display = Show(threshold2, renderView1, 'UnstructuredGridRepresentation')

# Properties modified on threshold2Display
threshold2Display.Opacity = 0.29

# Properties modified on threshold2Display
threshold2Display.Opacity = 0.23

# Properties modified on threshold2Display
threshold2Display.Opacity = 0.12

# Properties modified on threshold2Display
threshold2Display.Opacity = 0.06


# current camera placement for renderView1
renderView1.CameraPosition = [0.00886309493333668, -0.015200096834484027, 0.6853924699131546]
renderView1.CameraFocalPoint = [0.00886309493333668, -0.015200096834484027, -0.02110375091433525]
renderView1.CameraParallelScale = 0.12489220493348169



# save screenshot
if save_images == 1:
    SaveScreenshot('2.png', renderView1, ImageResolution=[1435, 767])

# create a new 'Clip'
clip3 = Clip(Input=threshold2)
clip3.ClipType = 'Plane'
clip3.HyperTreeGridClipper = 'Plane'
clip3.Scalars = ['CELLS', 'PartID']
clip3.Value = 1.0

# init the 'Plane' selected for 'ClipType'
clip3.ClipType.Origin = [-2.8602778911590576e-05, 0.03985750116407871, -0.020484551787376404]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip3.HyperTreeGridClipper.Origin = [-2.8602778911590576e-05, 0.03985750116407871, -0.020484551787376404]

# show data in view
clip3Display = Show(clip3, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
clip3Display.Representation = 'Surface'
clip3Display.ColorArrayName = [None, '']
clip3Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip3Display.SelectOrientationVectors = 'None'
clip3Display.ScaleFactor = 0.01524368077516556
clip3Display.SelectScaleArray = 'None'
clip3Display.GlyphType = 'Arrow'
clip3Display.GlyphTableIndexArray = 'None'
clip3Display.GaussianRadius = 0.0007621840387582779
clip3Display.SetScaleArray = [None, '']
clip3Display.ScaleTransferFunction = 'PiecewiseFunction'
clip3Display.OpacityArray = [None, '']
clip3Display.OpacityTransferFunction = 'PiecewiseFunction'
clip3Display.DataAxesGrid = 'GridAxesRepresentation'
clip3Display.PolarAxes = 'PolarAxesRepresentation'
clip3Display.ScalarOpacityUnitDistance = 0.01760624811068953

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(threshold1)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=clip3.ClipType)

# create a new 'Clip'
clip4 = Clip(Input=threshold1)
clip4.ClipType = 'Plane'
clip4.HyperTreeGridClipper = 'Plane'
clip4.Scalars = ['CELLS', 'PartID']

# init the 'Plane' selected for 'ClipType'
clip4.ClipType.Origin = [-2.215057611465454e-05, 0.036630501970648766, -0.02110375091433525]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip4.HyperTreeGridClipper.Origin = [-2.215057611465454e-05, 0.036630501970648766, -0.02110375091433525]

# show data in view
clip4Display = Show(clip4, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
clip4Display.Representation = 'Surface'
clip4Display.ColorArrayName = [None, '']
clip4Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip4Display.SelectOrientationVectors = 'None'
clip4Display.ScaleFactor = 0.015760524570941927
clip4Display.SelectScaleArray = 'None'
clip4Display.GlyphType = 'Arrow'
clip4Display.GlyphTableIndexArray = 'None'
clip4Display.GaussianRadius = 0.0007880262285470962
clip4Display.SetScaleArray = [None, '']
clip4Display.ScaleTransferFunction = 'PiecewiseFunction'
clip4Display.OpacityArray = [None, '']
clip4Display.OpacityTransferFunction = 'PiecewiseFunction'
clip4Display.DataAxesGrid = 'GridAxesRepresentation'
clip4Display.PolarAxes = 'PolarAxesRepresentation'
clip4Display.ScalarOpacityUnitDistance = 0.016686807253029273

# update the view to ensure updated data information
renderView1.Update()

# hide data in view
Hide(threshold1, renderView1)

# hide data in view
Hide(threshold2, renderView1)

# set active source
SetActiveSource(clip3)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=clip4.ClipType)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=clip3.ClipType)

# change solid color
clip3Display.AmbientColor = [0.0, 0.3333333333333333, 1.0]
clip3Display.DiffuseColor = [0.0, 0.3333333333333333, 1.0]

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=clip3.ClipType)

# set active source
SetActiveSource(a1595505301165_fiber_rotatedvtk)

# current camera placement for renderView1
renderView1.CameraPosition = [0.7079473093484734, 0.013145228483577322, -0.03250350297623588]
renderView1.CameraFocalPoint = [0.0019936148638244476, -0.01453035383512435, -0.03309800300330218]
renderView1.CameraViewUp = [-0.03915244720149675, 0.997412393292155, 0.060295966576127805]
renderView1.CameraParallelScale = 0.12489220493348169

# save screenshot
if save_images == 1:
    SaveScreenshot('3.png', renderView1, ImageResolution=[1435, 767])

# Properties modified on a1595505301165_fiber_rotatedvtkDisplay
a1595505301165_fiber_rotatedvtkDisplay.Opacity = 0.09

# Properties modified on a1595505301165_fiber_rotatedvtkDisplay
a1595505301165_fiber_rotatedvtkDisplay.Opacity = 0.16

# Properties modified on a1595505301165_fiber_rotatedvtkDisplay
a1595505301165_fiber_rotatedvtkDisplay.Opacity = 0.13

# current camera placement for renderView1
renderView1.CameraPosition = [0.7073424074974186, 0.042724626666243444, 0.01763269483601032]
renderView1.CameraFocalPoint = [0.004651226566542791, -0.015430326800480674, -0.02686467219545233]
renderView1.CameraViewUp = [-0.07858042945297322, 0.9951225873176894, -0.05963348318800486]
renderView1.CameraParallelScale = 0.12489220493348169

# save screenshot
if save_images == 1:
    SaveScreenshot('4.png', renderView1, ImageResolution=[1435, 767])

# Properties modified on a1595505301165_fiber_rotatedvtkDisplay
a1595505301165_fiber_rotatedvtkDisplay.Opacity = 1.0

# current camera placement for renderView1
renderView1.CameraPosition = [0.478008601606686, 0.14201146368502096, 0.30148582899328896]
renderView1.CameraFocalPoint = [0.015492137250407456, -0.013576376177097107, -0.019120112803527465]
renderView1.CameraViewUp = [-0.20050453640965088, 0.9633407888727382, -0.17824829697139163]
renderView1.CameraParallelScale = 0.12489220493348169

# save screenshot
if save_images == 1:
    SaveScreenshot('5.png', renderView1, ImageResolution=[1435, 767])

# set active source
SetActiveSource(modelply)

# show data in view
modelplyDisplay = Show(modelply, renderView1, 'GeometryRepresentation')

# hide data in view
Hide(clip1, renderView1)

# Properties modified on modelplyDisplay
modelplyDisplay.Opacity = 1.0

# change representation type
modelplyDisplay.SetRepresentationType('Surface With Edges')

# current camera placement for renderView1
renderView1.CameraPosition = [-0.014267696011478495, 0.014524368875835645, 0.564550556253394]
renderView1.CameraFocalPoint = [0.008249435859237327, -0.015216795775393472, -0.01813775453249573]
renderView1.CameraViewUp = [0.011700438972819275, 0.9986544857291259, -0.05052046972206928]
renderView1.CameraParallelScale = 0.12489220493348169

# save screenshot
if save_images == 1:
    SaveScreenshot('6.png', renderView1, ImageResolution=[1435, 767])

# current camera placement for renderView1
renderView1.CameraPosition = [0.246959044019592, 0.04095271681126901, 0.5105579762808911]
renderView1.CameraFocalPoint = [0.012464466241954021, -0.014451873798682575, -0.021287724990851676]
renderView1.CameraViewUp = [-0.08458729945982328, 0.9942094876329927, -0.06627581361731047]
renderView1.CameraParallelScale = 0.12489220493348169

# save screenshot
if save_images == 1:
    SaveScreenshot('7.png', renderView1, ImageResolution=[1435, 767])

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [0.246959044019592, 0.04095271681126901, 0.5105579762808911]
renderView1.CameraFocalPoint = [0.012464466241954021, -0.014451873798682575, -0.021287724990851676]
renderView1.CameraViewUp = [-0.08458729945982328, 0.9942094876329927, -0.06627581361731047]
renderView1.CameraParallelScale = 0.12489220493348169

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
