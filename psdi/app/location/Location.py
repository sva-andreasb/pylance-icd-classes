def Location():
    '''    public Location(final MboSet ms)
    '''
def init():
    '''    public void init()
    '''
def initFieldFlagsOnMbo():
    '''    public void initFieldFlagsOnMbo(final String attrName)
    '''
def setReadonlyForOperORStoreAfterAdd():
    '''    public void setReadonlyForOperORStoreAfterAdd()
    '''
def add():
    '''    public void add()
    '''
def generateAutoKey():
    '''    public void generateAutoKey()
    '''
def getLocationMeterNowDate():
    '''    public Date getLocationMeterNowDate()
    '''
def modify():
    '''    public void modify()
    '''
def delete():
    '''    public void delete(final long access)
    '''
def canDelete():
    '''    public void canDelete()
    '''
def cannotChangeStatus():
    '''    public void cannotChangeStatus(final MboSetRemote msr)
    '''
def isStore():
    '''    public boolean isStore()
    '''
def isCourier():
    '''    public boolean isCourier()
    '''
def isHolding():
    '''    public boolean isHolding()
    '''
def isLabor():
    '''    public boolean isLabor()
    '''
def isOperating():
    '''    public boolean isOperating()
    '''
def isDecommissioned():
    '''    public boolean isDecommissioned()
    '''
def isVendor():
    '''    public boolean isVendor()
    '''
def authorizeUserStore():
    '''    public void authorizeUserStore(final String user)
    '''
def isTop():
    '''    public boolean isTop()
    '''
def hasChildren():
    '''    public boolean hasChildren()
    '''
def hasParents():
    '''    public boolean hasParents()
    '''
def getChildren():
    '''    public MboSetRemote getChildren()
    '''
def getChildrenInAllSystems():
    '''    public MboSetRemote getChildrenInAllSystems()
    '''
def getParents():
    '''    public MboSetRemote getParents()
    public MboSetRemote getParents(final String SystemId)
    '''
def getTop():
    '''    public MboSetRemote getTop()
    '''
def getHierarchies():
    '''    public String[] getHierarchies()
    '''
def showHierarchy():
    '''    public MboSetRemote showHierarchy()
    '''
def walkUpHierarchy():
    '''    public Vector walkUpHierarchy()
    '''
def getChildrenInPrimary():
    '''    public MboSetRemote getChildrenInPrimary()
    public MboSetRemote getChildrenInPrimary(final String locSiteId)
    '''
def inPrimarySystem():
    '''    public boolean inPrimarySystem()
    public boolean inPrimarySystem(final String locSiteId)
    '''
def getPrimaryLocations():
    '''    public MboSetRemote getPrimaryLocations()
    '''
def getNonPrimaryLocations():
    '''    public MboSetRemote getNonPrimaryLocations()
    '''
def getLocItem():
    '''    public String getLocItem()
    '''
def isLocationOccupied():
    '''    public boolean isLocationOccupied(final MboRemote asset)
    public boolean isLocationOccupied(final String itemnum)
    '''
def doesHoldingLocationExistForSite():
    '''    public boolean doesHoldingLocationExistForSite(final String siteid)
    '''
def getHoldingLocationForSite():
    '''    public MboRemote getHoldingLocationForSite(final String siteid)
    '''
def isInventory():
    '''    public boolean isInventory()
    '''
def updateDesc():
    '''    public void updateDesc()
    '''
def appValidate():
    '''    public void appValidate()
    '''
def save():
    '''    public void save()
    '''
def updateGLInfo():
    '''    public void updateGLInfo()
    '''
def generateLocationMetersForMeterGroup():
    '''    public void generateLocationMetersForMeterGroup()
    '''
def getClearDupSeqNumsOnMeterGroupChange():
    '''    public boolean getClearDupSeqNumsOnMeterGroupChange()
    '''
def checkForDuplicateMeterSequenceValues():
    '''    public void checkForDuplicateMeterSequenceValues()
    '''
def appendDescription():
    '''    public void appendDescription(final String descSpec)
    '''
def generateLocationSpec():
    '''    public MboSetRemote generateLocationSpec()
    '''
def canApplyIAS():
    '''    public boolean canApplyIAS()
    '''
def applyIAS():
    '''    public Object[] applyIAS(final boolean autokey)
    '''
def applyIASAutoNumAll():
    '''    public void applyIASAutoNumAll()
    '''
def applyIASCreateChild():
    '''    public MboRemote applyIASCreateChild(final MboRemote itemStruct, final boolean autokey)
    '''
def applyIASGenPMs():
    '''    public MboSetRemote applyIASGenPMs(final boolean autokey)
    '''
def canChangeStatus():
    '''    public void canChangeStatus(final String changeToStatus, final long accessModifier)
    '''
def setInitNonInteractiveStatChange():
    '''    public void setInitNonInteractiveStatChange(final boolean value)
    '''
def getInitNonInteractiveStatChange():
    '''    public boolean getInitNonInteractiveStatChange()
    '''
def changeStatus():
    '''    public void changeStatus(final String status, final Date asOfDate, final String memo, final long accessModifier)
    public void changeStatus(final String changedStatus, final Date asOfDate, final String memo, boolean rolltoallchildren, final boolean removefromallroutes, boolean rolltoallassets, final boolean removefromalljp, final boolean removefromactivesp, final boolean changepmstatus)
    '''
def trackStatusChangedAssetInLocations():
    '''    public void trackStatusChangedAssetInLocations(final long assetuid)
    '''
def hasAssetStatusChangedAlready():
    '''    public boolean hasAssetStatusChangedAlready(final long assetuid)
    '''
def isReferencedByOpenWO():
    '''    public boolean isReferencedByOpenWO()
    '''
def isReferencedByPM():
    '''    public boolean isReferencedByPM()
    '''
def isReferencedByActiveRoutes():
    '''    public boolean isReferencedByActiveRoutes()
    '''
def isReferencedByActiveSP():
    '''    public boolean isReferencedByActiveSP()
    '''
def isReferencedByJobPlans():
    '''    public boolean isReferencedByJobPlans()
    '''
def duplicate():
    '''    public MboRemote duplicate()
    '''
def copyInvReserveSetForIssues():
    '''    public void copyInvReserveSetForIssues(final MboSetRemote invReserveSet)
    '''
def copyInvReserveSetForTransferOut():
    '''    public void copyInvReserveSetForTransferOut(final MboSetRemote invReserveSet)
    '''
def copyInvReserveSetForTransferIn():
    '''    public void copyInvReserveSetForTransferIn(final MboSetRemote invReserveSet)
    '''
def copyMatUseTransSetForReturn():
    '''    public void copyMatUseTransSetForReturn(final MboSetRemote matUseSet)
    '''
def receiveRotableAssetOnMoveFromNonInventoryWithPOLine():
    '''    public MboRemote receiveRotableAssetOnMoveFromNonInventoryWithPOLine(final MboRemote asset, final String glCredit, final String glDebit, final MboRemote mrtMbo)
    '''
def receiveRotableAssetOnMoveFromNonInventory():
    '''    public MboRemote receiveRotableAssetOnMoveFromNonInventory(final MboRemote asset, final String glCredit, final String glDebit)
    '''
def copySparePartSetForIssues():
    '''    public void copySparePartSetForIssues(final MboSetRemote sparePartSet)
    '''
def copySparePartSetForTransferOut():
    '''    public void copySparePartSetForTransferOut(final MboSetRemote sparePartSet)
    '''
def copySparePartSetForTransferIn():
    '''    public void copySparePartSetForTransferIn(final MboSetRemote sparePartSet)
    '''
def copyInvBalancesSetForTransferOut():
    '''    public void copyInvBalancesSetForTransferOut(final MboSetRemote invBalancesSet)
    '''
def copyInvBalancesSetForTransferIn():
    '''    public void copyInvBalancesSetForTransferIn(final MboSetRemote invBalancesSet)
    '''
def copyPOLineSetForTransferOut():
    '''    public void copyPOLineSetForTransferOut(final MboSetRemote poLineSet)
    '''
def warningsCopyPOLineSetForTransferOut():
    '''    public void warningsCopyPOLineSetForTransferOut()
    '''
def copyPOLineSetForTransferIn():
    '''    public void copyPOLineSetForTransferIn(final MboSetRemote poLineSet)
    '''
def copyMatRecTransSetForTransferIn():
    '''    public void copyMatRecTransSetForTransferIn(final MboSetRemote matRecTransSet)
    '''
def getStatusListName():
    '''    public String getStatusListName()
    '''
def warningsCopyPOLineSetForTransferIn():
    '''    public void warningsCopyPOLineSetForTransferIn()
    '''
def warningsCopyMatRecTransSetForTransferIn():
    '''    public void warningsCopyMatRecTransSetForTransferIn()
    '''
def initRelationship():
    '''    public void initRelationship(final String relationName, final MboSetRemote mboSet)
    '''
def selectPOItemsOut():
    '''    public MboSetRemote selectPOItemsOut()
    '''
def selectReservedItemsOut():
    '''    public MboSetRemote selectReservedItemsOut()
    '''
def selectItemsForTransferOut():
    '''    public MboSetRemote selectItemsForTransferOut()
    '''
def selectPOItemsIn():
    '''    public MboSetRemote selectPOItemsIn()
    '''
def selectMatRecTransIn():
    '''    public MboSetRemote selectMatRecTransIn()
    '''
def selectReservedItemsIn():
    '''    public MboSetRemote selectReservedItemsIn()
    '''
def selectItemsForTransferIn():
    '''    public MboSetRemote selectItemsForTransferIn()
    '''
def selectItemsForReturn():
    '''    public MboSetRemote selectItemsForReturn()
    '''
def selectReservedItems():
    '''    public MboSetRemote selectReservedItems()
    '''
def canAssociateSystem():
    '''    public boolean canAssociateSystem()
    '''
def clearClassification():
    '''    public void clearClassification()
    '''
def setLocationAttributesForWO():
    '''    public void setLocationAttributesForWO()
    public void setLocationAttributesForWO(final AutoAttrUpdateSetRemote autoAttrUpdateSet)
    '''
def getWarrantyInfo():
    '''    public List getWarrantyInfo(final Date woDate, final boolean isParent)
    public List getWarrantyInfo(final Date woDate, final boolean isParent, final String type)
    '''
def hasMeters():
    '''    public void hasMeters()
    '''
def hasReadings():
    '''    public void hasReadings()
    '''
def getAssetForLocation():
    '''    public String getAssetForLocation()
    '''
def getLeaseContractForLocation():
    '''    public MboSetRemote getLeaseContractForLocation()
    '''
def getWarranty():
    '''    public MboSetRemote getWarranty()
    '''
def getWarrantyContractForLocation():
    '''    public MboSetRemote getWarrantyContractForLocation()
    '''
def autoWogen():
    '''    public void autoWogen()
    public void autoWogen(final MboRemote locationMeter)
    '''
def createTicket():
    '''    public void createTicket(final MboRemote tkMbo)
    '''
def createWO():
    '''    public void createWO(final MboRemote workorderMbo)
    '''
def copyLocationToCollectDetailsSet():
    '''    public void copyLocationToCollectDetailsSet(final MboSetRemote collectionSet)
    '''
def addLocationsToCollectDetails():
    '''    public void addLocationsToCollectDetails(final String collectionNum)
    '''
def createWorkorder():
    '''    public MboRemote createWorkorder(final String jpnum)
    '''
def createChange():
    '''    public MboRemote createChange(final String jpnum)
    '''
def createRelease():
    '''    public MboRemote createRelease(final String jpnum)
    '''
def createServiceRequest():
    '''    public MboRemote createServiceRequest(final String tickettemplateid)
    '''
def createProblem():
    '''    public MboRemote createProblem(final String tickettemplateid)
    '''
def createIncident():
    '''    public MboRemote createIncident(final String tickettemplateid)
    '''
def validateOrderQty():
    '''    public void validateOrderQty()
    '''
def queryDataSheets():
    '''    public void queryDataSheets(final PlusCWODSSetRemote woDsSet, final boolean loopCalibrations, final Date fromDate, final Date toDate)
    '''
def canBeUsedAsTagId():
    '''    public boolean canBeUsedAsTagId()
    '''
def getAssociatedAsset():
    '''    public AssetRemote getAssociatedAsset()
    '''
def getAddressSystemForLocationMbo():
    '''    public MboRemote getAddressSystemForLocationMbo()
    '''
def getAncestorSABasedOnAddressSystem():
    '''    public MboRemote getAncestorSABasedOnAddressSystem(final MboRemote child)
    '''
def getMboSet():
    '''    public MboSetRemote getMboSet(final String name)
    '''
def getServiceAddress():
    '''    public ServiceAddressRemote getServiceAddress()
    '''
def hasServiceAddress():
    '''    public boolean hasServiceAddress()
    '''
def saveGISData():
    '''    public void saveGISData(final String address, final String lat, final String lng)
    '''
def getLatitudeY():
    '''    public Double getLatitudeY()
    '''
def getLongitudeX():
    '''    public Double getLongitudeX()
    '''
def isGISDataReadonly():
    '''    public boolean isGISDataReadonly()
    '''
def getAddressString():
    '''    public String getAddressString()
    '''
def addMoreLocationsToSet():
    '''    public void addMoreLocationsToSet(final MboSetRemote selectedMoreMboSet, final MboSetRemote selectedMboSet)
    '''
def getAutoLocateObject():
    '''    public MboRemote getAutoLocateObject(final AutoLocatable nextInChain)
    public MboRemote getAutoLocateObject()
    '''
def hasCoords():
    '''    public Boolean hasCoords()
    '''
def getTopParentInSystem():
    '''    public MboRemote getTopParentInSystem(final String SystemId)
    '''
def managePMMeterTallyOnMeterDeleteUndelete():
    '''    public void managePMMeterTallyOnMeterDeleteUndelete(final MboRemote pmMeter, final String action)
    '''
def getPMMeterTally():
    '''    public int getPMMeterTally(final MboRemote pmMeter)
    '''
def getChildrenInSystem():
    '''    public MboSetRemote getChildrenInSystem()
    '''
