def Item():
'''public Item(final MboSet ms)
'''
pass
def getProcess():
'''public String getProcess()
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
def setLotTypeReadOnly():
'''public void setLotTypeReadOnly(final boolean state)
'''
pass
def initFieldFlagsOnMbo():
'''public void initFieldFlagsOnMbo(final String attrName)
'''
pass
def add():
'''public void add()
'''
pass
def canAddKitToStore():
'''public void canAddKitToStore()
'''
pass
def canModifyKitStructure():
'''public void canModifyKitStructure()
'''
pass
def isNewKitComponentUniqueToSet():
'''public void isNewKitComponentUniqueToSet(final Mbo newKitItemStruct)
'''
pass
def duplicate():
'''public MboRemote duplicate()
'''
pass
def createTopItemStruct():
'''public void createTopItemStruct()
'''
pass
def autoKeyItemnum():
'''public void autoKeyItemnum()
'''
pass
def isRotating():
'''public boolean isRotating()
'''
pass
def isCapitalized():
'''public boolean isCapitalized()
'''
pass
def isKit():
'''public boolean isKit()
'''
pass
def toggleRotating():
'''public void toggleRotating()
'''
pass
def changeCapitalizedStatus():
'''public MboSetRemote changeCapitalizedStatus(final boolean capitalized)
public void changeCapitalizedStatus(final boolean capitalized, final String capitalacc, final String memo)
'''
pass
def addToStore():
'''public InventoryRemote addToStore(final String store, final String category, final boolean validateLocationLater)
public InventoryRemote addToStore(final String store)
public InventoryRemote addToStore(final String store, final String category)
'''
pass
def isLotted():
'''public boolean isLotted()
'''
pass
def isConditionEnabled():
'''public boolean isConditionEnabled()
'''
pass
def getDefaultBin():
'''public String getDefaultBin()
'''
pass
def canDelete():
'''public void canDelete()
'''
pass
def delete():
'''public void delete(final long access)
'''
pass
def canSparePartAutoAdd():
'''public boolean canSparePartAutoAdd()
'''
pass
def sparePartExists():
'''public boolean sparePartExists(final String assetnum, final String siteid)
'''
pass
def addSparePart():
'''public MboRemote addSparePart(final String assetnum, final String siteid)
'''
pass
def applyIAS():
'''public void applyIAS(final MboRemote applyToMbo)
'''
pass
def createItemSpecSet():
'''public MboSetRemote createItemSpecSet()
'''
pass
def updateDesc():
'''public void updateDesc()
'''
pass
def updateRelatedObjects():
'''public void updateRelatedObjects(final String newStatus, final Date date, final String memo)
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
def appendDescription():
'''public void appendDescription(final String descSpec)
'''
pass
def generateAutoKey():
'''public void generateAutoKey()
'''
pass
def generateItemSpec():
'''public MboSetRemote generateItemSpec()
'''
pass
def processItemSpecSet():
'''public void processItemSpecSet()
'''
pass
def clearClassification():
'''public void clearClassification()
'''
pass
def removeSpecialOrderItems():
'''public boolean removeSpecialOrderItems(final Vector storeLoc)
'''
pass
def getOneHundredPercent():
'''public MboRemote getOneHundredPercent()
'''
pass
def setThisComponentsKitAndDefaultBin():
'''public void setThisComponentsKitAndDefaultBin(final String kitNum, final String defaultBin)
'''
pass
def getThisComponentsKit():
'''public String getThisComponentsKit()
'''
pass
def getThisComponentsDefaultBin():
'''public String getThisComponentsDefaultBin()
'''
pass
def getInternalItemType():
'''public String getInternalItemType()
'''
pass
def checkWOExists():
'''public boolean checkWOExists()
'''
pass
def checkInvBalancesExists():
'''public boolean checkInvBalancesExists()
'''
pass
def checkAssetExists():
'''public boolean checkAssetExists()
'''
pass
def checkJPExists():
'''public boolean checkJPExists()
'''
pass
def checkMRExists():
'''public boolean checkMRExists()
'''
pass
def checkPRExists():
'''public boolean checkPRExists()
'''
pass
def checkPOExists():
'''public boolean checkPOExists()
'''
pass
def checkContractExists():
'''public boolean checkContractExists()
'''
pass
def checkCIExists():
'''public boolean checkCIExists()
'''
pass
def changeStatus():
'''public void changeStatus(final String status, final Date date, final String memo, final long accessModifier)
public void changeStatus(final String status, boolean rolldown, final Date date, final String memo, final long accessModifier)
'''
pass
def validateChangeStatus():
'''public void validateChangeStatus(final String status, final boolean rolldown, final Date date, final String memo)
'''
pass
def isPendobs():
'''public boolean isPendobs()
'''
pass
def isObsolete():
'''public boolean isObsolete()
'''
pass
def isPlanning():
'''public boolean isPlanning()
'''
pass
def isRollDown():
'''public boolean isRollDown()
'''
pass
def updateInvVendor():
'''public void updateInvVendor()
'''
pass
def setUseThisItemSpecSet():
'''public void setUseThisItemSpecSet(final MboSetRemote itemSpecSet)
'''
pass
def getUseThisItemSpecSet():
'''public MboSetRemote getUseThisItemSpecSet()
'''
pass
def updateRotatingClassStructureSQLServer():
'''public void updateRotatingClassStructureSQLServer(String where, int counter, final long accessModifier)
'''
pass
def getNumberOfRotatingAssets():
'''public int getNumberOfRotatingAssets()
'''
pass
def processUpdateClassStructureID():
'''public void processUpdateClassStructureID(final String updateSql)
'''
pass
def getMboSet():
'''public MboSetRemote getMboSet(final String name)
'''
pass
def checkKitCostType():
'''public void checkKitCostType(final boolean isKit)
'''
pass
def createNewDepreciation():
'''public MboRemote createNewDepreciation()
'''
pass
def validateDepreciation():
'''public void validateDepreciation()
'''
pass
