def ():
    '''returns WOActivity\n\n
    (final MboServerInterface ms)\n
    (final String shiftNum, final Date shiftStartDate, final Date shiftEndDate)\n
    (final Date activityStartDate, final Date activityEndDate, final double duration, final double hours, final String craft, final boolean interruptibleFlag, final String intShift)\n
    '''
def populate():
    '''returns None\n\n
    populate(final boolean isResourceDataPersistedInScheduler)\n
    populate(final String startWeekDay, final long SKDProjectId, final boolean isResourceDataPersistedInScheduler)\n
    '''
def recalculateSKDLaborHrsTemp():
    '''returns None\n\n
    recalculateSKDLaborHrsTemp(final long SKDProjectId, final HashMap<String, HashMap<String, Double>> craftWorkHoursMap, final HashMap<String, HashMap<String, Double>> craftNonWorkHoursMap)\n
    '''
def getWeekHrs():
    '''returns double\n\n
    getWeekHrs(final Date actStartWeekDate, final HashMap<String, HashMap<String, Double>> crafHoursMap, final String craft, final Date minActDate, final Date maxActDate)\n
    '''
def getMonthHrs():
    '''returns double\n\n
    getMonthHrs(final String year, final String actTimePeriod, final HashMap<String, HashMap<String, Double>> crafHoursMap, final String craft, final Date minActDate, final Date maxActDate)\n
    '''
def deleteSKDLaborHours():
    '''returns None\n\n
    deleteSKDLaborHours()\n
    '''
def deleteSKDLaborHrs():
    '''returns None\n\n
    deleteSKDLaborHrs(final long SKDProjectId)\n
    '''
def deleteSKDLaborHrsTemp():
    '''returns None\n\n
    deleteSKDLaborHrsTemp()\n
    deleteSKDLaborHrsTemp(final long SKDProjectId)\n
    '''
def populateLaborHrs():
    '''returns None\n\n
    populateLaborHrs()\n
    '''
def populatePlannedAvblHrs():
    '''returns None\n\n
    populatePlannedAvblHrs(final String startWeekDay, final long SKDProjectId, final boolean isResourceDataPersistedInScheduler)\n
    '''
def populatePlannedLaborHrsDaily():
    '''returns None\n\n
    populatePlannedLaborHrsDaily(final long SKDProjectId, final String yearDate, final String monthDate, final String monthDateP, final String weekDate, final String dayDate, final String startWeekDate, final String workDate, final boolean isResourceDataPersistedInScheduler)\n
    '''
def addSKDLaborHrsTemp():
    '''returns None\n\n
    addSKDLaborHrsTemp(final long SKDProjectId, final HashMap<String, ArrayList<WOActivity>> craftActivityListMap, final String cond)\n
    '''
def populatePMPlannedLaborHrsDaily():
    '''returns None\n\n
    populatePMPlannedLaborHrsDaily(final long SKDProjectId, final String yearDate, final String monthDate, final String monthDateP, final String weekDate, final String dayDate, final String startWeekDate, final String workDate, final String newdatesql)\n
    '''
def populatePlannedCrewHrsDaily():
    '''returns None\n\n
    populatePlannedCrewHrsDaily(final long SKDProjectId, final String yearDate, final String monthDate, final String monthDateP, final String weekDate, final String dayDate, final String startWeekDate, final String workDate, final boolean isResourceDataPersisted)\n
    '''
def populatePMPlannedCrewHrsDaily():
    '''returns None\n\n
    populatePMPlannedCrewHrsDaily(final long SKDProjectId, final String yearDate, final String monthDate, final String monthDateP, final String weekDate, final String dayDate, final String startWeekDate, final String workDate, final String newdatesql)\n
    '''
def populatePlannedHrsWeeklyMonthy():
    '''returns None\n\n
    populatePlannedHrsWeeklyMonthy(final long SKDProjectId, final String yearDate, final String monthDate, final String monthDateP, final String weekDate, final String dayDate, final String startWeekDate, final String workDate)\n
    '''
def populateAvblLaborHrsDaily():
    '''returns None\n\n
    populateAvblLaborHrsDaily(final long SKDProjectId, final String yearDate, final String monthDate, final String monthDateP, final String weekDate, final String dayDate, final String startWeekDate, final String actDate, final String workDate)\n
    '''
def populatePMAvblLaborHrsDaily():
    '''returns None\n\n
    populatePMAvblLaborHrsDaily(final long SKDProjectId, final String yearDate, final String monthDate, final String monthDateP, final String weekDate, final String dayDate, final String startWeekDate, final String actDate, final String workDate, final String newdatesql)\n
    '''
def populateAvblCrewHrsDaily():
    '''returns None\n\n
    populateAvblCrewHrsDaily(final long SKDProjectId, final String yearDate, final String monthDate, final String monthDateP, final String weekDate, final String dayDate, final String startWeekDate, final String actDate, final String workDate)\n
    '''
def populatePMAvblCrewHrsDaily():
    '''returns None\n\n
    populatePMAvblCrewHrsDaily(final long SKDProjectId, final String yearDate, final String monthDate, final String monthDateP, final String weekDate, final String dayDate, final String startWeekDate, final String actDate, final String workDate, final String newdatesql)\n
    '''
def populateAvblHrsWeeklyMonthly():
    '''returns None\n\n
    populateAvblHrsWeeklyMonthly(final long SKDProjectId, final String yearDate, final String monthDate, final String monthDateP, final String weekDate, final String dayDate, final String startWeekDate, final String actDate, final String workDate)\n
    '''
def updateSKDTemp():
    '''returns None\n\n
    updateSKDTemp()\n
    updateSKDTemp(final long SKDProjectId)\n
    '''
def isSKDTempEmpty():
    '''returns boolean\n\n
    isSKDTempEmpty()\n
    isSKDTempEmpty(final long SKDProjectId)\n
    '''
def populateSKDLaborHrs():
    '''returns None\n\n
    populateSKDLaborHrs()\n
    populateSKDLaborHrs(final long SKDProjectId)\n
    '''
def updateTimePeriod():
    '''returns None\n\n
    updateTimePeriod()\n
    updateTimePeriod(final long SKDProjectId)\n
    '''
def executeStatement():
    '''returns None\n\n
    executeStatement(final String sqlStatement)\n
    '''
def isOverlaping():
    '''returns boolean\n\n
    isOverlaping(final WOActivity activity, final Shift shift)\n
    '''
def loadShiftData():
    '''returns None\n\n
    loadShiftData(final Long SKDProjectId)\n
    '''
def getShiftStartDate():
    '''returns Date\n\n
    getShiftStartDate()\n
    '''
def setShiftStartDate():
    '''returns None\n\n
    setShiftStartDate(final Date shiftStartDate)\n
    '''
def getShiftEndDate():
    '''returns Date\n\n
    getShiftEndDate()\n
    '''
def setShiftEndDate():
    '''returns None\n\n
    setShiftEndDate(final Date shiftEndDate)\n
    '''
def getShiftNum():
    '''returns String\n\n
    getShiftNum()\n
    '''
def setShiftNum():
    '''returns None\n\n
    setShiftNum(final String shiftNum)\n
    '''
def compareTo():
    '''returns int\n\n
    compareTo(final Object obj)\n
    compareTo(final Object obj)\n
    '''
def getOverlappingShifts():
    '''returns ArrayList<Shift>\n\n
    getOverlappingShifts()\n
    '''
def getInterruptible():
    '''returns boolean\n\n
    getInterruptible()\n
    '''
def getActivityStartDate():
    '''returns Date\n\n
    getActivityStartDate()\n
    '''
def setActivityStartDate():
    '''returns None\n\n
    setActivityStartDate(final Date activityStartDate)\n
    '''
def getActivityEndDate():
    '''returns Date\n\n
    getActivityEndDate()\n
    '''
def setActivityEndDate():
    '''returns None\n\n
    setActivityEndDate(final Date activityEndDate)\n
    '''
def getHours():
    '''returns double\n\n
    getHours()\n
    '''
def getDuration():
    '''returns double\n\n
    getDuration()\n
    '''
def getCraft():
    '''returns String\n\n
    getCraft()\n
    '''
def getHoursInShift0():
    '''returns double\n\n
    getHoursInShift0(final Date shiftStartDate)\n
    '''
def getHoursInShift():
    '''returns double\n\n
    getHoursInShift(final Date shiftStartDate)\n
    '''
def setHours():
    '''returns None\n\n
    setHours(final double hours)\n
    '''
def addOverlappingShifts():
    '''returns None\n\n
    addOverlappingShifts(final Shift shift)\n
    '''
def getShift():
    '''returns Shift\n\n
    getShift(final Date shiftStartDate)\n
    '''
def getFractionOverlap():
    '''returns double\n\n
    getFractionOverlap(final Date shiftStartDate)\n
    '''
def getFractionOverlap0():
    '''returns double\n\n
    getFractionOverlap0(final Date shiftStartDate)\n
    '''
