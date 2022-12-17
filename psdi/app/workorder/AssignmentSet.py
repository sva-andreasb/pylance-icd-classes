def ():
    '''returns AssignmentSet\n\n
    (final MboServerInterface ms)\n
    '''
def assignmentsForLaborCode():
    '''returns None\n\n
    assignmentsForLaborCode(final String labor)\n
    '''
def assignmentsForLaborCodeAndWorkOrder():
    '''returns None\n\n
    assignmentsForLaborCodeAndWorkOrder(final String labor, final String woIDs)\n
    '''
def assignmentsForCrewAndWorkOrder():
    '''returns None\n\n
    assignmentsForCrewAndWorkOrder(final String amcrew, final long[] workOrderIds)\n
    '''
def addToUserPrefWhere():
    '''returns String\n\n
    addToUserPrefWhere()\n
    '''
def getUserPrefWhere():
    '''returns String\n\n
    getUserPrefWhere()\n
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
def getSevenDayWindow():
    '''returns None\n\n
    getSevenDayWindow(final CalendarViewSetRemote calendarViewSet)\n
    '''
def getAddedAssignments():
    '''returns Vector<Long>\n\n
    getAddedAssignments()\n
    '''
def setDeletingAsgnmentsOnYesNoCx():
    '''returns None\n\n
    setDeletingAsgnmentsOnYesNoCx(final boolean deletingAsgnmentsOnYesNoCx)\n
    '''
def save():
    '''returns None\n\n
    save()\n
    '''
def fireEventsAfterDB():
    '''returns None\n\n
    fireEventsAfterDB(final MXTransaction txn)\n
    '''
def getRescheduled():
    '''returns int\n\n
    getRescheduled()\n
    '''
def getUnassigned():
    '''returns int\n\n
    getUnassigned()\n
    '''
def setRescheduled():
    '''returns None\n\n
    setRescheduled(final int rescheduled)\n
    '''
def setUnassigned():
    '''returns None\n\n
    setUnassigned(final int unassigned)\n
    '''
def assignLabor():
    '''returns None\n\n
    assignLabor(final LaborCraftRateRemote laborCraftRateMbo, final String theDay)\n
    '''
def startAssignment():
    '''returns MboSetRemote\n\n
    startAssignment()\n
    '''
def interruptAssignment():
    '''returns MboSetRemote\n\n
    interruptAssignment()\n
    '''
def finishAssignment():
    '''returns MboSetRemote\n\n
    finishAssignment()\n
    '''
def getColumnValue():
    '''returns String\n\n
    getColumnValue(final String columnName)\n
    '''
def getFinishDate():
    '''returns Date\n\n
    getFinishDate()\n
    '''
def setFinishDate():
    '''returns None\n\n
    setFinishDate(final Date finishDate)\n
    '''
def getEarliestDate():
    '''returns Date\n\n
    getEarliestDate()\n
    '''
def getLatestDate():
    '''returns Date\n\n
    getLatestDate()\n
    '''
def assignCrew():
    '''returns None\n\n
    assignCrew(final AMCrewRemote crewMbo, final String theDay)\n
    '''
def getUserAndQbeWhere():
    '''returns String\n\n
    getUserAndQbeWhere()\n
    '''
def fireEventsAfterDBCommit():
    '''returns None\n\n
    fireEventsAfterDBCommit(final MXTransaction txn)\n
    '''
