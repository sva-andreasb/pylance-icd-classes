def ():
    '''returns BIMWorkOrderTreeSet\n\n
    (final MboServerInterface ms)\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def getChildren():
    '''returns MboValueData[][]\n\n
    getChildren(final String object, final String key, final String[] attrs, final int maxRows)\n
    '''
def getParent():
    '''returns MboValueData[]\n\n
    getParent(final String object, String key, final String[] attrs)\n
    '''
def getSiblings():
    '''returns MboValueData[][]\n\n
    getSiblings(final String object, String key, final String[] attrs, final int maxRows)\n
    '''
def getTop():
    '''returns MboValueData[][]\n\n
    getTop(final String[] attrs, final int maxRows)\n
    '''
def getPathToTop():
    '''returns MboValueData[][]\n\n
    getPathToTop(final String object, String key, final String[] attrs, final int maxRows)\n
    '''
def count():
    '''returns int\n\n
    count()\n
    '''
def toBeSaved():
    '''returns boolean\n\n
    toBeSaved()\n
    '''
def setMboSetInfo():
    '''returns None\n\n
    setMboSetInfo(final MboSetInfo ms)\n
    '''
def setup():
    '''returns MboRemote\n\n
    setup()\n
    '''
def execute():
    '''returns None\n\n
    execute()\n
    execute(final MboRemote mbo)\n
    '''
def getMboForUniqueId():
    '''returns MboRemote\n\n
    getMboForUniqueId(final long uid)\n
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
