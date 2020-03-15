import nuke

def AutoReNameReadNode():

    for ReadNode in nuke.selectedNodes():
        ReadName = ReadNode["file"].value()
        NewReadName = ReadName.rsplit('-', 1)[-1]
        ReadNode["name"].setValue(NewReadName)
        ReadNode["label"].setValue(NewReadName)


nuke.menu('Nuke').addCommand('[LuAnhTuan]/RenameReadNode', 'AuToReNameReadNode.AutoReNameReadNode()', 'ctrl+a')
