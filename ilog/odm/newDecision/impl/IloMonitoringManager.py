COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns IloMonitoringManager\n\n
    ()\n
    '''
def addEngineListener():
    '''returns None\n\n
    addEngineListener(final IloIntermediateResultListener i)\n
    '''
def goalUpdateHappened():
    '''returns None\n\n
    goalUpdateHappened(final boolean hasSolution, final IloGoalReport goalReport, final long timeMilli)\n
    '''
def resultUpdateHappened():
    '''returns None\n\n
    resultUpdateHappened(final boolean hasSolution, final IloGoalReport goalReport, final long timeMilli)\n
    '''
def enginePhaseChanged():
    '''returns None\n\n
    enginePhaseChanged(final IloEnginePhase newPhase)\n
    '''
