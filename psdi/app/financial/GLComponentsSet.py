def ():
    '''returns GLComponentsSet\n\n
    (final MboServerInterface ms)\n
    '''
def findValidComponents():
    '''returns None\n\n
    findValidComponents(final int componentNumber, final String[] knownSegments, final boolean withAccessCheck, final boolean fromCOA, String orgID)\n
    '''
def getGLFormat():
    '''returns GLFormat\n\n
    getGLFormat(final String orgID)\n
    '''
def activateGLComponents():
    '''returns AccountSetRemote\n\n
    activateGLComponents(final String gla, final Vector compName, final Vector compDesc, final Vector compDescAsName, final Vector compOrder, final String ownerSysID, final String sourceSysID, final String senderSysID)\n
    '''
def inActivateGLComponents():
    '''returns AccountSetRemote\n\n
    inActivateGLComponents(final String gla, final Vector compName, final Vector compDesc, final Vector compDescAsName, final Vector compOrder, final String ownerSysID, final String sourceSysID, final String senderSysID)\n
    '''
def save():
    '''returns None\n\n
    save()\n
    '''
def getMultiSiteWhere():
    '''returns String\n\n
    getMultiSiteWhere()\n
    '''
def getNextValidCompList():
    '''returns String\n\n
    getNextValidCompList(final String whereClause, final String nextCompAttr)\n
    '''
