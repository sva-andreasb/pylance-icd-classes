def Location():
'''public Location(final MboSet ms)
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
def setReadonlyForOperORStoreAfterAdd():
'''public void setReadonlyForOperORStoreAfterAdd()
'''
pass
def add():
'''public void add()
'''
pass
def generateAutoKey():
'''public void generateAutoKey()
'''
pass
def getLocationMeterNowDate():
'''public Date getLocationMeterNowDate()
'''
pass
def modify():
'''public void modify()
'''
pass
def delete():
'''public void delete(final long access)
'''
pass
def canDelete():
'''public void canDelete()
'''
pass
def cannotChangeStatus():
'''public void cannotChangeStatus(final MboSetRemote msr)
'''
pass
def isStore():
'''public boolean isStore()
'''
pass
def isCourier():
'''public boolean isCourier()
'''
pass
def isHolding():
'''public boolean isHolding()
'''
pass
def isLabor():
'''public boolean isLabor()
'''
pass
def isOperating():
'''public boolean isOperating()
'''
pass
def isDecommissioned():
'''public boolean isDecommissioned()
'''
pass
def isVendor():
'''public boolean isVendor()
'''
pass
def authorizeUserStore():
'''public void authorizeUserStore(final String user)
'''
pass
def isTop():
'''public boolean isTop()
'''
pass
def hasChildren():
'''public boolean hasChildren()
'''
pass
def hasParents():
'''public boolean hasParents()
'''
pass
def getChildren():
'''public MboSetRemote getChildren()
'''
pass
def getChildrenInAllSystems():
'''public MboSetRemote getChildrenInAllSystems()
'''
pass
def getParents():
'''public MboSetRemote getParents()
public MboSetRemote getParents(final String SystemId)
'''
pass
def getTop():
'''public MboSetRemote getTop()
'''
pass
def getHierarchies():
'''public String[] getHierarchies()
'''
pass
def showHierarchy():
'''public MboSetRemote showHierarchy()
'''
pass
def walkUpHierarchy():
'''public Vector walkUpHierarchy()
'''
pass
def getChildrenInPrimary():
'''public MboSetRemote getChildrenInPrimary()
public MboSetRemote getChildrenInPrimary(final String locSiteId)
'''
pass
def inPrimarySystem():
'''public boolean inPrimarySystem()
public boolean inPrimarySystem(final String locSiteId)
'''
pass
def getPrimaryLocations():
'''public MboSetRemote getPrimaryLocations()
'''
pass
def getNonPrimaryLocations():
'''public MboSetRemote getNonPrimaryLocations()
'''
pass
def getLocItem():
'''public String getLocItem()
'''
pass
def isLocationOccupied():
'''public boolean isLocationOccupied(final MboRemote asset)
public boolean isLocationOccupied(final String itemnum)
'''
pass
def doesHoldingLocationExistForSite():
'''public boolean doesHoldingLocationExistForSite(final String siteid)
'''
pass
def getHoldingLocationForSite():
'''public MboRemote getHoldingLocationForSite(final String siteid)
'''
pass
def isInventory():
'''public boolean isInventory()
'''
pass
def updateDesc():
'''public void updateDesc()
'''
pass
def appValidate():
'''public void appValidate()
'''
pass
def save():
'''public void save()
'''
pass
def updateGLInfo():
'''public void updateGLInfo()
'''
pass
def generateLocationMetersForMeterGroup():
'''public void generateLocationMetersForMeterGroup()
'''
pass
def getClearDupSeqNumsOnMeterGroupChange():
'''public boolean getClearDupSeqNumsOnMeterGroupChange()
'''
pass
def checkForDuplicateMeterSequenceValues():
'''public void checkForDuplicateMeterSequenceValues()
'''
pass
def appendDescription():
'''public void appendDescription(final String descSpec)
'''
pass
def generateLocationSpec():
'''public MboSetRemote generateLocationSpec()
'''
pass
def canApplyIAS():
'''public boolean canApplyIAS()
'''
pass
def applyIAS():
'''public Object[] applyIAS(final boolean autokey)
'''
pass
def applyIASAutoNumAll():
'''public void applyIASAutoNumAll()
'''
pass
def applyIASCreateChild():
'''public MboRemote applyIASCreateChild(final MboRemote itemStruct, final boolean autokey)
'''
pass
def applyIASGenPMs():
'''public MboSetRemote applyIASGenPMs(final boolean autokey)
'''
pass
def canChangeStatus():
'''public void canChangeStatus(final String changeToStatus, final long accessModifier)
'''
pass
def setInitNonInteractiveStatChange():
'''public void setInitNonInteractiveStatChange(final boolean value)
'''
pass
def getInitNonInteractiveStatChange():
'''public boolean getInitNonInteractiveStatChange()
'''
pass
def changeStatus():
'''public void changeStatus(final String status, final Date asOfDate, final String memo, final long accessModifier)
public void changeStatus(final String changedStatus, final Date asOfDate, final String memo, boolean rolltoallchildren, final boolean removefromallroutes, boolean rolltoallassets, final boolean removefromalljp, final boolean removefromactivesp, final boolean changepmstatus)
'''
pass
def trackStatusChangedAssetInLocations():
'''public void trackStatusChangedAssetInLocations(final long assetuid)
'''
pass
def hasAssetStatusChangedAlready():
'''public boolean hasAssetStatusChangedAlready(final long assetuid)
'''
pass
def isReferencedByOpenWO():
'''public boolean isReferencedByOpenWO()
'''
pass
def isReferencedByPM():
'''public boolean isReferencedByPM()
'''
pass
def isReferencedByActiveRoutes():
'''public boolean isReferencedByActiveRoutes()
'''
pass
def isReferencedByActiveSP():
'''public boolean isReferencedByActiveSP()
'''
pass
def isReferencedByJobPlans():
'''public boolean isReferencedByJobPlans()
'''
pass
def duplicate():
'''public MboRemote duplicate()
'''
pass
def copyInvReserveSetForIssues():
'''public void copyInvReserveSetForIssues(final MboSetRemote invReserveSet)
'''
pass
def copyInvReserveSetForTransferOut():
'''public void copyInvReserveSetForTransferOut(final MboSetRemote invReserveSet)
'''
pass
def copyInvReserveSetForTransferIn():
'''public void copyInvReserveSetForTransferIn(final MboSetRemote invReserveSet)
'''
pass
def copyMatUseTransSetForReturn():
'''public void copyMatUseTransSetForReturn(final MboSetRemote matUseSet)
'''
pass
def receiveRotableAssetOnMoveFromNonInventoryWithPOLine():
'''public MboRemote receiveRotableAssetOnMoveFromNonInventoryWithPOLine(final MboRemote asset, final String glCredit, final String glDebit, final MboRemote mrtMbo)
'''
pass
def receiveRotableAssetOnMoveFromNonInventory():
'''public MboRemote receiveRotableAssetOnMoveFromNonInventory(final MboRemote asset, final String glCredit, final String glDebit)
'''
pass
def copySparePartSetForIssues():
'''public void copySparePartSetForIssues(final MboSetRemote sparePartSet)
'''
pass
def copySparePartSetForTransferOut():
'''public void copySparePartSetForTransferOut(final MboSetRemote sparePartSet)
'''
pass
def copySparePartSetForTransferIn():
'''public void copySparePartSetForTransferIn(final MboSetRemote sparePartSet)
'''
pass
def copyInvBalancesSetForTransferOut():
'''public void copyInvBalancesSetForTransferOut(final MboSetRemote invBalancesSet)
'''
pass
def copyInvBalancesSetForTransferIn():
'''public void copyInvBalancesSetForTransferIn(final MboSetRemote invBalancesSet)
'''
pass
def copyPOLineSetForTransferOut():
'''public void copyPOLineSetForTransferOut(final MboSetRemote poLineSet)
'''
pass
def warningsCopyPOLineSetForTransferOut():
'''public void warningsCopyPOLineSetForTransferOut()
'''
pass
def copyPOLineSetForTransferIn():
'''public void copyPOLineSetForTransferIn(final MboSetRemote poLineSet)
'''
pass
def copyMatRecTransSetForTransferIn():
'''public void copyMatRecTransSetForTransferIn(final MboSetRemote matRecTransSet)
'''
pass
def getStatusListName():
'''public String getStatusListName()
'''
pass
def warningsCopyPOLineSetForTransferIn():
'''public void warningsCopyPOLineSetForTransferIn()
'''
pass
def warningsCopyMatRecTransSetForTransferIn():
'''public void warningsCopyMatRecTransSetForTransferIn()
'''
pass
def initRelationship():
'''public void initRelationship(final String relationName, final MboSetRemote mboSet)
'''
pass
def selectPOItemsOut():
'''public MboSetRemote selectPOItemsOut()
'''
pass
def selectReservedItemsOut():
'''public MboSetRemote selectReservedItemsOut()
'''
pass
def selectItemsForTransferOut():
'''public MboSetRemote selectItemsForTransferOut()
'''
pass
def selectPOItemsIn():
'''public MboSetRemote selectPOItemsIn()
'''
pass
def selectMatRecTransIn():
'''public MboSetRemote selectMatRecTransIn()
'''
pass
def selectReservedItemsIn():
'''public MboSetRemote selectReservedItemsIn()
'''
pass
def selectItemsForTransferIn():
'''public MboSetRemote selectItemsForTransferIn()
'''
pass
def selectItemsForReturn():
'''public MboSetRemote selectItemsForReturn()
'''
pass
def selectReservedItems():
'''public MboSetRemote selectReservedItems()
'''
pass
def canAssociateSystem():
'''public boolean canAssociateSystem()
'''
pass
def clearClassification():
'''public void clearClassification()
'''
pass
def setLocationAttributesForWO():
'''public void setLocationAttributesForWO()
public void setLocationAttributesForWO(final AutoAttrUpdateSetRemote autoAttrUpdateSet)
'''
pass
def getWarrantyInfo():
'''public List getWarrantyInfo(final Date woDate, final boolean isParent)
public List getWarrantyInfo(final Date woDate, final boolean isParent, final String type)
'''
pass
def hasMeters():
'''public void hasMeters()
'''
pass
def hasReadings():
'''public void hasReadings()
'''
pass
def getAssetForLocation():
'''public String getAssetForLocation()
'''
pass
def getLeaseContractForLocation():
'''public MboSetRemote getLeaseContractForLocation()
'''
pass
def getWarranty():
'''public MboSetRemote getWarranty()
'''
pass
def getWarrantyContractForLocation():
'''public MboSetRemote getWarrantyContractForLocation()
'''
pass
def autoWogen():
'''public void autoWogen()
public void autoWogen(final MboRemote locationMeter)
'''
pass
def createTicket():
'''public void createTicket(final MboRemote tkMbo)
'''
pass
def createWO():
'''public void createWO(final MboRemote workorderMbo)
'''
pass
def copyLocationToCollectDetailsSet():
'''public void copyLocationToCollectDetailsSet(final MboSetRemote collectionSet)
'''
pass
def addLocationsToCollectDetails():
'''public void addLocationsToCollectDetails(final String collectionNum)
'''
pass
def createWorkorder():
'''public MboRemote createWorkorder(final String jpnum)
'''
pass
def createChange():
'''public MboRemote createChange(final String jpnum)
'''
pass
def createRelease():
'''public MboRemote createRelease(final String jpnum)
'''
pass
def createServiceRequest():
'''public MboRemote createServiceRequest(final String tickettemplateid)
'''
pass
def createProblem():
'''public MboRemote createProblem(final String tickettemplateid)
'''
pass
def createIncident():
'''public MboRemote createIncident(final String tickettemplateid)
'''
pass
def validateOrderQty():
'''public void validateOrderQty()
'''
pass
def queryDataSheets():
'''public void queryDataSheets(final PlusCWODSSetRemote woDsSet, final boolean loopCalibrations, final Date fromDate, final Date toDate)
'''
pass
def canBeUsedAsTagId():
'''public boolean canBeUsedAsTagId()
'''
pass
def getAssociatedAsset():
'''public AssetRemote getAssociatedAsset()
'''
pass
def getAddressSystemForLocationMbo():
'''public MboRemote getAddressSystemForLocationMbo()
'''
pass
def getAncestorSABasedOnAddressSystem():
'''public MboRemote getAncestorSABasedOnAddressSystem(final MboRemote child)
'''
pass
def getMboSet():
'''public MboSetRemote getMboSet(final String name)
'''
pass
def getServiceAddress():
'''public ServiceAddressRemote getServiceAddress()
'''
pass
def hasServiceAddress():
'''public boolean hasServiceAddress()
'''
pass
def saveGISData():
'''public void saveGISData(final String address, final String lat, final String lng)
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
def isGISDataReadonly():
'''public boolean isGISDataReadonly()
'''
pass
def getAddressString():
'''public String getAddressString()
'''
pass
def addMoreLocationsToSet():
'''public void addMoreLocationsToSet(final MboSetRemote selectedMoreMboSet, final MboSetRemote selectedMboSet)
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
def getTopParentInSystem():
'''public MboRemote getTopParentInSystem(final String SystemId)
'''
pass
def managePMMeterTallyOnMeterDeleteUndelete():
'''public void managePMMeterTallyOnMeterDeleteUndelete(final MboRemote pmMeter, final String action)
'''
pass
def getPMMeterTally():
'''public int getPMMeterTally(final MboRemote pmMeter)
'''
pass
def getChildrenInSystem():
'''public MboSetRemote getChildrenInSystem()
'''
pass
