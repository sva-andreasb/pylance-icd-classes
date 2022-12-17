DEFAULT_EARLIEST_START_PROPERTY = "String  \"earliestStart\""
DEFAULT_EARLIEST_FINISH_PROPERTY = "String  \"earliestFinish\""
DEFAULT_LATEST_START_PROPERTY = "String  \"latestStart\""
DEFAULT_LATEST_FINISH_PROPERTY = "String  \"latestFinish\""
DEFAULT_TOTAL_SLACK_PROPERTY = "String  \"totalSlack\""
DEFAULT_CRITICAL_PROPERTY = "String  \"critical\""
def ():
    '''returns IlvCriticalPathCalculator\n\n
    ()\n
    (final IlvGanttModel ganttModel)\n
    '''
def getGanttModel():
    '''returns IlvGanttModel\n\n
    getGanttModel()\n
    '''
def setGanttModel():
    '''returns None\n\n
    setGanttModel(final IlvGanttModel b)\n
    '''
def getProjectStart():
    '''returns Date\n\n
    getProjectStart()\n
    '''
def setProjectStart():
    '''returns None\n\n
    setProjectStart(final Date d)\n
    '''
def getCriticalThreshold():
    '''returns IlvDuration\n\n
    getCriticalThreshold()\n
    '''
def setCriticalThreshold():
    '''returns None\n\n
    setCriticalThreshold(final IlvDuration c)\n
    '''
def getEarliestStartProperty():
    '''returns String\n\n
    getEarliestStartProperty()\n
    '''
def setEarliestStartProperty():
    '''returns None\n\n
    setEarliestStartProperty(final String m)\n
    '''
def getEarliestFinishProperty():
    '''returns String\n\n
    getEarliestFinishProperty()\n
    '''
def setEarliestFinishProperty():
    '''returns None\n\n
    setEarliestFinishProperty(final String n)\n
    '''
def getLatestStartProperty():
    '''returns String\n\n
    getLatestStartProperty()\n
    '''
def setLatestStartProperty():
    '''returns None\n\n
    setLatestStartProperty(final String o)\n
    '''
def getLatestFinishProperty():
    '''returns String\n\n
    getLatestFinishProperty()\n
    '''
def setLatestFinishProperty():
    '''returns None\n\n
    setLatestFinishProperty(final String p)\n
    '''
def getTotalSlackProperty():
    '''returns String\n\n
    getTotalSlackProperty()\n
    '''
def setTotalSlackProperty():
    '''returns None\n\n
    setTotalSlackProperty(final String q)\n
    '''
def getCriticalProperty():
    '''returns String\n\n
    getCriticalProperty()\n
    '''
def setCriticalProperty():
    '''returns None\n\n
    setCriticalProperty(final String r)\n
    '''
def computeSchedule():
    '''returns None\n\n
    computeSchedule()\n
    '''
def addCriticalPathListener():
    '''returns None\n\n
    addCriticalPathListener(final CriticalPathListener criticalPathListener)\n
    '''
def removeCriticalPathListener():
    '''returns None\n\n
    removeCriticalPathListener(final CriticalPathListener criticalPathListener)\n
    '''
