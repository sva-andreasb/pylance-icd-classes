MULTIASSET_SITE_ERRORKEY = "String  MultiAssetSiteNotSame""
CREATEWOMULTI_NONE = "String  NONE""
CREATEWOMULTI_CHILD = "String  CHILD""
CREATEWOMULTI_TASK = "String  TASK""
CREATEWOMULTI_MULTI = "String  MULTI""
CREATEWOMULTI_TOPLEVEL = "String  TOPLEVEL""
def Ticket():
'''public Ticket(final MboSet ms)
'''
pass
def getProcess():
'''public String getProcess()
'''
pass
def canTemplateApply():
'''public void canTemplateApply()
'''
pass
def getStatusListName():
'''public String getStatusListName()
'''
pass
def init():
'''public void init()
'''
pass
def initFieldFlagsOnMbo():
'''public void initFieldFlagsOnMbo(final String attrName)
'''
pass
def canEditRelatedSet():
'''public void canEditRelatedSet(final String relationName)
'''
pass
def setRelatedMboEditibility():
'''public void setRelatedMboEditibility(final String relationName)
'''
pass
def initRelationship():
'''public void initRelationship(final String relationName, final MboSetRemote mboSet)
'''
pass
def add():
'''public void add()
'''
pass
def modify():
'''public void modify()
'''
pass
def changeStatus():
'''public void changeStatus(final String status, final Date date, final String memo, final long accessModifier)
'''
pass
def canDelete():
'''public void canDelete()
'''
pass
def canDeleteAttachedDocs():
'''public void canDeleteAttachedDocs()
'''
pass
def hasActuals():
'''public boolean hasActuals()
'''
pass
def appValidate():
'''public void appValidate()
'''
pass
def delete():
'''public void delete(final long accessModifier)
'''
pass
def duplicate():
'''public MboRemote duplicate()
'''
pass
def editHistory():
'''public void editHistory()
'''
pass
def isTicketInEditHist():
'''public boolean isTicketInEditHist()
'''
pass
def startTimer():
'''public void startTimer()
'''
pass
def tkChangeMaxStatus():
'''public void tkChangeMaxStatus(final String maxstatus)
'''
pass
def stopTimer():
'''public void stopTimer()
public MboRemote stopTimer(final Date finishdatetime, final boolean noStopTimerPopup)
public MboRemote stopTimer(final Date finishdatetime, final Date startDateTime, final boolean noStopTimerPopup)
'''
pass
def createIncident():
'''public MboRemote createIncident()
public MboRemote createIncident(final String tickettemplateid)
'''
pass
def createServiceRequest():
'''public MboRemote createServiceRequest()
public MboRemote createServiceRequest(final String tickettemplateid)
'''
pass
def createSR():
'''public MboRemote createSR()
public MboRemote createSR(final String tickettemplateid)
'''
pass
def createProblem():
'''public MboRemote createProblem()
public MboRemote createProblem(final String tickettemplateid)
'''
pass
def getFailListForReport():
'''public MboSetRemote getFailListForReport()
'''
pass
def copyFailListToReportSet():
'''public void copyFailListToReportSet(final MboSetRemote failListSet)
'''
pass
def removeFailureReport():
'''public void removeFailureReport()
'''
pass
def applyTemplate():
'''public void applyTemplate(final MboRemote templateMbo)
'''
pass
def ticketStatus():
'''public String ticketStatus()
'''
pass
def applyOwner():
'''public void applyOwner(final String ownerID)
'''
pass
def applyOwnerGroup():
'''public void applyOwnerGroup(final String ownergroupID)
'''
pass
def applyAssignedOwnerGroup():
'''public void applyAssignedOwnerGroup(final String ownergroupID)
'''
pass
def ownership():
'''public void ownership()
'''
pass
def createWorkorder():
'''public Vector createWorkorder()
public Vector createWorkorder(final MboSetRemote targetSet, final boolean saveSet)
public MboRemote createWorkorder(final String jpnum)
'''
pass
def createChange():
'''public Vector createChange()
public MboRemote createChange(final String jpnum)
'''
pass
def createRelease():
'''public Vector createRelease()
public MboRemote createRelease(final String jpnum)
'''
pass
def setLinearAssetFieldsReadOnly():
'''public void setLinearAssetFieldsReadOnly(MultiAssetLocCIRemote malocMbo, final boolean readonlystate)
'''
pass
def clearLinearAssetFields():
'''public void clearLinearAssetFields(final MultiAssetLocCIRemote malocMbo)
'''
pass
def createSolution():
'''public MboRemote createSolution()
'''
pass
def findTkSite():
'''public String findTkSite()
'''
pass
def incrActLabCost():
'''public void incrActLabCost(final double incrAmount)
'''
pass
def incrActLabHrs():
'''public void incrActLabHrs(final double incrAmount)
'''
pass
def getLocForAsset():
'''public void getLocForAsset()
'''
pass
def applyAssetLoc():
'''public void applyAssetLoc()
'''
pass
def calcGLAccount():
'''public String calcGLAccount()
'''
pass
def getActivityBasedOnWonum():
'''public MboRemote getActivityBasedOnWonum(final String wonum)
'''
pass
def copyTicketToRelatedRecSet():
'''public void copyTicketToRelatedRecSet(final MboSetRemote TicketSet)
'''
pass
def copyWOToRelatedRecSet():
'''public void copyWOToRelatedRecSet(final MboSetRemote WOSet)
'''
pass
def needPopupOnStopTimer():
'''public boolean needPopupOnStopTimer()
'''
pass
def updateWorkview():
'''public void updateWorkview()
'''
pass
def clearClassification():
'''public void clearClassification()
'''
pass
def similarTickets():
'''public MboSetRemote similarTickets()
'''
pass
def relateTickets():
'''public MboSetRemote relateTickets(final MboSetRemote tkSet)
'''
pass
def relateWorkorders():
'''public MboSetRemote relateWorkorders(final MboSetRemote woSet)
'''
pass
def copyLaborToLabTransSet():
'''public void copyLaborToLabTransSet(final MboSetRemote laborSet)
'''
pass
def updateOriginator():
'''public void updateOriginator()
'''
pass
def getValidateOrder():
'''public String[] getValidateOrder()
'''
pass
def getWOClassDescription():
'''public String getWOClassDescription(final String appname)
'''
pass
def copyAssetsToMultiAsset():
'''public void copyAssetsToMultiAsset(final AssetSetRemote assetSetRemote)
'''
pass
def copyLocationsToMultiAsset():
'''public void copyLocationsToMultiAsset(final MboSetRemote locationSetRemote)
'''
pass
def copyCIsToMultiAsset():
'''public void copyCIsToMultiAsset(final MboSetRemote ciSetRemote)
'''
pass
def copyRouteStopsToMultiAsset():
'''public void copyRouteStopsToMultiAsset(final MboSetRemote routestopSetRemote)
'''
pass
def copyCollectDetailsToMultiAsset():
'''public void copyCollectDetailsToMultiAsset(final MboSetRemote collectionDetailsetRemote)
'''
pass
def checkMultiAssetLocCISite():
'''public void checkMultiAssetLocCISite(final String multiAssetSite)
'''
pass
def setmultiassetrecord():
'''public void setmultiassetrecord()
'''
pass
def copyTicketFieldsToMultiAsset():
'''public void copyTicketFieldsToMultiAsset(final MultiAssetLocCIRemote multiAssetMbo)
'''
pass
def getTopOriginator():
'''public MboRemote getTopOriginator()
'''
pass
def doClassificationCreate():
'''public void doClassificationCreate(final MboRemote newMbo, final MboRemote sourceMbo, String keyAttribute)
'''
pass
def allowSelfServiceSolutionAccess():
'''public boolean allowSelfServiceSolutionAccess()
'''
pass
def checkOrigIsFollowup():
'''public void checkOrigIsFollowup()
'''
pass
def getRecordMboName():
'''public String getRecordMboName()
'''
pass
def canPropagateRepairFacility():
'''public boolean canPropagateRepairFacility(final MboRemote newWorkorder)
'''
pass
def propagateRepairFacility():
'''public void propagateRepairFacility(final MboRemote newWorkorder)
'''
pass
def getTKServiceAddress():
'''public TKServiceAddressRemote getTKServiceAddress()
'''
pass
def hasServiceAddress():
'''public boolean hasServiceAddress()
'''
pass
def getServiceAddress():
'''public TKServiceAddressRemote getServiceAddress()
'''
pass
def getLatitudeY():
'''public Double getLatitudeY()
'''
pass
def getLongitudeX():
'''public Double getLongitudeX()
'''
pass
def getAddressString():
'''public String getAddressString()
'''
pass
def saveGISData():
'''public void saveGISData(final String address, final String lat, final String lng)
'''
pass
def isGISDataReadonly():
'''public boolean isGISDataReadonly()
'''
pass
def updateServiceAddress():
'''public void updateServiceAddress()
'''
pass
def getAutoLocateObject():
'''public MboRemote getAutoLocateObject(final AutoLocatable nextInChain)
public MboRemote getAutoLocateObject()
'''
pass
def hasCoords():
'''public Boolean hasCoords()
'''
pass
def updateReportedAndAffectedUser():
'''public void updateReportedAndAffectedUser(final String dataAttribute, final MboRemote lookupMbo)
'''
pass
def setDontSkipCreatePrimaryMALCI():
'''public void setDontSkipCreatePrimaryMALCI(final boolean dontSkip)
'''
pass
def getDontSkipCreatePrimaryMALCI():
'''public boolean getDontSkipCreatePrimaryMALCI()
'''
pass
def createPrimaryMultiAssetRecord():
'''public void createPrimaryMultiAssetRecord()
'''
pass
def toIncludeFilterBy():
'''public void toIncludeFilterBy(final boolean toSet)
'''
pass
def getIncludeFilterBy():
'''public boolean getIncludeFilterBy()
'''
pass
