IBM_COPYRIGHT = "String \n\nLicensed Materials - Property of IBM\n5725-E24\n(C)Copyright IBM Corporation 2007, 2013.\nAll Rights Reserved.\nUS Government Users Restricted Rights - Use, duplication \nor disclosure restricted by GSA ADP Schedule Contract with IBM Corp.\n\n""
DECOMMISSION_CIS_IN_BASELINE_PROPERTY = "String cci.changestatus.decommissionCIsInBaseline""
intLinkMethodUI = "String User Interface""
intLinkMethodReconciliation = "String Reconciliation""
intLinkMethodOther = "String Other""
linkRuleCreateGeneric = "String CCIAssetCICreateGeneric""
def CCICI():
'''public CCICI(final MboSet ms)
'''
pass
def isTopLevel():
'''public boolean isTopLevel()
'''
pass
def save():
'''public void save()
'''
pass
def getDISInfo():
'''public DISInfo getDISInfo()
'''
pass
def updateCIAssetLinkInfo():
'''public void updateCIAssetLinkInfo(final Date linkDate, final String linkBy, final String linkMethod, final String linkRule, final boolean toUpdateLinkRule)
'''
pass
def syncAuthorizedCI():
'''public ArrayList<CCIPromotionResults> syncAuthorizedCI(final long synchronizationOptions)
public ArrayList<CCIPromotionResults> syncAuthorizedCI(final long synchronizationOptions, final CCITraversalCache cache)
'''
pass
def copyAttributeFromActualCI():
'''public void copyAttributeFromActualCI(final CISpecRemote ciSpec)
'''
pass
def getSpecificationAttribute():
'''public SpecificationMboRemote getSpecificationAttribute(final String assetAttrID)
'''
pass
def delete():
'''public void delete(final long accessModifier)
public void delete(final boolean dontCheckoptherApps, final long accessModifier)
'''
pass
def undelete():
'''public void undelete()
'''
pass
def changeStatus():
'''public void changeStatus(final String status, final Date asOfDate, final String memo)
public void changeStatus(final String status, final Date asOfDate, final String memo, final boolean childFlag)
'''
pass
def duplicate():
'''public MboRemote duplicate()
'''
pass
def getSourceRelations():
'''public MboSetRemote getSourceRelations(final Date asOf)
public MboSetRemote getSourceRelations()
'''
pass
def getTargetRelations():
'''public MboSetRemote getTargetRelations(final Date asOf)
public MboSetRemote getTargetRelations()
'''
pass
def handleRFC():
'''public void handleRFC(final MboRemote parentCI)
'''
pass
def generateSpecSet():
'''public MboSetRemote generateSpecSet(final CCITraversalCache tc)
'''
pass
def processOldAndNewSpecSets():
'''public void processOldAndNewSpecSets(final MboSetRemote oldSpecDeletedSet, final MboSetRemote newSpecSet)
'''
pass
def sortedClassSpecSet():
'''public Vector sortedClassSpecSet(final MboSetRemote classSpecSet, final MboRemote mbo)
'''
pass
def addDetailInfor():
'''public void addDetailInfor(final SpecificationMboRemote smr, final MboRemote wo, final CCITraversalCache.ClassSpecInfo csi, final CCITraversalCache.ClassSpecUseWithInfo csuwi)
'''
pass
def createGenericAsset():
'''public boolean createGenericAsset()
public boolean createGenericAsset(final String reconTaskName)
public boolean createGenericAsset(final boolean isValidateDupDisGuid, final boolean isValidateLinkRule, final LinkValidatorMetaLoader linkRuleMetaLoader)
'''
pass
def clearStatusChangeFields():
'''public synchronized void clearStatusChangeFields()
'''
pass
def getDefaultStatus():
'''public String getDefaultStatus()
'''
pass
def changeStatusBypassingChecks():
'''public void changeStatusBypassingChecks(final String targetStatus, String memo)
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
def getSAMboFromAssetLoc():
'''public MboRemote getSAMboFromAssetLoc()
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
def hasCoords():
'''public Boolean hasCoords()
'''
pass
def actionOnAssetNumFld():
'''public void actionOnAssetNumFld(final MboRemote asset)
'''
pass
