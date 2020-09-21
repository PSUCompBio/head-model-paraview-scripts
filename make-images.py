# trace generated using paraview version 5.7.0-RC2
#
# To ensure correct image size when batch processing, please search
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
import os.path
import glob

# enter folder id that is downloaded from nsfcareer
folder_id=1600265334475

# if you want to save images to local directory, 1= save, 0= don't save
save_images = 1

# modify the paths (user name and download location)
#read_path_brain = 'C:\\Users\\rhk12\\Downloads\\%s\\' % folder_id
read_path_brain = 'C:\\Users\\rhk12\\Box Sync\\personal\\Business\\BrainSimTech\\Development\\Head-Models\\%s-FEMesh\\' % folder_id

# note the $s (1) below. This is for when you download from nsfcareer.io, the
#file names are the same.
#read_ply = 'C:\\Users\\rhk12\\Downloads\\%s (1)\\avatars\\*\\face\\model.ply' % folder_id
read_ply_path = 'C:\\Users\\rhk12\\Box Sync\\personal\\Business\\BrainSimTech\\Development\\Head-Models\\%s-avatar\\avatars\\*\\face\\' % folder_id

############################################################################
###########  should not need to change anything below ######################
############################################################################
#print (read_ply)
#sprint(glob.glob(read_ply_path))

for item in glob.glob(read_ply_path):
    #print (item)
    read_ply = item


read_ply2 = read_ply + 'model.ply'
print ('read_ply2 = ', read_ply2)


brainfile = '%s_brain_rotated.vtk' % folder_id
fiberfile = '%s_fiber_rotated.vtk' % folder_id

brainfile_path = read_path_brain + brainfile
fiberfile_path = read_path_brain + fiberfile

print ('read_path_brain = ', read_path_brain)

#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'PLY Reader'
modelply = PLYReader(FileNames=[read_ply2])

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1231, 718]

# show data in view
modelplyDisplay = Show(modelply, renderView1)

# # trace defaults for the display properties.
# modelplyDisplay.Representation = 'Surface'
# modelplyDisplay.ColorArrayName = [None, '']
# modelplyDisplay.OSPRayScaleArray = 'TCoords'
# modelplyDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
# modelplyDisplay.SelectOrientationVectors = 'None'
# modelplyDisplay.ScaleFactor = 0.023842415213584902
# modelplyDisplay.SelectScaleArray = 'None'
# modelplyDisplay.GlyphType = 'Arrow'
# modelplyDisplay.GlyphTableIndexArray = 'None'
# modelplyDisplay.GaussianRadius = 0.001192120760679245
# modelplyDisplay.SetScaleArray = ['POINTS', 'TCoords']
# modelplyDisplay.ScaleTransferFunction = 'PiecewiseFunction'
# modelplyDisplay.OpacityArray = ['POINTS', 'TCoords']
# modelplyDisplay.OpacityTransferFunction = 'PiecewiseFunction'
# modelplyDisplay.DataAxesGrid = 'GridAxesRepresentation'
# modelplyDisplay.PolarAxes = 'PolarAxesRepresentation'

# # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
# modelplyDisplay.ScaleTransferFunction.Points = [0.012195363640785217, 0.0, 0.5, 0.0, 0.5833437442779541, 1.0, 0.5, 0.0]
#
# # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
# modelplyDisplay.OpacityTransferFunction.Points = [0.012195363640785217, 0.0, 0.5, 0.0, 0.5833437442779541, 1.0, 0.5, 0.0]

# reset view to fit data
renderView1.ResetCamera()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [0.0004459694027900696, -0.012621521949768066, 0.6783159120159341]
renderView1.CameraFocalPoint = [0.0004459694027900696, -0.012621521949768066, -0.007184971123933792]
renderView1.CameraParallelScale = 0.17742068399119526


# update the view to ensure updated data information
renderView1.Update()

# create a new 'Clip'
clip1 = Clip(Input=modelply)
clip1.ClipType = 'Plane'
clip1.Scalars = [None, '']

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [0.0004459694027900696, -0.012621521949768066, -0.007184971123933792]

# Properties modified on clip1
clip1.Scalars = ['POINTS', '']

# show data in view
clip1Display = Show(clip1, renderView1)

# # trace defaults for the display properties.
# clip1Display.Representation = 'Surface'
# clip1Display.ColorArrayName = [None, '']
# clip1Display.OSPRayScaleArray = 'TCoords'
# clip1Display.OSPRayScaleFunction = 'PiecewiseFunction'
# clip1Display.SelectOrientationVectors = 'None'
# clip1Display.ScaleFactor = 0.023842415213584902
# clip1Display.SelectScaleArray = 'None'
# clip1Display.GlyphType = 'Arrow'
# clip1Display.GlyphTableIndexArray = 'None'
# clip1Display.GaussianRadius = 0.001192120760679245
# clip1Display.SetScaleArray = ['POINTS', 'TCoords']
# clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
# clip1Display.OpacityArray = ['POINTS', 'TCoords']
# clip1Display.OpacityTransferFunction = 'PiecewiseFunction'
# clip1Display.DataAxesGrid = 'GridAxesRepresentation'
# clip1Display.PolarAxes = 'PolarAxesRepresentation'
# clip1Display.ScalarOpacityUnitDistance = 0.02167448838382505
#
# # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
# clip1Display.ScaleTransferFunction.Points = [0.012195363640785217, 0.0, 0.5, 0.0, 0.5833437442779541, 1.0, 0.5, 0.0]
#
# # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
# clip1Display.OpacityTransferFunction.Points = [0.012195363640785217, 0.0, 0.5, 0.0, 0.5833437442779541, 1.0, 0.5, 0.0]

# get display properties
clip1Display = GetDisplayProperties(clip1, view=renderView1)

# change solid color
clip1Display.AmbientColor = [0.9294117647058824, 0.7098039215686275, 0.5333333333333333]
clip1Display.DiffuseColor = [0.9294117647058824, 0.7098039215686275, 0.5333333333333333]

# change solid color
clip1Display.AmbientColor = [1.0, 0.7568627450980392, 0.5725490196078431]
clip1Display.DiffuseColor = [1.0, 0.7568627450980392, 0.5725490196078431]


# hide data in view
Hide(modelply, renderView1)

# update the view to ensure updated data information
renderView1.Update()

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [0.361129942617539, 0.09702900927179788, 0.5653491267727693]
renderView1.CameraFocalPoint = [0.0004459694027900685, -0.012621521949768027, -0.00718497112393379]
renderView1.CameraViewUp = [-0.11245283556274531, 0.9866124482840203, -0.1181111199883806]
renderView1.CameraParallelScale = 0.17742068399119526

#### uncomment the following to render all views
#RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).


# create a new 'Legacy VTK Reader'
brain_rotatedvtk = LegacyVTKReader(FileNames=[brainfile_path])

# # find source
# modelply = FindSource('model.ply')
#
# # find source
# clip1 = FindSource('Clip1')
#
# # get active view
# renderView1 = GetActiveViewOrCreate('RenderView')
# # uncomment following to set a specific view size
# # renderView1.ViewSize = [2528, 1625]

# show data in view
brain_rotatedvtkDisplay = Show(brain_rotatedvtk, renderView1)

# # trace defaults for the display properties.
# brain_rotatedvtkDisplay.Representation = 'Surface'
# brain_rotatedvtkDisplay.ColorArrayName = [None, '']
# brain_rotatedvtkDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
# brain_rotatedvtkDisplay.SelectOrientationVectors = 'None'
# brain_rotatedvtkDisplay.ScaleFactor = 0.016796400398015977
# brain_rotatedvtkDisplay.SelectScaleArray = 'None'
# brain_rotatedvtkDisplay.GlyphType = 'Arrow'
# brain_rotatedvtkDisplay.GlyphTableIndexArray = 'None'
# brain_rotatedvtkDisplay.GaussianRadius = 0.0008398200199007988
# brain_rotatedvtkDisplay.SetScaleArray = [None, '']
# brain_rotatedvtkDisplay.ScaleTransferFunction = 'PiecewiseFunction'
# brain_rotatedvtkDisplay.OpacityArray = [None, '']
# brain_rotatedvtkDisplay.OpacityTransferFunction = 'PiecewiseFunction'
# brain_rotatedvtkDisplay.DataAxesGrid = 'GridAxesRepresentation'
# brain_rotatedvtkDisplay.PolarAxes = 'PolarAxesRepresentation'
# brain_rotatedvtkDisplay.ScalarOpacityUnitDistance = 0.009883262528836716


# create a new 'Threshold'
threshold1 = Threshold(Input=brain_rotatedvtk)
threshold1.Scalars = ['CELLS', 'Part ID']
threshold1.ThresholdRange = [0.0, 0.0]


# get active view
#renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [2528, 1625]

# show data in view
threshold1Display = Show(threshold1, renderView1)

# # trace defaults for the display properties.
# threshold1Display.Representation = 'Surface'
# threshold1Display.ColorArrayName = [None, '']
# threshold1Display.OSPRayScaleFunction = 'PiecewiseFunction'
# threshold1Display.SelectOrientationVectors = 'None'
# threshold1Display.ScaleFactor = 0.016796400398015977
# threshold1Display.SelectScaleArray = 'None'
# threshold1Display.GlyphType = 'Arrow'
# threshold1Display.GlyphTableIndexArray = 'None'
# threshold1Display.GaussianRadius = 0.0008398200199007988
# threshold1Display.SetScaleArray = [None, '']
# threshold1Display.ScaleTransferFunction = 'PiecewiseFunction'
# threshold1Display.OpacityArray = [None, '']
# threshold1Display.OpacityTransferFunction = 'PiecewiseFunction'
# threshold1Display.DataAxesGrid = 'GridAxesRepresentation'
# threshold1Display.PolarAxes = 'PolarAxesRepresentation'
# threshold1Display.ScalarOpacityUnitDistance = 0.009883262528836716

# hide data in view
Hide(brain_rotatedvtk, renderView1)


# create a new 'Clip'
clip2 = Clip(Input=threshold1)
clip2.ClipType = 'Plane'
clip2.Scalars = ['CELLS', 'Part ID']

# init the 'Plane' selected for 'ClipType'
clip2.ClipType.Origin = [-2.2199004888534546e-05, 0.034602999687194824, -0.0191040001809597]

# # find source
# modelply = FindSource('model.ply')
#
# # find source
# clip1 = FindSource('Clip1')
#
# # get active view
# renderView1 = GetActiveViewOrCreate('RenderView')
# # uncomment following to set a specific view size
# # renderView1.ViewSize = [2528, 1625]

# show data in view
clip2Display = Show(clip2, renderView1)
#
# # trace defaults for the display properties.
# clip2Display.Representation = 'Surface'
# clip2Display.ColorArrayName = [None, '']
# clip2Display.OSPRayScaleFunction = 'PiecewiseFunction'
# clip2Display.SelectOrientationVectors = 'None'
# clip2Display.ScaleFactor = 0.016793532669544222
# clip2Display.SelectScaleArray = 'None'
# clip2Display.GlyphType = 'Arrow'
# clip2Display.GlyphTableIndexArray = 'None'
# clip2Display.GaussianRadius = 0.000839676633477211
# clip2Display.SetScaleArray = [None, '']
# clip2Display.ScaleTransferFunction = 'PiecewiseFunction'
# clip2Display.OpacityArray = [None, '']
# clip2Display.OpacityTransferFunction = 'PiecewiseFunction'
# clip2Display.DataAxesGrid = 'GridAxesRepresentation'
# clip2Display.PolarAxes = 'PolarAxesRepresentation'
# clip2Display.ScalarOpacityUnitDistance = 0.017420762002468605

# hide data in view
Hide(threshold1, renderView1)

# # find source
# a1600265334475_brain_rotatedvtk = FindSource('1600265334475_brain_rotated.vtk')
#
#


# create a new 'Threshold'
threshold2 = Threshold(Input=brain_rotatedvtk)
threshold2.Scalars = ['CELLS', 'Part ID']
# threshold2.ThresholdRange = [0.0, 9.0]
#
# # find source
# modelply = FindSource('model.ply')
#
# # find source
# clip1 = FindSource('Clip1')
#
# # find source
# clip2 = FindSource('Clip2')

# Properties modified on threshold2
threshold2.ThresholdRange = [1.0, 1.0]

# # get active view
# renderView1 = GetActiveViewOrCreate('RenderView')
# # uncomment following to set a specific view size
# # renderView1.ViewSize = [2528, 1625]

# show data in view
threshold2Display = Show(threshold2, renderView1)
#
# # trace defaults for the display properties.
# threshold2Display.Representation = 'Surface'
# threshold2Display.ColorArrayName = [None, '']
# threshold2Display.OSPRayScaleFunction = 'PiecewiseFunction'
# threshold2Display.SelectOrientationVectors = 'None'
# threshold2Display.ScaleFactor = 0.016116880252957346
# threshold2Display.SelectScaleArray = 'None'
# threshold2Display.GlyphType = 'Arrow'
# threshold2Display.GlyphTableIndexArray = 'None'
# threshold2Display.GaussianRadius = 0.0008058440126478672
# threshold2Display.SetScaleArray = [None, '']
# threshold2Display.ScaleTransferFunction = 'PiecewiseFunction'
# threshold2Display.OpacityArray = [None, '']
# threshold2Display.OpacityTransferFunction = 'PiecewiseFunction'
# threshold2Display.DataAxesGrid = 'GridAxesRepresentation'
# threshold2Display.PolarAxes = 'PolarAxesRepresentation'
# threshold2Display.ScalarOpacityUnitDistance = 0.016563881750601347

# hide data in view
Hide(brain_rotatedvtk, renderView1)




# create a new 'Clip'
clip3 = Clip(Input=threshold2)
clip3.ClipType = 'Plane'
clip3.Scalars = ['CELLS', 'Part ID']
clip3.Value = 1.0

# init the 'Plane' selected for 'ClipType'
clip3.ClipType.Origin = [-3.094971179962158e-05, 0.03780300170183182, -0.019258400425314903]
#
# # find source
# modelply = FindSource('model.ply')
#
# # find source
# clip1 = FindSource('Clip1')
#
# # find source
# clip2 = FindSource('Clip2')
#
# # find source
# threshold1 = FindSource('Threshold1')
#
# # find source
# a1600265334475_brain_rotatedvtk = FindSource('1600265334475_brain_rotated.vtk')
#
# # get active view
# renderView1 = GetActiveViewOrCreate('RenderView')
# # uncomment following to set a specific view size
# # renderView1.ViewSize = [2528, 1625]

# show data in view
clip3Display = Show(clip3, renderView1)
#
# # trace defaults for the display properties.
# clip3Display.Representation = 'Surface'
# clip3Display.ColorArrayName = [None, '']
# clip3Display.OSPRayScaleFunction = 'PiecewiseFunction'
# clip3Display.SelectOrientationVectors = 'None'
# clip3Display.ScaleFactor = 0.01611562557518482
# clip3Display.SelectScaleArray = 'None'
# clip3Display.GlyphType = 'Arrow'
# clip3Display.GlyphTableIndexArray = 'None'
# clip3Display.GaussianRadius = 0.0008057812787592412
# clip3Display.SetScaleArray = [None, '']
# clip3Display.ScaleTransferFunction = 'PiecewiseFunction'
# clip3Display.OpacityArray = [None, '']
# clip3Display.OpacityTransferFunction = 'PiecewiseFunction'
# clip3Display.DataAxesGrid = 'GridAxesRepresentation'
# clip3Display.PolarAxes = 'PolarAxesRepresentation'
# clip3Display.ScalarOpacityUnitDistance = 0.018236409827184236

# hide data in view
Hide(threshold2, renderView1)

# # update the view to ensure updated data information
# renderView1.Update()

# change solid color
clip3Display.AmbientColor = [0.0, 0.0, 1.0]
clip3Display.DiffuseColor = [0.0, 0.0, 1.0]

#############################################################
#############################################################




# create a new 'Threshold'
threshold3 = Threshold(Input=brain_rotatedvtk)
threshold3.Scalars = ['CELLS', 'Part ID']
threshold3.ThresholdRange = [2.0, 9.0]
#
# # find source
# modelply = FindSource('model.ply')
#
# # find source
# clip1 = FindSource('Clip1')
#
# # find source
# clip2 = FindSource('Clip2')
#
# # find source
# threshold1 = FindSource('Threshold1')
#
# # find source
# threshold2 = FindSource('Threshold2')
#
# # find source
# clip3 = FindSource('Clip3')
#
# # Properties modified on threshold3
# threshold3.ThresholdRange = [2.0, 9.0]
#
# # get active view
# renderView1 = GetActiveViewOrCreate('RenderView')
# # uncomment following to set a specific view size
# # renderView1.ViewSize = [2528, 1625]

# show data in view
threshold3Display = Show(threshold3, renderView1)
#
# # trace defaults for the display properties.
# threshold3Display.Representation = 'Surface'
# threshold3Display.ColorArrayName = [None, '']
# threshold3Display.OSPRayScaleFunction = 'PiecewiseFunction'
# threshold3Display.SelectOrientationVectors = 'None'
# threshold3Display.ScaleFactor = 0.015613999590277672
# threshold3Display.SelectScaleArray = 'None'
# threshold3Display.GlyphType = 'Arrow'
# threshold3Display.GlyphTableIndexArray = 'None'
# threshold3Display.GaussianRadius = 0.0007806999795138836
# threshold3Display.SetScaleArray = [None, '']
# threshold3Display.ScaleTransferFunction = 'PiecewiseFunction'
# threshold3Display.OpacityArray = [None, '']
# threshold3Display.OpacityTransferFunction = 'PiecewiseFunction'
# threshold3Display.DataAxesGrid = 'GridAxesRepresentation'
# threshold3Display.PolarAxes = 'PolarAxesRepresentation'
# threshold3Display.ScalarOpacityUnitDistance = 0.010766248436550553

# hide data in view
Hide(brain_rotatedvtk, renderView1)

############################################################
##############################################################


# create a new 'Clip'
clip4 = Clip(Input=threshold3)
clip4.ClipType = 'Plane'
clip4.Scalars = ['CELLS', 'Part ID']
clip4.Value = 5.5

# init the 'Plane' selected for 'ClipType'
clip4.ClipType.Origin = [-3.8350000977516174e-05, 0.03766200132668018, -0.019286999478936195]
#
# # find source
# modelply = FindSource('model.ply')
#
# # find source
# clip1 = FindSource('Clip1')
#
# # find source
# clip2 = FindSource('Clip2')
#
# # find source
# threshold1 = FindSource('Threshold1')
#
# # find source
# a1600265334475_brain_rotatedvtk = FindSource('1600265334475_brain_rotated.vtk')
#
# # find source
# threshold2 = FindSource('Threshold2')
#
# # find source
# clip3 = FindSource('Clip3')
#
# # get active view
# renderView1 = GetActiveViewOrCreate('RenderView')
# # uncomment following to set a specific view size
# # renderView1.ViewSize = [2528, 1625]

# show data in view
clip4Display = Show(clip4, renderView1)
#
# # trace defaults for the display properties.
# clip4Display.Representation = 'Surface'
# clip4Display.ColorArrayName = [None, '']
# clip4Display.OSPRayScaleFunction = 'PiecewiseFunction'
# clip4Display.SelectOrientationVectors = 'None'
# clip4Display.ScaleFactor = 0.015612902119755745
# clip4Display.SelectScaleArray = 'None'
# clip4Display.GlyphType = 'Arrow'
# clip4Display.GlyphTableIndexArray = 'None'
# clip4Display.GaussianRadius = 0.0007806451059877873
# clip4Display.SetScaleArray = [None, '']
# clip4Display.ScaleTransferFunction = 'PiecewiseFunction'
# clip4Display.OpacityArray = [None, '']
# clip4Display.OpacityTransferFunction = 'PiecewiseFunction'
# clip4Display.DataAxesGrid = 'GridAxesRepresentation'
# clip4Display.PolarAxes = 'PolarAxesRepresentation'
# clip4Display.ScalarOpacityUnitDistance = 0.011684978574366735

# hide data in view
Hide(threshold3, renderView1)

#############################################################
#############################################################



# set scalar coloring
ColorBy(clip4Display, ('CELLS', 'Part ID'))

# # rescale color and/or opacity maps used to include current data range
# clip4Display.RescaleTransferFunctionToDataRange(True, False)
#
# # show color bar/color legend
# clip4Display.SetScalarBarVisibility(renderView1, True)
#
# # get color transfer function/color map for 'PartID'
# partIDLUT = GetColorTransferFunction('PartID')
#
# # get opacity transfer function/opacity map for 'PartID'
# partIDPWF = GetOpacityTransferFunction('PartID')


#############################################################
#############################################################

# create a new 'Legacy VTK Reader'
fiber_rotatedvtk = LegacyVTKReader(FileNames=[fiberfile_path])
#
# # find source
# modelply = FindSource('model.ply')
#
# # find source
# clip1 = FindSource('Clip1')
#
# # find source
# clip2 = FindSource('Clip2')
#
# # find source
# threshold1 = FindSource('Threshold1')
#
# # get active view
# renderView1 = GetActiveViewOrCreate('RenderView')
# # uncomment following to set a specific view size
# # renderView1.ViewSize = [2528, 1625]

# show data in view
fiber_rotatedvtkDisplay = Show(fiber_rotatedvtk, renderView1)
#
# # trace defaults for the display properties.
# a1600265334475_fiber_rotatedvtkDisplay.Representation = 'Surface'
# a1600265334475_fiber_rotatedvtkDisplay.ColorArrayName = [None, '']
# a1600265334475_fiber_rotatedvtkDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
# a1600265334475_fiber_rotatedvtkDisplay.SelectOrientationVectors = 'None'
# a1600265334475_fiber_rotatedvtkDisplay.ScaleFactor = 0.015039640292525292
# a1600265334475_fiber_rotatedvtkDisplay.SelectScaleArray = 'None'
# a1600265334475_fiber_rotatedvtkDisplay.GlyphType = 'Arrow'
# a1600265334475_fiber_rotatedvtkDisplay.GlyphTableIndexArray = 'None'
# a1600265334475_fiber_rotatedvtkDisplay.GaussianRadius = 0.0007519820146262646
# a1600265334475_fiber_rotatedvtkDisplay.SetScaleArray = [None, '']
# a1600265334475_fiber_rotatedvtkDisplay.ScaleTransferFunction = 'PiecewiseFunction'
# a1600265334475_fiber_rotatedvtkDisplay.OpacityArray = [None, '']
# a1600265334475_fiber_rotatedvtkDisplay.OpacityTransferFunction = 'PiecewiseFunction'
# a1600265334475_fiber_rotatedvtkDisplay.DataAxesGrid = 'GridAxesRepresentation'
# a1600265334475_fiber_rotatedvtkDisplay.PolarAxes = 'PolarAxesRepresentation'
# a1600265334475_fiber_rotatedvtkDisplay.ScalarOpacityUnitDistance = 0.0044438609832472015
#
# # find source
# a1600265334475_brain_rotatedvtk = FindSource('1600265334475_brain_rotated.vtk')
#
# # find source
# threshold2 = FindSource('Threshold2')
#
# # find source
# clip3 = FindSource('Clip3')
#
# # find source
# clip4 = FindSource('Clip4')
#
# # find source
# threshold3 = FindSource('Threshold3')
#
# # update the view to ensure updated data information
# renderView1.Update()




#############################################################
#############################################################


# change solid color
fiber_rotatedvtkDisplay.AmbientColor = [0.0, 0.0, 0.0]
fiber_rotatedvtkDisplay.DiffuseColor = [0.0, 0.0, 0.0]



#############################################################
#############################################################


# current camera placement for renderView1
renderView1.CameraPosition = [0.361129942617539, 0.09702900927179788, 0.5653491267727693]
renderView1.CameraFocalPoint = [0.0004459694027900685, -0.012621521949768027, -0.00718497112393379]
renderView1.CameraViewUp = [-0.11245283556274531, 0.9866124482840203, -0.1181111199883806]
renderView1.CameraParallelScale = 0.17742068399119526

# update the view to ensure updated data information
renderView1.Update()

# save screenshot
if save_images == 1:
    SaveScreenshot('1.png', renderView1, ImageResolution=[1435, 767])

#
# #############################################################
# #############################################################


# current camera placement for renderView1
renderView1.CameraPosition = [0.6294728616625519, 0.0797671983914115, -0.14616004751814973]
renderView1.CameraFocalPoint = [-0.012370843440294264, -0.012621521949768072, -0.007147137075662621]
renderView1.CameraViewUp = [-0.13338718673120198, 0.9901651411097798, 0.04220013918205998]
renderView1.CameraParallelScale = 0.1716467158339834

# save screenshot
if save_images == 1:
    SaveScreenshot('2.png', renderView1, ImageResolution=[1435, 767])

#############################################################
#############################################################

# current camera placement for renderView1
renderView1.CameraPosition = [-0.007882559328110095, -0.09091010205367836, 0.651480038671261]
renderView1.CameraFocalPoint = [-0.012286670817691478, -0.011184983638189133, -0.0068877278481427]
renderView1.CameraViewUp = [0.000817271941923272, 0.9927479725462539, 0.1202114598192511]
renderView1.CameraParallelScale = 0.1716467158339834

# update the view to ensure updated data information
renderView1.Update()

# save screenshot
if save_images == 1:
    SaveScreenshot('3.png', renderView1, ImageResolution=[1435, 767])



#############################################################
#############################################################

# show data in view
threshold1Display = Show(threshold1, renderView1)

# # trace defaults for the display properties.
# threshold1Display.Representation = 'Surface'
# threshold1Display.ColorArrayName = [None, '']
# threshold1Display.OSPRayScaleFunction = 'PiecewiseFunction'
# threshold1Display.SelectOrientationVectors = 'None'
# threshold1Display.ScaleFactor = 0.016796400398015977
# threshold1Display.SelectScaleArray = 'None'
# threshold1Display.GlyphType = 'Arrow'
# threshold1Display.GlyphTableIndexArray = 'None'
# threshold1Display.GaussianRadius = 0.0008398200199007988
# threshold1Display.SetScaleArray = [None, '']
# threshold1Display.ScaleTransferFunction = 'PiecewiseFunction'
# threshold1Display.OpacityArray = [None, '']
# threshold1Display.OpacityTransferFunction = 'PiecewiseFunction'
# threshold1Display.DataAxesGrid = 'GridAxesRepresentation'
# threshold1Display.PolarAxes = 'PolarAxesRepresentation'
# threshold1Display.ScalarOpacityUnitDistance = 0.01599442273080559

# Properties modified on threshold1Display
threshold1Display.Opacity = 0.14


# save screenshot
if save_images == 1:
    SaveScreenshot('4.png', renderView1, ImageResolution=[1435, 767])


#############################################################
#############################################################



# hide data in view
Hide(clip1, renderView1)
#
# find source
pLYReader1 = FindSource('PLYReader1')

# set active source
SetActiveSource(pLYReader1)

# show data in view
pLYReader1Display = Show(pLYReader1, renderView1)
#
# # trace defaults for the display properties.
# pLYReader1Display.Representation = 'Surface'
# pLYReader1Display.ColorArrayName = [None, '']
# pLYReader1Display.OSPRayScaleArray = 'TCoords'
# pLYReader1Display.OSPRayScaleFunction = 'PiecewiseFunction'
# pLYReader1Display.SelectOrientationVectors = 'None'
# pLYReader1Display.ScaleFactor = 0.023842415213584902
# pLYReader1Display.SelectScaleArray = 'None'
# pLYReader1Display.GlyphType = 'Arrow'
# pLYReader1Display.GlyphTableIndexArray = 'None'
# pLYReader1Display.GaussianRadius = 0.001192120760679245
# pLYReader1Display.SetScaleArray = ['POINTS', 'TCoords']
# pLYReader1Display.ScaleTransferFunction = 'PiecewiseFunction'
# pLYReader1Display.OpacityArray = ['POINTS', 'TCoords']
# pLYReader1Display.OpacityTransferFunction = 'PiecewiseFunction'
# pLYReader1Display.DataAxesGrid = 'GridAxesRepresentation'
# pLYReader1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
pLYReader1Display.ScaleTransferFunction.Points = [0.012195363640785217, 0.0, 0.5, 0.0, 0.5833437442779541, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
pLYReader1Display.OpacityTransferFunction.Points = [0.012195363640785217, 0.0, 0.5, 0.0, 0.5833437442779541, 1.0, 0.5, 0.0]

# change solid color
pLYReader1Display.AmbientColor = [1.0, 0.6666666666666666, 0.4980392156862745]
pLYReader1Display.DiffuseColor = [1.0, 0.6666666666666666, 0.4980392156862745]

# Properties modified on pLYReader1Display
pLYReader1Display.Opacity = 0.19

# Properties modified on pLYReader1Display
pLYReader1Display.Opacity = 0.31

# find source
clip4 = FindSource('Clip4')

# hide data in view
Hide(clip4, renderView1)

# set active source
SetActiveSource(clip4)

# show data in view
clip4Display = Show(clip4, renderView1)

# get color transfer function/color map for 'PartID'
partIDLUT = GetColorTransferFunction('PartID')

# get opacity transfer function/opacity map for 'PartID'
partIDPWF = GetOpacityTransferFunction('PartID')

# trace defaults for the display properties.
clip4Display.Representation = 'Surface'
clip4Display.ColorArrayName = ['CELLS', 'Part ID']
clip4Display.LookupTable = partIDLUT
clip4Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip4Display.SelectOrientationVectors = 'None'
clip4Display.ScaleFactor = 0.015612902119755745
clip4Display.SelectScaleArray = 'None'
clip4Display.GlyphType = 'Arrow'
clip4Display.GlyphTableIndexArray = 'None'
clip4Display.GaussianRadius = 0.0007806451059877873
clip4Display.SetScaleArray = [None, '']
clip4Display.ScaleTransferFunction = 'PiecewiseFunction'
clip4Display.OpacityArray = [None, '']
clip4Display.OpacityTransferFunction = 'PiecewiseFunction'
clip4Display.DataAxesGrid = 'GridAxesRepresentation'
clip4Display.PolarAxes = 'PolarAxesRepresentation'
clip4Display.ScalarOpacityFunction = partIDPWF
clip4Display.ScalarOpacityUnitDistance = 0.011684978574366735

# show color bar/color legend
clip4Display.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(clip4, renderView1)

# show data in view
clip4Display = Show(clip4, renderView1)

# show color bar/color legend
clip4Display.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(clip4, renderView1)

# find source
clip3 = FindSource('Clip3')

# hide data in view
Hide(clip3, renderView1)

# find source
threshold1 = FindSource('Threshold1')

# hide data in view
Hide(threshold1, renderView1)

# find source
clip2 = FindSource('Clip2')

# hide data in view
Hide(clip2, renderView1)

# show data in view
clip4Display = Show(clip4, renderView1)

# show color bar/color legend
clip4Display.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(clip4, renderView1)

# set active source
SetActiveSource(clip3)

# show data in view
clip3Display = Show(clip3, renderView1)

# trace defaults for the display properties.
clip3Display.Representation = 'Surface'
clip3Display.AmbientColor = [0.0, 0.0, 1.0]
clip3Display.ColorArrayName = [None, '']
clip3Display.DiffuseColor = [0.0, 0.0, 1.0]
clip3Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip3Display.SelectOrientationVectors = 'None'
clip3Display.ScaleFactor = 0.01611562557518482
clip3Display.SelectScaleArray = 'None'
clip3Display.GlyphType = 'Arrow'
clip3Display.GlyphTableIndexArray = 'None'
clip3Display.GaussianRadius = 0.0008057812787592412
clip3Display.SetScaleArray = [None, '']
clip3Display.ScaleTransferFunction = 'PiecewiseFunction'
clip3Display.OpacityArray = [None, '']
clip3Display.OpacityTransferFunction = 'PiecewiseFunction'
clip3Display.DataAxesGrid = 'GridAxesRepresentation'
clip3Display.PolarAxes = 'PolarAxesRepresentation'
clip3Display.ScalarOpacityUnitDistance = 0.018236409827184236

# hide data in view
Hide(clip3, renderView1)

# find source
threshold2 = FindSource('Threshold2')

# set active source
SetActiveSource(threshold2)

# show data in view
threshold2Display = Show(threshold2, renderView1)

# trace defaults for the display properties.
threshold2Display.Representation = 'Surface'
threshold2Display.ColorArrayName = [None, '']
threshold2Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold2Display.SelectOrientationVectors = 'None'
threshold2Display.ScaleFactor = 0.016116880252957346
threshold2Display.SelectScaleArray = 'None'
threshold2Display.GlyphType = 'Arrow'
threshold2Display.GlyphTableIndexArray = 'None'
threshold2Display.GaussianRadius = 0.0008058440126478672
threshold2Display.SetScaleArray = [None, '']
threshold2Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold2Display.OpacityArray = [None, '']
threshold2Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold2Display.DataAxesGrid = 'GridAxesRepresentation'
threshold2Display.PolarAxes = 'PolarAxesRepresentation'
threshold2Display.ScalarOpacityUnitDistance = 0.016563881750601347

# hide data in view
Hide(threshold2, renderView1)

# set active source
SetActiveSource(threshold1)

# show data in view
threshold1Display = Show(threshold1, renderView1)

# trace defaults for the display properties.
threshold1Display.Representation = 'Surface'
threshold1Display.ColorArrayName = [None, '']
threshold1Display.Opacity = 0.14
threshold1Display.OSPRayScaleFunction = 'PiecewiseFunction'
threshold1Display.SelectOrientationVectors = 'None'
threshold1Display.ScaleFactor = 0.016796400398015977
threshold1Display.SelectScaleArray = 'None'
threshold1Display.GlyphType = 'Arrow'
threshold1Display.GlyphTableIndexArray = 'None'
threshold1Display.GaussianRadius = 0.0008398200199007988
threshold1Display.SetScaleArray = [None, '']
threshold1Display.ScaleTransferFunction = 'PiecewiseFunction'
threshold1Display.OpacityArray = [None, '']
threshold1Display.OpacityTransferFunction = 'PiecewiseFunction'
threshold1Display.DataAxesGrid = 'GridAxesRepresentation'
threshold1Display.PolarAxes = 'PolarAxesRepresentation'
threshold1Display.ScalarOpacityUnitDistance = 0.01599442273080559

# hide data in view
Hide(threshold1, renderView1)

# Properties modified on threshold1Display
threshold1Display.Opacity = 0.37

# Properties modified on threshold1Display
threshold1Display.Opacity = 0.18

# show data in view
threshold1Display = Show(threshold1, renderView1)

# Properties modified on threshold1Display
threshold1Display.Opacity = 0.4

# Properties modified on threshold1Display
threshold1Display.Opacity = 0.13

# set active source
SetActiveSource(threshold2)

# show data in view
threshold2Display = Show(threshold2, renderView1)

# Properties modified on threshold2Display
threshold2Display.Opacity = 0.29

# hide data in view
Hide(threshold2, renderView1)

# set active source
SetActiveSource(threshold1)


# Properties modified on threshold1Display
threshold1Display.Opacity = 0.34

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [-0.0030714895564439805, -0.01736261911418504, 0.6561424071548163]
renderView1.CameraFocalPoint = [-0.012276421977422462, -0.011085148657443962, -0.006955978667314148]
renderView1.CameraViewUp = [0.006835930266216789, 0.9999327217105367, 0.0093713451517863]
renderView1.CameraParallelScale = 0.1716467158339834


# save screenshot
if save_images == 1:
    SaveScreenshot('5.png', renderView1, ImageResolution=[1435, 767])
