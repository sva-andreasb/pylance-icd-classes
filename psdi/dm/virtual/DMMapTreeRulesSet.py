def DMMapTreeRulesSet():
    '''public DMMapTreeRulesSet(final MboServerInterface ms)
    '''
def addNode():
    '''public MboRemote addNode(final long uniqueId, final String nodeDesc, final String relationship, final String cfgObject, final String mboObject, final String hierarchy, final MboRemote relatedMBO)
    '''
def getAllHierarchies():
    '''public MboValueData[][] getAllHierarchies(final String object, final String key, final String[] attrs, final int maxRows)
    '''
def getChildren():
    '''public MboValueData[][] getChildren(final String object, final String key, final String[] attrs, final int maxRows)
    '''
def getHierarchy():
    '''public MboValueData[] getHierarchy(final String object, final String key)
    '''
def getParent():
    '''public MboValueData[] getParent(final String object, final String key, final String[] attrs)
    '''
def getPathToTop():
    '''public MboValueData[][] getPathToTop(final String object, final String key, final String[] attrs, final int maxRows)
    '''
def getSiblings():
    '''public MboValueData[][] getSiblings(final String object, final String key, final String[] attrs, final int maxRows)
    '''
def getTop():
    '''public MboValueData[][] getTop(final String[] attrs, final int maxRows)
    '''
def getUniqueIDValue():
    '''public MboValueData getUniqueIDValue(final String object, final String[] attributes, final String[] values)
    '''
def setHierarchy():
    '''public void setHierarchy(final String object, final String key, final String hierarchy)
    '''
def getRelatedMbo():
    '''public MboRemote getRelatedMbo(final long uniqueId)
    public MboRemote getRelatedMbo(final String uniqueId)
    '''
def getNodeMap():
    '''public DMMapTreeRulesSequence getNodeMap()
    '''
def setNodeMap():
    '''public void setNodeMap(final DMMapTreeRulesSequence nodeMap)
    '''
def findMbo():
    '''public MboRemote findMbo(final String key)
    '''
