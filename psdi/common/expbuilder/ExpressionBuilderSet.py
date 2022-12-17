def ():
    '''returns ExpressionBuilderSet\n\n
    (final MboServerInterface ms)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def setTreeObject():
    '''returns None\n\n
    setTreeObject(final String objectname)\n
    '''
def getTreeObject():
    '''returns String\n\n
    getTreeObject()\n
    '''
def getObjectAttribute():
    '''returns String\n\n
    getObjectAttribute()\n
    '''
def setObjectAttribute():
    '''returns None\n\n
    setObjectAttribute(final String attrname)\n
    '''
def setup():
    '''returns MboRemote\n\n
    setup()\n
    '''
def isDotNotationOn():
    '''returns boolean\n\n
    isDotNotationOn()\n
    '''
def isSubselectsOn():
    '''returns boolean\n\n
    isSubselectsOn()\n
    '''
def setDotNotation():
    '''returns None\n\n
    setDotNotation(final boolean flag)\n
    '''
def setSubSelects():
    '''returns None\n\n
    setSubSelects(final boolean flag)\n
    '''
def isRelationshipsOn():
    '''returns boolean\n\n
    isRelationshipsOn()\n
    '''
def isAttributesOn():
    '''returns boolean\n\n
    isAttributesOn()\n
    '''
def setRelationship():
    '''returns None\n\n
    setRelationship(final boolean flag)\n
    '''
def setAttributes():
    '''returns None\n\n
    setAttributes(final boolean flag)\n
    '''
def execute():
    '''returns None\n\n
    execute()\n
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
