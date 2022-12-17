def ():
    '''returns WorkflowEditor\n\n
    ()\n
    (final Workflow workflow)\n
    '''
def setEditable():
    '''returns None\n\n
    setEditable(final boolean editable)\n
    '''
def getTimestamp():
    '''returns int\n\n
    getTimestamp()\n
    '''
def hasUndoEntries():
    '''returns boolean\n\n
    hasUndoEntries()\n
    '''
def undo():
    '''returns boolean\n\n
    undo()\n
    '''
def getTopTimestamp():
    '''returns int\n\n
    getTopTimestamp()\n
    '''
def addWorkflowEditListener():
    '''returns None\n\n
    addWorkflowEditListener(final WorkflowEditListener listener)\n
    '''
def removeWorkflowEditListener():
    '''returns None\n\n
    removeWorkflowEditListener(final WorkflowEditListener listener)\n
    '''
def setSelected():
    '''returns None\n\n
    setSelected(final WorkflowEntity selection, final boolean user)\n
    '''
def getSelected():
    '''returns WorkflowEntity\n\n
    getSelected()\n
    '''
def add():
    '''returns None\n\n
    add(final WorkflowEntity entity)\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    delete(final WorkflowEntity entity)\n
    '''
def move():
    '''returns None\n\n
    move(final int column, final int row)\n
    move(final WorkflowEntity entity, final int column, final int row)\n
    '''
def hasChanges():
    '''returns boolean\n\n
    hasChanges()\n
    '''
def clearChanges():
    '''returns None\n\n
    clearChanges()\n
    '''
