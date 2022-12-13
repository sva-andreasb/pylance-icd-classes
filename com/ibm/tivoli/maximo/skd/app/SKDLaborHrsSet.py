def SKDLaborHrsSet():
    '''public SKDLaborHrsSet(final MboServerInterface ms)
    '''
def populate():
    '''public void populate(final boolean isResourceDataPersistedInScheduler)
    public void populate(final String startWeekDay, final long SKDProjectId, final boolean isResourceDataPersistedInScheduler)
    '''
def recalculateSKDLaborHrsTemp():
    '''public void recalculateSKDLaborHrsTemp(final long SKDProjectId, final HashMap<String, HashMap<String, Double>> craftWorkHoursMap, final HashMap<String, HashMap<String, Double>> craftNonWorkHoursMap)
    '''
def getWeekHrs():
    '''public double getWeekHrs(final Date actStartWeekDate, final HashMap<String, HashMap<String, Double>> crafHoursMap, final String craft, final Date minActDate, final Date maxActDate)
    '''
def getMonthHrs():
    '''public double getMonthHrs(final String year, final String actTimePeriod, final HashMap<String, HashMap<String, Double>> crafHoursMap, final String craft, final Date minActDate, final Date maxActDate)
    '''
def getResourceAvailData():
    '''public HashMap<String, HashMap<String, Double>> getResourceAvailData(final Long projectId, final boolean workTime, final boolean isResourceDataPersistedInScheduler)
    '''
def getCrewAvailData():
    '''public HashMap<String, HashMap<String, Double>> getCrewAvailData(final Long projectId, final boolean workTime)
    '''
def deleteSKDLaborHours():
    '''public void deleteSKDLaborHours()
    '''
def deleteSKDLaborHrs():
    '''public void deleteSKDLaborHrs(final long SKDProjectId)
    '''
def deleteSKDLaborHrsTemp():
    '''public void deleteSKDLaborHrsTemp()
    public void deleteSKDLaborHrsTemp(final long SKDProjectId)
    '''
def populateLaborHrs():
    '''public void populateLaborHrs()
    '''
def populatePlannedAvblHrs():
    '''public void populatePlannedAvblHrs(final String startWeekDay, final long SKDProjectId, final boolean isResourceDataPersistedInScheduler)
    '''
def populatePlannedLaborHrsDaily():
    '''public void populatePlannedLaborHrsDaily(final long SKDProjectId, final String yearDate, final String monthDate, final String monthDateP, final String weekDate, final String dayDate, final String startWeekDate, final String workDate, final boolean isResourceDataPersistedInScheduler)
    '''
def addSKDLaborHrsTemp():
    '''public void addSKDLaborHrsTemp(final long SKDProjectId, final HashMap<String, ArrayList<WOActivity>> craftActivityListMap, final String cond)
    '''
def populatePMPlannedLaborHrsDaily():
    '''public void populatePMPlannedLaborHrsDaily(final long SKDProjectId, final String yearDate, final String monthDate, final String monthDateP, final String weekDate, final String dayDate, final String startWeekDate, final String workDate, final String newdatesql)
    '''
def populatePlannedCrewHrsDaily():
    '''public void populatePlannedCrewHrsDaily(final long SKDProjectId, final String yearDate, final String monthDate, final String monthDateP, final String weekDate, final String dayDate, final String startWeekDate, final String workDate, final boolean isResourceDataPersisted)
    '''
def populatePMPlannedCrewHrsDaily():
    '''public void populatePMPlannedCrewHrsDaily(final long SKDProjectId, final String yearDate, final String monthDate, final String monthDateP, final String weekDate, final String dayDate, final String startWeekDate, final String workDate, final String newdatesql)
    '''
def populatePlannedHrsWeeklyMonthy():
    '''public void populatePlannedHrsWeeklyMonthy(final long SKDProjectId, final String yearDate, final String monthDate, final String monthDateP, final String weekDate, final String dayDate, final String startWeekDate, final String workDate)
    '''
def populateAvblLaborHrsDaily():
    '''public void populateAvblLaborHrsDaily(final long SKDProjectId, final String yearDate, final String monthDate, final String monthDateP, final String weekDate, final String dayDate, final String startWeekDate, final String actDate, final String workDate)
    '''
def populatePMAvblLaborHrsDaily():
    '''public void populatePMAvblLaborHrsDaily(final long SKDProjectId, final String yearDate, final String monthDate, final String monthDateP, final String weekDate, final String dayDate, final String startWeekDate, final String actDate, final String workDate, final String newdatesql)
    '''
def populateAvblCrewHrsDaily():
    '''public void populateAvblCrewHrsDaily(final long SKDProjectId, final String yearDate, final String monthDate, final String monthDateP, final String weekDate, final String dayDate, final String startWeekDate, final String actDate, final String workDate)
    '''
def populatePMAvblCrewHrsDaily():
    '''public void populatePMAvblCrewHrsDaily(final long SKDProjectId, final String yearDate, final String monthDate, final String monthDateP, final String weekDate, final String dayDate, final String startWeekDate, final String actDate, final String workDate, final String newdatesql)
    '''
def populateAvblHrsWeeklyMonthly():
    '''public void populateAvblHrsWeeklyMonthly(final long SKDProjectId, final String yearDate, final String monthDate, final String monthDateP, final String weekDate, final String dayDate, final String startWeekDate, final String actDate, final String workDate)
    '''
def updateSKDTemp():
    '''public void updateSKDTemp()
    public void updateSKDTemp(final long SKDProjectId)
    '''
def isSKDTempEmpty():
    '''public boolean isSKDTempEmpty()
    public boolean isSKDTempEmpty(final long SKDProjectId)
    '''
def populateSKDLaborHrs():
    '''public void populateSKDLaborHrs()
    public void populateSKDLaborHrs(final long SKDProjectId)
    '''
def updateTimePeriod():
    '''public void updateTimePeriod()
    public void updateTimePeriod(final long SKDProjectId)
    '''
def executeStatement():
    '''public void executeStatement(final String sqlStatement)
    '''
def isOverlaping():
    '''public boolean isOverlaping(final WOActivity activity, final Shift shift)
    '''
def loadShiftData():
    '''public void loadShiftData(final Long SKDProjectId)
    '''
def Shift():
    '''public Shift(final String shiftNum, final Date shiftStartDate, final Date shiftEndDate)
    '''
def getShiftStartDate():
    '''public Date getShiftStartDate()
    '''
def setShiftStartDate():
    '''public void setShiftStartDate(final Date shiftStartDate)
    '''
def getShiftEndDate():
    '''public Date getShiftEndDate()
    '''
def setShiftEndDate():
    '''public void setShiftEndDate(final Date shiftEndDate)
    '''
def getShiftNum():
    '''public String getShiftNum()
    '''
def setShiftNum():
    '''public void setShiftNum(final String shiftNum)
    '''
def compareTo():
    '''public int compareTo(final Object obj)
    public int compareTo(final Object obj)
    '''
def getOverlappingShifts():
    '''public ArrayList<Shift> getOverlappingShifts()
    '''
def WOActivity():
    '''public WOActivity(final Date activityStartDate, final Date activityEndDate, final double duration, final double hours, final String craft, final boolean interruptibleFlag, final String intShift)
    '''
def getInterruptible():
    '''public boolean getInterruptible()
    '''
def getActivityStartDate():
    '''public Date getActivityStartDate()
    '''
def setActivityStartDate():
    '''public void setActivityStartDate(final Date activityStartDate)
    '''
def getActivityEndDate():
    '''public Date getActivityEndDate()
    '''
def setActivityEndDate():
    '''public void setActivityEndDate(final Date activityEndDate)
    '''
def getHours():
    '''public double getHours()
    '''
def getDuration():
    '''public double getDuration()
    '''
def getCraft():
    '''public String getCraft()
    '''
def getHoursInShift0():
    '''public double getHoursInShift0(final Date shiftStartDate)
    '''
def getHoursInShift():
    '''public double getHoursInShift(final Date shiftStartDate)
    '''
def setHours():
    '''public void setHours(final double hours)
    '''
def addOverlappingShifts():
    '''public void addOverlappingShifts(final Shift shift)
    '''
def getShift():
    '''public Shift getShift(final Date shiftStartDate)
    '''
def getFractionOverlap():
    '''public double getFractionOverlap(final Date shiftStartDate)
    '''
def getFractionOverlap0():
    '''public double getFractionOverlap0(final Date shiftStartDate)
    '''
