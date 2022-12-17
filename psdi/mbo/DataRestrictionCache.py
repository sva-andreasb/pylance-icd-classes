def ():
    '''returns RestrictionBundle\n\n
    ()\n
    ()\n
    '''
def get():
    '''returns RestrictionBundle\n\n
    get(final int level, final MboSetRemote msr)\n
    get(final int level, final MboSetRemote msr, final String attrName)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def reload():
    '''returns None\n\n
    reload()\n
    reload(final String key)\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty()\n
    '''
def getNoGrpNoAppRestriction():
    '''returns DataRestriction\n\n
    getNoGrpNoAppRestriction()\n
    '''
def getNoGrpWithAppRestriction():
    '''returns DataRestriction\n\n
    getNoGrpWithAppRestriction()\n
    '''
def getPerGrpRestrictions():
    '''returns ArrayList<Object[]>\n\n
    getPerGrpRestrictions()\n
    '''
def addGrpRestriction():
    '''returns None\n\n
    addGrpRestriction(final String grp, DataRestriction withOutApp, final DataRestriction withApp)\n
    '''
def setGenericRestriction():
    '''returns None\n\n
    setGenericRestriction(final DataRestriction withOutApp, final DataRestriction withApp)\n
    '''
def markGrpNoRestriction():
    '''returns None\n\n
    markGrpNoRestriction(final String grp)\n
    '''
