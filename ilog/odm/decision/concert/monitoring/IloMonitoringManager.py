COPYRIGHT_NOTICE = "String  Copyright IBM Corporation 2005,2012""
def addPhaseListener():
'''public void addPhaseListener(final IloEnginePhaseListener listener)
'''
pass
def removeListener():
'''public boolean removeListener(final IloEnginePhaseListener listener)
'''
pass
def addSolveAnywayCallback():
'''public void addSolveAnywayCallback(final IloSolveAnywayCallback cb)
'''
pass
def removeSolveAnywayCallback():
'''public boolean removeSolveAnywayCallback(final IloSolveAnywayCallback cb)
'''
pass
def searchFeasibleSolutionEvent():
'''public boolean searchFeasibleSolutionEvent(final String model, final IloPriority maxRelaxablePriorityLevel, final Collection<?> relaxblesRanges, final boolean isHighestPriority)
'''
pass
def searchOptimalSolutionEvent():
'''public boolean searchOptimalSolutionEvent(final String model, final IloPriority maxRelaxablePriorityLevel, final Collection<?> relaxblesRanges)
'''
pass
def setPhase():
'''public void setPhase(final IloEnginePhase phase)
'''
pass
def buildModelEvent():
'''public boolean buildModelEvent(final String modelingType, final String model, final String label)
'''
pass
def publishSolutionEvent():
'''public boolean publishSolutionEvent(final String publicationType, final String modelName, final String label)
'''
pass
def getController():
'''public IloConcertController getController()
'''
pass
def end():
'''public void end()
'''
pass
