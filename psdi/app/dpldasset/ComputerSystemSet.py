def ():
    '''returns ComputerSystemSet\n\n
    (final MboServerInterface ms)\n
    '''
def getQbe():
    '''returns String\n\n
    getQbe(final String attribute)\n
    '''
def resetQbe():
    '''returns None\n\n
    resetQbe()\n
    '''
def setQbe():
    '''returns None\n\n
    setQbe(final String attribute, final String expression)\n
    '''
def getUserWhere():
    '''returns String\n\n
    getUserWhere(final String alias)\n
    '''
def getUserAndQbeWhere():
    '''returns String\n\n
    getUserAndQbeWhere()\n
    '''
def getChildren():
    '''returns MboValueData[][]\n\n
    getChildren(final String object, final String key, final String[] attrs, final int maxRows)\n
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
