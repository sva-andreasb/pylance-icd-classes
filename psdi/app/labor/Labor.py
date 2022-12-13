def Labor():
'''public Labor(final MboSet ms)
'''
pass
def init():
'''public void init()
'''
pass
def canDelete():
'''public void canDelete()
'''
pass
def delete():
'''public void delete(final long accessModifier)
'''
pass
def add():
'''public void add()
'''
pass
def appValidate():
'''public void appValidate()
'''
pass
def duplicate():
'''public MboRemote duplicate()
'''
pass
def generateAutoKey():
'''public void generateAutoKey()
'''
pass
def zeroYTD():
'''public void zeroYTD(final boolean bReported, final boolean bOvertime, final boolean bOTRefused)
'''
pass
def associateLoc():
'''public void associateLoc(final String loc)
'''
pass
def getSiteUserForLabor():
'''public SiteAuth getSiteUserForLabor()
'''
pass
def getUserNameForLabor():
'''public String getUserNameForLabor()
'''
pass
def getStatusListName():
'''public String getStatusListName()
'''
pass
def changeStatus():
'''public void changeStatus(final String newStatus, final Date date, final String memo)
'''
pass
def getServerDateColumn():
'''public Date[] getServerDateColumn()
'''
pass
def setServerDateColumn():
'''public void setServerDateColumn(final Date[] newServerDateColumn)
'''
pass
def setWorkHrs():
'''public void setWorkHrs(final Date DayOneClientDate)
public void setWorkHrs(final Date DayOneClientDate, final boolean isCreateAMGrid)
'''
pass
def getServerDTFromClientDT():
'''public Date getServerDTFromClientDT(final Date clientDateTime, final GregorianCalendar scratchCal)
'''
pass
def getClientDTFromServerDT():
'''public Date getClientDTFromServerDT(final Date serverDateTime, final GregorianCalendar scratchCal)
'''
pass
def getWPEndDateTime():
'''public Date getWPEndDateTime(final MboRemote WorkTimeMbo, final Date wpStartDateTime, final GregorianCalendar scratchCal, final AvailCalc availCalc)
'''
pass
def getDayNAssignmentSet():
'''public MboSetRemote getDayNAssignmentSet(final MboRemote theLaborMbo, final Date wpStartDateTime, final Date wpEndDateTime)
'''
pass
def getAssignedHours():
'''public double getAssignedHours(final boolean insideCurrentDateWorkingTime, final Date rangeStartDateTime, final Date rangeFinishDateTime, final MboSetRemote dayNAssignmentSet)
'''
pass
def getEarliestUnassignedDateTime():
'''public Date getEarliestUnassignedDateTime(final MboSetRemote dayNAssignmentSet, final Date rangeStartDateTime, final Date rangeFinishDateTime)
'''
pass
def checkCalendarAndShift():
'''public void checkCalendarAndShift()
'''
pass
def updateCalendar():
'''public void updateCalendar()
'''
pass
def calculateAvailabilityData():
'''public void calculateAvailabilityData()
'''
pass
def hasCoords():
'''public Boolean hasCoords()
'''
pass
def getLatitudeY():
'''public Double getLatitudeY()
'''
pass
def getLongitudeX():
'''public Double getLongitudeX()
'''
pass
def getAddressString():
'''public String getAddressString()
'''
pass
def isGISDataReadonly():
'''public boolean isGISDataReadonly()
'''
pass
def saveGISData():
'''public void saveGISData(final String address, final String lat, final String lng)
'''
pass
def getLocationAccuracy():
'''public Double getLocationAccuracy()
'''
pass
def getAltitude():
'''public Double getAltitude()
'''
pass
def getAltitudeAccuracy():
'''public Double getAltitudeAccuracy()
'''
pass
def getHeading():
'''public Double getHeading()
'''
pass
def getLastUpdate():
'''public Date getLastUpdate()
'''
pass
def getSpeed():
'''public Double getSpeed()
'''
pass
def saveLBSData():
'''public void saveLBSData(final Double lat, final Double lng, final Double locationAccuracy, final Double altitudeAccuracy, final Double altitude, final Double heading, final Double speed)
'''
pass
def getEligibleHours():
'''public double[] getEligibleHours()
'''
pass
