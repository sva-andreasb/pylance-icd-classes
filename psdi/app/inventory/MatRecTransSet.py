def clearVector():
    '''returns None\n\n
    clearVector()\n
    '''
def addWarnings():
    '''returns None\n\n
    addWarnings(final MXException mx)\n
    '''
def ():
    '''returns MatRecTransSet\n\n
    (final MboServerInterface ms)\n
    '''
def validateOrderQty():
    '''returns None\n\n
    validateOrderQty()\n
    '''
def deleteUnSelected():
    '''returns None\n\n
    deleteUnSelected()\n
    '''
def copyInvReserveSet():
    '''returns None\n\n
    copyInvReserveSet(final MboSetRemote invReserveSet, final String inOrOut)\n
    '''
def copySparePartSet():
    '''returns None\n\n
    copySparePartSet(final MboSetRemote sparePartSet, final String inOrOut)\n
    '''
def copyInvBalancesSet():
    '''returns None\n\n
    copyInvBalancesSet(final MboSetRemote invBalancesSet, final String inOrOut)\n
    '''
def copyPOLineSet():
    '''returns None\n\n
    copyPOLineSet(final MboSetRemote poLineSet, final String inOrOut)\n
    '''
def warningsFromCopyPOItems():
    '''returns None\n\n
    warningsFromCopyPOItems()\n
    '''
def copyMatRecTransSet():
    '''returns None\n\n
    copyMatRecTransSet(final MboSetRemote matRecTransSet, final String inOrOut)\n
    '''
def warningsFromCopyMatRecTransItems():
    '''returns None\n\n
    warningsFromCopyMatRecTransItems()\n
    '''
def setLocation():
    '''returns None\n\n
    setLocation(final String loc)\n
    '''
def getLocation():
    '''returns String\n\n
    getLocation()\n
    '''
def setPONum():
    '''returns None\n\n
    setPONum(final String po)\n
    '''
def getPONum():
    '''returns String\n\n
    getPONum()\n
    '''
def approveReceipts():
    '''returns Vector\n\n
    approveReceipts(final Date todaysDate)\n
    '''
def canAdd():
    '''returns None\n\n
    canAdd()\n
    '''
def setQbe():
    '''returns None\n\n
    setQbe(final String attribute, final String expression)\n
    '''
def getUserWhere():
    '''returns String\n\n
    getUserWhere(final String alias)\n
    '''
def resetQbe():
    '''returns None\n\n
    resetQbe()\n
    '''
def createAssets():
    '''returns None\n\n
    createAssets(final String ponum, final int polinenum, final String ownersysid, final String siteid)\n
    '''
def createReturnsForAssets():
    '''returns None\n\n
    createReturnsForAssets(final PO po, final MboSetRemote matRecTransAssetSetRemote)\n
    '''
def checkInspectedTotal():
    '''returns None\n\n
    checkInspectedTotal()\n
    '''
def returnIPCParts():
    '''returns None\n\n
    returnIPCParts(final IpcSelectedPartsSetRemote partset)\n
    '''
def preValidateIpcBom():
    '''returns None\n\n
    preValidateIpcBom(final IpcBomSetRemote bomset)\n
    '''
def setToExecuteCompleteAdd():
    '''returns None\n\n
    setToExecuteCompleteAdd(final boolean toset)\n
    '''
def toExecuteCompleteAdd():
    '''returns boolean\n\n
    toExecuteCompleteAdd()\n
    '''
def getNumberOfActualDateExceptions():
    '''returns int\n\n
    getNumberOfActualDateExceptions()\n
    '''
def incrNumberOfActualDateExceptions():
    '''returns None\n\n
    incrNumberOfActualDateExceptions(final int i)\n
    '''
def setCrossOrgExchangeRate():
    '''returns None\n\n
    setCrossOrgExchangeRate(final MboRemote newMatRec, final MboRemote transferOutMatRec)\n
    '''
def setLineNumAssetMap():
    '''returns None\n\n
    setLineNumAssetMap(final String linenum, final String rotassetnum)\n
    '''
def setShipReceiptCountMap():
    '''returns None\n\n
    setShipReceiptCountMap(final String linenum, final long count)\n
    '''
def setVoidShipReceiptCountMap():
    '''returns None\n\n
    setVoidShipReceiptCountMap(final String linenum, final long count)\n
    '''
