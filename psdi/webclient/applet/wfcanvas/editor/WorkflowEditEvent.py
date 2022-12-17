NODE_ADDED = "int  0"
NODE_REMOVED = "int  1"
NODE_SELECTED = "int  2"
NODE_MOVING = "int  3"
NODE_MOVED = "int  4"
RELATIONSHIP_ADDED = "int  5"
RELATIONSHIP_REMOVED = "int  6"
RELATIONSHIP_SELECTED = "int  7"
UNDOSTATE_CHANGE = "int  8"
def ():
    '''returns WorkflowEditEvent\n\n
    (final Object source, final int type, final Workflow workflow, final WorkflowEntity entity)\n
    '''
def getType():
    '''returns int\n\n
    getType()\n
    '''
def getWorkflow():
    '''returns Workflow\n\n
    getWorkflow()\n
    '''
def getEntity():
    '''returns WorkflowEntity\n\n
    getEntity()\n
    '''
