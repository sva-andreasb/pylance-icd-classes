PLUSC_OP_RGE_FROM = "String  PLUSCOPRGEFROM""
PLUSC_OP_RGE_TO = "String  PLUSCOPRGETO""
PLUSC_IS_CON_DESC = "String  PLUSCISCONDESC""
PLUSC_IS_CON_DESC_LONGDESC = "String  PLUSCISCONDESC_LONGDESCRIPTION""
PLUSC_IS_CONTAM = "String  PLUSCISCONTAM""
PLUSC_IS_MTE_CLASS = "String  PLUSCISMTECLASS""
PLUSC_IS_MTE = "String  PLUSCISMTE""
PLUSC_DUE_DATE_NP = "String  PLUSCDUEDATE_NP""
PLUSC_DUE_DATE = "String  PLUSCDUEDATE""
PLUSC_IS_CALIBRATION = "String  ISCALIBRATION""
def Asset():
'''public Asset(final MboSet ms)
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
def getAssetMeterNowDate():
'''public Date getAssetMeterNowDate()
'''
pass
def modify():
'''public void modify()
'''
pass
def add():
'''public void add()
'''
pass
def updateDesc():
'''public void updateDesc()
'''
pass
def save():
'''public void save()
'''
pass
def createAssetTrans():
'''public MboRemote createAssetTrans()
'''
pass
def createMatRecTrans():
'''public MboRemote createMatRecTrans()
'''
pass
def delete():
'''public void delete(final long modifier)
'''
pass
def canDelete():
'''public void canDelete()
'''
pass
def appValidate():
'''public void appValidate()
'''
pass
def isInventoryTypeLocation():
'''public boolean isInventoryTypeLocation()
'''
pass
def isInventoryLocation():
'''public boolean isInventoryLocation()
'''
pass
def isDecommissionedLocation():
'''public boolean isDecommissionedLocation()
'''
pass
def getBinnum():
'''public void getBinnum()
'''
pass
def createHistoryForWorkOrder():
'''public void createHistoryForWorkOrder(final String wonum)
'''
pass
def setChildren():
'''public void setChildren(final boolean value)
'''
pass
def isRotating():
'''public boolean isRotating()
'''
pass
def recordAssetStatusChange():
'''public void recordAssetStatusChange(final MboRemote woMbo, final Date changeDate, final String code, final boolean operational)
'''
pass
def reportDowntime():
'''public void reportDowntime(final MboRemote woMbo, final Date startDate, final Date endDate, final double hoursDown, final String code, final boolean operational)
'''
pass
def lastAssetStatusForAssetnum():
'''public MboRemote lastAssetStatusForAssetnum()
'''
pass
def lastUpOrDownAssetStatusForAssetnum():
'''public MboRemote lastUpOrDownAssetStatusForAssetnum()
'''
pass
def intermediateAssetStatusExists():
'''public boolean intermediateAssetStatusExists(final Date newDTStart, final Date mostRecentNotRunningAssetStatusDate)
'''
pass
def calculateDownTime():
'''public double calculateDownTime(final Date lastChangeDate, final Date currentChangeDate)
'''
pass
def issueAsset():
'''public void issueAsset(final String newLocation, final String memo, final Date dateMoved, final String wonum, final boolean checkMismatch, final boolean checkOccupied, final boolean updateWo, final String matUseTransID)
'''
pass
def returnAsset():
'''public void returnAsset(final String newLocation, final String memo, final Date dateMoved, final String wonum, final String newBinnum, final String ponum, final String glCreditAcct, final String glDebitAcct, final boolean updateWo, final String matRecTransID)
'''
pass
def canReturnAsset():
'''public void canReturnAsset(final String newLocation, final String memo, final Date dateMoved, final String wonum, final String newBinnum, final String ponum, final String glCreditAcct, final String glDebitAcct, final boolean updateWo, final String matRecTransID)
'''
pass
def returnAssetForAsset():
'''public void returnAssetForAsset(final String newLocation, final String memo, final Date dateMoved, final String wonum, final String newBinnum, final String ponum, final String glCreditAcct, final String glDebitAcct, final boolean updateWo)
'''
pass
def moveAssetWithinNonInventory():
'''public void moveAssetWithinNonInventory(final String newLocation, final String memo, final Date dateMoved, final String enterBy, final String wonum, final String toParent, final boolean checkMismatch, final boolean checkOccupied, final boolean updateWo)
public void moveAssetWithinNonInventory(final String newLocation, final String memo, final Date dateMoved, final String wonum, final String toParent, final boolean checkMismatch, final boolean checkOccupied, final boolean updateWo)
'''
pass
def canMoveAssetWithinNonInventory():
'''public void canMoveAssetWithinNonInventory(final String newLocation, final String memo, final Date dateMoved, final String enterBy, final String wonum, final String toParent, final boolean checkMismatch, final boolean checkOccupied, final boolean updateWo)
public void canMoveAssetWithinNonInventory(final String newLocation, final String memo, final Date dateMoved, final String wonum, final String toParent, final boolean checkMismatch, final boolean checkOccupied, final boolean updateWo)
'''
pass
def moveAssetWithinInventory():
'''public void moveAssetWithinInventory(final String newLocation, final String memo, final Date dateMoved, final String newBinnum, final String ponum, final String glCreditAcct, final String glDebitAcct, final String matRecTransID)
'''
pass
def moveAssetWithinInventoryAcrossOrgFromHolding():
'''public void moveAssetWithinInventoryAcrossOrgFromHolding(final String newLocation, final String memo, final Date dateMoved, final String newBinnum, final String orgid, final String glCreditAcct, final String glDebitAcct, final String matRecTransID)
'''
pass
def canMoveAssetWithinInventory():
'''public void canMoveAssetWithinInventory(final String newLocation, final String memo, final Date dateMoved, final String newBinnum, final String ponum, final String glCreditAcct, final String glDebitAcct, final String matRecTransID)
'''
pass
def canMoveAssetWithinInventoryCrossOrgFromHolding():
'''public void canMoveAssetWithinInventoryCrossOrgFromHolding(final String newLocation, final String memo, final Date dateMoved, final String newBinnum, final String orgid, final String glCreditAcct, final String glDebitAcct, final String matRecTransID)
'''
pass
def isLocAuthorized():
'''public void isLocAuthorized(final MboRemote ofloc)
'''
pass
def isGLAccountValid():
'''public void isGLAccountValid(final String glAccount, final String glType)
public void isGLAccountValid(final String glAccount, final String glType, final String orgId)
'''
pass
def isGLAccountPartialValid():
'''public void isGLAccountPartialValid(final String glAccount)
'''
pass
def incrInvCost():
'''public void incrInvCost(final double amount)
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
def getParents():
'''public MboSetRemote getParents()
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
def getTop():
'''public MboSetRemote getTop()
'''
pass
def getHierarchies():
'''public String[] getHierarchies()
'''
pass
def alreadyAppliedIAS():
'''public boolean alreadyAppliedIAS()
'''
pass
def canApplyIAS():
'''public void canApplyIAS()
'''
pass
def applyIAS():
'''public void applyIAS(final boolean autokey)
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
def isAssetBeingCreatedViaApplyIAS():
'''public boolean isAssetBeingCreatedViaApplyIAS()
'''
pass
def applyIASGenPMs():
'''public MboSetRemote applyIASGenPMs(final boolean autokey)
'''
pass
def applyIASGenSpareParts():
'''public MboSetRemote applyIASGenSpareParts(final MboSetRemote itemStructSet)
'''
pass
def autoKeyAll():
'''public void autoKeyAll(final boolean doChildren)
'''
pass
def setAssetnumOnRelated():
'''public void setAssetnumOnRelated()
'''
pass
def generateAutoKey():
'''public void generateAutoKey()
'''
pass
def autoKeyAssetnumForChildSet():
'''public void autoKeyAssetnumForChildSet(final boolean doChildren)
'''
pass
def autoKeyPmnumForSet():
'''public void autoKeyPmnumForSet(final boolean doChildren)
'''
pass
def setParent():
'''public void setParent(final String newParent)
'''
pass
def acceptMyNewSet():
'''public void acceptMyNewSet(final MboSetRemote myNewSet)
'''
pass
def getMyChildAssetSet():
'''public MboSetRemote getMyChildAssetSet()
'''
pass
def getMySparePartSet():
'''public MboSetRemote getMySparePartSet()
'''
pass
def getMyPMSet():
'''public MboSetRemote getMyPMSet()
'''
pass
def getMyParent():
'''public MboRemote getMyParent()
'''
pass
def getChild():
'''public MboRemote getChild(final int row)
'''
pass
def getValidateOrder():
'''public String[] getValidateOrder()
'''
pass
def zeroCosts():
'''public void zeroCosts(final boolean ytd, final boolean total)
'''
pass
def setItemNum():
'''public void setItemNum(final String newItem, final String itemSetID, final String conditionCode)
'''
pass
def appendDescription():
'''public void appendDescription(final String descSpec)
'''
pass
def generateAssetSpec():
'''public MboSetRemote generateAssetSpec()
'''
pass
def clearClassification():
'''public void clearClassification()
'''
pass
def duplicate():
'''public MboRemote duplicate()
'''
pass
def copySpareParts():
'''public void copySpareParts(final MboSetRemote spareParts)
'''
pass
def initRelationship():
'''public void initRelationship(final String relationName, final MboSetRemote mboSet)
'''
pass
def validateAssetSite():
'''public void validateAssetSite(final String asset_type, final String siteid)
'''
pass
def checkForAssetSite():
'''public void checkForAssetSite(final String siteid)
'''
pass
def checkForChildrenAssetSite():
'''public void checkForChildrenAssetSite(final String siteid)
'''
pass
def checkForNewAssetSite():
'''public void checkForNewAssetSite(final boolean replaceAssetFlag)
'''
pass
def setWoNumAssetMv():
'''public void setWoNumAssetMv(final String wonum)
'''
pass
def setPoNumAssetMv():
'''public void setPoNumAssetMv(final String ponum)
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
def getStatusListName():
'''public String getStatusListName()
'''
pass
def canChangeStatus():
'''public void canChangeStatus(final String changeToStatus, final long accessModifier)
'''
pass
def changeStatus():
'''public void changeStatus(final String status, final boolean rollToAllChildren, final boolean removeFromActiveRoutes, final boolean removeFromActiveSP, final boolean changePMStatus)
public void changeStatus(final String status, boolean rollToAllChildren, final boolean removeFromActiveRoutes, final boolean removeFromActiveSP, final boolean changePMStatus, final Hashtable changedStatusPMs, final LocationRemote topLevelLocationOnStatusChangeFromLocStatChangeRollDown)
public void changeStatus(final String status, final boolean rollToAllChildren, final boolean removeFromActiveRoutes, final boolean removeFromActiveSP, final boolean changePMStatus, final Hashtable changedStatusPMs)
'''
pass
def isActiveRoutes():
'''public boolean isActiveRoutes()
'''
pass
def isActiveSP():
'''public boolean isActiveSP()
'''
pass
def isActivePM():
'''public boolean isActivePM()
'''
pass
def createAssetToBeMoved():
'''public Asset createAssetToBeMoved()
'''
pass
def setValuesForMboSet():
'''public void setValuesForMboSet(final MboSetRemote mboSet)
'''
pass
def validateMoveAcrossOrg():
'''public void validateMoveAcrossOrg(final String siteid)
'''
pass
def validateCopySpecAcrossOrgSite():
'''public boolean validateCopySpecAcrossOrgSite(final String siteid)
'''
pass
def setAssetAttributesForWO():
'''public void setAssetAttributesForWO()
public void setAssetAttributesForWO(final AutoAttrUpdateSetRemote autoAttrUpdateSet)
'''
pass
def getWarrantyInfo():
'''public List<Mbo> getWarrantyInfo(final Date woDate, final boolean isParent)
public List<Mbo> getWarrantyInfo(final Date woDate, final boolean isParent, final String type)
'''
pass
def getParentAsset():
'''public MboRemote getParentAsset(final Date date)
'''
pass
def getRootParent():
'''public MboRemote getRootParent()
'''
pass
def assetMoved():
'''public void assetMoved()
'''
pass
def childInBundle():
'''public void childInBundle()
'''
pass
def addMoreAssetsToSet():
'''public void addMoreAssetsToSet(final MboSetRemote selectedMoreMboSet, final MboSetRemote selectedMboSet)
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
def getIssueUnitForItem():
'''public String getIssueUnitForItem(final String location)
'''
pass
def getLeaseContractForAsset():
'''public MboSetRemote getLeaseContractForAsset()
'''
pass
def getWarrantyContractForAsset():
'''public MboSetRemote getWarrantyContractForAsset()
'''
pass
def getPurchaseContractForAsset():
'''public MboSetRemote getPurchaseContractForAsset()
'''
pass
def getWarranty():
'''public MboSetRemote getWarranty()
'''
pass
def autoWogen():
'''public void autoWogen()
public void autoWogen(final MboRemote assetMeter)
'''
pass
def setDefaults():
'''public void setDefaults(final String siteid, final String storeloc)
'''
pass
def getDefSiteId():
'''public String getDefSiteId()
'''
pass
def getDefStoreloc():
'''public String getDefStoreloc()
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
def copyAssetToCollectDetailsSet():
'''public void copyAssetToCollectDetailsSet(final MboSetRemote collectionSet)
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
def copyAdditionalPMAttributes():
'''public void copyAdditionalPMAttributes(final MboRemote copyToMbo, final MboRemote copyFromMbo)
'''
pass
def updateRelatedCI():
'''public void updateRelatedCI(final String newlocation, final String newsite, final String newassetnum, final boolean isChild, final String ChangeBy, final String ChangeDate)
'''
pass
def copyAssetSpecToAssetSpec():
'''public void copyAssetSpecToAssetSpec(final MboRemote newAsset)
'''
pass
def setInCopyingAssetSpecReceiveRotating():
'''public void setInCopyingAssetSpecReceiveRotating(final boolean inCopying)
'''
pass
def getInCopyingAssetSpecReceiveRotating():
'''public boolean getInCopyingAssetSpecReceiveRotating()
'''
pass
def setRememberToClearAssesInHash():
'''public void setRememberToClearAssesInHash(final boolean remberToClear)
'''
pass
def notifyAssetSpecValueChanged():
'''public void notifyAssetSpecValueChanged(final boolean valueChanged)
'''
pass
def isAssetSpecSetModified():
'''public boolean isAssetSpecSetModified()
'''
pass
def duplicateCalAsset():
'''public MboRemote duplicateCalAsset(final MboRemote newAssetRemote)
'''
pass
def setPhysicalLoc():
'''public void setPhysicalLoc()
'''
pass
def querySpotChecks():
'''public void querySpotChecks(final MboSetRemote plusWOSet, final Date fromDate, final Date toDate)
'''
pass
def queryDataSheets():
'''public void queryDataSheets(final PlusCWODSSetRemote woDsSet, final boolean loopCalibrations, final Date fromDate, final Date toDate)
'''
pass
def queryToolWoActuals():
'''public void queryToolWoActuals(final MboSetRemote plusWoSet, final Date fromDate, final Date toDate)
'''
pass
def viewDataSheets():
'''public MboSetRemote viewDataSheets(final MboRemote newDS)
'''
pass
def validateOperatingRange():
'''public void validateOperatingRange()
'''
pass
def calculateNextCalDueDate():
'''public Date calculateNextCalDueDate()
'''
pass
def getTagLocation():
'''public LocationRemote getTagLocation()
'''
pass
def getAssetBeingReplacedByThisInSwap():
'''public String[] getAssetBeingReplacedByThisInSwap()
'''
pass
def setAssetBeingReplacedByThisInSwap():
'''public void setAssetBeingReplacedByThisInSwap(final String[] assetBeingReplacedByThisInSwap)
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
def isGISDataReadonly():
'''public boolean isGISDataReadonly()
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
def getMboSet():
'''public MboSetRemote getMboSet(final String name)
'''
pass
def getServiceAddress():
'''public ServiceAddressRemote getServiceAddress()
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
def getLocationAccuracy():
'''public Double getLocationAccuracy()
'''
pass
def getAltitude():
'''public Double getAltitude()
'''
pass
def getAltitudeAccuracy():
'''public Double getAltitudeAccuracy()
'''
pass
def getHeading():
'''public Double getHeading()
'''
pass
def getLastUpdate():
'''public Date getLastUpdate()
'''
pass
def getSpeed():
'''public Double getSpeed()
'''
pass
def saveLBSData():
'''public void saveLBSData(final Double lat, final Double lng, final Double locationAccuracy, final Double altitudeAccuracy, final Double altitude, final Double heading, final Double speed)
'''
pass
def getLBSLatitudeY():
'''public Double getLBSLatitudeY()
'''
pass
def getLBSLongitudeX():
'''public Double getLBSLongitudeX()
'''
pass
def getPeriodTypeValue():
'''public String getPeriodTypeValue()
'''
pass
def createNewDepreciation():
'''public MboRemote createNewDepreciation()
'''
pass
def swapDepreciationSchedule():
'''public void swapDepreciationSchedule()
'''
pass
def swapDepreciationScheduleValidate():
'''public void swapDepreciationScheduleValidate()
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
def getCurrentMeterLife():
'''public Double getCurrentMeterLife(final String meterName)
'''
pass
def getDepreciationCurrentValue():
'''public Double getDepreciationCurrentValue()
'''
pass
def createDepreciationScheduleBasedOnItemFromMatrecTrans():
'''public MboRemote createDepreciationScheduleBasedOnItemFromMatrecTrans(final String itemNum, final String itemSetId, final MboRemote matrecTrans)
'''
pass
def createDepreciationScheduleBasedOnItem():
'''public void createDepreciationScheduleBasedOnItem(final MboRemote itemMbo)
'''
pass
def cleanupAssetsMap():
'''public static void cleanupAssetsMap()
'''
pass
def hasAssetSpecBeenCreated():
'''public boolean hasAssetSpecBeenCreated()
'''
pass
def setAssetSpecCreated():
'''public void setAssetSpecCreated(final boolean created)
'''
pass
def changeMaxStatus():
'''public void changeMaxStatus(final String internalStatus, final Date date, final String memo)
'''
pass
def assetInTransit():
'''public void assetInTransit()
'''
pass
