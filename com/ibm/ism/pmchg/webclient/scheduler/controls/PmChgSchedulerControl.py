def PmChgSchedulerControl():
'''public PmChgSchedulerControl(final long constFlags, final int numberOfDays, final int contigInterval)
'''
pass
def getChildren():
'''public Map<String, PmChgSchedulerTaskInfo> getChildren(final MboRemote changeMbo)
'''
pass
def loadTasks():
'''public Map<String, PmChgSchedulerTaskInfo> loadTasks(final MboRemote changeMbo, final Date startDate, final Date endDate)
'''
pass
def findAvailableTimes():
'''public void findAvailableTimes(final MboRemote changeMbo, final Date startDate, final Date endDate, final Map<String, PmChgSchedulerTaskInfo> tasksInfoMap)
'''
pass
def saveSchedule():
'''public void saveSchedule(final MboRemote changeMbo, final Map<String, PmChgSchedulerTaskInfo> tasksInfoMap)
'''
pass
def calculateSchedule():
'''public void calculateSchedule(final MboRemote changeMbo, final Date startDate, final Map<String, PmChgSchedulerTaskInfo> tasksInfoMap)
'''
pass
def findChangeSchedulableDates():
'''public List<String> findChangeSchedulableDates(final MboRemote changeMbo, final Date startDate, final Date endDate, final Map<String, PmChgSchedulerTaskInfo> tasksInfoMap, final TimeZone clientTZ, final TimeZone serverTZ)
'''
pass
def getTaskScheduledDates():
'''public List<String> getTaskScheduledDates(final MboRemote changeMbo, final Map<String, PmChgSchedulerTaskInfo> tasksInfoMap, final TimeZone tz)
'''
pass
def getMessages():
'''public Map<String, String> getMessages(final MboRemote mbo, final String msgGroup)
'''
pass
def updateActivitiesStartFinishDates():
'''public void updateActivitiesStartFinishDates(final Map<String, PmChgSchedulerTaskInfo> tasksInfoMap)
'''
pass
