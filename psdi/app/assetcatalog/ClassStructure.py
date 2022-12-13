def ClassStructure():
'''public ClassStructure(final MboSet ms)
'''
pass
def add():
'''public void add()
'''
pass
def init():
'''public void init()
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
def undelete():
'''public void undelete()
'''
pass
def duplicate():
'''public MboRemote duplicate()
'''
pass
def getClassificationMbo():
'''public MboRemote getClassificationMbo()
'''
pass
def isGenAssetDesc():
'''public boolean isGenAssetDesc()
'''
pass
def genClassstructureDesc():
'''public String genClassstructureDesc()
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
def getTop():
'''public MboSetRemote getTop()
'''
pass
def storeParentClassStructures():
'''public void storeParentClassStructures()
'''
pass
def getParentClassStructures():
'''public Vector getParentClassStructures()
'''
pass
def storeChildClassStructures():
'''public void storeChildClassStructures()
'''
pass
def getChildClassStructures():
'''public Vector getChildClassStructures()
'''
pass
def getHierarchyPath():
'''public String getHierarchyPath()
'''
pass
def getHierarchies():
'''public String[] getHierarchies()
'''
pass
def uncheckUseWith():
'''public void uncheckUseWith(final String attributename)
'''
pass
def clearParentClassification():
'''public void clearParentClassification()
'''
pass
def appValidate():
'''public void appValidate()
'''
pass
def smartFindByObjectName():
'''public MboSetRemote smartFindByObjectName(final String sourceObj, final String targetAttrName, final String value, final boolean exact)
'''
pass
def hasSiteOrgSecurity():
'''public boolean hasSiteOrgSecurity()
'''
pass
def populateUseWith():
'''public void populateUseWith(final MboRemote parent)
public void populateUseWith(final MboRemote parent, final MboSetRemote thisUseWithSet)
'''
pass
def getUseWith():
'''public MboRemote getUseWith(String objectName)
'''
pass
def deleteUseWith():
'''public MboSetRemote deleteUseWith(final MboRemote parent)
'''
pass
def applyUpHierarchy():
'''public void applyUpHierarchy(MboRemote parent)
'''
pass
def applyDownHierarchy():
'''public void applyDownHierarchy(final MboRemote classSpec)
'''
pass
def isTopLevel():
'''public boolean isTopLevel(final String objectName)
'''
pass
def inClassificationApp():
'''public boolean inClassificationApp()
'''
pass
def getMboSet():
'''public MboSetRemote getMboSet(final String name)
'''
pass
def getUseWithInClassificationApp():
'''public MboRemote getUseWithInClassificationApp(final String objectName)
'''
pass
def getMboValueData():
'''public MboValueData getMboValueData(final String attribute)
'''
pass
def getRealChildrenForUseWith():
'''public MboSetRemote getRealChildrenForUseWith(final String objectForUseWith, final String objectOrgId, final String orjectSiteId)
'''
pass
def getObjectsNotInUseWithDomain():
'''public MboSetRemote getObjectsNotInUseWithDomain(final String objectName, final boolean persistentObjectsOnly)
'''
pass
def userSaidToCheckOrgSite():
'''public boolean userSaidToCheckOrgSite()
'''
pass
def initFieldFlagsOnMbo():
'''public void initFieldFlagsOnMbo(final String attrName)
'''
pass
def canChangeOrgSite():
'''public void canChangeOrgSite(final String relationship, final MboValue orgSiteMbv)
public void canChangeOrgSite(final MboValue orgSiteMbv)
'''
pass
def setApplicationRequired():
'''public void setApplicationRequired(final String attribute, final boolean required)
'''
pass
def setByPassSortOrderValidation():
'''public void setByPassSortOrderValidation(final Boolean byPassSortOrderValidation)
'''
pass
