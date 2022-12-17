def ():
    '''returns BasicCommandStack\n\n
    ()\n
    '''
def execute():
    '''returns None\n\n
    execute(final Command command)\n
    '''
def canUndo():
    '''returns boolean\n\n
    canUndo()\n
    '''
def undo():
    '''returns None\n\n
    undo()\n
    '''
def canRedo():
    '''returns boolean\n\n
    canRedo()\n
    '''
def redo():
    '''returns None\n\n
    redo()\n
    '''
def flush():
    '''returns None\n\n
    flush()\n
    '''
def getUndoCommand():
    '''returns Command\n\n
    getUndoCommand()\n
    '''
def getRedoCommand():
    '''returns Command\n\n
    getRedoCommand()\n
    '''
def getMostRecentCommand():
    '''returns Command\n\n
    getMostRecentCommand()\n
    '''
def addCommandStackListener():
    '''returns None\n\n
    addCommandStackListener(final CommandStackListener listener)\n
    '''
def removeCommandStackListener():
    '''returns None\n\n
    removeCommandStackListener(final CommandStackListener listener)\n
    '''
def saveIsDone():
    '''returns None\n\n
    saveIsDone()\n
    '''
def isSaveNeeded():
    '''returns boolean\n\n
    isSaveNeeded()\n
    '''
