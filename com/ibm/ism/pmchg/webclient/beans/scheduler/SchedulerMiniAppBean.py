def SchedulerMiniAppBean():
    '''public SchedulerMiniAppBean()
    '''
def onReset():
    '''public void onReset()
    '''
def filterCss():
    '''public String filterCss(String css, final MiniAppControl control)
    '''
def setupBean():
    '''public void setupBean(final WebClientSession wcs)
    '''
def getApplicationResource():
    '''public String getApplicationResource(final String path)
    '''
def loadTasks():
    '''public String loadTasks(@MXEventParam("startDateMillis") final long startDateMillis, @MXEventParam("endDateMillis") final long endDateMillis)
    '''
def findAvailableTimes():
    '''public String findAvailableTimes(@MXEventParam("startDateMillis") final long startDateMillis, @MXEventParam("endDateMillis") final long endDateMillis, @MXEventParam("jsonString") final String jsonString)
    '''
def saveSchedule():
    '''public String saveSchedule(@MXEventParam("jsonString") final String jsonString)
    '''
def calculateSchedule():
    '''public String calculateSchedule(@MXEventParam("startDateMillis") final long startDateMillis, @MXEventParam("jsonString") final String jsonString)
    '''
def findChangeSchedulableDates():
    '''public String findChangeSchedulableDates(@MXEventParam("startDateMillis") final long startDateMillis, @MXEventParam("endDateMillis") final long endDateMillis, @MXEventParam("jsonString") final String jsonString)
    '''
def getTaskScheduledDates():
    '''public String getTaskScheduledDates(@MXEventParam("jsonString") final String jsonString)
    '''
def getMessages():
    '''public String getMessages(@MXEventParam("msgGroup") final String msgGroup)
    '''
def getLangCode():
    '''public String getLangCode()
    '''
def getTimeZone():
    '''public String getTimeZone()
    '''
def dialogclose():
    '''public int dialogclose()
    '''
