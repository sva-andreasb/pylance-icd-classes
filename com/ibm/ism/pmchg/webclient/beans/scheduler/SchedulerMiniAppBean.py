def ():
    '''returns SchedulerMiniAppBean\n\n
    ()\n
    '''
def onReset():
    '''returns None\n\n
    onReset()\n
    '''
def filterCss():
    '''returns String\n\n
    filterCss(String css, final MiniAppControl control)\n
    '''
def setupBean():
    '''returns None\n\n
    setupBean(final WebClientSession wcs)\n
    '''
def getApplicationResource():
    '''returns String\n\n
    getApplicationResource(final String path)\n
    '''
def loadTasks():
    '''returns String\n\n
    loadTasks(@MXEventParam("startDateMillis") final long startDateMillis, @MXEventParam("endDateMillis") final long endDateMillis)\n
    '''
def findAvailableTimes():
    '''returns String\n\n
    findAvailableTimes(@MXEventParam("startDateMillis") final long startDateMillis, @MXEventParam("endDateMillis") final long endDateMillis, @MXEventParam("jsonString") final String jsonString)\n
    '''
def saveSchedule():
    '''returns String\n\n
    saveSchedule(@MXEventParam("jsonString") final String jsonString)\n
    '''
def calculateSchedule():
    '''returns String\n\n
    calculateSchedule(@MXEventParam("startDateMillis") final long startDateMillis, @MXEventParam("jsonString") final String jsonString)\n
    '''
def findChangeSchedulableDates():
    '''returns String\n\n
    findChangeSchedulableDates(@MXEventParam("startDateMillis") final long startDateMillis, @MXEventParam("endDateMillis") final long endDateMillis, @MXEventParam("jsonString") final String jsonString)\n
    '''
def getTaskScheduledDates():
    '''returns String\n\n
    getTaskScheduledDates(@MXEventParam("jsonString") final String jsonString)\n
    '''
def getMessages():
    '''returns String\n\n
    getMessages(@MXEventParam("msgGroup") final String msgGroup)\n
    '''
def getLangCode():
    '''returns String\n\n
    getLangCode()\n
    '''
def getTimeZone():
    '''returns String\n\n
    getTimeZone()\n
    '''
def dialogclose():
    '''returns int\n\n
    dialogclose()\n
    '''
