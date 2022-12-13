COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def addPhaseListener():
    '''public void addPhaseListener(final IloEnginePhaseListener listener)
    '''
def removeListener():
    '''public boolean removeListener(final IloEnginePhaseListener listener)
    '''
def addSolveAnywayCallback():
    '''public void addSolveAnywayCallback(final IloSolveAnywayCallback cb)
    '''
def removeSolveAnywayCallback():
    '''public boolean removeSolveAnywayCallback(final IloSolveAnywayCallback cb)
    '''
def searchFeasibleSolutionEvent():
    '''public boolean searchFeasibleSolutionEvent(final String model, final IloPriority maxRelaxablePriorityLevel, final Collection<?> relaxblesRanges, final boolean isHighestPriority)
    '''
def searchOptimalSolutionEvent():
    '''public boolean searchOptimalSolutionEvent(final String model, final IloPriority maxRelaxablePriorityLevel, final Collection<?> relaxblesRanges)
    '''
def setPhase():
    '''public void setPhase(final IloEnginePhase phase)
    '''
def buildModelEvent():
    '''public boolean buildModelEvent(final String modelingType, final String model, final String label)
    '''
def publishSolutionEvent():
    '''public boolean publishSolutionEvent(final String publicationType, final String modelName, final String label)
    '''
def getController():
    '''public IloConcertController getController()
    '''
def end():
    '''public void end()
    '''
