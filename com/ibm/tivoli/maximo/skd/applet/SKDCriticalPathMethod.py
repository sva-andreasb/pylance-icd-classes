def ():
    '''returns SKDCriticalPathMethod\n\n
    (final IlvGanttModel model)\n
    '''
def setModel():
    '''returns None\n\n
    setModel(final IlvGanttModel model)\n
    '''
def setProjectStart():
    '''returns None\n\n
    setProjectStart(final Date projectStart)\n
    '''
def getProjectStart():
    '''returns Date\n\n
    getProjectStart()\n
    '''
def setCriticalThreshold():
    '''returns None\n\n
    setCriticalThreshold(final IlvDuration ilvduration)\n
    '''
def computeSchedule():
    '''returns None\n\n
    computeSchedule()\n
    computeSchedule(final IlvActivity[] selectedActivities)\n
    '''
def computeEarlyStartAndFinish():
    '''returns None\n\n
    computeEarlyStartAndFinish(final IlvActivity activity)\n
    '''
def computeLateStartAndFinish():
    '''returns None\n\n
    computeLateStartAndFinish(final IlvActivity activity)\n
    computeLateStartAndFinish(final IlvActivity activity, final Date parentLatestFinish)\n
    '''
def computeFloat():
    '''returns None\n\n
    computeFloat(final IlvActivity activity)\n
    '''
