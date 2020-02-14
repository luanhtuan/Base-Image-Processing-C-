
def nodeCopy_Pasted():

    for i in nuke.selectedNodes():
        i.setSelected(True)
        nuke.nodePaste("%clipboard%")

nodeCopy_Pasted()
