def WSIOTreeSet():
    '''public WSIOTreeSet(final MboServerInterface ms)
    '''
def getChildren():
    '''public MboValueData[][] getChildren(final String object, final String key, final String[] attrs, final int maxRows)
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
def getPathToTop():
    '''public MboValueData[][] getPathToTop(final String object, final String key, final String[] attrs, final int maxRows)
    '''
def fill():
    '''public void fill(final WSIO wsio, final boolean top, final LinkedHashMap<String, String> removeMap)
    public void fill(final MboRemote parentMbo, final boolean top)
    '''
def setup():
    '''public MboRemote setup()
    '''
def getUniqueIDValue():
    '''public MboValueData getUniqueIDValue(final String object, final String[] attributes, final String[] values)
    '''
def setHierarchy():
    '''public void setHierarchy(final String object, final String key, final String hierarchy)
    '''
def getAllHierarchies():
    '''public MboValueData[][] getAllHierarchies(final String object, final String key, final String[] attrs, final int maxRows)
    '''
def getHierarchy():
    '''public MboValueData[] getHierarchy(final String object, final String key)
    '''
def findMbo():
    '''public MboRemote findMbo(final MboRemote mbo, final String key)
    '''
