COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def onSearchFeasibleSolution():
    '''returns boolean\n\n
    onSearchFeasibleSolution(final String model, final IloPriority maxRelaxablePriorityLevel, final Collection<?> relaxblesRanges, final boolean isHighestPriority)\n
    '''
def onSearchOptimalSolution():
    '''returns boolean\n\n
    onSearchOptimalSolution(final String model, final IloPriority maxRelaxablePriorityLevel)\n
    '''
def main():
    '''returns boolean\n\n
    main(final IloCplexCallbackInfo state)\n
    '''
def enginePhaseChanged():
    '''returns None\n\n
    enginePhaseChanged(final IloEnginePhase phase)\n
    '''
def onBuildModel():
    '''returns boolean\n\n
    onBuildModel(final String modelingType, final String model, final String label)\n
    '''
def onPublishSolution():
    '''returns boolean\n\n
    onPublishSolution(final String publicationType, final String model, final String label)\n
    '''
def mustAbort():
    '''returns boolean\n\n
    mustAbort()\n
    '''
