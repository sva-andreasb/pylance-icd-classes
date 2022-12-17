def ():
    '''returns PmChgSchedulerControl\n\n
    (final long constFlags, final int numberOfDays, final int contigInterval)\n
    '''
def findAvailableTimes():
    '''returns None\n\n
    findAvailableTimes(final MboRemote changeMbo, final Date startDate, final Date endDate, final Map<String, PmChgSchedulerTaskInfo> tasksInfoMap)\n
    '''
def saveSchedule():
    '''returns None\n\n
    saveSchedule(final MboRemote changeMbo, final Map<String, PmChgSchedulerTaskInfo> tasksInfoMap)\n
    '''
def calculateSchedule():
    '''returns None\n\n
    calculateSchedule(final MboRemote changeMbo, final Date startDate, final Map<String, PmChgSchedulerTaskInfo> tasksInfoMap)\n
    '''
def findChangeSchedulableDates():
    '''returns List<String>\n\n
    findChangeSchedulableDates(final MboRemote changeMbo, final Date startDate, final Date endDate, final Map<String, PmChgSchedulerTaskInfo> tasksInfoMap, final TimeZone clientTZ, final TimeZone serverTZ)\n
    '''
def getTaskScheduledDates():
    '''returns List<String>\n\n
    getTaskScheduledDates(final MboRemote changeMbo, final Map<String, PmChgSchedulerTaskInfo> tasksInfoMap, final TimeZone tz)\n
    '''
def updateActivitiesStartFinishDates():
    '''returns None\n\n
    updateActivitiesStartFinishDates(final Map<String, PmChgSchedulerTaskInfo> tasksInfoMap)\n
    '''
