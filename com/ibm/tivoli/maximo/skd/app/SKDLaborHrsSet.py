def SKDLaborHrsSet():
'''public SKDLaborHrsSet(final MboServerInterface ms)
'''
pass
def populate():
'''public void populate(final boolean isResourceDataPersistedInScheduler)
public void populate(final String startWeekDay, final long SKDProjectId, final boolean isResourceDataPersistedInScheduler)
'''
pass
def recalculateSKDLaborHrsTemp():
'''public void recalculateSKDLaborHrsTemp(final long SKDProjectId, final HashMap<String, HashMap<String, Double>> craftWorkHoursMap, final HashMap<String, HashMap<String, Double>> craftNonWorkHoursMap)
'''
pass
def getWeekHrs():
'''public double getWeekHrs(final Date actStartWeekDate, final HashMap<String, HashMap<String, Double>> crafHoursMap, final String craft, final Date minActDate, final Date maxActDate)
'''
pass
def getMonthHrs():
'''public double getMonthHrs(final String year, final String actTimePeriod, final HashMap<String, HashMap<String, Double>> crafHoursMap, final String craft, final Date minActDate, final Date maxActDate)
'''
pass
def getResourceAvailData():
'''public HashMap<String, HashMap<String, Double>> getResourceAvailData(final Long projectId, final boolean workTime, final boolean isResourceDataPersistedInScheduler)
'''
pass
def getCrewAvailData():
'''public HashMap<String, HashMap<String, Double>> getCrewAvailData(final Long projectId, final boolean workTime)
'''
pass
def deleteSKDLaborHours():
'''public void deleteSKDLaborHours()
'''
pass
def deleteSKDLaborHrs():
'''public void deleteSKDLaborHrs(final long SKDProjectId)
'''
pass
def deleteSKDLaborHrsTemp():
'''public void deleteSKDLaborHrsTemp()
public void deleteSKDLaborHrsTemp(final long SKDProjectId)
'''
pass
def populateLaborHrs():
'''public void populateLaborHrs()
'''
pass
def populatePlannedAvblHrs():
'''public void populatePlannedAvblHrs(final String startWeekDay, final long SKDProjectId, final boolean isResourceDataPersistedInScheduler)
'''
pass
def populatePlannedLaborHrsDaily():
'''public void populatePlannedLaborHrsDaily(final long SKDProjectId, final String yearDate, final String monthDate, final String monthDateP, final String weekDate, final String dayDate, final String startWeekDate, final String workDate, final boolean isResourceDataPersistedInScheduler)
'''
pass
def addSKDLaborHrsTemp():
'''public void addSKDLaborHrsTemp(final long SKDProjectId, final HashMap<String, ArrayList<WOActivity>> craftActivityListMap, final String cond)
'''
pass
def populatePMPlannedLaborHrsDaily():
'''public void populatePMPlannedLaborHrsDaily(final long SKDProjectId, final String yearDate, final String monthDate, final String monthDateP, final String weekDate, final String dayDate, final String startWeekDate, final String workDate, final String newdatesql)
'''
pass
def populatePlannedCrewHrsDaily():
'''public void populatePlannedCrewHrsDaily(final long SKDProjectId, final String yearDate, final String monthDate, final String monthDateP, final String weekDate, final String dayDate, final String startWeekDate, final String workDate, final boolean isResourceDataPersisted)
'''
pass
def populatePMPlannedCrewHrsDaily():
'''public void populatePMPlannedCrewHrsDaily(final long SKDProjectId, final String yearDate, final String monthDate, final String monthDateP, final String weekDate, final String dayDate, final String startWeekDate, final String workDate, final String newdatesql)
'''
pass
def populatePlannedHrsWeeklyMonthy():
'''public void populatePlannedHrsWeeklyMonthy(final long SKDProjectId, final String yearDate, final String monthDate, final String monthDateP, final String weekDate, final String dayDate, final String startWeekDate, final String workDate)
'''
pass
def populateAvblLaborHrsDaily():
'''public void populateAvblLaborHrsDaily(final long SKDProjectId, final String yearDate, final String monthDate, final String monthDateP, final String weekDate, final String dayDate, final String startWeekDate, final String actDate, final String workDate)
'''
pass
def populatePMAvblLaborHrsDaily():
'''public void populatePMAvblLaborHrsDaily(final long SKDProjectId, final String yearDate, final String monthDate, final String monthDateP, final String weekDate, final String dayDate, final String startWeekDate, final String actDate, final String workDate, final String newdatesql)
'''
pass
def populateAvblCrewHrsDaily():
'''public void populateAvblCrewHrsDaily(final long SKDProjectId, final String yearDate, final String monthDate, final String monthDateP, final String weekDate, final String dayDate, final String startWeekDate, final String actDate, final String workDate)
'''
pass
def populatePMAvblCrewHrsDaily():
'''public void populatePMAvblCrewHrsDaily(final long SKDProjectId, final String yearDate, final String monthDate, final String monthDateP, final String weekDate, final String dayDate, final String startWeekDate, final String actDate, final String workDate, final String newdatesql)
'''
pass
def populateAvblHrsWeeklyMonthly():
'''public void populateAvblHrsWeeklyMonthly(final long SKDProjectId, final String yearDate, final String monthDate, final String monthDateP, final String weekDate, final String dayDate, final String startWeekDate, final String actDate, final String workDate)
'''
pass
def updateSKDTemp():
'''public void updateSKDTemp()
public void updateSKDTemp(final long SKDProjectId)
'''
pass
def isSKDTempEmpty():
'''public boolean isSKDTempEmpty()
public boolean isSKDTempEmpty(final long SKDProjectId)
'''
pass
def populateSKDLaborHrs():
'''public void populateSKDLaborHrs()
public void populateSKDLaborHrs(final long SKDProjectId)
'''
pass
def updateTimePeriod():
'''public void updateTimePeriod()
public void updateTimePeriod(final long SKDProjectId)
'''
pass
def executeStatement():
'''public void executeStatement(final String sqlStatement)
'''
pass
def isOverlaping():
'''public boolean isOverlaping(final WOActivity activity, final Shift shift)
'''
pass
def loadShiftData():
'''public void loadShiftData(final Long SKDProjectId)
'''
pass
def Shift():
'''public Shift(final String shiftNum, final Date shiftStartDate, final Date shiftEndDate)
'''
pass
def getShiftStartDate():
'''public Date getShiftStartDate()
'''
pass
def setShiftStartDate():
'''public void setShiftStartDate(final Date shiftStartDate)
'''
pass
def getShiftEndDate():
'''public Date getShiftEndDate()
'''
pass
def setShiftEndDate():
'''public void setShiftEndDate(final Date shiftEndDate)
'''
pass
def getShiftNum():
'''public String getShiftNum()
'''
pass
def setShiftNum():
'''public void setShiftNum(final String shiftNum)
'''
pass
def compareTo():
'''public int compareTo(final Object obj)
public int compareTo(final Object obj)
'''
pass
def getOverlappingShifts():
'''public ArrayList<Shift> getOverlappingShifts()
'''
pass
def WOActivity():
'''public WOActivity(final Date activityStartDate, final Date activityEndDate, final double duration, final double hours, final String craft, final boolean interruptibleFlag, final String intShift)
'''
pass
def getInterruptible():
'''public boolean getInterruptible()
'''
pass
def getActivityStartDate():
'''public Date getActivityStartDate()
'''
pass
def setActivityStartDate():
'''public void setActivityStartDate(final Date activityStartDate)
'''
pass
def getActivityEndDate():
'''public Date getActivityEndDate()
'''
pass
def setActivityEndDate():
'''public void setActivityEndDate(final Date activityEndDate)
'''
pass
def getHours():
'''public double getHours()
'''
pass
def getDuration():
'''public double getDuration()
'''
pass
def getCraft():
'''public String getCraft()
'''
pass
def getHoursInShift0():
'''public double getHoursInShift0(final Date shiftStartDate)
'''
pass
def getHoursInShift():
'''public double getHoursInShift(final Date shiftStartDate)
'''
pass
def setHours():
'''public void setHours(final double hours)
'''
pass
def addOverlappingShifts():
'''public void addOverlappingShifts(final Shift shift)
'''
pass
def getShift():
'''public Shift getShift(final Date shiftStartDate)
'''
pass
def getFractionOverlap():
'''public double getFractionOverlap(final Date shiftStartDate)
'''
pass
def getFractionOverlap0():
'''public double getFractionOverlap0(final Date shiftStartDate)
'''
pass
