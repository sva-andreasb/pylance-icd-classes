def ():
    '''returns DMStrucSet\n\n
    (final MboServerInterface ms)\n
    '''
def add():
    '''returns MboRemote\n\n
    add(final long uniqueId, final String nodeDesc, final String relationship)\n
    '''
def getAllHierarchies():
    '''returns MboValueData[][]\n\n
    getAllHierarchies(final String object, final String key, final String[] attrs, final int maxRows)\n
    '''
def getChildren():
    '''returns MboValueData[][]\n\n
    getChildren(final String object, final String key, final String[] attrs, final int maxRows)\n
    '''
def getHierarchy():
    '''returns MboValueData[]\n\n
    getHierarchy(final String object, final String key)\n
    '''
def getParent():
    '''returns MboValueData[]\n\n
    getParent(final String object, final String key, final String[] attrs)\n
    '''
def getPathToTop():
    '''returns MboValueData[][]\n\n
    getPathToTop(final String object, final String key, final String[] attrs, final int maxRows)\n
    '''
def getSiblings():
    '''returns MboValueData[][]\n\n
    getSiblings(final String object, final String key, final String[] attrs, final int maxRows)\n
    '''
def getTop():
    '''returns MboValueData[][]\n\n
    getTop(final String[] attrs, final int maxRows)\n
    '''
def getUniqueIDValue():
    '''returns MboValueData\n\n
    getUniqueIDValue(final String object, final String[] attributes, final String[] values)\n
    '''
def setHierarchy():
    '''returns None\n\n
    setHierarchy(final String object, final String key, final String hierarchy)\n
    '''
def getRelatedMbo():
    '''returns MboRemote\n\n
    getRelatedMbo(final long uniqueId)\n
    '''
def getNodeMap():
    '''returns DMStrucNodeMap\n\n
    getNodeMap()\n
    '''
def setNodeMap():
    '''returns None\n\n
    setNodeMap(final DMStrucNodeMap nodeMap)\n
    '''
