
# --------------------------------------------------------------
#  SetFrameExpression.py
#  Version: 1.0.1
#  Author: Lu Anh Tuan
#
#  Last Modified by: Lu Anh Tuan
#  Last Updated: June 25th, 2019
# --------------------------------------------------------------

# --------------------------------------------------------------
#  USAGE:
#
#  set frame expression from Read-Node would you like to create!
# --------------------------------------------------------------


import nuke

def Start_Frame():

    panel = nuke.Panel("Frame__Start")
    panel.addSingleLineInput("Frame_Name", "frame: start at:")
    panel.addSingleLineInput("Number_Frame", "")

    if not panel.show():
        return

    KnobName = panel.value("Frame_Name")
    KnobNumber = panel.value("Number_Frame")

    # callback the knobname from Read  
    for i in nuke.allNodes("Read"):
        i.knob("frame_mode").setValue(1)
        i.knob("frame").setValue(KnobNumber)
        
    # check if user-input data if number of node to create is actually a number!
    try:
       int(KnobNumber)
    except:
       nuke.message("Please enter a number, not text, for amount of "+KnobName+" nodes!....")


utilitiesMenu = nuke.menu('Nuke').addMenu('[LuAnhTuan]')

utilitiesMenu.addCommand('SetReadNode_Frame_Expression', "SetFrameExpression.Start_Frame()")
