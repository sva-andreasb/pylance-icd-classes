def Labor():
    '''    public Labor(final MboSet ms)
    '''
def init():
    '''    public void init()
    '''
def canDelete():
    '''    public void canDelete()
    '''
def delete():
    '''    public void delete(final long accessModifier)
    '''
def add():
    '''    public void add()
    '''
def appValidate():
    '''    public void appValidate()
    '''
def duplicate():
    '''    public MboRemote duplicate()
    '''
def generateAutoKey():
    '''    public void generateAutoKey()
    '''
def zeroYTD():
    '''    public void zeroYTD(final boolean bReported, final boolean bOvertime, final boolean bOTRefused)
    '''
def associateLoc():
    '''    public void associateLoc(final String loc)
    '''
def getSiteUserForLabor():
    '''    public SiteAuth getSiteUserForLabor()
    '''
def getUserNameForLabor():
    '''    public String getUserNameForLabor()
    '''
def getStatusListName():
    '''    public String getStatusListName()
    '''
def changeStatus():
    '''    public void changeStatus(final String newStatus, final Date date, final String memo)
    '''
def getServerDateColumn():
    '''    public Date[] getServerDateColumn()
    '''
def setServerDateColumn():
    '''    public void setServerDateColumn(final Date[] newServerDateColumn)
    '''
def setWorkHrs():
    '''    public void setWorkHrs(final Date DayOneClientDate)
    public void setWorkHrs(final Date DayOneClientDate, final boolean isCreateAMGrid)
    '''
def getServerDTFromClientDT():
    '''    public Date getServerDTFromClientDT(final Date clientDateTime, final GregorianCalendar scratchCal)
    '''
def getClientDTFromServerDT():
    '''    public Date getClientDTFromServerDT(final Date serverDateTime, final GregorianCalendar scratchCal)
    '''
def getWPEndDateTime():
    '''    public Date getWPEndDateTime(final MboRemote WorkTimeMbo, final Date wpStartDateTime, final GregorianCalendar scratchCal, final AvailCalc availCalc)
    '''
def getDayNAssignmentSet():
    '''    public MboSetRemote getDayNAssignmentSet(final MboRemote theLaborMbo, final Date wpStartDateTime, final Date wpEndDateTime)
    '''
def getAssignedHours():
    '''    public double getAssignedHours(final boolean insideCurrentDateWorkingTime, final Date rangeStartDateTime, final Date rangeFinishDateTime, final MboSetRemote dayNAssignmentSet)
    '''
def getEarliestUnassignedDateTime():
    '''    public Date getEarliestUnassignedDateTime(final MboSetRemote dayNAssignmentSet, final Date rangeStartDateTime, final Date rangeFinishDateTime)
    '''
def checkCalendarAndShift():
    '''    public void checkCalendarAndShift()
    '''
def updateCalendar():
    '''    public void updateCalendar()
    '''
def calculateAvailabilityData():
    '''    public void calculateAvailabilityData()
    '''
def hasCoords():
    '''    public Boolean hasCoords()
    '''
def getLatitudeY():
    '''    public Double getLatitudeY()
    '''
def getLongitudeX():
    '''    public Double getLongitudeX()
    '''
def getAddressString():
    '''    public String getAddressString()
    '''
def isGISDataReadonly():
    '''    public boolean isGISDataReadonly()
    '''
def saveGISData():
    '''    public void saveGISData(final String address, final String lat, final String lng)
    '''
def getLocationAccuracy():
    '''    public Double getLocationAccuracy()
    '''
def getAltitude():
    '''    public Double getAltitude()
    '''
def getAltitudeAccuracy():
    '''    public Double getAltitudeAccuracy()
    '''
def getHeading():
    '''    public Double getHeading()
    '''
def getLastUpdate():
    '''    public Date getLastUpdate()
    '''
def getSpeed():
    '''    public Double getSpeed()
    '''
def saveLBSData():
    '''    public void saveLBSData(final Double lat, final Double lng, final Double locationAccuracy, final Double altitudeAccuracy, final Double altitude, final Double heading, final Double speed)
    '''
def getEligibleHours():
    '''    public double[] getEligibleHours()
    '''
