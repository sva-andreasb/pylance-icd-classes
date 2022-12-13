def PmChgSchedulerControl():
    '''    public PmChgSchedulerControl(final long constFlags, final int numberOfDays, final int contigInterval)
    '''
def getChildren():
    '''    public Map<String, PmChgSchedulerTaskInfo> getChildren(final MboRemote changeMbo)
    '''
def loadTasks():
    '''    public Map<String, PmChgSchedulerTaskInfo> loadTasks(final MboRemote changeMbo, final Date startDate, final Date endDate)
    '''
def findAvailableTimes():
    '''    public void findAvailableTimes(final MboRemote changeMbo, final Date startDate, final Date endDate, final Map<String, PmChgSchedulerTaskInfo> tasksInfoMap)
    '''
def saveSchedule():
    '''    public void saveSchedule(final MboRemote changeMbo, final Map<String, PmChgSchedulerTaskInfo> tasksInfoMap)
    '''
def calculateSchedule():
    '''    public void calculateSchedule(final MboRemote changeMbo, final Date startDate, final Map<String, PmChgSchedulerTaskInfo> tasksInfoMap)
    '''
def findChangeSchedulableDates():
    '''    public List<String> findChangeSchedulableDates(final MboRemote changeMbo, final Date startDate, final Date endDate, final Map<String, PmChgSchedulerTaskInfo> tasksInfoMap, final TimeZone clientTZ, final TimeZone serverTZ)
    '''
def getTaskScheduledDates():
    '''    public List<String> getTaskScheduledDates(final MboRemote changeMbo, final Map<String, PmChgSchedulerTaskInfo> tasksInfoMap, final TimeZone tz)
    '''
def getMessages():
    '''    public Map<String, String> getMessages(final MboRemote mbo, final String msgGroup)
    '''
def updateActivitiesStartFinishDates():
    '''    public void updateActivitiesStartFinishDates(final Map<String, PmChgSchedulerTaskInfo> tasksInfoMap)
    '''
