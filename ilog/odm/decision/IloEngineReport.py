COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
NO_STATUS = "int  -1"
FAILURE = "int  0"
SUCCESS = "int  1"
def ():
    '''returns IloEngineReport\n\n
    ()\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
def getExplainStatus():
    '''returns int\n\n
    getExplainStatus()\n
    '''
def getExplainException():
    '''returns Exception\n\n
    getExplainException()\n
    '''
def getExplanationDepth():
    '''returns int\n\n
    getExplanationDepth()\n
    '''
def isFullExplanation():
    '''returns boolean\n\n
    isFullExplanation()\n
    '''
def getSolveStatus():
    '''returns int\n\n
    getSolveStatus()\n
    '''
def getRelaxationLevel():
    '''returns IloPriority\n\n
    getRelaxationLevel()\n
    '''
def getSolveException():
    '''returns Exception\n\n
    getSolveException()\n
    '''
def setExplanationDepth():
    '''returns None\n\n
    setExplanationDepth(final int i)\n
    '''
def setExplainException():
    '''returns None\n\n
    setExplainException(final Exception exception)\n
    '''
def setExplanationStatus():
    '''returns None\n\n
    setExplanationStatus(final boolean v)\n
    '''
def setFullExplanation():
    '''returns None\n\n
    setFullExplanation(final boolean b)\n
    '''
def setRelaxationLevel():
    '''returns None\n\n
    setRelaxationLevel(final IloPriority priority)\n
    '''
def setSolveException():
    '''returns None\n\n
    setSolveException(final Exception exception)\n
    '''
def setSolveStatus():
    '''returns None\n\n
    setSolveStatus(final boolean v)\n
    '''
def print():
    '''returns IloTabulatedStream\n\n
    print(final OutputStream os)\n
    print(final IloTabulatedStream stm)\n
    '''
def setRelaxationAvailable():
    '''returns None\n\n
    setRelaxationAvailable(final boolean hasRelaxation)\n
    '''
def hasRelaxation():
    '''returns boolean\n\n
    hasRelaxation()\n
    '''
