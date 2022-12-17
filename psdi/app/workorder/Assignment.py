def ():
    '''returns Assignment\n\n
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
def calledFromAssignmentManager():
    '''returns boolean\n\n
    calledFromAssignmentManager()\n
    '''
def completeAssignment():
    '''returns None\n\n
    completeAssignment(final String status, final Date date)\n
    completeAssignment()\n
    completeAssignment(final boolean completeWO)\n
    '''
def getLabTransSet():
    '''returns LabTransSetRemote\n\n
    getLabTransSet()\n
    '''
def createLabTrans():
    '''returns None\n\n
    createLabTrans(final WORemote ownerWO)\n
    '''
def getToolTransSet():
    '''returns ToolTransSetRemote\n\n
    getToolTransSet()\n
    '''
def createToolTransCrew():
    '''returns None\n\n
    createToolTransCrew(final WORemote ownerWO, final AMCrewRemote crew)\n
    '''
def completeTheWO():
    '''returns None\n\n
    completeTheWO(final WORemote ownerWO)\n
    '''
def canFinishWO():
    '''returns boolean\n\n
    canFinishWO(final WO woMbo)\n
    '''
def getWPEndDateTime():
    '''returns Date\n\n
    getWPEndDateTime(final MboRemote WorkTimeMbo, final Date wpStartDateTime, final GregorianCalendar scratchCal, final AvailCalc availCalc)\n
    '''
def calcFinishDate():
    '''returns None\n\n
    calcFinishDate()\n
    '''
def propagateKeyValue():
    '''returns None\n\n
    propagateKeyValue(final String keyName, final String keyValue)\n
    '''
def startAssignment():
    '''returns None\n\n
    startAssignment(final Date startDate)\n
    '''
def interruptAssignment():
    '''returns None\n\n
    interruptAssignment(final Date interruptDate)\n
    '''
def finishAssignment():
    '''returns None\n\n
    finishAssignment(final Date finishDate)\n
    '''
def getCrewWorkZoneWhere():
    '''returns String\n\n
    getCrewWorkZoneWhere(final MboRemote owner)\n
    getCrewWorkZoneWhere(final String assetNum, final String location, final String siteId, final String orgId)\n
    '''
def getLaborWorkZoneWhere():
    '''returns String\n\n
    getLaborWorkZoneWhere(final String assetNum, final String location, final String siteId, final String orgId)\n
    getLaborWorkZoneWhere(final MboRemote owner)\n
    '''
def countMembers():
    '''returns int\n\n
    countMembers()\n
    '''
def getAvailableLabor():
    '''returns MboSetRemote\n\n
    getAvailableLabor()\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def undelete():
    '''returns None\n\n
    undelete()\n
    '''
def modify():
    '''returns None\n\n
    modify()\n
    '''
