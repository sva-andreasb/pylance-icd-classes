def ():
    '''returns AMCrewLaborSet\n\n
    (final MboServerInterface ms)\n
    '''
def getLaborRequirementStatus():
    '''returns String\n\n
    getLaborRequirementStatus(final MboRemote laborPos)\n
    '''
def getLaborPositionQualStatus():
    '''returns String\n\n
    getLaborPositionQualStatus(final MboRemote crewQual, final Date desireddate)\n
    '''
def getLaborQualStatus():
    '''returns String\n\n
    getLaborQualStatus(final MboRemote crewQual, final Date desireddate)\n
    '''
def getToBeDeletedMbo():
    '''returns MboRemote\n\n
    getToBeDeletedMbo()\n
    '''
def needRefresh():
    '''returns boolean\n\n
    needRefresh()\n
    '''
def getEffectiveDate():
    '''returns Date\n\n
    getEffectiveDate(Date effectivedate)\n
    '''
def getEffectiveDateTimeMinus():
    '''returns Date\n\n
    getEffectiveDateTimeMinus(Date effectivedate)\n
    '''
def getEffectiveDateTimePlus():
    '''returns Date\n\n
    getEffectiveDateTimePlus(Date effectivedate)\n
    '''
def getEndDate():
    '''returns Date\n\n
    getEndDate(Date enddate)\n
    '''
def getCurrentDate():
    '''returns Date\n\n
    getCurrentDate()\n
    '''
def removeLaborAssignment():
    '''returns MboSetRemote\n\n
    removeLaborAssignment(final MboRemote unrestrictedMbo, final MboRemote amCrewLab, final String dialogID)\n
    removeLaborAssignment(final MboRemote unrestrictedMbo, final MboRemote amCrewLab, final String dialogID, final MboRemote collision)\n
    '''
def createAMCrewLaborForRemove():
    '''returns None\n\n
    createAMCrewLaborForRemove(final MboRemote unrestrictedMbo, final MboRemote amCrewLab, final String dialogID)\n
    '''
def createAMCrewLabor():
    '''returns None\n\n
    createAMCrewLabor(final MboRemote unrestrictedMbo, final MboRemote owner)\n
    createAMCrewLabor(final MboRemote unrestrictedMbo, final MboRemote owner, final boolean fromNewRow, final String dialogID)\n
    createAMCrewLabor(final MboRemote unrestrictedMbo, final MboRemote owner, final boolean fromNewRow)\n
    '''
def checkExistingLabor():
    '''returns None\n\n
    checkExistingLabor(final MboRemote unrestrictedMbo, final MboRemote owner)\n
    '''
def checkForSecondEntry():
    '''returns None\n\n
    checkForSecondEntry(final MboRemote unrestrictedMbo, final MboRemote owner)\n
    '''
def createAMCrewLaborSqEntry():
    '''returns None\n\n
    createAMCrewLaborSqEntry(final MboRemote unrestrictedMbo, final MboRemote owner)\n
    '''
def checkPositionSequence():
    '''returns None\n\n
    checkPositionSequence(final MboRemote unrestrictedMbo, final MboRemote owner)\n
    '''
def checkSetInMemory():
    '''returns boolean\n\n
    checkSetInMemory(final MboRemote unrestrictedMbo, final MboSetRemote foundCollisions)\n
    checkSetInMemory(final MboRemote unrestrictedMbo, final MboSetRemote foundCollisions, final boolean findAnyOverlap)\n
    '''
def isFromNewRow():
    '''returns boolean\n\n
    isFromNewRow()\n
    '''
def setFromNewRow():
    '''returns None\n\n
    setFromNewRow(final boolean fromNewRow)\n
    '''
def updateStatusTableViewStatusDialog():
    '''returns None\n\n
    updateStatusTableViewStatusDialog()\n
    '''
def getEndDateTimePlus():
    '''returns Date\n\n
    getEndDateTimePlus(Date enddate)\n
    '''
