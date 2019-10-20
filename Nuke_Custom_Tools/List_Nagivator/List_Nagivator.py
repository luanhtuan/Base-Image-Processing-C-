def list_Nagivator():

    node_list = []
    for i in nuke.selectedNodes():
        node_list.append(i.name())
    
    node_list.sort()
    print"NODE NAME LIST: \n"

    for i in node_list:
        print"• " +i

    nuke.message("There are "+str(len(node_list))+" in the list.\n\nThe first node in the list"+node_list[0]+"\nThe last node in the list"+node_list[-1]+" ")

list_Nagivator()
