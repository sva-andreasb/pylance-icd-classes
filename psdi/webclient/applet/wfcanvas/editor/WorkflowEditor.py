def WorkflowEditor():
    '''public WorkflowEditor()
    public WorkflowEditor(final Workflow workflow)
    '''
def setEditable():
    '''public void setEditable(final boolean editable)
    '''
def getTimestamp():
    '''public int getTimestamp()
    '''
def hasUndoEntries():
    '''public boolean hasUndoEntries()
    '''
def undo():
    '''public boolean undo()
    '''
def getTopTimestamp():
    '''public int getTopTimestamp()
    '''
def addWorkflowEditListener():
    '''public void addWorkflowEditListener(final WorkflowEditListener listener)
    '''
def removeWorkflowEditListener():
    '''public void removeWorkflowEditListener(final WorkflowEditListener listener)
    '''
def setSelected():
    '''public void setSelected(final WorkflowEntity selection, final boolean user)
    '''
def getSelected():
    '''public WorkflowEntity getSelected()
    '''
def add():
    '''public void add(final WorkflowEntity entity)
    '''
def delete():
    '''public void delete()
    public void delete(final WorkflowEntity entity)
    '''
def move():
    '''public void move(final int column, final int row)
    public void move(final WorkflowEntity entity, final int column, final int row)
    '''
def hasChanges():
    '''public boolean hasChanges()
    '''
def clearChanges():
    '''public void clearChanges()
    '''
