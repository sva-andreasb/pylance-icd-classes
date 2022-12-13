def LabTransSet():
    '''public LabTransSet(final MboServerInterface ms)
    '''
def setOwner():
    '''public void setOwner(final MboRemote mbo)
    '''
def setWork():
    '''public void setWork(final boolean workActLab)
    '''
def getWork():
    '''public boolean getWork()
    '''
def setNonWork():
    '''public void setNonWork(final boolean nonWorkActLab)
    '''
def getNonWork():
    '''public boolean getNonWork()
    '''
def setOTRefused():
    '''public void setOTRefused(final boolean otRefusedActLab)
    '''
def getOTRefused():
    '''public boolean getOTRefused()
    '''
def setUnapproved():
    '''public void setUnapproved(final boolean unapprovedActLab)
    '''
def getUnapproved():
    '''public boolean getUnapproved()
    '''
def setAllDates():
    '''public void setAllDates(final boolean allDatesActLab)
    '''
def setStartDate():
    '''public void setStartDate(final Date startDateActLab)
    '''
def setEndDate():
    '''public void setEndDate(final Date endDateActLab)
    '''
def getAllDates():
    '''public boolean getAllDates()
    '''
def getStartDate():
    '''public Date getStartDate()
    '''
def getEndDate():
    '''public Date getEndDate()
    '''
def addToUserPrefWhere():
    '''public String addToUserPrefWhere()
    '''
def getUserPrefWhere():
    '''public String getUserPrefWhere()
    '''
def addDates():
    '''public Date addDates(final Date date, final int days)
    '''
def canAdd():
    '''public void canAdd()
    '''
def addAtIndex():
    '''public MboRemote addAtIndex(final long accessModifier, final int index)
    '''
def remove():
    '''public void remove(final MboRemote mbo)
    '''
def addListener():
    '''public void addListener(final MboSetListener l)
    '''
def removeListener():
    '''public void removeListener(final MboSetListener l)
    '''
def reportModifiedMbo():
    '''public void reportModifiedMbo(final MboRemote modifiedMbo)
    '''
def startTimer():
    '''public MboRemote startTimer()
    public MboRemote startTimer(final Date targetDateTime)
    '''
def stopTimer():
    '''public MboRemote stopTimer()
    public MboRemote stopTimer(final Date targetStopDate, final boolean noStopTimerPopup)
    public MboRemote stopTimer(final Date targetStopDate, final Date startDateTime, final boolean noStopTimerPopup)
    '''
def setLaborSet():
    '''public void setLaborSet(final LaborSetRemote assignLaborSet)
    '''
def getLaborSet():
    '''public LaborSetRemote getLaborSet()
    '''
def setCraftSet():
    '''public void setCraftSet(final LaborSet assignCraftSet)
    '''
def getCraftSet():
    '''public LaborSet getCraftSet()
    '''
def copyPlannedLaborToLabTransSet():
    '''public void copyPlannedLaborToLabTransSet(final MboSetRemote wmassignmentsSet)
    '''
def copyLaborToLabTransSet():
    '''public void copyLaborToLabTransSet(final MboSetRemote laborSet)
    '''
def fromCopyLaborToLabTransSet():
    '''public boolean fromCopyLaborToLabTransSet()
    '''
def addDeltaHours():
    '''public void addDeltaHours(final String laborcode, final String orgid, final double reghrs, final double othrs)
    '''
def transCommitted():
    '''public void transCommitted()
    '''
def crewLabTrans():
    '''public MboRemote crewLabTrans(final String laborCode, final String laborOrg, final Date targetDateTime)
    '''
def activeTimer():
    '''public boolean activeTimer()
    '''
def forceDBSort():
    '''public boolean forceDBSort(final String attrName)
    '''
