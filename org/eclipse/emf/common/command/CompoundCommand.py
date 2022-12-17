LAST_COMMAND_ALL = "int  Integer.MIN_VALUE"
MERGE_COMMAND_ALL = "int  Integer.MAX_VALUE"
def ():
    '''returns CompoundCommand\n\n
    ()\n
    (final String label)\n
    (final String label, final String description)\n
    (final List commandList)\n
    (final String label, final List commandList)\n
    (final String label, final String description, final List commandList)\n
    (final int resultIndex)\n
    (final int resultIndex, final String label)\n
    (final int resultIndex, final String label, final String description)\n
    (final int resultIndex, final List commandList)\n
    (final int resultIndex, final String label, final List commandList)\n
    (final int resultIndex, final String label, final String description, final List commandList)\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty()\n
    '''
def getCommandList():
    '''returns List\n\n
    getCommandList()\n
    '''
def getResultIndex():
    '''returns int\n\n
    getResultIndex()\n
    '''
def execute():
    '''returns None\n\n
    execute()\n
    '''
def canUndo():
    '''returns boolean\n\n
    canUndo()\n
    '''
def undo():
    '''returns None\n\n
    undo()\n
    '''
def redo():
    '''returns None\n\n
    redo()\n
    '''
def getResult():
    '''returns Collection\n\n
    getResult()\n
    '''
def getAffectedObjects():
    '''returns Collection\n\n
    getAffectedObjects()\n
    '''
def getLabel():
    '''returns String\n\n
    getLabel()\n
    '''
def getDescription():
    '''returns String\n\n
    getDescription()\n
    '''
def append():
    '''returns None\n\n
    append(final Command command)\n
    '''
def appendAndExecute():
    '''returns boolean\n\n
    appendAndExecute(final Command command)\n
    '''
def appendIfCanExecute():
    '''returns boolean\n\n
    appendIfCanExecute(final Command command)\n
    '''
def dispose():
    '''returns None\n\n
    dispose()\n
    '''
def unwrap():
    '''returns Command\n\n
    unwrap()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
