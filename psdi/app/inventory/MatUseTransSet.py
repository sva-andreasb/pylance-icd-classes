def ():
    '''returns MatUseTransSet\n\n
    (final MboServerInterface ms)\n
    '''
def copyInvReserveSet():
    '''returns None\n\n
    copyInvReserveSet(final MboSetRemote invReserveSet)\n
    '''
def copySparePartSet():
    '''returns None\n\n
    copySparePartSet(final MboSetRemote sparePartSet)\n
    '''
def addMatUseFromInvReserve():
    '''returns MboRemote\n\n
    addMatUseFromInvReserve(final MboRemote invRes)\n
    '''
def copyMatUseTransSet():
    '''returns None\n\n
    copyMatUseTransSet(final MboSetRemote matUseSet)\n
    '''
def setDateRange():
    '''returns None\n\n
    setDateRange(final int type)\n
    '''
def getDateRange():
    '''returns int\n\n
    getDateRange()\n
    '''
def setLastNDays():
    '''returns None\n\n
    setLastNDays(final int nDays)\n
    '''
def getLastNDays():
    '''returns int\n\n
    getLastNDays()\n
    '''
def setStartDate():
    '''returns None\n\n
    setStartDate(final Date startDateActLab)\n
    '''
def setEndDate():
    '''returns None\n\n
    setEndDate(final Date endDateActLab)\n
    '''
def getStartDate():
    '''returns Date\n\n
    getStartDate()\n
    '''
def getEndDate():
    '''returns Date\n\n
    getEndDate()\n
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
def returnIPCParts():
    '''returns None\n\n
    returnIPCParts(final IpcSelectedPartsSetRemote partset)\n
    '''
def preValidateIpcBom():
    '''returns None\n\n
    preValidateIpcBom(final IpcBomSetRemote bomset)\n
    '''
def addDeltaCurbal():
    '''returns None\n\n
    addDeltaCurbal(final MboRemote invBal, final double quantity, final MboRemote currentMatUse)\n
    '''
def addDeltaIssueYTD():
    '''returns None\n\n
    addDeltaIssueYTD(final MboRemote inventory, final double quantity, final MboRemote currentMatUse)\n
    '''
def transCommitted():
    '''returns None\n\n
    transCommitted()\n
    '''
def getInvReserveVector():
    '''returns Vector\n\n
    getInvReserveVector()\n
    '''
def getUncommittedTransVector():
    '''returns Vector\n\n
    getUncommittedTransVector()\n
    '''
def setUncommittedTransVector():
    '''returns None\n\n
    setUncommittedTransVector(final Vector uncommitted)\n
    '''
def clearVectors():
    '''returns None\n\n
    clearVectors()\n
    '''
def storeToRotatingAssetHash():
    '''returns None\n\n
    storeToRotatingAssetHash(final MboRemote matUse)\n
    '''
def rotAssetExists():
    '''returns MboRemote\n\n
    rotAssetExists(final MboRemote matUse)\n
    '''
def getLifoFifoInHash():
    '''returns Hashtable\n\n
    getLifoFifoInHash()\n
    '''
