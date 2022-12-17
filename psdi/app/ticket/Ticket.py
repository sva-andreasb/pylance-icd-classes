MULTIASSET_SITE_ERRORKEY = "String  \"MultiAssetSiteNotSame\""
CREATEWOMULTI_NONE = "String  \"NONE\""
CREATEWOMULTI_CHILD = "String  \"CHILD\""
CREATEWOMULTI_TASK = "String  \"TASK\""
CREATEWOMULTI_MULTI = "String  \"MULTI\""
CREATEWOMULTI_TOPLEVEL = "String  \"TOPLEVEL\""
def ():
    '''returns Ticket\n\n
    (final MboSet ms)\n
    '''
def getProcess():
    '''returns String\n\n
    getProcess()\n
    '''
def canTemplateApply():
    '''returns None\n\n
    canTemplateApply()\n
    '''
def getStatusListName():
    '''returns String\n\n
    getStatusListName()\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def initFieldFlagsOnMbo():
    '''returns None\n\n
    initFieldFlagsOnMbo(final String attrName)\n
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
def add():
    '''returns None\n\n
    add()\n
    '''
def modify():
    '''returns None\n\n
    modify()\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(final String status, final Date date, final String memo, final long accessModifier)\n
    '''
def canDelete():
    '''returns None\n\n
    canDelete()\n
    '''
def canDeleteAttachedDocs():
    '''returns None\n\n
    canDeleteAttachedDocs()\n
    '''
def hasActuals():
    '''returns boolean\n\n
    hasActuals()\n
    '''
def appValidate():
    '''returns None\n\n
    appValidate()\n
    '''
def delete():
    '''returns None\n\n
    delete(final long accessModifier)\n
    '''
def duplicate():
    '''returns MboRemote\n\n
    duplicate()\n
    '''
def editHistory():
    '''returns None\n\n
    editHistory()\n
    '''
def isTicketInEditHist():
    '''returns boolean\n\n
    isTicketInEditHist()\n
    '''
def startTimer():
    '''returns None\n\n
    startTimer()\n
    '''
def tkChangeMaxStatus():
    '''returns None\n\n
    tkChangeMaxStatus(final String maxstatus)\n
    '''
def stopTimer():
    '''returns MboRemote\n\n
    stopTimer()\n
    stopTimer(final Date finishdatetime, final boolean noStopTimerPopup)\n
    stopTimer(final Date finishdatetime, final Date startDateTime, final boolean noStopTimerPopup)\n
    '''
def createIncident():
    '''returns MboRemote\n\n
    createIncident()\n
    createIncident(final String tickettemplateid)\n
    '''
def createServiceRequest():
    '''returns MboRemote\n\n
    createServiceRequest()\n
    createServiceRequest(final String tickettemplateid)\n
    '''
def createSR():
    '''returns MboRemote\n\n
    createSR()\n
    createSR(final String tickettemplateid)\n
    '''
def createProblem():
    '''returns MboRemote\n\n
    createProblem()\n
    createProblem(final String tickettemplateid)\n
    '''
def getFailListForReport():
    '''returns MboSetRemote\n\n
    getFailListForReport()\n
    '''
def copyFailListToReportSet():
    '''returns None\n\n
    copyFailListToReportSet(final MboSetRemote failListSet)\n
    '''
def removeFailureReport():
    '''returns None\n\n
    removeFailureReport()\n
    '''
def applyTemplate():
    '''returns None\n\n
    applyTemplate(final MboRemote templateMbo)\n
    '''
def ticketStatus():
    '''returns String\n\n
    ticketStatus()\n
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
def createWorkorder():
    '''returns MboRemote\n\n
    createWorkorder()\n
    createWorkorder(final MboSetRemote targetSet, final boolean saveSet)\n
    createWorkorder(final String jpnum)\n
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
def setLinearAssetFieldsReadOnly():
    '''returns None\n\n
    setLinearAssetFieldsReadOnly(MultiAssetLocCIRemote malocMbo, final boolean readonlystate)\n
    '''
def clearLinearAssetFields():
    '''returns None\n\n
    clearLinearAssetFields(final MultiAssetLocCIRemote malocMbo)\n
    '''
def createSolution():
    '''returns MboRemote\n\n
    createSolution()\n
    '''
def findTkSite():
    '''returns String\n\n
    findTkSite()\n
    '''
def incrActLabCost():
    '''returns None\n\n
    incrActLabCost(final double incrAmount)\n
    '''
def incrActLabHrs():
    '''returns None\n\n
    incrActLabHrs(final double incrAmount)\n
    '''
def getLocForAsset():
    '''returns None\n\n
    getLocForAsset()\n
    '''
def applyAssetLoc():
    '''returns None\n\n
    applyAssetLoc()\n
    '''
def calcGLAccount():
    '''returns String\n\n
    calcGLAccount()\n
    '''
def getActivityBasedOnWonum():
    '''returns MboRemote\n\n
    getActivityBasedOnWonum(final String wonum)\n
    '''
def copyTicketToRelatedRecSet():
    '''returns None\n\n
    copyTicketToRelatedRecSet(final MboSetRemote TicketSet)\n
    '''
def copyWOToRelatedRecSet():
    '''returns None\n\n
    copyWOToRelatedRecSet(final MboSetRemote WOSet)\n
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
def similarTickets():
    '''returns MboSetRemote\n\n
    similarTickets()\n
    '''
def relateTickets():
    '''returns MboSetRemote\n\n
    relateTickets(final MboSetRemote tkSet)\n
    '''
def relateWorkorders():
    '''returns MboSetRemote\n\n
    relateWorkorders(final MboSetRemote woSet)\n
    '''
def copyLaborToLabTransSet():
    '''returns None\n\n
    copyLaborToLabTransSet(final MboSetRemote laborSet)\n
    '''
def updateOriginator():
    '''returns None\n\n
    updateOriginator()\n
    '''
def getValidateOrder():
    '''returns String[]\n\n
    getValidateOrder()\n
    '''
def getWOClassDescription():
    '''returns String\n\n
    getWOClassDescription(final String appname)\n
    '''
def copyAssetsToMultiAsset():
    '''returns None\n\n
    copyAssetsToMultiAsset(final AssetSetRemote assetSetRemote)\n
    '''
def copyLocationsToMultiAsset():
    '''returns None\n\n
    copyLocationsToMultiAsset(final MboSetRemote locationSetRemote)\n
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
    copyCollectDetailsToMultiAsset(final MboSetRemote collectionDetailsetRemote)\n
    '''
def checkMultiAssetLocCISite():
    '''returns None\n\n
    checkMultiAssetLocCISite(final String multiAssetSite)\n
    '''
def setmultiassetrecord():
    '''returns None\n\n
    setmultiassetrecord()\n
    '''
def copyTicketFieldsToMultiAsset():
    '''returns None\n\n
    copyTicketFieldsToMultiAsset(final MultiAssetLocCIRemote multiAssetMbo)\n
    '''
def getTopOriginator():
    '''returns MboRemote\n\n
    getTopOriginator()\n
    '''
def doClassificationCreate():
    '''returns None\n\n
    doClassificationCreate(final MboRemote newMbo, final MboRemote sourceMbo, String keyAttribute)\n
    '''
def allowSelfServiceSolutionAccess():
    '''returns boolean\n\n
    allowSelfServiceSolutionAccess()\n
    '''
def checkOrigIsFollowup():
    '''returns None\n\n
    checkOrigIsFollowup()\n
    '''
def getRecordMboName():
    '''returns String\n\n
    getRecordMboName()\n
    '''
def canPropagateRepairFacility():
    '''returns boolean\n\n
    canPropagateRepairFacility(final MboRemote newWorkorder)\n
    '''
def propagateRepairFacility():
    '''returns None\n\n
    propagateRepairFacility(final MboRemote newWorkorder)\n
    '''
def getTKServiceAddress():
    '''returns TKServiceAddressRemote\n\n
    getTKServiceAddress()\n
    '''
def hasServiceAddress():
    '''returns boolean\n\n
    hasServiceAddress()\n
    '''
def getServiceAddress():
    '''returns TKServiceAddressRemote\n\n
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
def updateServiceAddress():
    '''returns None\n\n
    updateServiceAddress()\n
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
def updateReportedAndAffectedUser():
    '''returns None\n\n
    updateReportedAndAffectedUser(final String dataAttribute, final MboRemote lookupMbo)\n
    '''
def setDontSkipCreatePrimaryMALCI():
    '''returns None\n\n
    setDontSkipCreatePrimaryMALCI(final boolean dontSkip)\n
    '''
def getDontSkipCreatePrimaryMALCI():
    '''returns boolean\n\n
    getDontSkipCreatePrimaryMALCI()\n
    '''
def createPrimaryMultiAssetRecord():
    '''returns None\n\n
    createPrimaryMultiAssetRecord()\n
    '''
def toIncludeFilterBy():
    '''returns None\n\n
    toIncludeFilterBy(final boolean toSet)\n
    '''
def getIncludeFilterBy():
    '''returns boolean\n\n
    getIncludeFilterBy()\n
    '''
