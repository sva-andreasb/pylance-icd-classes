def ():
    '''returns ExpBuilderObjectTreeSet\n\n
    (final MboServerInterface ms)\n
    '''
def setRelationshipTreeObject():
    '''returns None\n\n
    setRelationshipTreeObject(final String treeObject)\n
    '''
def setup():
    '''returns MboRemote\n\n
    setup()\n
    '''
def isDotNotationOn():
    '''returns boolean\n\n
    isDotNotationOn()\n
    '''
def isSubSelectsOn():
    '''returns boolean\n\n
    isSubSelectsOn()\n
    '''
def isRelationshipsOn():
    '''returns boolean\n\n
    isRelationshipsOn()\n
    '''
def isAttributesOn():
    '''returns boolean\n\n
    isAttributesOn()\n
    '''
def setIncludeNonpersistentAttributes():
    '''returns None\n\n
    setIncludeNonpersistentAttributes(final boolean flag)\n
    '''
def getIncludeNonpersistentAttributes():
    '''returns boolean\n\n
    getIncludeNonpersistentAttributes()\n
    '''
def setDotNotation():
    '''returns None\n\n
    setDotNotation(final boolean flag)\n
    '''
def setSubSelects():
    '''returns None\n\n
    setSubSelects(final boolean flag)\n
    '''
def setRelationship():
    '''returns None\n\n
    setRelationship(final boolean flag)\n
    '''
def setAttributes():
    '''returns None\n\n
    setAttributes(final boolean flag)\n
    '''
def getTreeControlProps():
    '''returns HashMap\n\n
    getTreeControlProps()\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def getDotNotation():
    '''returns String\n\n
    getDotNotation(final int attTreeID)\n
    '''
def getColonizedNodeValue():
    '''returns String\n\n
    getColonizedNodeValue(final int attTreeID)\n
    '''
def getAttributeMboUniqueID():
    '''returns long\n\n
    getAttributeMboUniqueID(final int attTreeID)\n
    '''
def getSelectedNode():
    '''returns String\n\n
    getSelectedNode(final String maxattributeid)\n
    '''
def getChildren():
    '''returns MboValueData[][]\n\n
    getChildren(final String object, final String key, final String[] attrs, final int maxRows)\n
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
def getPathToTop():
    '''returns MboValueData[][]\n\n
    getPathToTop(final String object, final String key, final String[] attrs, final int maxRows)\n
    '''
def isTreeTop():
    '''returns boolean\n\n
    isTreeTop()\n
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
def reset():
    '''returns None\n\n
    reset()\n
    '''
