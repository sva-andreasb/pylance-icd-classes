DEFAULT_EARLIEST_START_PROPERTY = "String  \"earliestStart\""
DEFAULT_EARLIEST_FINISH_PROPERTY = "String  \"earliestFinish\""
DEFAULT_LATEST_START_PROPERTY = "String  \"latestStart\""
DEFAULT_LATEST_FINISH_PROPERTY = "String  \"latestFinish\""
DEFAULT_TOTAL_SLACK_PROPERTY = "String  \"totalSlack\""
DEFAULT_CRITICAL_PROPERTY = "String  \"critical\""
def ():
    '''returns IlvGanttModelScheduler\n\n
    ()\n
    (final IlvGanttModel ganttModel)\n
    '''
def getGanttModel():
    '''returns IlvGanttModel\n\n
    getGanttModel()\n
    '''
def setGanttModel():
    '''returns None\n\n
    setGanttModel(final IlvGanttModel ganttModel)\n
    '''
def getProjectStart():
    '''returns Date\n\n
    getProjectStart()\n
    '''
def setProjectStart():
    '''returns None\n\n
    setProjectStart(final Date date)\n
    '''
def getCriticalThreshold():
    '''returns IlvDuration\n\n
    getCriticalThreshold()\n
    '''
def setCriticalThreshold():
    '''returns None\n\n
    setCriticalThreshold(final IlvDuration criticalThreshold)\n
    '''
def getEarliestStartProperty():
    '''returns String\n\n
    getEarliestStartProperty()\n
    '''
def setEarliestStartProperty():
    '''returns None\n\n
    setEarliestStartProperty(final String earliestStartProperty)\n
    '''
def getEarliestFinishProperty():
    '''returns String\n\n
    getEarliestFinishProperty()\n
    '''
def setEarliestFinishProperty():
    '''returns None\n\n
    setEarliestFinishProperty(final String earliestFinishProperty)\n
    '''
def getLatestStartProperty():
    '''returns String\n\n
    getLatestStartProperty()\n
    '''
def setLatestStartProperty():
    '''returns None\n\n
    setLatestStartProperty(final String latestStartProperty)\n
    '''
def getLatestFinishProperty():
    '''returns String\n\n
    getLatestFinishProperty()\n
    '''
def setLatestFinishProperty():
    '''returns None\n\n
    setLatestFinishProperty(final String latestFinishProperty)\n
    '''
def getTotalSlackProperty():
    '''returns String\n\n
    getTotalSlackProperty()\n
    '''
def setTotalSlackProperty():
    '''returns None\n\n
    setTotalSlackProperty(final String totalSlackProperty)\n
    '''
def getCriticalProperty():
    '''returns String\n\n
    getCriticalProperty()\n
    '''
def setCriticalProperty():
    '''returns None\n\n
    setCriticalProperty(final String criticalProperty)\n
    '''
def isScheduling():
    '''returns boolean\n\n
    isScheduling()\n
    '''
def beginSchedulingSession():
    '''returns None\n\n
    beginSchedulingSession()\n
    '''
def endSchedulingSession():
    '''returns None\n\n
    endSchedulingSession()\n
    '''
def schedule():
    '''returns None\n\n
    schedule()\n
    '''
def isAutoScheduling():
    '''returns boolean\n\n
    isAutoScheduling()\n
    '''
def setAutoScheduling():
    '''returns None\n\n
    setAutoScheduling(final boolean b)\n
    '''
def getErrorHandler():
    '''returns ErrorHandler\n\n
    getErrorHandler()\n
    '''
def setErrorHandler():
    '''returns None\n\n
    setErrorHandler(final ErrorHandler e)\n
    '''
def addCriticalPathListener():
    '''returns None\n\n
    addCriticalPathListener(final CriticalPathListener criticalPathListener)\n
    '''
def removeCriticalPathListener():
    '''returns None\n\n
    removeCriticalPathListener(final CriticalPathListener criticalPathListener)\n
    '''
def error():
    '''returns None\n\n
    error(final IlvConstraintCycleException ex, final IlvGanttModel ilvGanttModel)\n
    '''
def propertyChanged():
    '''returns None\n\n
    propertyChanged(final GanttModelPropertyEvent ganttModelPropertyEvent)\n
    '''
def activityChanged():
    '''returns None\n\n
    activityChanged(final ActivityEvent activityEvent)\n
    '''
def activitiesInserted():
    '''returns None\n\n
    activitiesInserted(final ActivitiesInsertedEvent activitiesInsertedEvent)\n
    '''
def activitiesRemoved():
    '''returns None\n\n
    activitiesRemoved(final ActivitiesRemovedEvent activitiesRemovedEvent)\n
    '''
def activityMoved():
    '''returns None\n\n
    activityMoved(final ActivityMovedEvent activityMovedEvent)\n
    '''
def constraintChanged():
    '''returns None\n\n
    constraintChanged(final ConstraintEvent constraintEvent)\n
    '''
