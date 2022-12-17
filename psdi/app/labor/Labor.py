def ():
    '''returns Labor\n\n
    (final MboSet ms)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def canDelete():
    '''returns None\n\n
    canDelete()\n
    '''
def delete():
    '''returns None\n\n
    delete(final long accessModifier)\n
    '''
def add():
    '''returns None\n\n
    add()\n
    '''
def appValidate():
    '''returns None\n\n
    appValidate()\n
    '''
def duplicate():
    '''returns MboRemote\n\n
    duplicate()\n
    '''
def generateAutoKey():
    '''returns None\n\n
    generateAutoKey()\n
    '''
def zeroYTD():
    '''returns None\n\n
    zeroYTD(final boolean bReported, final boolean bOvertime, final boolean bOTRefused)\n
    '''
def associateLoc():
    '''returns None\n\n
    associateLoc(final String loc)\n
    '''
def getSiteUserForLabor():
    '''returns SiteAuth\n\n
    getSiteUserForLabor()\n
    '''
def getUserNameForLabor():
    '''returns String\n\n
    getUserNameForLabor()\n
    '''
def getStatusListName():
    '''returns String\n\n
    getStatusListName()\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(final String newStatus, final Date date, final String memo)\n
    '''
def getServerDateColumn():
    '''returns Date[]\n\n
    getServerDateColumn()\n
    '''
def setServerDateColumn():
    '''returns None\n\n
    setServerDateColumn(final Date[] newServerDateColumn)\n
    '''
def setWorkHrs():
    '''returns None\n\n
    setWorkHrs(final Date DayOneClientDate)\n
    setWorkHrs(final Date DayOneClientDate, final boolean isCreateAMGrid)\n
    '''
def getServerDTFromClientDT():
    '''returns Date\n\n
    getServerDTFromClientDT(final Date clientDateTime, final GregorianCalendar scratchCal)\n
    '''
def getClientDTFromServerDT():
    '''returns Date\n\n
    getClientDTFromServerDT(final Date serverDateTime, final GregorianCalendar scratchCal)\n
    '''
def getWPEndDateTime():
    '''returns Date\n\n
    getWPEndDateTime(final MboRemote WorkTimeMbo, final Date wpStartDateTime, final GregorianCalendar scratchCal, final AvailCalc availCalc)\n
    '''
def getDayNAssignmentSet():
    '''returns MboSetRemote\n\n
    getDayNAssignmentSet(final MboRemote theLaborMbo, final Date wpStartDateTime, final Date wpEndDateTime)\n
    '''
def getAssignedHours():
    '''returns double\n\n
    getAssignedHours(final boolean insideCurrentDateWorkingTime, final Date rangeStartDateTime, final Date rangeFinishDateTime, final MboSetRemote dayNAssignmentSet)\n
    '''
def getEarliestUnassignedDateTime():
    '''returns Date\n\n
    getEarliestUnassignedDateTime(final MboSetRemote dayNAssignmentSet, final Date rangeStartDateTime, final Date rangeFinishDateTime)\n
    '''
def checkCalendarAndShift():
    '''returns None\n\n
    checkCalendarAndShift()\n
    '''
def updateCalendar():
    '''returns None\n\n
    updateCalendar()\n
    '''
def calculateAvailabilityData():
    '''returns None\n\n
    calculateAvailabilityData()\n
    '''
def hasCoords():
    '''returns Boolean\n\n
    hasCoords()\n
    '''
def getLatitudeY():
    '''returns Double\n\n
    getLatitudeY()\n
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
def getEligibleHours():
    '''returns double[]\n\n
    getEligibleHours()\n
    '''
