# head-model-paraview-scripts

Python Paraview scripts to make images based on vtk files downloaded from nsfcareer.io

# To Run:

pvpython make-images.py

Note, I have an alias set up for pvpython in my .bashrc file. E.g,
alias paraview="/cygdrive/c/Program\ Files/ParaView\ 5.8.1-RC1-Windows-Python3.7-msvc2015-64bit/bin/paraview.exe"
alias pvpython="/cygdrive/c/Program\ Files/ParaView\ 5.8.1-RC1-Windows-Python3.7-msvc2015-64bit/bin/pvpython.exe"

# Things to change in the python folder before running

## Enter folder id that is downloaded from nsfcareer

folder_id = 1595511788889

## If you want to save images to local directory, 1= save, 0= don't save

save_images = 1

## modify the paths (user name and download location)

read_path_brain = 'C:\\Users\\rhk12\\Downloads\\%s (1)\\' % folder_id
read_ply = 'C:\\Users\\rhk12\\Downloads\\%s\\avatars\\\*\\face\\model.ply' % folder_id
