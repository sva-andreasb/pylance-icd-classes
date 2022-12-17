def ():
    '''returns UserProfileHierarchySet\n\n
    (final MboServerInterface ms)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def clearProfile():
    '''returns None\n\n
    clearProfile(final String userId)\n
    '''
def getChildren():
    '''returns MboValueData[][]\n\n
    getChildren(final String object, final String key, final String[] attrs, final int maxRows)\n
    '''
def getCategoryData():
    '''returns MboValueData[][]\n\n
    getCategoryData(final String object, final long key, final String[] attrs)\n
    '''
def getParent():
    '''returns MboValueData[]\n\n
    getParent(final String object, final String key, final String[] attrs)\n
    '''
def getSiblings():
    '''returns MboValueData[][]\n\n
    getSiblings(final String object, final String key, final String[] attrs, final int maxRows)\n
    '''
def getTop():
    '''returns MboValueData[][]\n\n
    getTop(final String[] attrs, final int maxRows)\n
    '''
def getAuthorizedStoreRooms():
    '''returns MboSetRemote\n\n
    getAuthorizedStoreRooms(final long key)\n
    '''
def getEntities():
    '''returns MboSetRemote\n\n
    getEntities()\n
    '''
def getAuthorizedApplications():
    '''returns MboSetRemote\n\n
    getAuthorizedApplications(final long ukey, final int sysFlag)\n
    '''
def getTolerances():
    '''returns MboSetRemote\n\n
    getTolerances(final long ukey)\n
    '''
def getLabor():
    '''returns MboSetRemote\n\n
    getLabor(final long key)\n
    '''
def getLaborFlags():
    '''returns MboSetRemote\n\n
    getLaborFlags()\n
    '''
def getAuthGLFields():
    '''returns HashSet\n\n
    getAuthGLFields(final long key)\n
    '''
def getAuthEntities():
    '''returns Set\n\n
    getAuthEntities()\n
    '''
def getAuthLabor():
    '''returns HashSet\n\n
    getAuthLabor(final long key)\n
    '''
def getAllAuthLabor():
    '''returns HashSet\n\n
    getAllAuthLabor(final MboSetRemote laborauthset)\n
    '''
def getGLFields():
    '''returns MboSetRemote\n\n
    getGLFields(final long ukey)\n
    '''
def resetMboSetALL():
    '''returns None\n\n
    resetMboSetALL(final String nodelabel)\n
    '''
def getLimits():
    '''returns MboSetRemote\n\n
    getLimits(final long ukey)\n
    '''
def hasSigOptions():
    '''returns boolean\n\n
    hasSigOptions(final String appname, final long ukey)\n
    '''
def hasRestrictions():
    '''returns boolean\n\n
    hasRestrictions(final String objectname)\n
    '''
def getLaborForFlag():
    '''returns HashSet\n\n
    getLaborForFlag(final String flag)\n
    '''
def getPathToTop():
    '''returns MboValueData[][]\n\n
    getPathToTop(final String object, final String key, final String[] attrs, final int maxRows)\n
    '''
def getAllHierarchies():
    '''returns MboValueData[][]\n\n
    getAllHierarchies(final String object, final String key, final String[] attrs, final int maxRows)\n
    '''
def getHierarchy():
    '''returns MboValueData[]\n\n
    getHierarchy(final String object, final String key)\n
    '''
def setHierarchy():
    '''returns None\n\n
    setHierarchy(final String object, final String key, final String hierarchy)\n
    '''
def getUniqueIDValue():
    '''returns MboValueData\n\n
    getUniqueIDValue(final String object, final String[] attributes, final String[] values)\n
    '''
def getLevels():
    '''returns HashMap\n\n
    getLevels()\n
    '''
def getCategories():
    '''returns HashMap\n\n
    getCategories()\n
    '''
