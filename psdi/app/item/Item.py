def Item():
    '''public Item(final MboSet ms)
    '''
def getProcess():
    '''public String getProcess()
    '''
def getStatusListName():
    '''public String getStatusListName()
    '''
def init():
    '''public void init()
    '''
def setLotTypeReadOnly():
    '''public void setLotTypeReadOnly(final boolean state)
    '''
def initFieldFlagsOnMbo():
    '''public void initFieldFlagsOnMbo(final String attrName)
    '''
def add():
    '''public void add()
    '''
def canAddKitToStore():
    '''public void canAddKitToStore()
    '''
def canModifyKitStructure():
    '''public void canModifyKitStructure()
    '''
def isNewKitComponentUniqueToSet():
    '''public void isNewKitComponentUniqueToSet(final Mbo newKitItemStruct)
    '''
def duplicate():
    '''public MboRemote duplicate()
    '''
def createTopItemStruct():
    '''public void createTopItemStruct()
    '''
def autoKeyItemnum():
    '''public void autoKeyItemnum()
    '''
def isRotating():
    '''public boolean isRotating()
    '''
def isCapitalized():
    '''public boolean isCapitalized()
    '''
def isKit():
    '''public boolean isKit()
    '''
def toggleRotating():
    '''public void toggleRotating()
    '''
def changeCapitalizedStatus():
    '''public MboSetRemote changeCapitalizedStatus(final boolean capitalized)
    public void changeCapitalizedStatus(final boolean capitalized, final String capitalacc, final String memo)
    '''
def addToStore():
    '''public InventoryRemote addToStore(final String store, final String category, final boolean validateLocationLater)
    public InventoryRemote addToStore(final String store)
    public InventoryRemote addToStore(final String store, final String category)
    '''
def isLotted():
    '''public boolean isLotted()
    '''
def isConditionEnabled():
    '''public boolean isConditionEnabled()
    '''
def getDefaultBin():
    '''public String getDefaultBin()
    '''
def canDelete():
    '''public void canDelete()
    '''
def delete():
    '''public void delete(final long access)
    '''
def canSparePartAutoAdd():
    '''public boolean canSparePartAutoAdd()
    '''
def sparePartExists():
    '''public boolean sparePartExists(final String assetnum, final String siteid)
    '''
def addSparePart():
    '''public MboRemote addSparePart(final String assetnum, final String siteid)
    '''
def applyIAS():
    '''public void applyIAS(final MboRemote applyToMbo)
    '''
def createItemSpecSet():
    '''public MboSetRemote createItemSpecSet()
    '''
def updateDesc():
    '''public void updateDesc()
    '''
def updateRelatedObjects():
    '''public void updateRelatedObjects(final String newStatus, final Date date, final String memo)
    '''
def appValidate():
    '''public void appValidate()
    '''
def save():
    '''public void save()
    '''
def appendDescription():
    '''public void appendDescription(final String descSpec)
    '''
def generateAutoKey():
    '''public void generateAutoKey()
    '''
def generateItemSpec():
    '''public MboSetRemote generateItemSpec()
    '''
def processItemSpecSet():
    '''public void processItemSpecSet()
    '''
def clearClassification():
    '''public void clearClassification()
    '''
def removeSpecialOrderItems():
    '''public boolean removeSpecialOrderItems(final Vector storeLoc)
    '''
def getOneHundredPercent():
    '''public MboRemote getOneHundredPercent()
    '''
def setThisComponentsKitAndDefaultBin():
    '''public void setThisComponentsKitAndDefaultBin(final String kitNum, final String defaultBin)
    '''
def getThisComponentsKit():
    '''public String getThisComponentsKit()
    '''
def getThisComponentsDefaultBin():
    '''public String getThisComponentsDefaultBin()
    '''
def getInternalItemType():
    '''public String getInternalItemType()
    '''
def checkWOExists():
    '''public boolean checkWOExists()
    '''
def checkInvBalancesExists():
    '''public boolean checkInvBalancesExists()
    '''
def checkAssetExists():
    '''public boolean checkAssetExists()
    '''
def checkJPExists():
    '''public boolean checkJPExists()
    '''
def checkMRExists():
    '''public boolean checkMRExists()
    '''
def checkPRExists():
    '''public boolean checkPRExists()
    '''
def checkPOExists():
    '''public boolean checkPOExists()
    '''
def checkContractExists():
    '''public boolean checkContractExists()
    '''
def checkCIExists():
    '''public boolean checkCIExists()
    '''
def changeStatus():
    '''public void changeStatus(final String status, final Date date, final String memo, final long accessModifier)
    public void changeStatus(final String status, boolean rolldown, final Date date, final String memo, final long accessModifier)
    '''
def validateChangeStatus():
    '''public void validateChangeStatus(final String status, final boolean rolldown, final Date date, final String memo)
    '''
def isPendobs():
    '''public boolean isPendobs()
    '''
def isObsolete():
    '''public boolean isObsolete()
    '''
def isPlanning():
    '''public boolean isPlanning()
    '''
def isRollDown():
    '''public boolean isRollDown()
    '''
def updateInvVendor():
    '''public void updateInvVendor()
    '''
def setUseThisItemSpecSet():
    '''public void setUseThisItemSpecSet(final MboSetRemote itemSpecSet)
    '''
def getUseThisItemSpecSet():
    '''public MboSetRemote getUseThisItemSpecSet()
    '''
def updateRotatingClassStructureSQLServer():
    '''public void updateRotatingClassStructureSQLServer(String where, int counter, final long accessModifier)
    '''
def getNumberOfRotatingAssets():
    '''public int getNumberOfRotatingAssets()
    '''
def processUpdateClassStructureID():
    '''public void processUpdateClassStructureID(final String updateSql)
    '''
def getMboSet():
    '''public MboSetRemote getMboSet(final String name)
    '''
def checkKitCostType():
    '''public void checkKitCostType(final boolean isKit)
    '''
def createNewDepreciation():
    '''public MboRemote createNewDepreciation()
    '''
def validateDepreciation():
    '''public void validateDepreciation()
    '''
