PLUSC_OP_RGE_FROM = "String  \"PLUSCOPRGEFROM\""
PLUSC_OP_RGE_TO = "String  \"PLUSCOPRGETO\""
PLUSC_IS_CON_DESC = "String  \"PLUSCISCONDESC\""
PLUSC_IS_CON_DESC_LONGDESC = "String  \"PLUSCISCONDESC_LONGDESCRIPTION\""
PLUSC_IS_CONTAM = "String  \"PLUSCISCONTAM\""
PLUSC_IS_MTE_CLASS = "String  \"PLUSCISMTECLASS\""
PLUSC_IS_MTE = "String  \"PLUSCISMTE\""
PLUSC_DUE_DATE_NP = "String  \"PLUSCDUEDATE_NP\""
PLUSC_DUE_DATE = "String  \"PLUSCDUEDATE\""
PLUSC_IS_CALIBRATION = "String  \"ISCALIBRATION\""
def ():
    '''returns Asset\n\n
    (final MboSet ms)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def initFieldFlagsOnMbo():
    '''returns None\n\n
    initFieldFlagsOnMbo(final String attrName)\n
    '''
def getAssetMeterNowDate():
    '''returns Date\n\n
    getAssetMeterNowDate()\n
    '''
def modify():
    '''returns None\n\n
    modify()\n
    '''
def add():
    '''returns None\n\n
    add()\n
    '''
def updateDesc():
    '''returns None\n\n
    updateDesc()\n
    '''
def save():
    '''returns None\n\n
    save()\n
    '''
def createAssetTrans():
    '''returns MboRemote\n\n
    createAssetTrans()\n
    '''
def createMatRecTrans():
    '''returns MboRemote\n\n
    createMatRecTrans()\n
    '''
def delete():
    '''returns None\n\n
    delete(final long modifier)\n
    '''
def canDelete():
    '''returns None\n\n
    canDelete()\n
    '''
def appValidate():
    '''returns None\n\n
    appValidate()\n
    '''
def isInventoryTypeLocation():
    '''returns boolean\n\n
    isInventoryTypeLocation()\n
    '''
def isInventoryLocation():
    '''returns boolean\n\n
    isInventoryLocation()\n
    '''
def isDecommissionedLocation():
    '''returns boolean\n\n
    isDecommissionedLocation()\n
    '''
def getBinnum():
    '''returns None\n\n
    getBinnum()\n
    '''
def createHistoryForWorkOrder():
    '''returns None\n\n
    createHistoryForWorkOrder(final String wonum)\n
    '''
def setChildren():
    '''returns None\n\n
    setChildren(final boolean value)\n
    '''
def isRotating():
    '''returns boolean\n\n
    isRotating()\n
    '''
def recordAssetStatusChange():
    '''returns None\n\n
    recordAssetStatusChange(final MboRemote woMbo, final Date changeDate, final String code, final boolean operational)\n
    '''
def reportDowntime():
    '''returns None\n\n
    reportDowntime(final MboRemote woMbo, final Date startDate, final Date endDate, final double hoursDown, final String code, final boolean operational)\n
    '''
def lastAssetStatusForAssetnum():
    '''returns MboRemote\n\n
    lastAssetStatusForAssetnum()\n
    '''
def lastUpOrDownAssetStatusForAssetnum():
    '''returns MboRemote\n\n
    lastUpOrDownAssetStatusForAssetnum()\n
    '''
def intermediateAssetStatusExists():
    '''returns boolean\n\n
    intermediateAssetStatusExists(final Date newDTStart, final Date mostRecentNotRunningAssetStatusDate)\n
    '''
def calculateDownTime():
    '''returns double\n\n
    calculateDownTime(final Date lastChangeDate, final Date currentChangeDate)\n
    '''
def issueAsset():
    '''returns None\n\n
    issueAsset(final String newLocation, final String memo, final Date dateMoved, final String wonum, final boolean checkMismatch, final boolean checkOccupied, final boolean updateWo, final String matUseTransID)\n
    '''
def returnAsset():
    '''returns None\n\n
    returnAsset(final String newLocation, final String memo, final Date dateMoved, final String wonum, final String newBinnum, final String ponum, final String glCreditAcct, final String glDebitAcct, final boolean updateWo, final String matRecTransID)\n
    '''
def canReturnAsset():
    '''returns None\n\n
    canReturnAsset(final String newLocation, final String memo, final Date dateMoved, final String wonum, final String newBinnum, final String ponum, final String glCreditAcct, final String glDebitAcct, final boolean updateWo, final String matRecTransID)\n
    '''
def returnAssetForAsset():
    '''returns None\n\n
    returnAssetForAsset(final String newLocation, final String memo, final Date dateMoved, final String wonum, final String newBinnum, final String ponum, final String glCreditAcct, final String glDebitAcct, final boolean updateWo)\n
    '''
def moveAssetWithinNonInventory():
    '''returns None\n\n
    moveAssetWithinNonInventory(final String newLocation, final String memo, final Date dateMoved, final String enterBy, final String wonum, final String toParent, final boolean checkMismatch, final boolean checkOccupied, final boolean updateWo)\n
    moveAssetWithinNonInventory(final String newLocation, final String memo, final Date dateMoved, final String wonum, final String toParent, final boolean checkMismatch, final boolean checkOccupied, final boolean updateWo)\n
    '''
def canMoveAssetWithinNonInventory():
    '''returns None\n\n
    canMoveAssetWithinNonInventory(final String newLocation, final String memo, final Date dateMoved, final String enterBy, final String wonum, final String toParent, final boolean checkMismatch, final boolean checkOccupied, final boolean updateWo)\n
    canMoveAssetWithinNonInventory(final String newLocation, final String memo, final Date dateMoved, final String wonum, final String toParent, final boolean checkMismatch, final boolean checkOccupied, final boolean updateWo)\n
    '''
def moveAssetWithinInventory():
    '''returns None\n\n
    moveAssetWithinInventory(final String newLocation, final String memo, final Date dateMoved, final String newBinnum, final String ponum, final String glCreditAcct, final String glDebitAcct, final String matRecTransID)\n
    '''
def moveAssetWithinInventoryAcrossOrgFromHolding():
    '''returns None\n\n
    moveAssetWithinInventoryAcrossOrgFromHolding(final String newLocation, final String memo, final Date dateMoved, final String newBinnum, final String orgid, final String glCreditAcct, final String glDebitAcct, final String matRecTransID)\n
    '''
def canMoveAssetWithinInventory():
    '''returns None\n\n
    canMoveAssetWithinInventory(final String newLocation, final String memo, final Date dateMoved, final String newBinnum, final String ponum, final String glCreditAcct, final String glDebitAcct, final String matRecTransID)\n
    '''
def canMoveAssetWithinInventoryCrossOrgFromHolding():
    '''returns None\n\n
    canMoveAssetWithinInventoryCrossOrgFromHolding(final String newLocation, final String memo, final Date dateMoved, final String newBinnum, final String orgid, final String glCreditAcct, final String glDebitAcct, final String matRecTransID)\n
    '''
def isLocAuthorized():
    '''returns None\n\n
    isLocAuthorized(final MboRemote ofloc)\n
    '''
def isGLAccountValid():
    '''returns None\n\n
    isGLAccountValid(final String glAccount, final String glType)\n
    isGLAccountValid(final String glAccount, final String glType, final String orgId)\n
    '''
def isGLAccountPartialValid():
    '''returns None\n\n
    isGLAccountPartialValid(final String glAccount)\n
    '''
def incrInvCost():
    '''returns None\n\n
    incrInvCost(final double amount)\n
    '''
def isTop():
    '''returns boolean\n\n
    isTop()\n
    '''
def hasChildren():
    '''returns boolean\n\n
    hasChildren()\n
    '''
def hasParents():
    '''returns boolean\n\n
    hasParents()\n
    '''
def getChildren():
    '''returns MboSetRemote\n\n
    getChildren()\n
    '''
def getParents():
    '''returns MboSetRemote\n\n
    getParents()\n
    '''
def showHierarchy():
    '''returns MboSetRemote\n\n
    showHierarchy()\n
    '''
def walkUpHierarchy():
    '''returns Vector\n\n
    walkUpHierarchy()\n
    '''
def getTop():
    '''returns MboSetRemote\n\n
    getTop()\n
    '''
def getHierarchies():
    '''returns String[]\n\n
    getHierarchies()\n
    '''
def alreadyAppliedIAS():
    '''returns boolean\n\n
    alreadyAppliedIAS()\n
    '''
def canApplyIAS():
    '''returns None\n\n
    canApplyIAS()\n
    '''
def applyIAS():
    '''returns None\n\n
    applyIAS(final boolean autokey)\n
    '''
def applyIASAutoNumAll():
    '''returns None\n\n
    applyIASAutoNumAll()\n
    '''
def applyIASCreateChild():
    '''returns MboRemote\n\n
    applyIASCreateChild(final MboRemote itemStruct, final boolean autokey)\n
    '''
def isAssetBeingCreatedViaApplyIAS():
    '''returns boolean\n\n
    isAssetBeingCreatedViaApplyIAS()\n
    '''
def applyIASGenPMs():
    '''returns MboSetRemote\n\n
    applyIASGenPMs(final boolean autokey)\n
    '''
def applyIASGenSpareParts():
    '''returns MboSetRemote\n\n
    applyIASGenSpareParts(final MboSetRemote itemStructSet)\n
    '''
def autoKeyAll():
    '''returns None\n\n
    autoKeyAll(final boolean doChildren)\n
    '''
def setAssetnumOnRelated():
    '''returns None\n\n
    setAssetnumOnRelated()\n
    '''
def generateAutoKey():
    '''returns None\n\n
    generateAutoKey()\n
    '''
def autoKeyAssetnumForChildSet():
    '''returns None\n\n
    autoKeyAssetnumForChildSet(final boolean doChildren)\n
    '''
def autoKeyPmnumForSet():
    '''returns None\n\n
    autoKeyPmnumForSet(final boolean doChildren)\n
    '''
def setParent():
    '''returns None\n\n
    setParent(final String newParent)\n
    '''
def acceptMyNewSet():
    '''returns None\n\n
    acceptMyNewSet(final MboSetRemote myNewSet)\n
    '''
def getMyChildAssetSet():
    '''returns MboSetRemote\n\n
    getMyChildAssetSet()\n
    '''
def getMySparePartSet():
    '''returns MboSetRemote\n\n
    getMySparePartSet()\n
    '''
def getMyPMSet():
    '''returns MboSetRemote\n\n
    getMyPMSet()\n
    '''
def getMyParent():
    '''returns MboRemote\n\n
    getMyParent()\n
    '''
def getChild():
    '''returns MboRemote\n\n
    getChild(final int row)\n
    '''
def getValidateOrder():
    '''returns String[]\n\n
    getValidateOrder()\n
    '''
def zeroCosts():
    '''returns None\n\n
    zeroCosts(final boolean ytd, final boolean total)\n
    '''
def setItemNum():
    '''returns None\n\n
    setItemNum(final String newItem, final String itemSetID, final String conditionCode)\n
    '''
def appendDescription():
    '''returns None\n\n
    appendDescription(final String descSpec)\n
    '''
def generateAssetSpec():
    '''returns MboSetRemote\n\n
    generateAssetSpec()\n
    '''
def clearClassification():
    '''returns None\n\n
    clearClassification()\n
    '''
def duplicate():
    '''returns MboRemote\n\n
    duplicate()\n
    '''
def copySpareParts():
    '''returns None\n\n
    copySpareParts(final MboSetRemote spareParts)\n
    '''
def initRelationship():
    '''returns None\n\n
    initRelationship(final String relationName, final MboSetRemote mboSet)\n
    '''
def validateAssetSite():
    '''returns None\n\n
    validateAssetSite(final String asset_type, final String siteid)\n
    '''
def checkForAssetSite():
    '''returns None\n\n
    checkForAssetSite(final String siteid)\n
    '''
def checkForChildrenAssetSite():
    '''returns None\n\n
    checkForChildrenAssetSite(final String siteid)\n
    '''
def checkForNewAssetSite():
    '''returns None\n\n
    checkForNewAssetSite(final boolean replaceAssetFlag)\n
    '''
def setWoNumAssetMv():
    '''returns None\n\n
    setWoNumAssetMv(final String wonum)\n
    '''
def setPoNumAssetMv():
    '''returns None\n\n
    setPoNumAssetMv(final String ponum)\n
    '''
def getClearDupSeqNumsOnMeterGroupChange():
    '''returns boolean\n\n
    getClearDupSeqNumsOnMeterGroupChange()\n
    '''
def checkForDuplicateMeterSequenceValues():
    '''returns None\n\n
    checkForDuplicateMeterSequenceValues()\n
    '''
def getStatusListName():
    '''returns String\n\n
    getStatusListName()\n
    '''
def canChangeStatus():
    '''returns None\n\n
    canChangeStatus(final String changeToStatus, final long accessModifier)\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(final String status, final boolean rollToAllChildren, final boolean removeFromActiveRoutes, final boolean removeFromActiveSP, final boolean changePMStatus)\n
    changeStatus(final String status, boolean rollToAllChildren, final boolean removeFromActiveRoutes, final boolean removeFromActiveSP, final boolean changePMStatus, final Hashtable changedStatusPMs, final LocationRemote topLevelLocationOnStatusChangeFromLocStatChangeRollDown)\n
    changeStatus(final String status, final boolean rollToAllChildren, final boolean removeFromActiveRoutes, final boolean removeFromActiveSP, final boolean changePMStatus, final Hashtable changedStatusPMs)\n
    '''
def isActiveRoutes():
    '''returns boolean\n\n
    isActiveRoutes()\n
    '''
def isActiveSP():
    '''returns boolean\n\n
    isActiveSP()\n
    '''
def isActivePM():
    '''returns boolean\n\n
    isActivePM()\n
    '''
def createAssetToBeMoved():
    '''returns Asset\n\n
    createAssetToBeMoved()\n
    '''
def setValuesForMboSet():
    '''returns None\n\n
    setValuesForMboSet(final MboSetRemote mboSet)\n
    '''
def validateMoveAcrossOrg():
    '''returns None\n\n
    validateMoveAcrossOrg(final String siteid)\n
    '''
def validateCopySpecAcrossOrgSite():
    '''returns boolean\n\n
    validateCopySpecAcrossOrgSite(final String siteid)\n
    '''
def setAssetAttributesForWO():
    '''returns None\n\n
    setAssetAttributesForWO()\n
    setAssetAttributesForWO(final AutoAttrUpdateSetRemote autoAttrUpdateSet)\n
    '''
def getWarrantyInfo():
    '''returns List<Mbo>\n\n
    getWarrantyInfo(final Date woDate, final boolean isParent)\n
    getWarrantyInfo(final Date woDate, final boolean isParent, final String type)\n
    '''
def getParentAsset():
    '''returns MboRemote\n\n
    getParentAsset(final Date date)\n
    '''
def getRootParent():
    '''returns MboRemote\n\n
    getRootParent()\n
    '''
def assetMoved():
    '''returns None\n\n
    assetMoved()\n
    '''
def childInBundle():
    '''returns None\n\n
    childInBundle()\n
    '''
def addMoreAssetsToSet():
    '''returns None\n\n
    addMoreAssetsToSet(final MboSetRemote selectedMoreMboSet, final MboSetRemote selectedMboSet)\n
    '''
def hasMeters():
    '''returns None\n\n
    hasMeters()\n
    '''
def hasReadings():
    '''returns None\n\n
    hasReadings()\n
    '''
def getIssueUnitForItem():
    '''returns String\n\n
    getIssueUnitForItem(final String location)\n
    '''
def getLeaseContractForAsset():
    '''returns MboSetRemote\n\n
    getLeaseContractForAsset()\n
    '''
def getWarrantyContractForAsset():
    '''returns MboSetRemote\n\n
    getWarrantyContractForAsset()\n
    '''
def getPurchaseContractForAsset():
    '''returns MboSetRemote\n\n
    getPurchaseContractForAsset()\n
    '''
def getWarranty():
    '''returns MboSetRemote\n\n
    getWarranty()\n
    '''
def autoWogen():
    '''returns None\n\n
    autoWogen()\n
    autoWogen(final MboRemote assetMeter)\n
    '''
def setDefaults():
    '''returns None\n\n
    setDefaults(final String siteid, final String storeloc)\n
    '''
def getDefSiteId():
    '''returns String\n\n
    getDefSiteId()\n
    '''
def getDefStoreloc():
    '''returns String\n\n
    getDefStoreloc()\n
    '''
def createTicket():
    '''returns None\n\n
    createTicket(final MboRemote tkMbo)\n
    '''
def createWO():
    '''returns None\n\n
    createWO(final MboRemote workorderMbo)\n
    '''
def copyAssetToCollectDetailsSet():
    '''returns None\n\n
    copyAssetToCollectDetailsSet(final MboSetRemote collectionSet)\n
    '''
def createWorkorder():
    '''returns MboRemote\n\n
    createWorkorder(final String jpnum)\n
    '''
def createChange():
    '''returns MboRemote\n\n
    createChange(final String jpnum)\n
    '''
def createRelease():
    '''returns MboRemote\n\n
    createRelease(final String jpnum)\n
    '''
def createServiceRequest():
    '''returns MboRemote\n\n
    createServiceRequest(final String tickettemplateid)\n
    '''
def createProblem():
    '''returns MboRemote\n\n
    createProblem(final String tickettemplateid)\n
    '''
def createIncident():
    '''returns MboRemote\n\n
    createIncident(final String tickettemplateid)\n
    '''
def copyAdditionalPMAttributes():
    '''returns None\n\n
    copyAdditionalPMAttributes(final MboRemote copyToMbo, final MboRemote copyFromMbo)\n
    '''
def updateRelatedCI():
    '''returns None\n\n
    updateRelatedCI(final String newlocation, final String newsite, final String newassetnum, final boolean isChild, final String ChangeBy, final String ChangeDate)\n
    '''
def copyAssetSpecToAssetSpec():
    '''returns None\n\n
    copyAssetSpecToAssetSpec(final MboRemote newAsset)\n
    '''
def setInCopyingAssetSpecReceiveRotating():
    '''returns None\n\n
    setInCopyingAssetSpecReceiveRotating(final boolean inCopying)\n
    '''
def getInCopyingAssetSpecReceiveRotating():
    '''returns boolean\n\n
    getInCopyingAssetSpecReceiveRotating()\n
    '''
def setRememberToClearAssesInHash():
    '''returns None\n\n
    setRememberToClearAssesInHash(final boolean remberToClear)\n
    '''
def notifyAssetSpecValueChanged():
    '''returns None\n\n
    notifyAssetSpecValueChanged(final boolean valueChanged)\n
    '''
def isAssetSpecSetModified():
    '''returns boolean\n\n
    isAssetSpecSetModified()\n
    '''
def duplicateCalAsset():
    '''returns MboRemote\n\n
    duplicateCalAsset(final MboRemote newAssetRemote)\n
    '''
def setPhysicalLoc():
    '''returns None\n\n
    setPhysicalLoc()\n
    '''
def querySpotChecks():
    '''returns None\n\n
    querySpotChecks(final MboSetRemote plusWOSet, final Date fromDate, final Date toDate)\n
    '''
def queryDataSheets():
    '''returns None\n\n
    queryDataSheets(final PlusCWODSSetRemote woDsSet, final boolean loopCalibrations, final Date fromDate, final Date toDate)\n
    '''
def queryToolWoActuals():
    '''returns None\n\n
    queryToolWoActuals(final MboSetRemote plusWoSet, final Date fromDate, final Date toDate)\n
    '''
def viewDataSheets():
    '''returns MboSetRemote\n\n
    viewDataSheets(final MboRemote newDS)\n
    '''
def validateOperatingRange():
    '''returns None\n\n
    validateOperatingRange()\n
    '''
def calculateNextCalDueDate():
    '''returns Date\n\n
    calculateNextCalDueDate()\n
    '''
def getTagLocation():
    '''returns LocationRemote\n\n
    getTagLocation()\n
    '''
def getAssetBeingReplacedByThisInSwap():
    '''returns String[]\n\n
    getAssetBeingReplacedByThisInSwap()\n
    '''
def setAssetBeingReplacedByThisInSwap():
    '''returns None\n\n
    setAssetBeingReplacedByThisInSwap(final String[] assetBeingReplacedByThisInSwap)\n
    '''
def hasServiceAddress():
    '''returns boolean\n\n
    hasServiceAddress()\n
    '''
def saveGISData():
    '''returns None\n\n
    saveGISData(final String address, final String lat, final String lng)\n
    '''
def isGISDataReadonly():
    '''returns boolean\n\n
    isGISDataReadonly()\n
    '''
def getLatitudeY():
    '''returns Double\n\n
    getLatitudeY()\n
    '''
def getLongitudeX():
    '''returns Double\n\n
    getLongitudeX()\n
    '''
def getAddressString():
    '''returns String\n\n
    getAddressString()\n
    '''
def getMboSet():
    '''returns MboSetRemote\n\n
    getMboSet(final String name)\n
    '''
def getServiceAddress():
    '''returns ServiceAddressRemote\n\n
    getServiceAddress()\n
    '''
def getAutoLocateObject():
    '''returns MboRemote\n\n
    getAutoLocateObject(final AutoLocatable nextInChain)\n
    getAutoLocateObject()\n
    '''
def hasCoords():
    '''returns Boolean\n\n
    hasCoords()\n
    '''
def getLocationAccuracy():
    '''returns Double\n\n
    getLocationAccuracy()\n
    '''
def getAltitude():
    '''returns Double\n\n
    getAltitude()\n
    '''
def getAltitudeAccuracy():
    '''returns Double\n\n
    getAltitudeAccuracy()\n
    '''
def getHeading():
    '''returns Double\n\n
    getHeading()\n
    '''
def getLastUpdate():
    '''returns Date\n\n
    getLastUpdate()\n
    '''
def getSpeed():
    '''returns Double\n\n
    getSpeed()\n
    '''
def saveLBSData():
    '''returns None\n\n
    saveLBSData(final Double lat, final Double lng, final Double locationAccuracy, final Double altitudeAccuracy, final Double altitude, final Double heading, final Double speed)\n
    '''
def getLBSLatitudeY():
    '''returns Double\n\n
    getLBSLatitudeY()\n
    '''
def getLBSLongitudeX():
    '''returns Double\n\n
    getLBSLongitudeX()\n
    '''
def getPeriodTypeValue():
    '''returns String\n\n
    getPeriodTypeValue()\n
    '''
def createNewDepreciation():
    '''returns MboRemote\n\n
    createNewDepreciation()\n
    '''
def swapDepreciationSchedule():
    '''returns None\n\n
    swapDepreciationSchedule()\n
    '''
def swapDepreciationScheduleValidate():
    '''returns None\n\n
    swapDepreciationScheduleValidate()\n
    '''
def managePMMeterTallyOnMeterDeleteUndelete():
    '''returns None\n\n
    managePMMeterTallyOnMeterDeleteUndelete(final MboRemote pmMeter, final String action)\n
    '''
def getPMMeterTally():
    '''returns int\n\n
    getPMMeterTally(final MboRemote pmMeter)\n
    '''
def getCurrentMeterLife():
    '''returns Double\n\n
    getCurrentMeterLife(final String meterName)\n
    '''
def getDepreciationCurrentValue():
    '''returns Double\n\n
    getDepreciationCurrentValue()\n
    '''
def createDepreciationScheduleBasedOnItemFromMatrecTrans():
    '''returns MboRemote\n\n
    createDepreciationScheduleBasedOnItemFromMatrecTrans(final String itemNum, final String itemSetId, final MboRemote matrecTrans)\n
    '''
def createDepreciationScheduleBasedOnItem():
    '''returns None\n\n
    createDepreciationScheduleBasedOnItem(final MboRemote itemMbo)\n
    '''
def hasAssetSpecBeenCreated():
    '''returns boolean\n\n
    hasAssetSpecBeenCreated()\n
    '''
def setAssetSpecCreated():
    '''returns None\n\n
    setAssetSpecCreated(final boolean created)\n
    '''
def changeMaxStatus():
    '''returns None\n\n
    changeMaxStatus(final String internalStatus, final Date date, final String memo)\n
    '''
def assetInTransit():
    '''returns None\n\n
    assetInTransit()\n
    '''
