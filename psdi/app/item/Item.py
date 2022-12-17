def ():
    '''returns Item\n\n
    (final MboSet ms)\n
    '''
def getProcess():
    '''returns String\n\n
    getProcess()\n
    '''
def getStatusListName():
    '''returns String\n\n
    getStatusListName()\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def setLotTypeReadOnly():
    '''returns None\n\n
    setLotTypeReadOnly(final boolean state)\n
    '''
def initFieldFlagsOnMbo():
    '''returns None\n\n
    initFieldFlagsOnMbo(final String attrName)\n
    '''
def add():
    '''returns None\n\n
    add()\n
    '''
def canAddKitToStore():
    '''returns None\n\n
    canAddKitToStore()\n
    '''
def canModifyKitStructure():
    '''returns None\n\n
    canModifyKitStructure()\n
    '''
def isNewKitComponentUniqueToSet():
    '''returns None\n\n
    isNewKitComponentUniqueToSet(final Mbo newKitItemStruct)\n
    '''
def duplicate():
    '''returns MboRemote\n\n
    duplicate()\n
    '''
def createTopItemStruct():
    '''returns None\n\n
    createTopItemStruct()\n
    '''
def autoKeyItemnum():
    '''returns None\n\n
    autoKeyItemnum()\n
    '''
def isRotating():
    '''returns boolean\n\n
    isRotating()\n
    '''
def isCapitalized():
    '''returns boolean\n\n
    isCapitalized()\n
    '''
def isKit():
    '''returns boolean\n\n
    isKit()\n
    '''
def toggleRotating():
    '''returns None\n\n
    toggleRotating()\n
    '''
def changeCapitalizedStatus():
    '''returns None\n\n
    changeCapitalizedStatus(final boolean capitalized)\n
    changeCapitalizedStatus(final boolean capitalized, final String capitalacc, final String memo)\n
    '''
def addToStore():
    '''returns InventoryRemote\n\n
    addToStore(final String store, final String category, final boolean validateLocationLater)\n
    addToStore(final String store)\n
    addToStore(final String store, final String category)\n
    '''
def isLotted():
    '''returns boolean\n\n
    isLotted()\n
    '''
def isConditionEnabled():
    '''returns boolean\n\n
    isConditionEnabled()\n
    '''
def getDefaultBin():
    '''returns String\n\n
    getDefaultBin()\n
    '''
def canDelete():
    '''returns None\n\n
    canDelete()\n
    '''
def delete():
    '''returns None\n\n
    delete(final long access)\n
    '''
def canSparePartAutoAdd():
    '''returns boolean\n\n
    canSparePartAutoAdd()\n
    '''
def sparePartExists():
    '''returns boolean\n\n
    sparePartExists(final String assetnum, final String siteid)\n
    '''
def addSparePart():
    '''returns MboRemote\n\n
    addSparePart(final String assetnum, final String siteid)\n
    '''
def applyIAS():
    '''returns None\n\n
    applyIAS(final MboRemote applyToMbo)\n
    '''
def createItemSpecSet():
    '''returns MboSetRemote\n\n
    createItemSpecSet()\n
    '''
def updateDesc():
    '''returns None\n\n
    updateDesc()\n
    '''
def updateRelatedObjects():
    '''returns None\n\n
    updateRelatedObjects(final String newStatus, final Date date, final String memo)\n
    '''
def appValidate():
    '''returns None\n\n
    appValidate()\n
    '''
def save():
    '''returns None\n\n
    save()\n
    '''
def appendDescription():
    '''returns None\n\n
    appendDescription(final String descSpec)\n
    '''
def generateAutoKey():
    '''returns None\n\n
    generateAutoKey()\n
    '''
def generateItemSpec():
    '''returns MboSetRemote\n\n
    generateItemSpec()\n
    '''
def processItemSpecSet():
    '''returns None\n\n
    processItemSpecSet()\n
    '''
def clearClassification():
    '''returns None\n\n
    clearClassification()\n
    '''
def removeSpecialOrderItems():
    '''returns boolean\n\n
    removeSpecialOrderItems(final Vector storeLoc)\n
    '''
def getOneHundredPercent():
    '''returns MboRemote\n\n
    getOneHundredPercent()\n
    '''
def setThisComponentsKitAndDefaultBin():
    '''returns None\n\n
    setThisComponentsKitAndDefaultBin(final String kitNum, final String defaultBin)\n
    '''
def getThisComponentsKit():
    '''returns String\n\n
    getThisComponentsKit()\n
    '''
def getThisComponentsDefaultBin():
    '''returns String\n\n
    getThisComponentsDefaultBin()\n
    '''
def getInternalItemType():
    '''returns String\n\n
    getInternalItemType()\n
    '''
def checkWOExists():
    '''returns boolean\n\n
    checkWOExists()\n
    '''
def checkInvBalancesExists():
    '''returns boolean\n\n
    checkInvBalancesExists()\n
    '''
def checkAssetExists():
    '''returns boolean\n\n
    checkAssetExists()\n
    '''
def checkJPExists():
    '''returns boolean\n\n
    checkJPExists()\n
    '''
def checkMRExists():
    '''returns boolean\n\n
    checkMRExists()\n
    '''
def checkPRExists():
    '''returns boolean\n\n
    checkPRExists()\n
    '''
def checkPOExists():
    '''returns boolean\n\n
    checkPOExists()\n
    '''
def checkContractExists():
    '''returns boolean\n\n
    checkContractExists()\n
    '''
def checkCIExists():
    '''returns boolean\n\n
    checkCIExists()\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(final String status, final Date date, final String memo, final long accessModifier)\n
    changeStatus(final String status, boolean rolldown, final Date date, final String memo, final long accessModifier)\n
    '''
def validateChangeStatus():
    '''returns None\n\n
    validateChangeStatus(final String status, final boolean rolldown, final Date date, final String memo)\n
    '''
def isPendobs():
    '''returns boolean\n\n
    isPendobs()\n
    '''
def isObsolete():
    '''returns boolean\n\n
    isObsolete()\n
    '''
def isPlanning():
    '''returns boolean\n\n
    isPlanning()\n
    '''
def isRollDown():
    '''returns boolean\n\n
    isRollDown()\n
    '''
def updateInvVendor():
    '''returns None\n\n
    updateInvVendor()\n
    '''
def setUseThisItemSpecSet():
    '''returns None\n\n
    setUseThisItemSpecSet(final MboSetRemote itemSpecSet)\n
    '''
def getUseThisItemSpecSet():
    '''returns MboSetRemote\n\n
    getUseThisItemSpecSet()\n
    '''
def updateRotatingClassStructureSQLServer():
    '''returns None\n\n
    updateRotatingClassStructureSQLServer(String where, int counter, final long accessModifier)\n
    '''
def getNumberOfRotatingAssets():
    '''returns int\n\n
    getNumberOfRotatingAssets()\n
    '''
def processUpdateClassStructureID():
    '''returns None\n\n
    processUpdateClassStructureID(final String updateSql)\n
    '''
def getMboSet():
    '''returns MboSetRemote\n\n
    getMboSet(final String name)\n
    '''
def checkKitCostType():
    '''returns None\n\n
    checkKitCostType(final boolean isKit)\n
    '''
def createNewDepreciation():
    '''returns MboRemote\n\n
    createNewDepreciation()\n
    '''
def validateDepreciation():
    '''returns None\n\n
    validateDepreciation()\n
    '''
