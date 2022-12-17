COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def addPhaseListener():
    '''returns None\n\n
    addPhaseListener(final IloEnginePhaseListener listener)\n
    '''
def removeListener():
    '''returns boolean\n\n
    removeListener(final IloEnginePhaseListener listener)\n
    '''
def addSolveAnywayCallback():
    '''returns None\n\n
    addSolveAnywayCallback(final IloSolveAnywayCallback cb)\n
    '''
def removeSolveAnywayCallback():
    '''returns boolean\n\n
    removeSolveAnywayCallback(final IloSolveAnywayCallback cb)\n
    '''
def searchFeasibleSolutionEvent():
    '''returns boolean\n\n
    searchFeasibleSolutionEvent(final String model, final IloPriority maxRelaxablePriorityLevel, final Collection<?> relaxblesRanges, final boolean isHighestPriority)\n
    '''
def searchOptimalSolutionEvent():
    '''returns boolean\n\n
    searchOptimalSolutionEvent(final String model, final IloPriority maxRelaxablePriorityLevel, final Collection<?> relaxblesRanges)\n
    '''
def setPhase():
    '''returns None\n\n
    setPhase(final IloEnginePhase phase)\n
    '''
def buildModelEvent():
    '''returns boolean\n\n
    buildModelEvent(final String modelingType, final String model, final String label)\n
    '''
def publishSolutionEvent():
    '''returns boolean\n\n
    publishSolutionEvent(final String publicationType, final String modelName, final String label)\n
    '''
def getController():
    '''returns IloConcertController\n\n
    getController()\n
    '''
def end():
    '''returns None\n\n
    end()\n
    '''
