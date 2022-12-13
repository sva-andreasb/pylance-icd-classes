def LabTransSet():
'''public LabTransSet(final MboServerInterface ms)
'''
pass
def setOwner():
'''public void setOwner(final MboRemote mbo)
'''
pass
def setWork():
'''public void setWork(final boolean workActLab)
'''
pass
def getWork():
'''public boolean getWork()
'''
pass
def setNonWork():
'''public void setNonWork(final boolean nonWorkActLab)
'''
pass
def getNonWork():
'''public boolean getNonWork()
'''
pass
def setOTRefused():
'''public void setOTRefused(final boolean otRefusedActLab)
'''
pass
def getOTRefused():
'''public boolean getOTRefused()
'''
pass
def setUnapproved():
'''public void setUnapproved(final boolean unapprovedActLab)
'''
pass
def getUnapproved():
'''public boolean getUnapproved()
'''
pass
def setAllDates():
'''public void setAllDates(final boolean allDatesActLab)
'''
pass
def setStartDate():
'''public void setStartDate(final Date startDateActLab)
'''
pass
def setEndDate():
'''public void setEndDate(final Date endDateActLab)
'''
pass
def getAllDates():
'''public boolean getAllDates()
'''
pass
def getStartDate():
'''public Date getStartDate()
'''
pass
def getEndDate():
'''public Date getEndDate()
'''
pass
def addToUserPrefWhere():
'''public String addToUserPrefWhere()
'''
pass
def getUserPrefWhere():
'''public String getUserPrefWhere()
'''
pass
def addDates():
'''public Date addDates(final Date date, final int days)
'''
pass
def canAdd():
'''public void canAdd()
'''
pass
def addAtIndex():
'''public MboRemote addAtIndex(final long accessModifier, final int index)
'''
pass
def remove():
'''public void remove(final MboRemote mbo)
'''
pass
def addListener():
'''public void addListener(final MboSetListener l)
'''
pass
def removeListener():
'''public void removeListener(final MboSetListener l)
'''
pass
def reportModifiedMbo():
'''public void reportModifiedMbo(final MboRemote modifiedMbo)
'''
pass
def startTimer():
'''public MboRemote startTimer()
public MboRemote startTimer(final Date targetDateTime)
'''
pass
def stopTimer():
'''public MboRemote stopTimer()
public MboRemote stopTimer(final Date targetStopDate, final boolean noStopTimerPopup)
public MboRemote stopTimer(final Date targetStopDate, final Date startDateTime, final boolean noStopTimerPopup)
'''
pass
def setLaborSet():
'''public void setLaborSet(final LaborSetRemote assignLaborSet)
'''
pass
def getLaborSet():
'''public LaborSetRemote getLaborSet()
'''
pass
def setCraftSet():
'''public void setCraftSet(final LaborSet assignCraftSet)
'''
pass
def getCraftSet():
'''public LaborSet getCraftSet()
'''
pass
def copyPlannedLaborToLabTransSet():
'''public void copyPlannedLaborToLabTransSet(final MboSetRemote wmassignmentsSet)
'''
pass
def copyLaborToLabTransSet():
'''public void copyLaborToLabTransSet(final MboSetRemote laborSet)
'''
pass
def fromCopyLaborToLabTransSet():
'''public boolean fromCopyLaborToLabTransSet()
'''
pass
def addDeltaHours():
'''public void addDeltaHours(final String laborcode, final String orgid, final double reghrs, final double othrs)
'''
pass
def transCommitted():
'''public void transCommitted()
'''
pass
def crewLabTrans():
'''public MboRemote crewLabTrans(final String laborCode, final String laborOrg, final Date targetDateTime)
'''
pass
def activeTimer():
'''public boolean activeTimer()
'''
pass
def forceDBSort():
'''public boolean forceDBSort(final String attrName)
'''
pass
