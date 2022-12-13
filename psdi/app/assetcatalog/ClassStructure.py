def ClassStructure():
    '''    public ClassStructure(final MboSet ms)
    '''
def add():
    '''    public void add()
    '''
def init():
    '''    public void init()
    '''
def canDelete():
    '''    public void canDelete()
    '''
def delete():
    '''    public void delete(final long access)
    '''
def undelete():
    '''    public void undelete()
    '''
def duplicate():
    '''    public MboRemote duplicate()
    '''
def getClassificationMbo():
    '''    public MboRemote getClassificationMbo()
    '''
def isGenAssetDesc():
    '''    public boolean isGenAssetDesc()
    '''
def genClassstructureDesc():
    '''    public String genClassstructureDesc()
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
def getParents():
    '''    public MboSetRemote getParents()
    '''
def getTop():
    '''    public MboSetRemote getTop()
    '''
def storeParentClassStructures():
    '''    public void storeParentClassStructures()
    '''
def getParentClassStructures():
    '''    public Vector getParentClassStructures()
    '''
def storeChildClassStructures():
    '''    public void storeChildClassStructures()
    '''
def getChildClassStructures():
    '''    public Vector getChildClassStructures()
    '''
def getHierarchyPath():
    '''    public String getHierarchyPath()
    '''
def getHierarchies():
    '''    public String[] getHierarchies()
    '''
def uncheckUseWith():
    '''    public void uncheckUseWith(final String attributename)
    '''
def clearParentClassification():
    '''    public void clearParentClassification()
    '''
def appValidate():
    '''    public void appValidate()
    '''
def smartFindByObjectName():
    '''    public MboSetRemote smartFindByObjectName(final String sourceObj, final String targetAttrName, final String value, final boolean exact)
    '''
def hasSiteOrgSecurity():
    '''    public boolean hasSiteOrgSecurity()
    '''
def populateUseWith():
    '''    public void populateUseWith(final MboRemote parent)
    public void populateUseWith(final MboRemote parent, final MboSetRemote thisUseWithSet)
    '''
def getUseWith():
    '''    public MboRemote getUseWith(String objectName)
    '''
def deleteUseWith():
    '''    public MboSetRemote deleteUseWith(final MboRemote parent)
    '''
def applyUpHierarchy():
    '''    public void applyUpHierarchy(MboRemote parent)
    '''
def applyDownHierarchy():
    '''    public void applyDownHierarchy(final MboRemote classSpec)
    '''
def isTopLevel():
    '''    public boolean isTopLevel(final String objectName)
    '''
def inClassificationApp():
    '''    public boolean inClassificationApp()
    '''
def getMboSet():
    '''    public MboSetRemote getMboSet(final String name)
    '''
def getUseWithInClassificationApp():
    '''    public MboRemote getUseWithInClassificationApp(final String objectName)
    '''
def getMboValueData():
    '''    public MboValueData getMboValueData(final String attribute)
    '''
def getRealChildrenForUseWith():
    '''    public MboSetRemote getRealChildrenForUseWith(final String objectForUseWith, final String objectOrgId, final String orjectSiteId)
    '''
def getObjectsNotInUseWithDomain():
    '''    public MboSetRemote getObjectsNotInUseWithDomain(final String objectName, final boolean persistentObjectsOnly)
    '''
def userSaidToCheckOrgSite():
    '''    public boolean userSaidToCheckOrgSite()
    '''
def initFieldFlagsOnMbo():
    '''    public void initFieldFlagsOnMbo(final String attrName)
    '''
def canChangeOrgSite():
    '''    public void canChangeOrgSite(final String relationship, final MboValue orgSiteMbv)
    public void canChangeOrgSite(final MboValue orgSiteMbv)
    '''
def setApplicationRequired():
    '''    public void setApplicationRequired(final String attribute, final boolean required)
    '''
def setByPassSortOrderValidation():
    '''    public void setByPassSortOrderValidation(final Boolean byPassSortOrderValidation)
    '''
