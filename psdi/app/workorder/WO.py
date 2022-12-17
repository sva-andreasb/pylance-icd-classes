crewDurStatic = "String  \"Static\""
crewDurDynamic = "String  \"Dynamic\""
crewDurCrewPos = "String  \"PLUSDCRW\""
APPLYASSETLOC = "String  \"WO.ApplyingAssetLoc\""
def isChangeInHierarchy():
    '''returns boolean\n\n
    isChangeInHierarchy()\n
    '''
def setChangeInHierarchy():
    '''returns None\n\n
    setChangeInHierarchy(final boolean changeInHierarchy)\n
    '''
def getPreviousParent():
    '''returns String\n\n
    getPreviousParent()\n
    '''
def setPreviousParent():
    '''returns None\n\n
    setPreviousParent(final String previousParent)\n
    '''
def ():
    '''returns compareJPTask\n\n
    (final MboSet ms)\n
    ()\n
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
def isCharacteristic():
    '''returns boolean\n\n
    isCharacteristic()\n
    '''
def canEditRelatedSet():
    '''returns None\n\n
    canEditRelatedSet(final String relationName)\n
    '''
def setRelatedMboEditibility():
    '''returns None\n\n
    setRelatedMboEditibility(final String relationName)\n
    '''
def initRelationship():
    '''returns None\n\n
    initRelationship(final String relationName, final MboSetRemote mboSet)\n
    '''
def modify():
    '''returns None\n\n
    modify()\n
    '''
def add():
    '''returns None\n\n
    add()\n
    '''
def updateServiceAddress():
    '''returns None\n\n
    updateServiceAddress()\n
    '''
def createJobEntry():
    '''returns MboRemote\n\n
    createJobEntry()\n
    '''
def createAssignRepLoc():
    '''returns None\n\n
    createAssignRepLoc()\n
    '''
def getCrewMemberCount():
    '''returns int\n\n
    getCrewMemberCount(final Date desiredDate)\n
    '''
def copyDoclinksToWO():
    '''returns None\n\n
    copyDoclinksToWO()\n
    copyDoclinksToWO(final WO wo)\n
    '''
def inChildSubSet():
    '''returns boolean\n\n
    inChildSubSet()\n
    '''
def canDelete():
    '''returns None\n\n
    canDelete()\n
    '''
def getSimilarWorkOrders():
    '''returns WOSetRemote\n\n
    getSimilarWorkOrders()\n
    '''
def getAlreadyReportedSet():
    '''returns WOSetRemote\n\n
    getAlreadyReportedSet()\n
    '''
def getLocForAsset():
    '''returns None\n\n
    getLocForAsset()\n
    '''
def applyAssetLoc():
    '''returns None\n\n
    applyAssetLoc()\n
    applyAssetLoc(final boolean calcSafetyPlan)\n
    '''
def copyJobPlanToWorkPlan():
    '''returns None\n\n
    copyJobPlanToWorkPlan()\n
    '''
def copyJobPlanToWorkPlanNoNestedJP():
    '''returns None\n\n
    copyJobPlanToWorkPlanNoNestedJP()\n
    '''
def clearWorkPlanInfo():
    '''returns None\n\n
    clearWorkPlanInfo()\n
    '''
def calculateConstaintDates():
    '''returns None\n\n
    calculateConstaintDates(final MboValue startOffset, final MboValue finishOffset, final MboValue woDur)\n
    '''
def getAddingFirstJobTask():
    '''returns boolean\n\n
    getAddingFirstJobTask()\n
    '''
def getCopyingJobTasks():
    '''returns boolean\n\n
    getCopyingJobTasks()\n
    '''
def getCopyingWorkPlanAssignments():
    '''returns boolean\n\n
    getCopyingWorkPlanAssignments()\n
    '''
def applyingJobPlan():
    '''returns boolean\n\n
    applyingJobPlan()\n
    '''
def setParentValuesForNestedjpWO():
    '''returns None\n\n
    setParentValuesForNestedjpWO(final MboRemote newChild, final MboRemote parent)\n
    '''
def generateTaskID():
    '''returns None\n\n
    generateTaskID()\n
    '''
def copySafetyPlanToWoSafetyPlan():
    '''returns None\n\n
    copySafetyPlanToWoSafetyPlan()\n
    '''
def setJobPlanFieldFlag():
    '''returns None\n\n
    setJobPlanFieldFlag()\n
    '''
def startWFOnWoReqSave():
    '''returns boolean\n\n
    startWFOnWoReqSave()\n
    '''
def updateForMovedAsset():
    '''returns None\n\n
    updateForMovedAsset(final MboRemote movedAsset)\n
    '''
def incrEstLabCost():
    '''returns None\n\n
    incrEstLabCost(final double incrAmount, final boolean isExternal)\n
    '''
def incrEstLabHours():
    '''returns None\n\n
    incrEstLabHours(final double incrAmount, final boolean isExternal)\n
    '''
def incrEstToolCost():
    '''returns None\n\n
    incrEstToolCost(final double incrAmount)\n
    '''
def incrEstMatCost():
    '''returns None\n\n
    incrEstMatCost(final double incrAmount)\n
    '''
def incrEstServCost():
    '''returns None\n\n
    incrEstServCost(final double incrAmount)\n
    '''
def incrActMatCost():
    '''returns None\n\n
    incrActMatCost(final double incrAmount, final boolean isOutsideCost)\n
    '''
def incrActLabCost():
    '''returns None\n\n
    incrActLabCost(final double incrAmount, final boolean isOutsideCost)\n
    '''
def incrActLabHrs():
    '''returns None\n\n
    incrActLabHrs(final double incrAmount, final boolean isExternal)\n
    '''
def incrActToolCost():
    '''returns None\n\n
    incrActToolCost(final double incrAmount, final boolean isOutsideCost)\n
    '''
def incrActServCost():
    '''returns None\n\n
    incrActServCost(final double incrAmount)\n
    '''
def haveReceivedDirectIssue():
    '''returns None\n\n
    haveReceivedDirectIssue(final MboRemote poMbo, final MboRemote poLineMbo)\n
    '''
def getValidateOrder():
    '''returns String[]\n\n
    getValidateOrder()\n
    '''
def isCanceled():
    '''returns boolean\n\n
    isCanceled()\n
    '''
def generateAutoKey():
    '''returns None\n\n
    generateAutoKey()\n
    '''
def isAssetChargeStore():
    '''returns boolean\n\n
    isAssetChargeStore()\n
    '''
def canChargeStore():
    '''returns boolean\n\n
    canChargeStore()\n
    '''
def calcGLAccount():
    '''returns None\n\n
    calcGLAccount()\n
    '''
def getSubWorkOrders():
    '''returns MboSetRemote\n\n
    getSubWorkOrders()\n
    '''
def canApplyRoute():
    '''returns None\n\n
    canApplyRoute()\n
    canApplyRoute(final long accessModifier)\n
    canApplyRoute(final String routeID)\n
    canApplyRoute(final String routeID, final long accessModifier)\n
    '''
def applyRoute():
    '''returns None\n\n
    applyRoute(final String routeID, final String storeLoc)\n
    applyRoute(final String routeID, final String storeLoc, final String storeLocSite)\n
    applyRoute(final String routeID, final String storeLoc, final String storeLocSite, final long accessModifier)\n
    applyRoute(final String routeID, final String storeLoc, final String storeLocSite, final long accessModifier, final MboSetRemote infoSet)\n
    '''
def getGrandTotals():
    '''returns Vector\n\n
    getGrandTotals()\n
    '''
def getDuplicated():
    '''returns boolean\n\n
    getDuplicated()\n
    '''
def setDuplicated():
    '''returns None\n\n
    setDuplicated(final boolean duplicated)\n
    '''
def duplicate():
    '''returns MboRemote\n\n
    duplicate()\n
    '''
def canGenFollowUpWo():
    '''returns None\n\n
    canGenFollowUpWo()\n
    '''
def genFollowUpWo():
    '''returns MboRemote\n\n
    genFollowUpWo()\n
    '''
def setSafetyPlanFieldFlag():
    '''returns None\n\n
    setSafetyPlanFieldFlag()\n
    '''
def getServiceTotal():
    '''returns double\n\n
    getServiceTotal()\n
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
def hasSafetyPlan():
    '''returns boolean\n\n
    hasSafetyPlan()\n
    '''
def getChildren():
    '''returns MboSetRemote\n\n
    getChildren()\n
    '''
def getChildNoTask():
    '''returns MboSetRemote\n\n
    getChildNoTask()\n
    '''
def getTasksOnly():
    '''returns MboSetRemote\n\n
    getTasksOnly()\n
    '''
def getParents():
    '''returns MboSetRemote\n\n
    getParents()\n
    '''
def getTop():
    '''returns MboSetRemote\n\n
    getTop()\n
    '''
def getHierarchies():
    '''returns String[]\n\n
    getHierarchies()\n
    '''
def copySparePartsToWpMatSet():
    '''returns None\n\n
    copySparePartsToWpMatSet(final MboSetRemote sparePartSet)\n
    '''
def copySparePartsToMatUseSet():
    '''returns None\n\n
    copySparePartsToMatUseSet(final MboSetRemote sparePartSet)\n
    '''
def copyInvresvItemsToMatUseSet():
    '''returns None\n\n
    copyInvresvItemsToMatUseSet(final MboSetRemote InvresvItemSet)\n
    '''
def copyPlanToolToToolTransSet():
    '''returns None\n\n
    copyPlanToolToToolTransSet(final MboSetRemote planToolSet)\n
    '''
def copyPlanLaborToLabTransSet():
    '''returns None\n\n
    copyPlanLaborToLabTransSet(final MboSetRemote planLaborSet)\n
    '''
def applyHazardToWoHazardSet():
    '''returns None\n\n
    applyHazardToWoHazardSet(final MboRemote spRelatedasset, final MboSetRemote hazardSet)\n
    '''
def enterQuickReportingMode():
    '''returns None\n\n
    enterQuickReportingMode()\n
    '''
def isQuickReportingMode():
    '''returns boolean\n\n
    isQuickReportingMode()\n
    '''
def isApproved():
    '''returns boolean\n\n
    isApproved()\n
    '''
def getTaskForWonum():
    '''returns String\n\n
    getTaskForWonum(final String wonum)\n
    '''
def getWOforTask():
    '''returns MboRemote\n\n
    getWOforTask(final String task)\n
    '''
def getWOforWonum():
    '''returns WORemote\n\n
    getWOforWonum(final String wonum)\n
    '''
def getWOClassDescription():
    '''returns String\n\n
    getWOClassDescription(final MboRemote theMboRemote)\n
    '''
def changeWorkOrderParent():
    '''returns None\n\n
    changeWorkOrderParent(final MboRemote woparent)\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(final String status, final Date date, final String memo, final long accessModifier)\n
    changeStatus(final String status, final Date date, final String memo, final long accessModifier, final boolean comingFromReceiving)\n
    '''
def changeChildrenStatus():
    '''returns None\n\n
    changeChildrenStatus()\n
    '''
def getParentMbo():
    '''returns WO\n\n
    getParentMbo()\n
    '''
def getWoFromCombined():
    '''returns WORemote\n\n
    getWoFromCombined(final String findWonum)\n
    '''
def canRemoveSafetyPlan():
    '''returns None\n\n
    canRemoveSafetyPlan()\n
    '''
def removeSafetyPlan():
    '''returns None\n\n
    removeSafetyPlan()\n
    '''
def canReportDowntime():
    '''returns None\n\n
    canReportDowntime()\n
    '''
def getOwnSet():
    '''returns MboSetRemote\n\n
    getOwnSet()\n
    '''
def setAttrFromWoGen():
    '''returns None\n\n
    setAttrFromWoGen(final MboRemote woGen)\n
    '''
def getECommHelperRemote():
    '''returns ECommHelperRemote\n\n
    getECommHelperRemote()\n
    '''
def editHistory():
    '''returns None\n\n
    editHistory()\n
    '''
def isWOInEditHist():
    '''returns boolean\n\n
    isWOInEditHist()\n
    '''
def propagateKeyValue():
    '''returns None\n\n
    propagateKeyValue(final String keyName, final String keyValue)\n
    '''
def getPM():
    '''returns PMRemote\n\n
    getPM()\n
    '''
def getAsset():
    '''returns AssetRemote\n\n
    getAsset()\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    delete(final long accessModifier)\n
    '''
def undelete():
    '''returns None\n\n
    undelete()\n
    '''
def getFailListForReport():
    '''returns MboSetRemote\n\n
    getFailListForReport()\n
    '''
def copyFailListToReportSet():
    '''returns None\n\n
    copyFailListToReportSet(final MboSetRemote failListSet)\n
    '''
def copyLaborToWpLaborSet():
    '''returns None\n\n
    copyLaborToWpLaborSet(final MboSetRemote laborSet)\n
    '''
def copyCraftRateToWpLaborSet():
    '''returns None\n\n
    copyCraftRateToWpLaborSet(final MboSetRemote craftRateSet)\n
    '''
def copyLaborToLabTransSet():
    '''returns None\n\n
    copyLaborToLabTransSet(final MboSetRemote laborSet)\n
    '''
def copyItemToWpMatSet():
    '''returns None\n\n
    copyItemToWpMatSet(final MboSetRemote itemSet)\n
    '''
def copyServiceItemsToWpSerSet():
    '''returns None\n\n
    copyServiceItemsToWpSerSet(final MboSetRemote serviceItemSet)\n
    '''
def copyItemToMatUseTransSet():
    '''returns None\n\n
    copyItemToMatUseTransSet(final MboSetRemote itemSet)\n
    '''
def copyToolToWpToolSet():
    '''returns None\n\n
    copyToolToWpToolSet(final MboSetRemote toolSet)\n
    '''
def copyMatUseTransToToolTransSet():
    '''returns None\n\n
    copyMatUseTransToToolTransSet(final MboSetRemote matUseTransSet)\n
    '''
def copyToolToToolTransSet():
    '''returns None\n\n
    copyToolToToolTransSet(final MboSetRemote toolSet)\n
    '''
def copyMRLineToPlanMaterialSet():
    '''returns None\n\n
    copyMRLineToPlanMaterialSet(final MboSetRemote mrLineSet)\n
    '''
def getMboSet():
    '''returns MboSetRemote\n\n
    getMboSet(String name)\n
    '''
def getPOTotal():
    '''returns double\n\n
    getPOTotal()\n
    '''
def getPRTotal():
    '''returns double\n\n
    getPRTotal()\n
    '''
def makeSelectedChildren():
    '''returns None\n\n
    makeSelectedChildren(final MboSetRemote selectSet)\n
    makeSelectedChildren(final MboSetRemote selectSet, String dialogLabel)\n
    '''
def canRemoveWorkPlan():
    '''returns None\n\n
    canRemoveWorkPlan()\n
    '''
def removeWorkPlan():
    '''returns boolean\n\n
    removeWorkPlan()\n
    '''
def hasActuals():
    '''returns boolean\n\n
    hasActuals()\n
    '''
def hasPlanMoveModify():
    '''returns boolean\n\n
    hasPlanMoveModify()\n
    '''
def removeFailureReport():
    '''returns None\n\n
    removeFailureReport()\n
    '''
def promptForDowntimeReport():
    '''returns boolean\n\n
    promptForDowntimeReport(final String newStatus)\n
    '''
def promptForFailureReport():
    '''returns boolean\n\n
    promptForFailureReport(final String newStatus)\n
    '''
def createJPFromWO():
    '''returns MboRemote\n\n
    createJPFromWO(final String jpnum, final String description, final String longdescription)\n
    createJPFromWO(final Date date, final String jpnum, final String description, final String longdescription)\n
    '''
def createJPHeaderFromWO():
    '''returns Mbo\n\n
    createJPHeaderFromWO(final String jpnum, final String description, final String longdescription)\n
    '''
def createWorkorder():
    '''returns MboRemote\n\n
    createWorkorder()\n
    createWorkorder(final String jpnum)\n
    createWorkorder(final MboSetRemote workorderSet)\n
    createWorkorder(final MboSetRemote workorderSet, final String jpnum, final boolean saveSet)\n
    '''
def createChange():
    '''returns MboRemote\n\n
    createChange()\n
    createChange(final String jpnum)\n
    '''
def createRelease():
    '''returns MboRemote\n\n
    createRelease()\n
    createRelease(final String jpnum)\n
    '''
def createServiceRequest():
    '''returns MboRemote\n\n
    createServiceRequest()\n
    createServiceRequest(final String tickettemplateid)\n
    '''
def createProblem():
    '''returns MboRemote\n\n
    createProblem()\n
    createProblem(final String tickettemplateid)\n
    '''
def createIncident():
    '''returns MboRemote\n\n
    createIncident()\n
    createIncident(final String tickettemplateid)\n
    '''
def orphan():
    '''returns None\n\n
    orphan()\n
    '''
def handleChildren():
    '''returns None\n\n
    handleChildren()\n
    '''
def handleTasks():
    '''returns None\n\n
    handleTasks()\n
    '''
def handleUndeleteTasks():
    '''returns None\n\n
    handleUndeleteTasks()\n
    '''
def handleUndeleteChildren():
    '''returns None\n\n
    handleUndeleteChildren()\n
    '''
def deleteChildren():
    '''returns None\n\n
    deleteChildren(final boolean task)\n
    '''
def undeleteChildren():
    '''returns None\n\n
    undeleteChildren(final boolean task)\n
    '''
def isWoAcceptsChargesEditable():
    '''returns boolean\n\n
    isWoAcceptsChargesEditable()\n
    '''
def getTaskIdsThatAcceptCharges():
    '''returns String\n\n
    getTaskIdsThatAcceptCharges()\n
    '''
def pmAlertStatus():
    '''returns MboSetRemote\n\n
    pmAlertStatus(final String status)\n
    '''
def pmAlert():
    '''returns MboSetRemote\n\n
    pmAlert()\n
    '''
def getStatus():
    '''returns String\n\n
    getStatus(final String status)\n
    '''
def woCancel():
    '''returns boolean\n\n
    woCancel()\n
    '''
def canEnterMeterReadings():
    '''returns None\n\n
    canEnterMeterReadings()\n
    '''
def startTimer():
    '''returns None\n\n
    startTimer()\n
    startTimer(final Date startdatetime, final Long anywhererefid, final String transtype)\n
    '''
def stopTimer():
    '''returns MboRemote\n\n
    stopTimer()\n
    stopTimer(final Date finishdatetime, final boolean noStopTimerPopup)\n
    stopTimer(final Date finishdatetime, final Date startDateTime, final boolean noStopTimerPopup)\n
    '''
def getStopTimerLabtrans():
    '''returns MboRemote\n\n
    getStopTimerLabtrans()\n
    '''
def needPopupOnStopTimer():
    '''returns boolean\n\n
    needPopupOnStopTimer()\n
    '''
def updateWorkview():
    '''returns None\n\n
    updateWorkview()\n
    '''
def clearClassification():
    '''returns None\n\n
    clearClassification()\n
    '''
def applyOwner():
    '''returns None\n\n
    applyOwner(final String ownerID)\n
    '''
def applyOwnerGroup():
    '''returns None\n\n
    applyOwnerGroup(final String ownergroupID)\n
    '''
def applyAssignedOwnerGroup():
    '''returns None\n\n
    applyAssignedOwnerGroup(final String ownergroupID)\n
    '''
def ownership():
    '''returns None\n\n
    ownership()\n
    '''
def copyAssetSpecToAutoAttrUpdateSet():
    '''returns None\n\n
    copyAssetSpecToAutoAttrUpdateSet(final MboSetRemote assetspecset, final MboRemote woasset)\n
    '''
def copyLocSpecToAutoAttrUpdateSet():
    '''returns None\n\n
    copyLocSpecToAutoAttrUpdateSet(final MboSetRemote locspecset, final MboRemote woasset)\n
    '''
def copyCISpecToAutoAttrUpdateSet():
    '''returns None\n\n
    copyCISpecToAutoAttrUpdateSet(final MboSetRemote cispecset, final MboRemote woasset)\n
    '''
def applyToAllAssetLoc():
    '''returns None\n\n
    applyToAllAssetLoc(final MboRemote attrupdate)\n
    '''
def copyAssets():
    '''returns None\n\n
    copyAssets(final MboSetRemote assetset)\n
    '''
def copyLocations():
    '''returns None\n\n
    copyLocations(final MboSetRemote locationset)\n
    '''
def moveModifyAssets():
    '''returns boolean\n\n
    moveModifyAssets()\n
    moveModifyAssets(final boolean checkonly)\n
    '''
def moveAllAssets():
    '''returns None\n\n
    moveAllAssets()\n
    '''
def modifyAllAssetLocationAttributes():
    '''returns None\n\n
    modifyAllAssetLocationAttributes()\n
    '''
def removeUserCust():
    '''returns None\n\n
    removeUserCust()\n
    removeUserCust(final boolean removeAssetUserCustPlans, final boolean removeLocUserCustPlans)\n
    removeUserCust(final boolean removeAssetUserCustPlans, final boolean removeLocUserCustPlans, final MboRemote multiassetlocci)\n
    '''
def restoreUserCust():
    '''returns None\n\n
    restoreUserCust()\n
    restoreUserCust(final MboRemote multiassetlocci)\n
    '''
def clearMoveandDeleteAttrUpdate():
    '''returns None\n\n
    clearMoveandDeleteAttrUpdate()\n
    '''
def clearMoveAssetFields():
    '''returns None\n\n
    clearMoveAssetFields()\n
    '''
def updateWarrantyContracts():
    '''returns None\n\n
    updateWarrantyContracts()\n
    '''
def getServiceContractInClause():
    '''returns String\n\n
    getServiceContractInClause()\n
    '''
def getWODate():
    '''returns Date\n\n
    getWODate()\n
    '''
def userVerifiedRemoveSafetyPlan():
    '''returns boolean\n\n
    userVerifiedRemoveSafetyPlan()\n
    '''
def getSafetyPlanID():
    '''returns String\n\n
    getSafetyPlanID()\n
    '''
def copyTicketToRelatedRecSet():
    '''returns None\n\n
    copyTicketToRelatedRecSet(final MboSetRemote TicketSet)\n
    copyTicketToRelatedRecSet(final MboSetRemote TicketSet, final boolean copyToParent)\n
    '''
def copyTicketParentToRelatedRecSet():
    '''returns None\n\n
    copyTicketParentToRelatedRecSet(final MboSetRemote TicketSet)\n
    '''
def copyWOToRelatedRecSet():
    '''returns None\n\n
    copyWOToRelatedRecSet(final MboSetRemote woSet)\n
    copyWOToRelatedRecSet(final MboSetRemote woSet, final boolean copyToParent)\n
    '''
def copyWOParentToRelatedRecSet():
    '''returns None\n\n
    copyWOParentToRelatedRecSet(final MboSetRemote woSet)\n
    '''
def copyParentValuesToRelatedRec():
    '''returns None\n\n
    copyParentValuesToRelatedRec(final MboRemote relatedMbo)\n
    '''
def updateOriginator():
    '''returns None\n\n
    updateOriginator()\n
    '''
def getWOObjectName():
    '''returns String\n\n
    getWOObjectName()\n
    '''
def getRecordMboName():
    '''returns String\n\n
    getRecordMboName()\n
    '''
def setHashForSelectedRecord():
    '''returns None\n\n
    setHashForSelectedRecord(final HashSet hs)\n
    '''
def getHashForSelectedRecord():
    '''returns HashSet\n\n
    getHashForSelectedRecord()\n
    '''
def clearHashForSelectedRecord():
    '''returns None\n\n
    clearHashForSelectedRecord()\n
    '''
def relateWorkorders():
    '''returns MboSetRemote\n\n
    relateWorkorders(final MboSetRemote woSet)\n
    '''
def relateTickets():
    '''returns MboSetRemote\n\n
    relateTickets(final MboSetRemote ticketSet)\n
    '''
def copyAssetsToMultiAsset():
    '''returns None\n\n
    copyAssetsToMultiAsset(final AssetSetRemote assetSetRemote)\n
    '''
def copyLocationsToMultiAsset():
    '''returns None\n\n
    copyLocationsToMultiAsset(final MboSetRemote locationSetRemote)\n
    '''
def checkNestedJobPlans():
    '''returns boolean\n\n
    checkNestedJobPlans()\n
    '''
def setRemoveWorkPlan():
    '''returns None\n\n
    setRemoveWorkPlan(final boolean removeChildFlag)\n
    '''
def getRemoveWorkPlan():
    '''returns boolean\n\n
    getRemoveWorkPlan()\n
    '''
def copyCIsToMultiAsset():
    '''returns None\n\n
    copyCIsToMultiAsset(final MboSetRemote ciSetRemote)\n
    '''
def copyRouteStopsToMultiAsset():
    '''returns None\n\n
    copyRouteStopsToMultiAsset(final MboSetRemote routestopSetRemote)\n
    '''
def copyCollectDetailsToMultiAsset():
    '''returns None\n\n
    copyCollectDetailsToMultiAsset(final MboSetRemote routestopSetRemote)\n
    '''
def appValidate():
    '''returns None\n\n
    appValidate()\n
    '''
def setmultiassetrecord():
    '''returns None\n\n
    setmultiassetrecord()\n
    '''
def copyWOFieldsToMultiAsset():
    '''returns None\n\n
    copyWOFieldsToMultiAsset(final MultiAssetLocCIRemote multiAssetMbo)\n
    '''
def getFlowControlState():
    '''returns int\n\n
    getFlowControlState()\n
    getFlowControlState(final WO wo, final String status)\n
    '''
def isFlowControlComplete():
    '''returns boolean\n\n
    isFlowControlComplete()\n
    isFlowControlComplete(final WO wo, final String status)\n
    '''
def getStartStatusForWorkType():
    '''returns String\n\n
    getStartStatusForWorkType()\n
    getStartStatusForWorkType(final WO wo)\n
    '''
def getCompleteStatusForWorkType():
    '''returns String\n\n
    getCompleteStatusForWorkType()\n
    getCompleteStatusForWorkType(final WO wo)\n
    '''
def getPredecessors():
    '''returns Vector\n\n
    getPredecessors()\n
    '''
def getSuccessors():
    '''returns Vector\n\n
    getSuccessors()\n
    '''
def getChildrenThatHaveNoPredecessors():
    '''returns Vector\n\n
    getChildrenThatHaveNoPredecessors()\n
    '''
def suspendChildrensProcessFlow():
    '''returns None\n\n
    suspendChildrensProcessFlow(final boolean torf)\n
    '''
def setChildrensFlowControl():
    '''returns None\n\n
    setChildrensFlowControl(final boolean torf)\n
    '''
def changeChildrensFieldValue():
    '''returns None\n\n
    changeChildrensFieldValue(final String fieldname, final String fieldvalue, final long accessModifier)\n
    '''
def executeProcessFlowControlAction():
    '''returns None\n\n
    executeProcessFlowControlAction()\n
    '''
def changeStatusProcessFlowControl():
    '''returns None\n\n
    changeStatusProcessFlowControl()\n
    '''
def startSuccessors():
    '''returns boolean\n\n
    startSuccessors(final Mbo mbo, final Vector successors, final Date date, final String memo, final long accessModifier)\n
    '''
def adjustSuccVectors():
    '''returns None\n\n
    adjustSuccVectors(final Vector existingSuccs, final Vector newSuccs)\n
    '''
def areAllPredecessorsComplete():
    '''returns boolean\n\n
    areAllPredecessorsComplete()\n
    areAllPredecessorsComplete(final WO wo)\n
    areAllPredecessorsComplete(final String targetStatus, final boolean fully)\n
    areAllPredecessorsComplete(final WO wo, final String targetStatus, final boolean fully)\n
    '''
def areAllPredecessorsSufficientlyComplete():
    '''returns boolean\n\n
    areAllPredecessorsSufficientlyComplete(final WO wo, final String targetStatus)\n
    '''
def getContemplatedAction():
    '''returns int\n\n
    getContemplatedAction(final WO wo, final String targetStatus)\n
    '''
def isSufficientlyFlowControlComplete():
    '''returns boolean\n\n
    isSufficientlyFlowControlComplete(final WO wo, final String reltypeToSuccessor, final int contemplatedAction)\n
    isSufficientlyFlowControlComplete(final WO wo, final String status, final String reltypeToSuccessor, final int contemplatedAction)\n
    '''
def getChildPFCOrder():
    '''returns Vector\n\n
    getChildPFCOrder(final boolean getChildrenWOs, final boolean appendSiteid)\n
    '''
def findPredecessorPosition():
    '''returns int\n\n
    findPredecessorPosition(final Vector vector2Search, final String wonum, final Hashtable htNetwork)\n
    '''
def bulkReschedule():
    '''returns None\n\n
    bulkReschedule(final boolean resched, final Date reschedDate, final boolean fromListTab)\n
    bulkReschedule(final boolean resched, final Date reschedDate)\n
    '''
def getRescheduled():
    '''returns int\n\n
    getRescheduled()\n
    '''
def getUnassigned():
    '''returns int\n\n
    getUnassigned()\n
    '''
def unassignWOAssignments():
    '''returns None\n\n
    unassignWOAssignments(AssignmentSet assignSet, final Date reschedDate)\n
    '''
def unassignAssignments():
    '''returns None\n\n
    unassignAssignments(final AssignmentSet assignSet, final Date reschedDate)\n
    '''
def rescheduleAssignments():
    '''returns None\n\n
    rescheduleAssignments(AssignmentSet assignSet, final Date reschedDate, final boolean fromListTab)\n
    rescheduleAssignments(final AssignmentSet assignSet, final Date reschedDate)\n
    '''
def getLCRSqlFormatHashMap():
    '''returns HashMap\n\n
    getLCRSqlFormatHashMap(final AssignmentSet assignSet)\n
    '''
def calculateScheduleFinishDate():
    '''returns Date\n\n
    calculateScheduleFinishDate(final WO wo, final Date schedStartDate)\n
    '''
def setWOScheduleDates():
    '''returns None\n\n
    setWOScheduleDates(final WO wo, Date schedStartDate)\n
    setWOScheduleDates(final WO wo, Date schedStartDate, final double duration)\n
    '''
def restoreSplitAssignments():
    '''returns AssignmentSet\n\n
    restoreSplitAssignments(AssignmentSet assignSet)\n
    '''
def getToplevelParentAssign():
    '''returns Assignment\n\n
    getToplevelParentAssign(Assignment assign, final AssignmentSet assignSet, final HashMap assignIndexMap)\n
    '''
def removeCompleteStartedAssigns():
    '''returns AssignmentSet\n\n
    removeCompleteStartedAssigns(final AssignmentSet assignSet, final HashMap assignIndexMap)\n
    '''
def applyToAllUser():
    '''returns None\n\n
    applyToAllUser(final MboRemote woModUser)\n
    '''
def setPrimaryLinearAssetFieldsReadOnly():
    '''returns None\n\n
    setPrimaryLinearAssetFieldsReadOnly(MultiAssetLocCIRemote multiAssetMbo, final boolean readonlystate)\n
    '''
def clearPrimaryLinearAssetFields():
    '''returns None\n\n
    clearPrimaryLinearAssetFields(final MultiAssetLocCIRemote multiAssetMbo)\n
    '''
def copyLinearAssetFieldsFromRouteStop():
    '''returns None\n\n
    copyLinearAssetFieldsFromRouteStop(final MboRemote toMbo, final MboRemote routestop)\n
    '''
def setRemoveWorkPlanFlag():
    '''returns None\n\n
    setRemoveWorkPlanFlag(final boolean removeWorkplan)\n
    '''
def getRemoveWorkPlanFlag():
    '''returns boolean\n\n
    getRemoveWorkPlanFlag()\n
    '''
def getTopOwner():
    '''returns MboRemote\n\n
    getTopOwner()\n
    '''
def checkCompStatus():
    '''returns None\n\n
    checkCompStatus()\n
    '''
def doClassificationCreateTicketViews():
    '''returns None\n\n
    doClassificationCreateTicketViews(final MboRemote newMbo)\n
    '''
def doClassificationCreateWOViews():
    '''returns None\n\n
    doClassificationCreateWOViews(final MboRemote newMbo)\n
    '''
def doClassificationCreateWOSpecFromJobPlan():
    '''returns None\n\n
    doClassificationCreateWOSpecFromJobPlan(final MboRemote newMbo, final MboRemote sourceMbo)\n
    '''
def CheckOrigIsFollowup():
    '''returns None\n\n
    CheckOrigIsFollowup()\n
    '''
def clearSkipCopyFields():
    '''returns None\n\n
    clearSkipCopyFields()\n
    '''
def routeStopExists():
    '''returns boolean\n\n
    routeStopExists()\n
    '''
def isListSelected():
    '''returns boolean\n\n
    isListSelected()\n
    '''
def setListSelected():
    '''returns None\n\n
    setListSelected(final boolean isListSelected)\n
    '''
def getCopydocMboSet():
    '''returns MboSetRemote\n\n
    getCopydocMboSet(String name)\n
    '''
def setAvailibilityStatus():
    '''returns MTLStatus\n\n
    setAvailibilityStatus(final boolean changeStatus)\n
    '''
def setStoreroomStatus():
    '''returns MTLStatus\n\n
    setStoreroomStatus(final boolean changeStatus)\n
    '''
def setDirectIssueStatus():
    '''returns MTLStatus\n\n
    setDirectIssueStatus()\n
    '''
def setChildrenStatus():
    '''returns MTLStatus\n\n
    setChildrenStatus(final MTLStatus storeroomStatus, final MTLStatus directIssueStatus, final boolean changeStatus)\n
    '''
def setMaterialAvailStatus():
    '''returns MTLStatus\n\n
    setMaterialAvailStatus()\n
    '''
def smartFillForAllSites():
    '''returns MboSetRemote\n\n
    smartFillForAllSites(final String attribute, final String value, final boolean exact)\n
    '''
def smartFindForAllSites():
    '''returns MboSetRemote\n\n
    smartFindForAllSites(final String attribute, final String value, final boolean exact)\n
    '''
def isRevEnabled():
    '''returns boolean\n\n
    isRevEnabled()\n
    '''
def isCalibrationInstalled():
    '''returns boolean\n\n
    isCalibrationInstalled()\n
    '''
def isFromMobile():
    '''returns boolean\n\n
    isFromMobile()\n
    '''
def setFromMobile():
    '''returns None\n\n
    setFromMobile(final boolean isFromMobile)\n
    '''
def setCompleteWOFromEveryplace():
    '''returns None\n\n
    setCompleteWOFromEveryplace(boolean completeWOFromEveryplace)\n
    '''
def manageCircleEffect():
    '''returns None\n\n
    manageCircleEffect(final MboRemote thisToolTrans)\n
    '''
def getWorkTypeCal():
    '''returns String\n\n
    getWorkTypeCal()\n
    '''
def getTranslatedWorkTypeCal():
    '''returns String\n\n
    getTranslatedWorkTypeCal()\n
    '''
def getJobRevNum():
    '''returns String\n\n
    getJobRevNum(final Mbo PlusCWO)\n
    '''
def isValidJPRevNum():
    '''returns boolean\n\n
    isValidJPRevNum(final String jpNum, final String revNum)\n
    '''
def getWorkType():
    '''returns String\n\n
    getWorkType()\n
    '''
def checkRequiredDatasheets():
    '''returns boolean\n\n
    checkRequiredDatasheets()\n
    '''
def duplicateWODS():
    '''returns MboRemote\n\n
    duplicateWODS(final MboRemote newWO)\n
    '''
def canEditRelatedSetCal():
    '''returns None\n\n
    canEditRelatedSetCal(final String relationName)\n
    '''
def canEditAsFoundAsLeftFields():
    '''returns boolean\n\n
    canEditAsFoundAsLeftFields()\n
    '''
def copyJobPlanToWorkPlanCal():
    '''returns None\n\n
    copyJobPlanToWorkPlanCal()\n
    '''
def copyDSPlanToWO():
    '''returns None\n\n
    copyDSPlanToWO(final Mbo ds)\n
    '''
def updatePreviousAsLeftValues():
    '''returns None\n\n
    updatePreviousAsLeftValues()\n
    '''
def isTolWarning():
    '''returns boolean\n\n
    isTolWarning()\n
    '''
def canEditAsset():
    '''returns boolean\n\n
    canEditAsset()\n
    '''
def changeStatusCal():
    '''returns None\n\n
    changeStatusCal(final String status, final Date date, final String memo, final long accessModifier, final boolean comingFromReceiving)\n
    '''
def managePlusCNextDate():
    '''returns None\n\n
    managePlusCNextDate()\n
    '''
def getLoopRotAsset():
    '''returns MboRemote\n\n
    getLoopRotAsset(final MboRemote toolMbo)\n
    '''
def validateRotatingAsset():
    '''returns boolean\n\n
    validateRotatingAsset(final MboRemote toolMbo)\n
    '''
def generateWORelRecord():
    '''returns None\n\n
    generateWORelRecord(final WORemote oldWO)\n
    '''
def checkWorkPackStatus():
    '''returns None\n\n
    checkWorkPackStatus()\n
    '''
def parentMbo():
    '''returns MboRemote\n\n
    parentMbo(final String wonum)\n
    '''
def updateHierarchyWPStatus():
    '''returns MboRemote\n\n
    updateHierarchyWPStatus(final MboRemote parentMbo, final MboRemote mainMbo, final String previousParentValue, final Boolean parentChanged)\n
    '''
def refreshWorkPackHierarchy():
    '''returns None\n\n
    refreshWorkPackHierarchy()\n
    refreshWorkPackHierarchy(final WORemote mbo)\n
    '''
def setPMWOCancelUserListResponse():
    '''returns None\n\n
    setPMWOCancelUserListResponse(final boolean response)\n
    '''
def getPMWOCancelUserListResponse():
    '''returns boolean\n\n
    getPMWOCancelUserListResponse()\n
    '''
def canDeleteAttachedDocs():
    '''returns None\n\n
    canDeleteAttachedDocs()\n
    '''
def getWOServiceAddress():
    '''returns WOServiceAddressRemote\n\n
    getWOServiceAddress()\n
    '''
def hasServiceAddress():
    '''returns boolean\n\n
    hasServiceAddress()\n
    '''
def getServiceAddress():
    '''returns WOServiceAddressRemote\n\n
    getServiceAddress()\n
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
def saveGISData():
    '''returns None\n\n
    saveGISData(final String address, final String lat, final String lng)\n
    '''
def isGISDataReadonly():
    '''returns boolean\n\n
    isGISDataReadonly()\n
    '''
def updateChildrensServiceAddress():
    '''returns None\n\n
    updateChildrensServiceAddress(final WO currentWO)\n
    '''
def getAmCrewLabor():
    '''returns MboRemote\n\n
    getAmCrewLabor(final String laborCode, final String laborOrg)\n
    '''
def getAmCrew():
    '''returns MboRemote\n\n
    getAmCrew(final String crew, final String laborOrg)\n
    '''
def getAmCrewLaborSet():
    '''returns MboSetRemote\n\n
    getAmCrewLaborSet(final String crew, final String laborOrg)\n
    '''
def isMobileCrew():
    '''returns boolean\n\n
    isMobileCrew(final String laborCode, final String laborOrg)\n
    '''
def isCrew():
    '''returns boolean\n\n
    isCrew(final String laborCode, final String laborOrg)\n
    '''
def createToolTransEveryplace():
    '''returns None\n\n
    createToolTransEveryplace(final MboRemote labTransMbo)\n
    '''
def getAmCrewToolSet():
    '''returns MboSetRemote\n\n
    getAmCrewToolSet(final String crew)\n
    '''
def getAutoLocateObject():
    '''returns MboRemote\n\n
    getAutoLocateObject()\n
    getAutoLocateObject(final AutoLocatable nextInChain)\n
    '''
def hasCoords():
    '''returns Boolean\n\n
    hasCoords()\n
    '''
def setClearLBSLocation():
    '''returns None\n\n
    setClearLBSLocation(final boolean setLocation)\n
    '''
def setPMWOCancelUserMainAndChildren():
    '''returns None\n\n
    setPMWOCancelUserMainAndChildren(final int response)\n
    '''
def getPMWOCancelUserMainAndChildren():
    '''returns int\n\n
    getPMWOCancelUserMainAndChildren()\n
    '''
def setWoOwnerDuringStatusChange():
    '''returns None\n\n
    setWoOwnerDuringStatusChange(final MboRemote parentWO)\n
    '''
def getWoOwnerDuringStatusChange():
    '''returns MboRemote\n\n
    getWoOwnerDuringStatusChange()\n
    '''
def checkForActiveLabTrans():
    '''returns boolean\n\n
    checkForActiveLabTrans()\n
    '''
def copyCrewTypeToWpLaborSet():
    '''returns None\n\n
    copyCrewTypeToWpLaborSet(final MboSetRemote crewTypeSet)\n
    '''
def setStoreroomStatusWOGen():
    '''returns MTLStatus\n\n
    setStoreroomStatusWOGen(final boolean changeStatus)\n
    '''
def setDirectIssueStatusWOGen():
    '''returns MTLStatus\n\n
    setDirectIssueStatusWOGen()\n
    '''
def checkSynonymStatusDate():
    '''returns None\n\n
    checkSynonymStatusDate(final String status, Date date)\n
    '''
def getTargStartDate():
    '''returns Date\n\n
    getTargStartDate(final Date date, final String calledFromFlag)\n
    '''
def getPMNextDate():
    '''returns Date\n\n
    getPMNextDate(final Date date, final String calledFromFlag)\n
    '''
def getPMExtDate():
    '''returns Date\n\n
    getPMExtDate(final Date date, final String calledFromFlag)\n
    '''
def getSharedMatUseTransSet():
    '''returns MboSetRemote\n\n
    getSharedMatUseTransSet(final MboRemote wpm)\n
    '''
def isFullyIssued():
    '''returns boolean\n\n
    isFullyIssued(final MboRemote wpm)\n
    '''
def ProcessParentInVector():
    '''returns None\n\n
    ProcessParentInVector(final MboRemote currentParent)\n
    '''
def isPartiallyIssued():
    '''returns boolean\n\n
    isPartiallyIssued(final MboRemote wpm)\n
    '''
def hasUndeleteFRCompleted():
    '''returns boolean\n\n
    hasUndeleteFRCompleted()\n
    '''
def getAvailableLabor():
    '''returns MboSetRemote\n\n
    getAvailableLabor()\n
    '''
def setChangeStatusSet():
    '''returns None\n\n
    setChangeStatusSet(final MboSetRemote changeStatusSet)\n
    '''
def getChangeStatusSet():
    '''returns MboSetRemote\n\n
    getChangeStatusSet()\n
    '''
def canCreateRelatedRecord():
    '''returns boolean\n\n
    canCreateRelatedRecord()\n
    '''
def setTopWOInWOGen():
    '''returns None\n\n
    setTopWOInWOGen(final MboRemote topWO)\n
    '''
def getTopWOInWOGen():
    '''returns MboRemote\n\n
    getTopWOInWOGen()\n
    '''
def getUnCommittedWOs():
    '''returns Vector\n\n
    getUnCommittedWOs()\n
    '''
def storeUnCommittedWOs():
    '''returns None\n\n
    storeUnCommittedWOs(final MboRemote childWO)\n
    '''
def setAsyncChangeStatus():
    '''returns None\n\n
    setAsyncChangeStatus()\n
    '''
def isAsyncStatusChange():
    '''returns boolean\n\n
    isAsyncStatusChange()\n
    '''
def setAppDefaultValue():
    '''returns None\n\n
    setAppDefaultValue()\n
    '''
def initMXYesNoHash():
    '''returns None\n\n
    initMXYesNoHash(final HashMap<String, MXApplicationYesNoCancelException> hash)\n
    '''
def setMustApplyDJP():
    '''returns None\n\n
    setMustApplyDJP(final boolean mustApplyDJP)\n
    '''
def mustApplyDJP():
    '''returns boolean\n\n
    mustApplyDJP()\n
    '''
def calculateDynamicJobPlan():
    '''returns None\n\n
    calculateDynamicJobPlan()\n
    '''
def mustApplyLinearCalculation():
    '''returns boolean\n\n
    mustApplyLinearCalculation()\n
    '''
def calculateTotalWorkUnitsFor():
    '''returns None\n\n
    calculateTotalWorkUnitsFor(final MboRemote multiAssetLocCI, final String unitOfWork)\n
    '''
def calculateTotalWorkUnits():
    '''returns None\n\n
    calculateTotalWorkUnits()\n
    '''
def isCalculationAppliedSuccessfully():
    '''returns boolean\n\n
    isCalculationAppliedSuccessfully()\n
    '''
def getWorkLog():
    '''returns MboSetRemote\n\n
    getWorkLog()\n
    '''
def getWoHazardPrecHashMap():
    '''returns Map\n\n
    getWoHazardPrecHashMap()\n
    '''
def incrementWoHazardPrecHashMap():
    '''returns None\n\n
    incrementWoHazardPrecHashMap(final String precautionid)\n
    '''
def decrementWoHazardPrecHashMap():
    '''returns None\n\n
    decrementWoHazardPrecHashMap(final String precautionid)\n
    '''
def compare():
    '''returns int\n\n
    compare(final MboRemote m1, final MboRemote m2)\n
    '''
