def ():
    '''returns CostValue\n\n
    (final MboServerInterface ms)\n
    (final Date workDate, final Date startTime, final Date endTime, final Integer year, final Integer workHours, final Integer week, final Date startWeekDay)\n
    (final long skdProjectID, final int year, final int weekPeriod, final Date startWeekDay, final String contentUID)\n
    (final String field, final Double value)\n
    '''
def populate():
    '''returns None\n\n
    populate(final String startWeekDay, final long SKDProjectId)\n
    populate()\n
    '''
def deleteSKDCost():
    '''returns None\n\n
    deleteSKDCost()\n
    deleteSKDCost(final long SKDProjectId)\n
    '''
def deleteSKDCostTemp():
    '''returns None\n\n
    deleteSKDCostTemp()\n
    deleteSKDCostTemp(final long SKDProjectId)\n
    '''
def populateWAPPRCestCost():
    '''returns None\n\n
    populateWAPPRCestCost()\n
    populateWAPPRCestCost(final String startWeekDay, final long SKDProjectId)\n
    '''
def populateAPPRCestCost():
    '''returns None\n\n
    populateAPPRCestCost()\n
    populateAPPRCestCost(final String startWeekDay, final long SKDProjectId)\n
    '''
def populateWAPPRSestCost():
    '''returns None\n\n
    populateWAPPRSestCost()\n
    populateWAPPRSestCost(final String startWeekDay, final long SKDProjectId)\n
    '''
def populateAPPRSestCost():
    '''returns None\n\n
    populateAPPRSestCost()\n
    populateAPPRSestCost(final String startWeekDay, final long SKDProjectId)\n
    '''
def populateActLabCost():
    '''returns None\n\n
    populateActLabCost()\n
    populateActLabCost(final String startWeekDay, final long SKDProjectId)\n
    '''
def populateActMatCost():
    '''returns None\n\n
    populateActMatCost()\n
    populateActMatCost(final String startWeekDay, final long SKDProjectId)\n
    '''
def populateActServCost():
    '''returns None\n\n
    populateActServCost()\n
    populateActServCost(final String startWeekDay, final long SKDProjectId)\n
    '''
def populateActToolCost():
    '''returns None\n\n
    populateActToolCost()\n
    populateActToolCost(final String startWeekDay, final long SKDProjectId)\n
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
def populateSKDCost():
    '''returns None\n\n
    populateSKDCost()\n
    populateSKDCost(final long SKDProjectId)\n
    '''
def updateTotalCost():
    '''returns None\n\n
    updateTotalCost()\n
    updateTotalCost(final long SKDProjectId)\n
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
def getPrimaryKey():
    '''returns String\n\n
    getPrimaryKey(final String project, final String tableID)\n
    '''
def getWorkDate():
    '''returns Date\n\n
    getWorkDate()\n
    '''
def getStartTime():
    '''returns Date\n\n
    getStartTime()\n
    '''
def getEndTime():
    '''returns Date\n\n
    getEndTime()\n
    '''
def getYear():
    '''returns int\n\n
    getYear()\n
    getYear()\n
    '''
def getWorkHours():
    '''returns Integer\n\n
    getWorkHours()\n
    '''
def getWeek():
    '''returns Integer\n\n
    getWeek()\n
    '''
def getStartWeekDay():
    '''returns Date\n\n
    getStartWeekDay()\n
    getStartWeekDay()\n
    '''
def getSkdProjectID():
    '''returns long\n\n
    getSkdProjectID()\n
    '''
def getTimePeriod():
    '''returns String\n\n
    getTimePeriod()\n
    '''
def getWeekPeriod():
    '''returns int\n\n
    getWeekPeriod()\n
    '''
def getContentUID():
    '''returns String\n\n
    getContentUID()\n
    '''
def getTotalHours():
    '''returns double\n\n
    getTotalHours()\n
    '''
def addHours():
    '''returns None\n\n
    addHours(final double hours)\n
    '''
def getActivityHours():
    '''returns double\n\n
    getActivityHours()\n
    '''
def setActivityHours():
    '''returns None\n\n
    setActivityHours(final double activityHours)\n
    '''
def setValue():
    '''returns None\n\n
    setValue(final String field, final Double value)\n
    setValue(final Double value)\n
    '''
def getValue():
    '''returns Double\n\n
    getValue(final String field)\n
    getValue()\n
    '''
def getField():
    '''returns String\n\n
    getField()\n
    '''
def setField():
    '''returns None\n\n
    setField(final String field)\n
    '''
