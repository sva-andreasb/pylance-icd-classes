MULTIASSET_SITE_ERRORKEY = "String  \"MultiAssetSiteNotSame\""
CREATEWOMULTI_NONE = "String  \"NONE\""
CREATEWOMULTI_CHILD = "String  \"CHILD\""
CREATEWOMULTI_TASK = "String  \"TASK\""
CREATEWOMULTI_MULTI = "String  \"MULTI\""
CREATEWOMULTI_TOPLEVEL = "String  \"TOPLEVEL\""
def Ticket():
    '''public Ticket(final MboSet ms)
    '''
def getProcess():
    '''public String getProcess()
    '''
def canTemplateApply():
    '''public void canTemplateApply()
    '''
def getStatusListName():
    '''public String getStatusListName()
    '''
def init():
    '''public void init()
    '''
def initFieldFlagsOnMbo():
    '''public void initFieldFlagsOnMbo(final String attrName)
    '''
def canEditRelatedSet():
    '''public void canEditRelatedSet(final String relationName)
    '''
def setRelatedMboEditibility():
    '''public void setRelatedMboEditibility(final String relationName)
    '''
def initRelationship():
    '''public void initRelationship(final String relationName, final MboSetRemote mboSet)
    '''
def add():
    '''public void add()
    '''
def modify():
    '''public void modify()
    '''
def changeStatus():
    '''public void changeStatus(final String status, final Date date, final String memo, final long accessModifier)
    '''
def canDelete():
    '''public void canDelete()
    '''
def canDeleteAttachedDocs():
    '''public void canDeleteAttachedDocs()
    '''
def hasActuals():
    '''public boolean hasActuals()
    '''
def appValidate():
    '''public void appValidate()
    '''
def delete():
    '''public void delete(final long accessModifier)
    '''
def duplicate():
    '''public MboRemote duplicate()
    '''
def editHistory():
    '''public void editHistory()
    '''
def isTicketInEditHist():
    '''public boolean isTicketInEditHist()
    '''
def startTimer():
    '''public void startTimer()
    '''
def tkChangeMaxStatus():
    '''public void tkChangeMaxStatus(final String maxstatus)
    '''
def stopTimer():
    '''public void stopTimer()
    public MboRemote stopTimer(final Date finishdatetime, final boolean noStopTimerPopup)
    public MboRemote stopTimer(final Date finishdatetime, final Date startDateTime, final boolean noStopTimerPopup)
    '''
def createIncident():
    '''public MboRemote createIncident()
    public MboRemote createIncident(final String tickettemplateid)
    '''
def createServiceRequest():
    '''public MboRemote createServiceRequest()
    public MboRemote createServiceRequest(final String tickettemplateid)
    '''
def createSR():
    '''public MboRemote createSR()
    public MboRemote createSR(final String tickettemplateid)
    '''
def createProblem():
    '''public MboRemote createProblem()
    public MboRemote createProblem(final String tickettemplateid)
    '''
def getFailListForReport():
    '''public MboSetRemote getFailListForReport()
    '''
def copyFailListToReportSet():
    '''public void copyFailListToReportSet(final MboSetRemote failListSet)
    '''
def removeFailureReport():
    '''public void removeFailureReport()
    '''
def applyTemplate():
    '''public void applyTemplate(final MboRemote templateMbo)
    '''
def ticketStatus():
    '''public String ticketStatus()
    '''
def applyOwner():
    '''public void applyOwner(final String ownerID)
    '''
def applyOwnerGroup():
    '''public void applyOwnerGroup(final String ownergroupID)
    '''
def applyAssignedOwnerGroup():
    '''public void applyAssignedOwnerGroup(final String ownergroupID)
    '''
def ownership():
    '''public void ownership()
    '''
def createWorkorder():
    '''public Vector createWorkorder()
    public Vector createWorkorder(final MboSetRemote targetSet, final boolean saveSet)
    public MboRemote createWorkorder(final String jpnum)
    '''
def createChange():
    '''public Vector createChange()
    public MboRemote createChange(final String jpnum)
    '''
def createRelease():
    '''public Vector createRelease()
    public MboRemote createRelease(final String jpnum)
    '''
def setLinearAssetFieldsReadOnly():
    '''public void setLinearAssetFieldsReadOnly(MultiAssetLocCIRemote malocMbo, final boolean readonlystate)
    '''
def clearLinearAssetFields():
    '''public void clearLinearAssetFields(final MultiAssetLocCIRemote malocMbo)
    '''
def createSolution():
    '''public MboRemote createSolution()
    '''
def findTkSite():
    '''public String findTkSite()
    '''
def incrActLabCost():
    '''public void incrActLabCost(final double incrAmount)
    '''
def incrActLabHrs():
    '''public void incrActLabHrs(final double incrAmount)
    '''
def getLocForAsset():
    '''public void getLocForAsset()
    '''
def applyAssetLoc():
    '''public void applyAssetLoc()
    '''
def calcGLAccount():
    '''public String calcGLAccount()
    '''
def getActivityBasedOnWonum():
    '''public MboRemote getActivityBasedOnWonum(final String wonum)
    '''
def copyTicketToRelatedRecSet():
    '''public void copyTicketToRelatedRecSet(final MboSetRemote TicketSet)
    '''
def copyWOToRelatedRecSet():
    '''public void copyWOToRelatedRecSet(final MboSetRemote WOSet)
    '''
def needPopupOnStopTimer():
    '''public boolean needPopupOnStopTimer()
    '''
def updateWorkview():
    '''public void updateWorkview()
    '''
def clearClassification():
    '''public void clearClassification()
    '''
def similarTickets():
    '''public MboSetRemote similarTickets()
    '''
def relateTickets():
    '''public MboSetRemote relateTickets(final MboSetRemote tkSet)
    '''
def relateWorkorders():
    '''public MboSetRemote relateWorkorders(final MboSetRemote woSet)
    '''
def copyLaborToLabTransSet():
    '''public void copyLaborToLabTransSet(final MboSetRemote laborSet)
    '''
def updateOriginator():
    '''public void updateOriginator()
    '''
def getValidateOrder():
    '''public String[] getValidateOrder()
    '''
def getWOClassDescription():
    '''public String getWOClassDescription(final String appname)
    '''
def copyAssetsToMultiAsset():
    '''public void copyAssetsToMultiAsset(final AssetSetRemote assetSetRemote)
    '''
def copyLocationsToMultiAsset():
    '''public void copyLocationsToMultiAsset(final MboSetRemote locationSetRemote)
    '''
def copyCIsToMultiAsset():
    '''public void copyCIsToMultiAsset(final MboSetRemote ciSetRemote)
    '''
def copyRouteStopsToMultiAsset():
    '''public void copyRouteStopsToMultiAsset(final MboSetRemote routestopSetRemote)
    '''
def copyCollectDetailsToMultiAsset():
    '''public void copyCollectDetailsToMultiAsset(final MboSetRemote collectionDetailsetRemote)
    '''
def checkMultiAssetLocCISite():
    '''public void checkMultiAssetLocCISite(final String multiAssetSite)
    '''
def setmultiassetrecord():
    '''public void setmultiassetrecord()
    '''
def copyTicketFieldsToMultiAsset():
    '''public void copyTicketFieldsToMultiAsset(final MultiAssetLocCIRemote multiAssetMbo)
    '''
def getTopOriginator():
    '''public MboRemote getTopOriginator()
    '''
def doClassificationCreate():
    '''public void doClassificationCreate(final MboRemote newMbo, final MboRemote sourceMbo, String keyAttribute)
    '''
def allowSelfServiceSolutionAccess():
    '''public boolean allowSelfServiceSolutionAccess()
    '''
def checkOrigIsFollowup():
    '''public void checkOrigIsFollowup()
    '''
def getRecordMboName():
    '''public String getRecordMboName()
    '''
def canPropagateRepairFacility():
    '''public boolean canPropagateRepairFacility(final MboRemote newWorkorder)
    '''
def propagateRepairFacility():
    '''public void propagateRepairFacility(final MboRemote newWorkorder)
    '''
def getTKServiceAddress():
    '''public TKServiceAddressRemote getTKServiceAddress()
    '''
def hasServiceAddress():
    '''public boolean hasServiceAddress()
    '''
def getServiceAddress():
    '''public TKServiceAddressRemote getServiceAddress()
    '''
def getLatitudeY():
    '''public Double getLatitudeY()
    '''
def getLongitudeX():
    '''public Double getLongitudeX()
    '''
def getAddressString():
    '''public String getAddressString()
    '''
def saveGISData():
    '''public void saveGISData(final String address, final String lat, final String lng)
    '''
def isGISDataReadonly():
    '''public boolean isGISDataReadonly()
    '''
def updateServiceAddress():
    '''public void updateServiceAddress()
    '''
def getAutoLocateObject():
    '''public MboRemote getAutoLocateObject(final AutoLocatable nextInChain)
    public MboRemote getAutoLocateObject()
    '''
def hasCoords():
    '''public Boolean hasCoords()
    '''
def updateReportedAndAffectedUser():
    '''public void updateReportedAndAffectedUser(final String dataAttribute, final MboRemote lookupMbo)
    '''
def setDontSkipCreatePrimaryMALCI():
    '''public void setDontSkipCreatePrimaryMALCI(final boolean dontSkip)
    '''
def getDontSkipCreatePrimaryMALCI():
    '''public boolean getDontSkipCreatePrimaryMALCI()
    '''
def createPrimaryMultiAssetRecord():
    '''public void createPrimaryMultiAssetRecord()
    '''
def toIncludeFilterBy():
    '''public void toIncludeFilterBy(final boolean toSet)
    '''
def getIncludeFilterBy():
    '''public boolean getIncludeFilterBy()
    '''
