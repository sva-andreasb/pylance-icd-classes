def UserProfileHierarchySet():
    '''public UserProfileHierarchySet(final MboServerInterface ms)
    '''
def init():
    '''public void init()
    '''
def clearProfile():
    '''public void clearProfile(final String userId)
    '''
def getChildren():
    '''public MboValueData[][] getChildren(final String object, final String key, final String[] attrs, final int maxRows)
    '''
def getCategoryData():
    '''public MboValueData[][] getCategoryData(final String object, final long key, final String[] attrs)
    '''
def getParent():
    '''public MboValueData[] getParent(final String object, final String key, final String[] attrs)
    '''
def getSiblings():
    '''public MboValueData[][] getSiblings(final String object, final String key, final String[] attrs, final int maxRows)
    '''
def getTop():
    '''public MboValueData[][] getTop(final String[] attrs, final int maxRows)
    '''
def getAuthorizedStoreRooms():
    '''public MboSetRemote getAuthorizedStoreRooms(final long key)
    '''
def getEntities():
    '''public MboSetRemote getEntities()
    '''
def getAuthorizedApplications():
    '''public MboSetRemote getAuthorizedApplications(final long ukey, final int sysFlag)
    '''
def getTolerances():
    '''public MboSetRemote getTolerances(final long ukey)
    '''
def getLabor():
    '''public MboSetRemote getLabor(final long key)
    '''
def getLaborFlags():
    '''public MboSetRemote getLaborFlags()
    '''
def getAuthGLFields():
    '''public HashSet getAuthGLFields(final long key)
    '''
def getAuthEntities():
    '''public Set getAuthEntities()
    '''
def getAuthLabor():
    '''public HashSet getAuthLabor(final long key)
    '''
def getAllAuthLabor():
    '''public HashSet getAllAuthLabor(final MboSetRemote laborauthset)
    '''
def getGLFields():
    '''public MboSetRemote getGLFields(final long ukey)
    '''
def resetMboSetALL():
    '''public void resetMboSetALL(final String nodelabel)
    '''
def getLimits():
    '''public MboSetRemote getLimits(final long ukey)
    '''
def hasSigOptions():
    '''public boolean hasSigOptions(final String appname, final long ukey)
    '''
def hasRestrictions():
    '''public boolean hasRestrictions(final String objectname)
    '''
def getLaborForFlag():
    '''public HashSet getLaborForFlag(final String flag)
    '''
def getPathToTop():
    '''public MboValueData[][] getPathToTop(final String object, final String key, final String[] attrs, final int maxRows)
    '''
def getAllHierarchies():
    '''public MboValueData[][] getAllHierarchies(final String object, final String key, final String[] attrs, final int maxRows)
    '''
def getHierarchy():
    '''public MboValueData[] getHierarchy(final String object, final String key)
    '''
def setHierarchy():
    '''public void setHierarchy(final String object, final String key, final String hierarchy)
    '''
def getUniqueIDValue():
    '''public MboValueData getUniqueIDValue(final String object, final String[] attributes, final String[] values)
    '''
def getLevels():
    '''public HashMap getLevels()
    '''
def getCategories():
    '''public HashMap getCategories()
    '''
