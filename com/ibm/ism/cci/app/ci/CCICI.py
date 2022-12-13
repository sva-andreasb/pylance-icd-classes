IBM_COPYRIGHT = "String  \"\n\nLicensed Materials - Property of IBM\n5725-E24\n(C)Copyright IBM Corporation 2007, 2013.\nAll Rights Reserved.\nUS Government Users Restricted Rights - Use, duplication \nor disclosure restricted by GSA ADP Schedule Contract with IBM Corp.\n\n\""
DECOMMISSION_CIS_IN_BASELINE_PROPERTY = "String  \"cci.changestatus.decommissionCIsInBaseline\""
intLinkMethodUI = "String  \"User Interface\""
intLinkMethodReconciliation = "String  \"Reconciliation\""
intLinkMethodOther = "String  \"Other\""
linkRuleCreateGeneric = "String  \"CCIAssetCICreateGeneric\""
def CCICI():
    '''public CCICI(final MboSet ms)
    '''
def isTopLevel():
    '''public boolean isTopLevel()
    '''
def save():
    '''public void save()
    '''
def getDISInfo():
    '''public DISInfo getDISInfo()
    '''
def updateCIAssetLinkInfo():
    '''public void updateCIAssetLinkInfo(final Date linkDate, final String linkBy, final String linkMethod, final String linkRule, final boolean toUpdateLinkRule)
    '''
def syncAuthorizedCI():
    '''public ArrayList<CCIPromotionResults> syncAuthorizedCI(final long synchronizationOptions)
    public ArrayList<CCIPromotionResults> syncAuthorizedCI(final long synchronizationOptions, final CCITraversalCache cache)
    '''
def copyAttributeFromActualCI():
    '''public void copyAttributeFromActualCI(final CISpecRemote ciSpec)
    '''
def getSpecificationAttribute():
    '''public SpecificationMboRemote getSpecificationAttribute(final String assetAttrID)
    '''
def delete():
    '''public void delete(final long accessModifier)
    public void delete(final boolean dontCheckoptherApps, final long accessModifier)
    '''
def undelete():
    '''public void undelete()
    '''
def changeStatus():
    '''public void changeStatus(final String status, final Date asOfDate, final String memo)
    public void changeStatus(final String status, final Date asOfDate, final String memo, final boolean childFlag)
    '''
def duplicate():
    '''public MboRemote duplicate()
    '''
def getSourceRelations():
    '''public MboSetRemote getSourceRelations(final Date asOf)
    public MboSetRemote getSourceRelations()
    '''
def getTargetRelations():
    '''public MboSetRemote getTargetRelations(final Date asOf)
    public MboSetRemote getTargetRelations()
    '''
def handleRFC():
    '''public void handleRFC(final MboRemote parentCI)
    '''
def generateSpecSet():
    '''public MboSetRemote generateSpecSet(final CCITraversalCache tc)
    '''
def processOldAndNewSpecSets():
    '''public void processOldAndNewSpecSets(final MboSetRemote oldSpecDeletedSet, final MboSetRemote newSpecSet)
    '''
def sortedClassSpecSet():
    '''public Vector sortedClassSpecSet(final MboSetRemote classSpecSet, final MboRemote mbo)
    '''
def addDetailInfor():
    '''public void addDetailInfor(final SpecificationMboRemote smr, final MboRemote wo, final CCITraversalCache.ClassSpecInfo csi, final CCITraversalCache.ClassSpecUseWithInfo csuwi)
    '''
def createGenericAsset():
    '''public boolean createGenericAsset()
    public boolean createGenericAsset(final String reconTaskName)
    public boolean createGenericAsset(final boolean isValidateDupDisGuid, final boolean isValidateLinkRule, final LinkValidatorMetaLoader linkRuleMetaLoader)
    '''
def clearStatusChangeFields():
    '''public synchronized void clearStatusChangeFields()
    '''
def getDefaultStatus():
    '''public String getDefaultStatus()
    '''
def changeStatusBypassingChecks():
    '''public void changeStatusBypassingChecks(final String targetStatus, String memo)
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
def getSAMboFromAssetLoc():
    '''public MboRemote getSAMboFromAssetLoc()
    '''
def getMboSet():
    '''public MboSetRemote getMboSet(final String name)
    '''
def getServiceAddress():
    '''public ServiceAddressRemote getServiceAddress()
    '''
def hasCoords():
    '''public Boolean hasCoords()
    '''
def actionOnAssetNumFld():
    '''public void actionOnAssetNumFld(final MboRemote asset)
    '''
