crewDurStatic = "String  \"Static\""
crewDurDynamic = "String  \"Dynamic\""
crewDurCrewPos = "String  \"PLUSDCRW\""
def AMCrew():
    '''public AMCrew(final MboSet ms)
    '''
def init():
    '''public void init()
    '''
def add():
    '''public void add()
    '''
def changeStatus():
    '''public void changeStatus(final String status, final Date date, final String memo, final long accessModifier)
    public void changeStatus(final String newStatus, final String memo)
    '''
def canDelete():
    '''public void canDelete()
    '''
def delete():
    '''public void delete(final long accessModifier)
    '''
def duplicate():
    '''public MboRemote duplicate()
    '''
def getStatusListName():
    '''public String getStatusListName()
    '''
def associateCrewType():
    '''public void associateCrewType()
    '''
def refreshkRequirements():
    '''public void refreshkRequirements()
    '''
def checkCalendarAndShift():
    '''public void checkCalendarAndShift()
    '''
def setWorkHrs():
    '''public void setWorkHrs(final Date DayOneClientDate)
    '''
def getServerDTFromClientDT():
    '''public Date getServerDTFromClientDT(final Date clientDateTime, final GregorianCalendar scratchCal)
    '''
def getClientDTFromServerDT():
    '''public Date getClientDTFromServerDT(final Date serverDateTime, final GregorianCalendar scratchCal)
    '''
def getAvailableMbo():
    '''public MboRemote getAvailableMbo(final Date startDate)
    '''
def getAvailableMboList():
    '''public List<MboRemote> getAvailableMboList(final Date startDate)
    '''
def getDateTime():
    '''public Date getDateTime(final Date workdt, final Date sttime)
    '''
def getWPEndDateTime():
    '''public Date getWPEndDateTime(final MboRemote WorkTimeMbo, final Date wpStartDateTime, final GregorianCalendar scratchCal)
    '''
def getDayNAssignmentSet():
    '''public MboSetRemote getDayNAssignmentSet(final MboRemote theCrewMbo, final Date wpStartDateTime, final Date wpEndDateTime)
    '''
def getAvailableHours():
    '''public double getAvailableHours(final Date startDate)
    '''
def getAssignedHours():
    '''public double getAssignedHours(final boolean insideCurrentDateWorkingTime, final Date wpStartDateTime, final Date wpEndDateTime, final MboSetRemote dayNAssignmentSet)
    '''
def getServerDateColumn():
    '''public Date[] getServerDateColumn()
    '''
def setServerDateColumn():
    '''public void setServerDateColumn(final Date[] newServerDateColumn)
    '''
def getLabors():
    '''public Collection getLabors(final Date currentDate)
    '''
def getTools():
    '''public Collection getTools(final Date currentDate)
    '''
def isAMGridCreated():
    '''public boolean isAMGridCreated()
    '''
def setAMGridCreated():
    '''public void setAMGridCreated(final boolean gridCreated)
    '''
def childHasChanged():
    '''public void childHasChanged()
    '''
def getMboSet():
    '''public MboSetRemote getMboSet(final String name)
    '''
def calculateAvailabilityData():
    '''public void calculateAvailabilityData()
    '''
def updateStandardRate():
    '''public void updateStandardRate()
    '''
def getEarliestUnassignedDateTime():
    '''public Date getEarliestUnassignedDateTime(final MboSetRemote dayNAssignmentSet, final Date rangeStartDateTime, final Date rangeFinishDateTime)
    '''
def getLatitudeY():
    '''public Double getLatitudeY()
    '''
def hasCoords():
    '''public Boolean hasCoords()
    '''
def getLongitudeX():
    '''public Double getLongitudeX()
    '''
def getAddressString():
    '''public String getAddressString()
    '''
def isGISDataReadonly():
    '''public boolean isGISDataReadonly()
    '''
def saveGISData():
    '''public void saveGISData(final String address, final String lat, final String lng)
    '''
def getLocationAccuracy():
    '''public Double getLocationAccuracy()
    '''
def getAltitude():
    '''public Double getAltitude()
    '''
def getAltitudeAccuracy():
    '''public Double getAltitudeAccuracy()
    '''
def getHeading():
    '''public Double getHeading()
    '''
def getLastUpdate():
    '''public Date getLastUpdate()
    '''
def getSpeed():
    '''public Double getSpeed()
    '''
def saveLBSData():
    '''public void saveLBSData(final Double lat, final Double lng, final Double locationAccuracy, final Double altitudeAccuracy, final Double altitude, final Double heading, final Double speed)
    '''
def getValidContract():
    '''public MboRemote getValidContract(final Date startDate)
    '''
def getCompositeWP():
    '''public MboRemote getCompositeWP(final List<MboRemote> modAvailList, final Date workDate)
    '''
def getCurrentShiftHours():
    '''public double getCurrentShiftHours(final Date workdate)
    '''
def getCurrentShiftStartDate():
    '''public Date getCurrentShiftStartDate(final Date effectiveDate)
    '''
def getCurrentShiftEndDate():
    '''public Date getCurrentShiftEndDate(final Date endDate)
    '''
def setCrewDate():
    '''public void setCrewDate(final Date date)
    '''
def getCrewDate():
    '''public Date getCrewDate()
    '''
def getCrewMemberCount():
    '''public int getCrewMemberCount(final Date desiredDate)
    '''
def setDateTo():
    '''public void setDateTo(final Date dateTo)
    '''
def getDateTo():
    '''public Date getDateTo()
    '''
def getEligibleHours():
    '''public double[] getEligibleHours()
    '''
