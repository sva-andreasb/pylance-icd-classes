def ():
    '''returns MaxIntObjectDetailSet\n\n
    (final MboServerInterface ms)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def canAdd():
    '''returns None\n\n
    canAdd()\n
    '''
def getChildren():
    '''returns MboValueData[][]\n\n
    getChildren(final String object, final String key, final String[] attrs, final int maxRows)\n
    getChildren(final String object, final String key, final String[] attrs, final int maxRows, final String cardinality)\n
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
def setOriginatingMosName():
    '''returns None\n\n
    setOriginatingMosName(final String origMosName)\n
    '''
def setOriginatingMbo():
    '''returns None\n\n
    setOriginatingMbo(final MboRemote origMbo)\n
    '''
