crewDurStatic = "String  \"Static\""
crewDurDynamic = "String  \"Dynamic\""
crewDurCrewPos = "String  \"PLUSDCRW\""
def ():
    '''returns AMCrew\n\n
    (final MboSet ms)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def add():
    '''returns None\n\n
    add()\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(final String status, final Date date, final String memo, final long accessModifier)\n
    changeStatus(final String newStatus, final String memo)\n
    '''
def canDelete():
    '''returns None\n\n
    canDelete()\n
    '''
def delete():
    '''returns None\n\n
    delete(final long accessModifier)\n
    '''
def duplicate():
    '''returns MboRemote\n\n
    duplicate()\n
    '''
def getStatusListName():
    '''returns String\n\n
    getStatusListName()\n
    '''
def associateCrewType():
    '''returns None\n\n
    associateCrewType()\n
    '''
def refreshkRequirements():
    '''returns None\n\n
    refreshkRequirements()\n
    '''
def checkCalendarAndShift():
    '''returns None\n\n
    checkCalendarAndShift()\n
    '''
def setWorkHrs():
    '''returns None\n\n
    setWorkHrs(final Date DayOneClientDate)\n
    '''
def getServerDTFromClientDT():
    '''returns Date\n\n
    getServerDTFromClientDT(final Date clientDateTime, final GregorianCalendar scratchCal)\n
    '''
def getClientDTFromServerDT():
    '''returns Date\n\n
    getClientDTFromServerDT(final Date serverDateTime, final GregorianCalendar scratchCal)\n
    '''
def getAvailableMbo():
    '''returns MboRemote\n\n
    getAvailableMbo(final Date startDate)\n
    '''
def getAvailableMboList():
    '''returns List<MboRemote>\n\n
    getAvailableMboList(final Date startDate)\n
    '''
def getDateTime():
    '''returns Date\n\n
    getDateTime(final Date workdt, final Date sttime)\n
    '''
def getWPEndDateTime():
    '''returns Date\n\n
    getWPEndDateTime(final MboRemote WorkTimeMbo, final Date wpStartDateTime, final GregorianCalendar scratchCal)\n
    '''
def getDayNAssignmentSet():
    '''returns MboSetRemote\n\n
    getDayNAssignmentSet(final MboRemote theCrewMbo, final Date wpStartDateTime, final Date wpEndDateTime)\n
    '''
def getAvailableHours():
    '''returns double\n\n
    getAvailableHours(final Date startDate)\n
    '''
def getAssignedHours():
    '''returns double\n\n
    getAssignedHours(final boolean insideCurrentDateWorkingTime, final Date wpStartDateTime, final Date wpEndDateTime, final MboSetRemote dayNAssignmentSet)\n
    '''
def getServerDateColumn():
    '''returns Date[]\n\n
    getServerDateColumn()\n
    '''
def setServerDateColumn():
    '''returns None\n\n
    setServerDateColumn(final Date[] newServerDateColumn)\n
    '''
def getLabors():
    '''returns Collection\n\n
    getLabors(final Date currentDate)\n
    '''
def getTools():
    '''returns Collection\n\n
    getTools(final Date currentDate)\n
    '''
def isAMGridCreated():
    '''returns boolean\n\n
    isAMGridCreated()\n
    '''
def setAMGridCreated():
    '''returns None\n\n
    setAMGridCreated(final boolean gridCreated)\n
    '''
def childHasChanged():
    '''returns None\n\n
    childHasChanged()\n
    '''
def getMboSet():
    '''returns MboSetRemote\n\n
    getMboSet(final String name)\n
    '''
def calculateAvailabilityData():
    '''returns None\n\n
    calculateAvailabilityData()\n
    '''
def updateStandardRate():
    '''returns None\n\n
    updateStandardRate()\n
    '''
def getEarliestUnassignedDateTime():
    '''returns Date\n\n
    getEarliestUnassignedDateTime(final MboSetRemote dayNAssignmentSet, final Date rangeStartDateTime, final Date rangeFinishDateTime)\n
    '''
def getLatitudeY():
    '''returns Double\n\n
    getLatitudeY()\n
    '''
def hasCoords():
    '''returns Boolean\n\n
    hasCoords()\n
    '''
def getLongitudeX():
    '''returns Double\n\n
    getLongitudeX()\n
    '''
def getAddressString():
    '''returns String\n\n
    getAddressString()\n
    '''
def isGISDataReadonly():
    '''returns boolean\n\n
    isGISDataReadonly()\n
    '''
def saveGISData():
    '''returns None\n\n
    saveGISData(final String address, final String lat, final String lng)\n
    '''
def getLocationAccuracy():
    '''returns Double\n\n
    getLocationAccuracy()\n
    '''
def getAltitude():
    '''returns Double\n\n
    getAltitude()\n
    '''
def getAltitudeAccuracy():
    '''returns Double\n\n
    getAltitudeAccuracy()\n
    '''
def getHeading():
    '''returns Double\n\n
    getHeading()\n
    '''
def getLastUpdate():
    '''returns Date\n\n
    getLastUpdate()\n
    '''
def getSpeed():
    '''returns Double\n\n
    getSpeed()\n
    '''
def saveLBSData():
    '''returns None\n\n
    saveLBSData(final Double lat, final Double lng, final Double locationAccuracy, final Double altitudeAccuracy, final Double altitude, final Double heading, final Double speed)\n
    '''
def getValidContract():
    '''returns MboRemote\n\n
    getValidContract(final Date startDate)\n
    '''
def getCompositeWP():
    '''returns MboRemote\n\n
    getCompositeWP(final List<MboRemote> modAvailList, final Date workDate)\n
    '''
def getCurrentShiftHours():
    '''returns double\n\n
    getCurrentShiftHours(final Date workdate)\n
    '''
def getCurrentShiftStartDate():
    '''returns Date\n\n
    getCurrentShiftStartDate(final Date effectiveDate)\n
    '''
def getCurrentShiftEndDate():
    '''returns Date\n\n
    getCurrentShiftEndDate(final Date endDate)\n
    '''
def setCrewDate():
    '''returns None\n\n
    setCrewDate(final Date date)\n
    '''
def getCrewDate():
    '''returns Date\n\n
    getCrewDate()\n
    '''
def getCrewMemberCount():
    '''returns int\n\n
    getCrewMemberCount(final Date desiredDate)\n
    '''
def setDateTo():
    '''returns None\n\n
    setDateTo(final Date dateTo)\n
    '''
def getDateTo():
    '''returns Date\n\n
    getDateTo()\n
    '''
def getEligibleHours():
    '''returns double[]\n\n
    getEligibleHours()\n
    '''
