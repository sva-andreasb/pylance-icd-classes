NODE_ADDED = "int  0"
NODE_REMOVED = "int  1"
NODE_SELECTED = "int  2"
NODE_MOVING = "int  3"
NODE_MOVED = "int  4"
RELATIONSHIP_ADDED = "int  5"
RELATIONSHIP_REMOVED = "int  6"
RELATIONSHIP_SELECTED = "int  7"
UNDOSTATE_CHANGE = "int  8"
def WorkflowEditEvent():
'''public WorkflowEditEvent(final Object source, final int type, final Workflow workflow, final WorkflowEntity entity)
'''
pass
def getType():
'''public int getType()
'''
pass
def getWorkflow():
'''public Workflow getWorkflow()
'''
pass
def getEntity():
'''public WorkflowEntity getEntity()
'''
pass
