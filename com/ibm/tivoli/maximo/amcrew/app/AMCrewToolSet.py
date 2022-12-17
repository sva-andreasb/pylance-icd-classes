def ():
    '''returns AMCrewToolSet\n\n
    (final MboServerInterface ms)\n
    '''
def createAMCrewTool():
    '''returns None\n\n
    createAMCrewTool(final MboRemote unrestrictedMbo, final MboRemote owner)\n
    createAMCrewTool(final MboRemote unrestrictedMbo, final MboRemote owner, final boolean fromNewRow, final String dialogID)\n
    createAMCrewTool(final MboRemote unrestrictedMbo, final MboRemote owner, final boolean fromNewRow)\n
    '''
def checkExistingTools():
    '''returns None\n\n
    checkExistingTools(final MboRemote unrestrictedMbo, final MboRemote owner)\n
    '''
def checkForSecondEntry():
    '''returns None\n\n
    checkForSecondEntry(final MboRemote unrestrictedMbo, final MboRemote owner)\n
    '''
def createAMCrewToolSqEntry():
    '''returns None\n\n
    createAMCrewToolSqEntry(final MboRemote unrestrictedMbo, final MboRemote owner)\n
    '''
def removeToolAssignment():
    '''returns MboSetRemote\n\n
    removeToolAssignment(final MboRemote unrestrictedMbo, final MboRemote amCrewTool, final String dialogID)\n
    removeToolAssignment(final MboRemote unrestrictedMbo, final MboRemote amCrewTool, final String dialogID, final MboRemote collision)\n
    '''
def createAMCrewToolForRemove():
    '''returns None\n\n
    createAMCrewToolForRemove(final MboRemote unrestrictedMbo, final MboRemote amCrewTool, final String dialogID)\n
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
def setFromNewRow():
    '''returns None\n\n
    setFromNewRow(final boolean fromNewRow)\n
    '''
def isFromNewRow():
    '''returns boolean\n\n
    isFromNewRow()\n
    '''
def updateStatusTableViewStatusDialog():
    '''returns None\n\n
    updateStatusTableViewStatusDialog()\n
    '''
