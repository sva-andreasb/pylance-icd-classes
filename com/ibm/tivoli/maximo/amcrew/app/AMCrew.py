crewDurStatic = "String  Static""
crewDurDynamic = "String  Dynamic""
crewDurCrewPos = "String  PLUSDCRW""
def AMCrew():
'''public AMCrew(final MboSet ms)
'''
pass
def init():
'''public void init()
'''
pass
def add():
'''public void add()
'''
pass
def changeStatus():
'''public void changeStatus(final String status, final Date date, final String memo, final long accessModifier)
public void changeStatus(final String newStatus, final String memo)
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
def duplicate():
'''public MboRemote duplicate()
'''
pass
def getStatusListName():
'''public String getStatusListName()
'''
pass
def associateCrewType():
'''public void associateCrewType()
'''
pass
def refreshkRequirements():
'''public void refreshkRequirements()
'''
pass
def checkCalendarAndShift():
'''public void checkCalendarAndShift()
'''
pass
def setWorkHrs():
'''public void setWorkHrs(final Date DayOneClientDate)
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
def getAvailableMbo():
'''public MboRemote getAvailableMbo(final Date startDate)
'''
pass
def getAvailableMboList():
'''public List<MboRemote> getAvailableMboList(final Date startDate)
'''
pass
def getDateTime():
'''public Date getDateTime(final Date workdt, final Date sttime)
'''
pass
def getWPEndDateTime():
'''public Date getWPEndDateTime(final MboRemote WorkTimeMbo, final Date wpStartDateTime, final GregorianCalendar scratchCal)
'''
pass
def getDayNAssignmentSet():
'''public MboSetRemote getDayNAssignmentSet(final MboRemote theCrewMbo, final Date wpStartDateTime, final Date wpEndDateTime)
'''
pass
def getAvailableHours():
'''public double getAvailableHours(final Date startDate)
'''
pass
def getAssignedHours():
'''public double getAssignedHours(final boolean insideCurrentDateWorkingTime, final Date wpStartDateTime, final Date wpEndDateTime, final MboSetRemote dayNAssignmentSet)
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
def getLabors():
'''public Collection getLabors(final Date currentDate)
'''
pass
def getTools():
'''public Collection getTools(final Date currentDate)
'''
pass
def isAMGridCreated():
'''public boolean isAMGridCreated()
'''
pass
def setAMGridCreated():
'''public void setAMGridCreated(final boolean gridCreated)
'''
pass
def childHasChanged():
'''public void childHasChanged()
'''
pass
def getMboSet():
'''public MboSetRemote getMboSet(final String name)
'''
pass
def calculateAvailabilityData():
'''public void calculateAvailabilityData()
'''
pass
def updateStandardRate():
'''public void updateStandardRate()
'''
pass
def getEarliestUnassignedDateTime():
'''public Date getEarliestUnassignedDateTime(final MboSetRemote dayNAssignmentSet, final Date rangeStartDateTime, final Date rangeFinishDateTime)
'''
pass
def getLatitudeY():
'''public Double getLatitudeY()
'''
pass
def hasCoords():
'''public Boolean hasCoords()
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
def getValidContract():
'''public MboRemote getValidContract(final Date startDate)
'''
pass
def getCompositeWP():
'''public MboRemote getCompositeWP(final List<MboRemote> modAvailList, final Date workDate)
'''
pass
def getCurrentShiftHours():
'''public double getCurrentShiftHours(final Date workdate)
'''
pass
def getCurrentShiftStartDate():
'''public Date getCurrentShiftStartDate(final Date effectiveDate)
'''
pass
def getCurrentShiftEndDate():
'''public Date getCurrentShiftEndDate(final Date endDate)
'''
pass
def setCrewDate():
'''public void setCrewDate(final Date date)
'''
pass
def getCrewDate():
'''public Date getCrewDate()
'''
pass
def getCrewMemberCount():
'''public int getCrewMemberCount(final Date desiredDate)
'''
pass
def setDateTo():
'''public void setDateTo(final Date dateTo)
'''
pass
def getDateTo():
'''public Date getDateTo()
'''
pass
def getEligibleHours():
'''public double[] getEligibleHours()
'''
pass
