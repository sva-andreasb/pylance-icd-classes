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
def Asset():
    '''public Asset(final MboSet ms)
    '''
def init():
    '''public void init()
    '''
def initFieldFlagsOnMbo():
    '''public void initFieldFlagsOnMbo(final String attrName)
    '''
def getAssetMeterNowDate():
    '''public Date getAssetMeterNowDate()
    '''
def modify():
    '''public void modify()
    '''
def add():
    '''public void add()
    '''
def updateDesc():
    '''public void updateDesc()
    '''
def save():
    '''public void save()
    '''
def createAssetTrans():
    '''public MboRemote createAssetTrans()
    '''
def createMatRecTrans():
    '''public MboRemote createMatRecTrans()
    '''
def delete():
    '''public void delete(final long modifier)
    '''
def canDelete():
    '''public void canDelete()
    '''
def appValidate():
    '''public void appValidate()
    '''
def isInventoryTypeLocation():
    '''public boolean isInventoryTypeLocation()
    '''
def isInventoryLocation():
    '''public boolean isInventoryLocation()
    '''
def isDecommissionedLocation():
    '''public boolean isDecommissionedLocation()
    '''
def getBinnum():
    '''public void getBinnum()
    '''
def createHistoryForWorkOrder():
    '''public void createHistoryForWorkOrder(final String wonum)
    '''
def setChildren():
    '''public void setChildren(final boolean value)
    '''
def isRotating():
    '''public boolean isRotating()
    '''
def recordAssetStatusChange():
    '''public void recordAssetStatusChange(final MboRemote woMbo, final Date changeDate, final String code, final boolean operational)
    '''
def reportDowntime():
    '''public void reportDowntime(final MboRemote woMbo, final Date startDate, final Date endDate, final double hoursDown, final String code, final boolean operational)
    '''
def lastAssetStatusForAssetnum():
    '''public MboRemote lastAssetStatusForAssetnum()
    '''
def lastUpOrDownAssetStatusForAssetnum():
    '''public MboRemote lastUpOrDownAssetStatusForAssetnum()
    '''
def intermediateAssetStatusExists():
    '''public boolean intermediateAssetStatusExists(final Date newDTStart, final Date mostRecentNotRunningAssetStatusDate)
    '''
def calculateDownTime():
    '''public double calculateDownTime(final Date lastChangeDate, final Date currentChangeDate)
    '''
def issueAsset():
    '''public void issueAsset(final String newLocation, final String memo, final Date dateMoved, final String wonum, final boolean checkMismatch, final boolean checkOccupied, final boolean updateWo, final String matUseTransID)
    '''
def returnAsset():
    '''public void returnAsset(final String newLocation, final String memo, final Date dateMoved, final String wonum, final String newBinnum, final String ponum, final String glCreditAcct, final String glDebitAcct, final boolean updateWo, final String matRecTransID)
    '''
def canReturnAsset():
    '''public void canReturnAsset(final String newLocation, final String memo, final Date dateMoved, final String wonum, final String newBinnum, final String ponum, final String glCreditAcct, final String glDebitAcct, final boolean updateWo, final String matRecTransID)
    '''
def returnAssetForAsset():
    '''public void returnAssetForAsset(final String newLocation, final String memo, final Date dateMoved, final String wonum, final String newBinnum, final String ponum, final String glCreditAcct, final String glDebitAcct, final boolean updateWo)
    '''
def moveAssetWithinNonInventory():
    '''public void moveAssetWithinNonInventory(final String newLocation, final String memo, final Date dateMoved, final String enterBy, final String wonum, final String toParent, final boolean checkMismatch, final boolean checkOccupied, final boolean updateWo)
    public void moveAssetWithinNonInventory(final String newLocation, final String memo, final Date dateMoved, final String wonum, final String toParent, final boolean checkMismatch, final boolean checkOccupied, final boolean updateWo)
    '''
def canMoveAssetWithinNonInventory():
    '''public void canMoveAssetWithinNonInventory(final String newLocation, final String memo, final Date dateMoved, final String enterBy, final String wonum, final String toParent, final boolean checkMismatch, final boolean checkOccupied, final boolean updateWo)
    public void canMoveAssetWithinNonInventory(final String newLocation, final String memo, final Date dateMoved, final String wonum, final String toParent, final boolean checkMismatch, final boolean checkOccupied, final boolean updateWo)
    '''
def moveAssetWithinInventory():
    '''public void moveAssetWithinInventory(final String newLocation, final String memo, final Date dateMoved, final String newBinnum, final String ponum, final String glCreditAcct, final String glDebitAcct, final String matRecTransID)
    '''
def moveAssetWithinInventoryAcrossOrgFromHolding():
    '''public void moveAssetWithinInventoryAcrossOrgFromHolding(final String newLocation, final String memo, final Date dateMoved, final String newBinnum, final String orgid, final String glCreditAcct, final String glDebitAcct, final String matRecTransID)
    '''
def canMoveAssetWithinInventory():
    '''public void canMoveAssetWithinInventory(final String newLocation, final String memo, final Date dateMoved, final String newBinnum, final String ponum, final String glCreditAcct, final String glDebitAcct, final String matRecTransID)
    '''
def canMoveAssetWithinInventoryCrossOrgFromHolding():
    '''public void canMoveAssetWithinInventoryCrossOrgFromHolding(final String newLocation, final String memo, final Date dateMoved, final String newBinnum, final String orgid, final String glCreditAcct, final String glDebitAcct, final String matRecTransID)
    '''
def isLocAuthorized():
    '''public void isLocAuthorized(final MboRemote ofloc)
    '''
def isGLAccountValid():
    '''public void isGLAccountValid(final String glAccount, final String glType)
    public void isGLAccountValid(final String glAccount, final String glType, final String orgId)
    '''
def isGLAccountPartialValid():
    '''public void isGLAccountPartialValid(final String glAccount)
    '''
def incrInvCost():
    '''public void incrInvCost(final double amount)
    '''
def isTop():
    '''public boolean isTop()
    '''
def hasChildren():
    '''public boolean hasChildren()
    '''
def hasParents():
    '''public boolean hasParents()
    '''
def getChildren():
    '''public MboSetRemote getChildren()
    '''
def getParents():
    '''public MboSetRemote getParents()
    '''
def showHierarchy():
    '''public MboSetRemote showHierarchy()
    '''
def walkUpHierarchy():
    '''public Vector walkUpHierarchy()
    '''
def getTop():
    '''public MboSetRemote getTop()
    '''
def getHierarchies():
    '''public String[] getHierarchies()
    '''
def alreadyAppliedIAS():
    '''public boolean alreadyAppliedIAS()
    '''
def canApplyIAS():
    '''public void canApplyIAS()
    '''
def applyIAS():
    '''public void applyIAS(final boolean autokey)
    '''
def applyIASAutoNumAll():
    '''public void applyIASAutoNumAll()
    '''
def applyIASCreateChild():
    '''public MboRemote applyIASCreateChild(final MboRemote itemStruct, final boolean autokey)
    '''
def isAssetBeingCreatedViaApplyIAS():
    '''public boolean isAssetBeingCreatedViaApplyIAS()
    '''
def applyIASGenPMs():
    '''public MboSetRemote applyIASGenPMs(final boolean autokey)
    '''
def applyIASGenSpareParts():
    '''public MboSetRemote applyIASGenSpareParts(final MboSetRemote itemStructSet)
    '''
def autoKeyAll():
    '''public void autoKeyAll(final boolean doChildren)
    '''
def setAssetnumOnRelated():
    '''public void setAssetnumOnRelated()
    '''
def generateAutoKey():
    '''public void generateAutoKey()
    '''
def autoKeyAssetnumForChildSet():
    '''public void autoKeyAssetnumForChildSet(final boolean doChildren)
    '''
def autoKeyPmnumForSet():
    '''public void autoKeyPmnumForSet(final boolean doChildren)
    '''
def setParent():
    '''public void setParent(final String newParent)
    '''
def acceptMyNewSet():
    '''public void acceptMyNewSet(final MboSetRemote myNewSet)
    '''
def getMyChildAssetSet():
    '''public MboSetRemote getMyChildAssetSet()
    '''
def getMySparePartSet():
    '''public MboSetRemote getMySparePartSet()
    '''
def getMyPMSet():
    '''public MboSetRemote getMyPMSet()
    '''
def getMyParent():
    '''public MboRemote getMyParent()
    '''
def getChild():
    '''public MboRemote getChild(final int row)
    '''
def getValidateOrder():
    '''public String[] getValidateOrder()
    '''
def zeroCosts():
    '''public void zeroCosts(final boolean ytd, final boolean total)
    '''
def setItemNum():
    '''public void setItemNum(final String newItem, final String itemSetID, final String conditionCode)
    '''
def appendDescription():
    '''public void appendDescription(final String descSpec)
    '''
def generateAssetSpec():
    '''public MboSetRemote generateAssetSpec()
    '''
def clearClassification():
    '''public void clearClassification()
    '''
def duplicate():
    '''public MboRemote duplicate()
    '''
def copySpareParts():
    '''public void copySpareParts(final MboSetRemote spareParts)
    '''
def initRelationship():
    '''public void initRelationship(final String relationName, final MboSetRemote mboSet)
    '''
def validateAssetSite():
    '''public void validateAssetSite(final String asset_type, final String siteid)
    '''
def checkForAssetSite():
    '''public void checkForAssetSite(final String siteid)
    '''
def checkForChildrenAssetSite():
    '''public void checkForChildrenAssetSite(final String siteid)
    '''
def checkForNewAssetSite():
    '''public void checkForNewAssetSite(final boolean replaceAssetFlag)
    '''
def setWoNumAssetMv():
    '''public void setWoNumAssetMv(final String wonum)
    '''
def setPoNumAssetMv():
    '''public void setPoNumAssetMv(final String ponum)
    '''
def getClearDupSeqNumsOnMeterGroupChange():
    '''public boolean getClearDupSeqNumsOnMeterGroupChange()
    '''
def checkForDuplicateMeterSequenceValues():
    '''public void checkForDuplicateMeterSequenceValues()
    '''
def getStatusListName():
    '''public String getStatusListName()
    '''
def canChangeStatus():
    '''public void canChangeStatus(final String changeToStatus, final long accessModifier)
    '''
def changeStatus():
    '''public void changeStatus(final String status, final boolean rollToAllChildren, final boolean removeFromActiveRoutes, final boolean removeFromActiveSP, final boolean changePMStatus)
    public void changeStatus(final String status, boolean rollToAllChildren, final boolean removeFromActiveRoutes, final boolean removeFromActiveSP, final boolean changePMStatus, final Hashtable changedStatusPMs, final LocationRemote topLevelLocationOnStatusChangeFromLocStatChangeRollDown)
    public void changeStatus(final String status, final boolean rollToAllChildren, final boolean removeFromActiveRoutes, final boolean removeFromActiveSP, final boolean changePMStatus, final Hashtable changedStatusPMs)
    '''
def isActiveRoutes():
    '''public boolean isActiveRoutes()
    '''
def isActiveSP():
    '''public boolean isActiveSP()
    '''
def isActivePM():
    '''public boolean isActivePM()
    '''
def createAssetToBeMoved():
    '''public Asset createAssetToBeMoved()
    '''
def setValuesForMboSet():
    '''public void setValuesForMboSet(final MboSetRemote mboSet)
    '''
def validateMoveAcrossOrg():
    '''public void validateMoveAcrossOrg(final String siteid)
    '''
def validateCopySpecAcrossOrgSite():
    '''public boolean validateCopySpecAcrossOrgSite(final String siteid)
    '''
def setAssetAttributesForWO():
    '''public void setAssetAttributesForWO()
    public void setAssetAttributesForWO(final AutoAttrUpdateSetRemote autoAttrUpdateSet)
    '''
def getWarrantyInfo():
    '''public List<Mbo> getWarrantyInfo(final Date woDate, final boolean isParent)
    public List<Mbo> getWarrantyInfo(final Date woDate, final boolean isParent, final String type)
    '''
def getParentAsset():
    '''public MboRemote getParentAsset(final Date date)
    '''
def getRootParent():
    '''public MboRemote getRootParent()
    '''
def assetMoved():
    '''public void assetMoved()
    '''
def childInBundle():
    '''public void childInBundle()
    '''
def addMoreAssetsToSet():
    '''public void addMoreAssetsToSet(final MboSetRemote selectedMoreMboSet, final MboSetRemote selectedMboSet)
    '''
def hasMeters():
    '''public void hasMeters()
    '''
def hasReadings():
    '''public void hasReadings()
    '''
def getIssueUnitForItem():
    '''public String getIssueUnitForItem(final String location)
    '''
def getLeaseContractForAsset():
    '''public MboSetRemote getLeaseContractForAsset()
    '''
def getWarrantyContractForAsset():
    '''public MboSetRemote getWarrantyContractForAsset()
    '''
def getPurchaseContractForAsset():
    '''public MboSetRemote getPurchaseContractForAsset()
    '''
def getWarranty():
    '''public MboSetRemote getWarranty()
    '''
def autoWogen():
    '''public void autoWogen()
    public void autoWogen(final MboRemote assetMeter)
    '''
def setDefaults():
    '''public void setDefaults(final String siteid, final String storeloc)
    '''
def getDefSiteId():
    '''public String getDefSiteId()
    '''
def getDefStoreloc():
    '''public String getDefStoreloc()
    '''
def createTicket():
    '''public void createTicket(final MboRemote tkMbo)
    '''
def createWO():
    '''public void createWO(final MboRemote workorderMbo)
    '''
def copyAssetToCollectDetailsSet():
    '''public void copyAssetToCollectDetailsSet(final MboSetRemote collectionSet)
    '''
def createWorkorder():
    '''public MboRemote createWorkorder(final String jpnum)
    '''
def createChange():
    '''public MboRemote createChange(final String jpnum)
    '''
def createRelease():
    '''public MboRemote createRelease(final String jpnum)
    '''
def createServiceRequest():
    '''public MboRemote createServiceRequest(final String tickettemplateid)
    '''
def createProblem():
    '''public MboRemote createProblem(final String tickettemplateid)
    '''
def createIncident():
    '''public MboRemote createIncident(final String tickettemplateid)
    '''
def copyAdditionalPMAttributes():
    '''public void copyAdditionalPMAttributes(final MboRemote copyToMbo, final MboRemote copyFromMbo)
    '''
def updateRelatedCI():
    '''public void updateRelatedCI(final String newlocation, final String newsite, final String newassetnum, final boolean isChild, final String ChangeBy, final String ChangeDate)
    '''
def copyAssetSpecToAssetSpec():
    '''public void copyAssetSpecToAssetSpec(final MboRemote newAsset)
    '''
def setInCopyingAssetSpecReceiveRotating():
    '''public void setInCopyingAssetSpecReceiveRotating(final boolean inCopying)
    '''
def getInCopyingAssetSpecReceiveRotating():
    '''public boolean getInCopyingAssetSpecReceiveRotating()
    '''
def setRememberToClearAssesInHash():
    '''public void setRememberToClearAssesInHash(final boolean remberToClear)
    '''
def notifyAssetSpecValueChanged():
    '''public void notifyAssetSpecValueChanged(final boolean valueChanged)
    '''
def isAssetSpecSetModified():
    '''public boolean isAssetSpecSetModified()
    '''
def duplicateCalAsset():
    '''public MboRemote duplicateCalAsset(final MboRemote newAssetRemote)
    '''
def setPhysicalLoc():
    '''public void setPhysicalLoc()
    '''
def querySpotChecks():
    '''public void querySpotChecks(final MboSetRemote plusWOSet, final Date fromDate, final Date toDate)
    '''
def queryDataSheets():
    '''public void queryDataSheets(final PlusCWODSSetRemote woDsSet, final boolean loopCalibrations, final Date fromDate, final Date toDate)
    '''
def queryToolWoActuals():
    '''public void queryToolWoActuals(final MboSetRemote plusWoSet, final Date fromDate, final Date toDate)
    '''
def viewDataSheets():
    '''public MboSetRemote viewDataSheets(final MboRemote newDS)
    '''
def validateOperatingRange():
    '''public void validateOperatingRange()
    '''
def calculateNextCalDueDate():
    '''public Date calculateNextCalDueDate()
    '''
def getTagLocation():
    '''public LocationRemote getTagLocation()
    '''
def getAssetBeingReplacedByThisInSwap():
    '''public String[] getAssetBeingReplacedByThisInSwap()
    '''
def setAssetBeingReplacedByThisInSwap():
    '''public void setAssetBeingReplacedByThisInSwap(final String[] assetBeingReplacedByThisInSwap)
    '''
def hasServiceAddress():
    '''public boolean hasServiceAddress()
    '''
def saveGISData():
    '''public void saveGISData(final String address, final String lat, final String lng)
    '''
def isGISDataReadonly():
    '''public boolean isGISDataReadonly()
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
def getMboSet():
    '''public MboSetRemote getMboSet(final String name)
    '''
def getServiceAddress():
    '''public ServiceAddressRemote getServiceAddress()
    '''
def getAutoLocateObject():
    '''public MboRemote getAutoLocateObject(final AutoLocatable nextInChain)
    public MboRemote getAutoLocateObject()
    '''
def hasCoords():
    '''public Boolean hasCoords()
    '''
def getLocationAccuracy():
    '''public Double getLocationAccuracy()
    '''
def getAltitude():
    '''public Double getAltitude()
    '''
def getAltitudeAccuracy():
    '''public Double getAltitudeAccuracy()
    '''
def getHeading():
    '''public Double getHeading()
    '''
def getLastUpdate():
    '''public Date getLastUpdate()
    '''
def getSpeed():
    '''public Double getSpeed()
    '''
def saveLBSData():
    '''public void saveLBSData(final Double lat, final Double lng, final Double locationAccuracy, final Double altitudeAccuracy, final Double altitude, final Double heading, final Double speed)
    '''
def getLBSLatitudeY():
    '''public Double getLBSLatitudeY()
    '''
def getLBSLongitudeX():
    '''public Double getLBSLongitudeX()
    '''
def getPeriodTypeValue():
    '''public String getPeriodTypeValue()
    '''
def createNewDepreciation():
    '''public MboRemote createNewDepreciation()
    '''
def swapDepreciationSchedule():
    '''public void swapDepreciationSchedule()
    '''
def swapDepreciationScheduleValidate():
    '''public void swapDepreciationScheduleValidate()
    '''
def managePMMeterTallyOnMeterDeleteUndelete():
    '''public void managePMMeterTallyOnMeterDeleteUndelete(final MboRemote pmMeter, final String action)
    '''
def getPMMeterTally():
    '''public int getPMMeterTally(final MboRemote pmMeter)
    '''
def getCurrentMeterLife():
    '''public Double getCurrentMeterLife(final String meterName)
    '''
def getDepreciationCurrentValue():
    '''public Double getDepreciationCurrentValue()
    '''
def createDepreciationScheduleBasedOnItemFromMatrecTrans():
    '''public MboRemote createDepreciationScheduleBasedOnItemFromMatrecTrans(final String itemNum, final String itemSetId, final MboRemote matrecTrans)
    '''
def createDepreciationScheduleBasedOnItem():
    '''public void createDepreciationScheduleBasedOnItem(final MboRemote itemMbo)
    '''
def cleanupAssetsMap():
    '''public static void cleanupAssetsMap()
    '''
def hasAssetSpecBeenCreated():
    '''public boolean hasAssetSpecBeenCreated()
    '''
def setAssetSpecCreated():
    '''public void setAssetSpecCreated(final boolean created)
    '''
def changeMaxStatus():
    '''public void changeMaxStatus(final String internalStatus, final Date date, final String memo)
    '''
def assetInTransit():
    '''public void assetInTransit()
    '''
