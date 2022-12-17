REL_EXIT = "int  0"
REL_ENTER = "int  1"
def ():
    '''returns DiagramWorkflowNode\n\n
    (final WorkflowNode node, final DiagramConfiguration configuration)\n
    (final WorkflowNode node, final DiagramConfiguration configuration, final boolean inToolbar)\n
    '''
def getCursorFromImage():
    '''returns Cursor\n\n
    getCursorFromImage()\n
    '''
def setFont():
    '''returns None\n\n
    setFont(final Font font)\n
    '''
def getWorkflowNode():
    '''returns WorkflowNode\n\n
    getWorkflowNode()\n
    '''
def isSuccessorOf():
    '''returns boolean\n\n
    isSuccessorOf(final DiagramWorkflowNode dnode)\n
    '''
def connectedTo():
    '''returns boolean\n\n
    connectedTo(final DiagramWorkflowNode dnode, final boolean isNegative)\n
    '''
def addIncomingRelationship():
    '''returns None\n\n
    addIncomingRelationship(final DiagramWorkflowRelationship rel)\n
    '''
def removeIncomingRelationship():
    '''returns None\n\n
    removeIncomingRelationship(final DiagramWorkflowRelationship rel)\n
    '''
def addOutgoingRelationship():
    '''returns None\n\n
    addOutgoingRelationship(final DiagramWorkflowRelationship rel)\n
    '''
def removeOutgoingRelationship():
    '''returns None\n\n
    removeOutgoingRelationship(final DiagramWorkflowRelationship rel)\n
    '''
def getIncomingRelationships():
    '''returns Vector\n\n
    getIncomingRelationships()\n
    '''
def getRelationships():
    '''returns Vector\n\n
    getRelationships(final int type)\n
    '''
def getOutgoingRelationships():
    '''returns Vector\n\n
    getOutgoingRelationships()\n
    '''
def getRelationshipLocation():
    '''returns int\n\n
    getRelationshipLocation(final DiagramWorkflowRelationship rel, final int type)\n
    '''
def compareTo():
    '''returns int\n\n
    compareTo(final Object o)\n
    '''
def getColumn():
    '''returns int\n\n
    getColumn()\n
    '''
def getRow():
    '''returns int\n\n
    getRow()\n
    '''
def getLocation():
    '''returns Point\n\n
    getLocation()\n
    '''
def getCenterPoint():
    '''returns int\n\n
    getCenterPoint()\n
    '''
def setSelected():
    '''returns None\n\n
    setSelected(final boolean state)\n
    '''
def setBackground():
    '''returns None\n\n
    setBackground(final Color background)\n
    '''
def getSelectedForeground():
    '''returns Color\n\n
    getSelectedForeground()\n
    '''
def setSelectedForeground():
    '''returns None\n\n
    setSelectedForeground(final Color selectedForeground)\n
    '''
def getSelectedBackground():
    '''returns Color\n\n
    getSelectedBackground()\n
    '''
def setSelectedBackground():
    '''returns None\n\n
    setSelectedBackground(final Color selectedBackground)\n
    '''
def moreInomingAllowed():
    '''returns boolean\n\n
    moreInomingAllowed()\n
    '''
def moreOutgoingAllowed():
    '''returns boolean\n\n
    moreOutgoingAllowed()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def sortRelationships():
    '''returns None\n\n
    sortRelationships()\n
    '''
def isIndexUsed():
    '''returns boolean\n\n
    isIndexUsed(final int index, final int type)\n
    '''
