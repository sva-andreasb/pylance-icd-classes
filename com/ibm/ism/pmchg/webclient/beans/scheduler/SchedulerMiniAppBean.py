def SchedulerMiniAppBean():
'''public SchedulerMiniAppBean()
'''
pass
def onReset():
'''public void onReset()
'''
pass
def filterCss():
'''public String filterCss(String css, final MiniAppControl control)
'''
pass
def setupBean():
'''public void setupBean(final WebClientSession wcs)
'''
pass
def getApplicationResource():
'''public String getApplicationResource(final String path)
'''
pass
def loadTasks():
'''public String loadTasks(@MXEventParam("startDateMillis") final long startDateMillis, @MXEventParam("endDateMillis") final long endDateMillis)
'''
pass
def findAvailableTimes():
'''public String findAvailableTimes(@MXEventParam("startDateMillis") final long startDateMillis, @MXEventParam("endDateMillis") final long endDateMillis, @MXEventParam("jsonString") final String jsonString)
'''
pass
def saveSchedule():
'''public String saveSchedule(@MXEventParam("jsonString") final String jsonString)
'''
pass
def calculateSchedule():
'''public String calculateSchedule(@MXEventParam("startDateMillis") final long startDateMillis, @MXEventParam("jsonString") final String jsonString)
'''
pass
def findChangeSchedulableDates():
'''public String findChangeSchedulableDates(@MXEventParam("startDateMillis") final long startDateMillis, @MXEventParam("endDateMillis") final long endDateMillis, @MXEventParam("jsonString") final String jsonString)
'''
pass
def getTaskScheduledDates():
'''public String getTaskScheduledDates(@MXEventParam("jsonString") final String jsonString)
'''
pass
def getMessages():
'''public String getMessages(@MXEventParam("msgGroup") final String msgGroup)
'''
pass
def getLangCode():
'''public String getLangCode()
'''
pass
def getTimeZone():
'''public String getTimeZone()
'''
pass
def dialogclose():
'''public int dialogclose()
'''
pass
