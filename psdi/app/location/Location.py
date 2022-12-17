def ():
    '''returns Location\n\n
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
def setReadonlyForOperORStoreAfterAdd():
    '''returns None\n\n
    setReadonlyForOperORStoreAfterAdd()\n
    '''
def add():
    '''returns None\n\n
    add()\n
    '''
def generateAutoKey():
    '''returns None\n\n
    generateAutoKey()\n
    '''
def getLocationMeterNowDate():
    '''returns Date\n\n
    getLocationMeterNowDate()\n
    '''
def modify():
    '''returns None\n\n
    modify()\n
    '''
def delete():
    '''returns None\n\n
    delete(final long access)\n
    '''
def canDelete():
    '''returns None\n\n
    canDelete()\n
    '''
def cannotChangeStatus():
    '''returns None\n\n
    cannotChangeStatus(final MboSetRemote msr)\n
    '''
def isStore():
    '''returns boolean\n\n
    isStore()\n
    '''
def isCourier():
    '''returns boolean\n\n
    isCourier()\n
    '''
def isHolding():
    '''returns boolean\n\n
    isHolding()\n
    '''
def isLabor():
    '''returns boolean\n\n
    isLabor()\n
    '''
def isOperating():
    '''returns boolean\n\n
    isOperating()\n
    '''
def isDecommissioned():
    '''returns boolean\n\n
    isDecommissioned()\n
    '''
def isVendor():
    '''returns boolean\n\n
    isVendor()\n
    '''
def authorizeUserStore():
    '''returns None\n\n
    authorizeUserStore(final String user)\n
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
def getChildrenInAllSystems():
    '''returns MboSetRemote\n\n
    getChildrenInAllSystems()\n
    '''
def getParents():
    '''returns MboSetRemote\n\n
    getParents()\n
    getParents(final String SystemId)\n
    '''
def getTop():
    '''returns MboSetRemote\n\n
    getTop()\n
    '''
def getHierarchies():
    '''returns String[]\n\n
    getHierarchies()\n
    '''
def showHierarchy():
    '''returns MboSetRemote\n\n
    showHierarchy()\n
    '''
def walkUpHierarchy():
    '''returns Vector\n\n
    walkUpHierarchy()\n
    '''
def getChildrenInPrimary():
    '''returns MboSetRemote\n\n
    getChildrenInPrimary()\n
    getChildrenInPrimary(final String locSiteId)\n
    '''
def inPrimarySystem():
    '''returns boolean\n\n
    inPrimarySystem()\n
    inPrimarySystem(final String locSiteId)\n
    '''
def getPrimaryLocations():
    '''returns MboSetRemote\n\n
    getPrimaryLocations()\n
    '''
def getNonPrimaryLocations():
    '''returns MboSetRemote\n\n
    getNonPrimaryLocations()\n
    '''
def getLocItem():
    '''returns String\n\n
    getLocItem()\n
    '''
def isLocationOccupied():
    '''returns boolean\n\n
    isLocationOccupied(final MboRemote asset)\n
    isLocationOccupied(final String itemnum)\n
    '''
def doesHoldingLocationExistForSite():
    '''returns boolean\n\n
    doesHoldingLocationExistForSite(final String siteid)\n
    '''
def getHoldingLocationForSite():
    '''returns MboRemote\n\n
    getHoldingLocationForSite(final String siteid)\n
    '''
def isInventory():
    '''returns boolean\n\n
    isInventory()\n
    '''
def updateDesc():
    '''returns None\n\n
    updateDesc()\n
    '''
def appValidate():
    '''returns None\n\n
    appValidate()\n
    '''
def save():
    '''returns None\n\n
    save()\n
    '''
def updateGLInfo():
    '''returns None\n\n
    updateGLInfo()\n
    '''
def generateLocationMetersForMeterGroup():
    '''returns None\n\n
    generateLocationMetersForMeterGroup()\n
    '''
def getClearDupSeqNumsOnMeterGroupChange():
    '''returns boolean\n\n
    getClearDupSeqNumsOnMeterGroupChange()\n
    '''
def checkForDuplicateMeterSequenceValues():
    '''returns None\n\n
    checkForDuplicateMeterSequenceValues()\n
    '''
def appendDescription():
    '''returns None\n\n
    appendDescription(final String descSpec)\n
    '''
def generateLocationSpec():
    '''returns MboSetRemote\n\n
    generateLocationSpec()\n
    '''
def canApplyIAS():
    '''returns boolean\n\n
    canApplyIAS()\n
    '''
def applyIAS():
    '''returns Object[]\n\n
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
def applyIASGenPMs():
    '''returns MboSetRemote\n\n
    applyIASGenPMs(final boolean autokey)\n
    '''
def canChangeStatus():
    '''returns None\n\n
    canChangeStatus(final String changeToStatus, final long accessModifier)\n
    '''
def setInitNonInteractiveStatChange():
    '''returns None\n\n
    setInitNonInteractiveStatChange(final boolean value)\n
    '''
def getInitNonInteractiveStatChange():
    '''returns boolean\n\n
    getInitNonInteractiveStatChange()\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(final String status, final Date asOfDate, final String memo, final long accessModifier)\n
    changeStatus(final String changedStatus, final Date asOfDate, final String memo, boolean rolltoallchildren, final boolean removefromallroutes, boolean rolltoallassets, final boolean removefromalljp, final boolean removefromactivesp, final boolean changepmstatus)\n
    '''
def trackStatusChangedAssetInLocations():
    '''returns None\n\n
    trackStatusChangedAssetInLocations(final long assetuid)\n
    '''
def hasAssetStatusChangedAlready():
    '''returns boolean\n\n
    hasAssetStatusChangedAlready(final long assetuid)\n
    '''
def isReferencedByOpenWO():
    '''returns boolean\n\n
    isReferencedByOpenWO()\n
    '''
def isReferencedByPM():
    '''returns boolean\n\n
    isReferencedByPM()\n
    '''
def isReferencedByActiveRoutes():
    '''returns boolean\n\n
    isReferencedByActiveRoutes()\n
    '''
def isReferencedByActiveSP():
    '''returns boolean\n\n
    isReferencedByActiveSP()\n
    '''
def isReferencedByJobPlans():
    '''returns boolean\n\n
    isReferencedByJobPlans()\n
    '''
def duplicate():
    '''returns MboRemote\n\n
    duplicate()\n
    '''
def copyInvReserveSetForIssues():
    '''returns None\n\n
    copyInvReserveSetForIssues(final MboSetRemote invReserveSet)\n
    '''
def copyInvReserveSetForTransferOut():
    '''returns None\n\n
    copyInvReserveSetForTransferOut(final MboSetRemote invReserveSet)\n
    '''
def copyInvReserveSetForTransferIn():
    '''returns None\n\n
    copyInvReserveSetForTransferIn(final MboSetRemote invReserveSet)\n
    '''
def copyMatUseTransSetForReturn():
    '''returns None\n\n
    copyMatUseTransSetForReturn(final MboSetRemote matUseSet)\n
    '''
def receiveRotableAssetOnMoveFromNonInventoryWithPOLine():
    '''returns MboRemote\n\n
    receiveRotableAssetOnMoveFromNonInventoryWithPOLine(final MboRemote asset, final String glCredit, final String glDebit, final MboRemote mrtMbo)\n
    '''
def receiveRotableAssetOnMoveFromNonInventory():
    '''returns MboRemote\n\n
    receiveRotableAssetOnMoveFromNonInventory(final MboRemote asset, final String glCredit, final String glDebit)\n
    '''
def copySparePartSetForIssues():
    '''returns None\n\n
    copySparePartSetForIssues(final MboSetRemote sparePartSet)\n
    '''
def copySparePartSetForTransferOut():
    '''returns None\n\n
    copySparePartSetForTransferOut(final MboSetRemote sparePartSet)\n
    '''
def copySparePartSetForTransferIn():
    '''returns None\n\n
    copySparePartSetForTransferIn(final MboSetRemote sparePartSet)\n
    '''
def copyInvBalancesSetForTransferOut():
    '''returns None\n\n
    copyInvBalancesSetForTransferOut(final MboSetRemote invBalancesSet)\n
    '''
def copyInvBalancesSetForTransferIn():
    '''returns None\n\n
    copyInvBalancesSetForTransferIn(final MboSetRemote invBalancesSet)\n
    '''
def copyPOLineSetForTransferOut():
    '''returns None\n\n
    copyPOLineSetForTransferOut(final MboSetRemote poLineSet)\n
    '''
def warningsCopyPOLineSetForTransferOut():
    '''returns None\n\n
    warningsCopyPOLineSetForTransferOut()\n
    '''
def copyPOLineSetForTransferIn():
    '''returns None\n\n
    copyPOLineSetForTransferIn(final MboSetRemote poLineSet)\n
    '''
def copyMatRecTransSetForTransferIn():
    '''returns None\n\n
    copyMatRecTransSetForTransferIn(final MboSetRemote matRecTransSet)\n
    '''
def getStatusListName():
    '''returns String\n\n
    getStatusListName()\n
    '''
def warningsCopyPOLineSetForTransferIn():
    '''returns None\n\n
    warningsCopyPOLineSetForTransferIn()\n
    '''
def warningsCopyMatRecTransSetForTransferIn():
    '''returns None\n\n
    warningsCopyMatRecTransSetForTransferIn()\n
    '''
def initRelationship():
    '''returns None\n\n
    initRelationship(final String relationName, final MboSetRemote mboSet)\n
    '''
def selectPOItemsOut():
    '''returns MboSetRemote\n\n
    selectPOItemsOut()\n
    '''
def selectReservedItemsOut():
    '''returns MboSetRemote\n\n
    selectReservedItemsOut()\n
    '''
def selectItemsForTransferOut():
    '''returns MboSetRemote\n\n
    selectItemsForTransferOut()\n
    '''
def selectPOItemsIn():
    '''returns MboSetRemote\n\n
    selectPOItemsIn()\n
    '''
def selectMatRecTransIn():
    '''returns MboSetRemote\n\n
    selectMatRecTransIn()\n
    '''
def selectReservedItemsIn():
    '''returns MboSetRemote\n\n
    selectReservedItemsIn()\n
    '''
def selectItemsForTransferIn():
    '''returns MboSetRemote\n\n
    selectItemsForTransferIn()\n
    '''
def selectItemsForReturn():
    '''returns MboSetRemote\n\n
    selectItemsForReturn()\n
    '''
def selectReservedItems():
    '''returns MboSetRemote\n\n
    selectReservedItems()\n
    '''
def canAssociateSystem():
    '''returns boolean\n\n
    canAssociateSystem()\n
    '''
def clearClassification():
    '''returns None\n\n
    clearClassification()\n
    '''
def setLocationAttributesForWO():
    '''returns None\n\n
    setLocationAttributesForWO()\n
    setLocationAttributesForWO(final AutoAttrUpdateSetRemote autoAttrUpdateSet)\n
    '''
def getWarrantyInfo():
    '''returns List\n\n
    getWarrantyInfo(final Date woDate, final boolean isParent)\n
    getWarrantyInfo(final Date woDate, final boolean isParent, final String type)\n
    '''
def hasMeters():
    '''returns None\n\n
    hasMeters()\n
    '''
def hasReadings():
    '''returns None\n\n
    hasReadings()\n
    '''
def getAssetForLocation():
    '''returns String\n\n
    getAssetForLocation()\n
    '''
def getLeaseContractForLocation():
    '''returns MboSetRemote\n\n
    getLeaseContractForLocation()\n
    '''
def getWarranty():
    '''returns MboSetRemote\n\n
    getWarranty()\n
    '''
def getWarrantyContractForLocation():
    '''returns MboSetRemote\n\n
    getWarrantyContractForLocation()\n
    '''
def autoWogen():
    '''returns None\n\n
    autoWogen()\n
    autoWogen(final MboRemote locationMeter)\n
    '''
def createTicket():
    '''returns None\n\n
    createTicket(final MboRemote tkMbo)\n
    '''
def createWO():
    '''returns None\n\n
    createWO(final MboRemote workorderMbo)\n
    '''
def copyLocationToCollectDetailsSet():
    '''returns None\n\n
    copyLocationToCollectDetailsSet(final MboSetRemote collectionSet)\n
    '''
def addLocationsToCollectDetails():
    '''returns None\n\n
    addLocationsToCollectDetails(final String collectionNum)\n
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
def validateOrderQty():
    '''returns None\n\n
    validateOrderQty()\n
    '''
def queryDataSheets():
    '''returns None\n\n
    queryDataSheets(final PlusCWODSSetRemote woDsSet, final boolean loopCalibrations, final Date fromDate, final Date toDate)\n
    '''
def canBeUsedAsTagId():
    '''returns boolean\n\n
    canBeUsedAsTagId()\n
    '''
def getAssociatedAsset():
    '''returns AssetRemote\n\n
    getAssociatedAsset()\n
    '''
def getAddressSystemForLocationMbo():
    '''returns MboRemote\n\n
    getAddressSystemForLocationMbo()\n
    '''
def getAncestorSABasedOnAddressSystem():
    '''returns MboRemote\n\n
    getAncestorSABasedOnAddressSystem(final MboRemote child)\n
    '''
def getMboSet():
    '''returns MboSetRemote\n\n
    getMboSet(final String name)\n
    '''
def getServiceAddress():
    '''returns ServiceAddressRemote\n\n
    getServiceAddress()\n
    '''
def hasServiceAddress():
    '''returns boolean\n\n
    hasServiceAddress()\n
    '''
def saveGISData():
    '''returns None\n\n
    saveGISData(final String address, final String lat, final String lng)\n
    '''
def getLatitudeY():
    '''returns Double\n\n
    getLatitudeY()\n
    '''
def getLongitudeX():
    '''returns Double\n\n
    getLongitudeX()\n
    '''
def isGISDataReadonly():
    '''returns boolean\n\n
    isGISDataReadonly()\n
    '''
def getAddressString():
    '''returns String\n\n
    getAddressString()\n
    '''
def addMoreLocationsToSet():
    '''returns None\n\n
    addMoreLocationsToSet(final MboSetRemote selectedMoreMboSet, final MboSetRemote selectedMboSet)\n
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
def getTopParentInSystem():
    '''returns MboRemote\n\n
    getTopParentInSystem(final String SystemId)\n
    '''
def managePMMeterTallyOnMeterDeleteUndelete():
    '''returns None\n\n
    managePMMeterTallyOnMeterDeleteUndelete(final MboRemote pmMeter, final String action)\n
    '''
def getPMMeterTally():
    '''returns int\n\n
    getPMMeterTally(final MboRemote pmMeter)\n
    '''
def getChildrenInSystem():
    '''returns MboSetRemote\n\n
    getChildrenInSystem()\n
    '''
