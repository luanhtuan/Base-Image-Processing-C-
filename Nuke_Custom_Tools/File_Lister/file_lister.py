# --------------------------------------------------------------
#  filepathLister.py
#  Version: 1.0.1
#  Author: Lu Anh Tuan
#
#  Last Modified by: Lu Anh Tuan
#  Last Updated: June 3rd, 2019
# --------------------------------------------------------------

# --------------------------------------------------------------
#  USAGE:
#
#  - List all files being read into a nuke script.
# --------------------------------------------------------------

# Import modules

import os
import nuke

def file_lister():

    script_name = os.path.basename(nuke.root()['name'].value())
    output_file = open("Dir:\somewhere\somewhere\ "+script_name+"_list_comp_output.txt", "w+")
    
    output_file.write("Nuke_script: "+script_name)
    output_file.write("\n\nFile & Version List:\n")
    
    
    node_name = ["Read", "ReadGeo", "Camera"]
    node_list = []
    
    for i in nuke.allNodes():
        for x in node_name:
            if i.knob("file") and i.Class() == x:
               node_list.append(i)
    
    
    for node in node_list:
        filePath = node["file"].value()
        fileName = os.path.basename(filePath)
    
        file_Name = fileName[0:fileName.find('_v')]
        file_Version = fileName[fileName.find('_v')+1:fileName.find('_v')+6]
    
        output_file.write("\nYou are using "+file_Version+" of "+file_Name)
    
    #out_file.close()

nuke.menu('Nuke').addCommand('Viewer/View_fileList', 'file_lister.file_lister()', ' ')
