def ():
    '''returns LabTransSet\n\n
    (final MboServerInterface ms)\n
    '''
def setOwner():
    '''returns None\n\n
    setOwner(final MboRemote mbo)\n
    '''
def setWork():
    '''returns None\n\n
    setWork(final boolean workActLab)\n
    '''
def getWork():
    '''returns boolean\n\n
    getWork()\n
    '''
def setNonWork():
    '''returns None\n\n
    setNonWork(final boolean nonWorkActLab)\n
    '''
def getNonWork():
    '''returns boolean\n\n
    getNonWork()\n
    '''
def setOTRefused():
    '''returns None\n\n
    setOTRefused(final boolean otRefusedActLab)\n
    '''
def getOTRefused():
    '''returns boolean\n\n
    getOTRefused()\n
    '''
def setUnapproved():
    '''returns None\n\n
    setUnapproved(final boolean unapprovedActLab)\n
    '''
def getUnapproved():
    '''returns boolean\n\n
    getUnapproved()\n
    '''
def setAllDates():
    '''returns None\n\n
    setAllDates(final boolean allDatesActLab)\n
    '''
def setStartDate():
    '''returns None\n\n
    setStartDate(final Date startDateActLab)\n
    '''
def setEndDate():
    '''returns None\n\n
    setEndDate(final Date endDateActLab)\n
    '''
def getAllDates():
    '''returns boolean\n\n
    getAllDates()\n
    '''
def getStartDate():
    '''returns Date\n\n
    getStartDate()\n
    '''
def getEndDate():
    '''returns Date\n\n
    getEndDate()\n
    '''
def addToUserPrefWhere():
    '''returns String\n\n
    addToUserPrefWhere()\n
    '''
def getUserPrefWhere():
    '''returns String\n\n
    getUserPrefWhere()\n
    '''
def addDates():
    '''returns Date\n\n
    addDates(final Date date, final int days)\n
    '''
def canAdd():
    '''returns None\n\n
    canAdd()\n
    '''
def addAtIndex():
    '''returns MboRemote\n\n
    addAtIndex(final long accessModifier, final int index)\n
    '''
def remove():
    '''returns None\n\n
    remove(final MboRemote mbo)\n
    '''
def addListener():
    '''returns None\n\n
    addListener(final MboSetListener l)\n
    '''
def removeListener():
    '''returns None\n\n
    removeListener(final MboSetListener l)\n
    '''
def reportModifiedMbo():
    '''returns None\n\n
    reportModifiedMbo(final MboRemote modifiedMbo)\n
    '''
def startTimer():
    '''returns MboRemote\n\n
    startTimer()\n
    startTimer(final Date targetDateTime)\n
    '''
def stopTimer():
    '''returns MboRemote\n\n
    stopTimer()\n
    stopTimer(final Date targetStopDate, final boolean noStopTimerPopup)\n
    stopTimer(final Date targetStopDate, final Date startDateTime, final boolean noStopTimerPopup)\n
    '''
def setLaborSet():
    '''returns None\n\n
    setLaborSet(final LaborSetRemote assignLaborSet)\n
    '''
def getLaborSet():
    '''returns LaborSetRemote\n\n
    getLaborSet()\n
    '''
def setCraftSet():
    '''returns None\n\n
    setCraftSet(final LaborSet assignCraftSet)\n
    '''
def getCraftSet():
    '''returns LaborSet\n\n
    getCraftSet()\n
    '''
def copyPlannedLaborToLabTransSet():
    '''returns None\n\n
    copyPlannedLaborToLabTransSet(final MboSetRemote wmassignmentsSet)\n
    '''
def copyLaborToLabTransSet():
    '''returns None\n\n
    copyLaborToLabTransSet(final MboSetRemote laborSet)\n
    '''
def fromCopyLaborToLabTransSet():
    '''returns boolean\n\n
    fromCopyLaborToLabTransSet()\n
    '''
def addDeltaHours():
    '''returns None\n\n
    addDeltaHours(final String laborcode, final String orgid, final double reghrs, final double othrs)\n
    '''
def transCommitted():
    '''returns None\n\n
    transCommitted()\n
    '''
def crewLabTrans():
    '''returns MboRemote\n\n
    crewLabTrans(final String laborCode, final String laborOrg, final Date targetDateTime)\n
    '''
def activeTimer():
    '''returns boolean\n\n
    activeTimer()\n
    '''
def forceDBSort():
    '''returns boolean\n\n
    forceDBSort(final String attrName)\n
    '''
