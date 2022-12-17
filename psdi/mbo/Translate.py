def ():
    '''returns Translate\n\n
    ()\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def toInternalString():
    '''returns String\n\n
    toInternalString(final String listName, final String value)\n
    toInternalString(final String listName, final String value, final MboRemote mbo)\n
    toInternalString(final String listName, final String value, final String siteId, final String orgId)\n
    '''
def toInternalStringNoException():
    '''returns String\n\n
    toInternalStringNoException(final String listName, final String value, final MboRemote mbo)\n
    '''
def getValuesVector():
    '''returns Vector\n\n
    getValuesVector(final String listName, final String siteId, final String orgId)\n
    '''
def toExternalList():
    '''returns String\n\n
    toExternalList(final String listName, final String value)\n
    toExternalList(final String listName, final String value, final MboRemote mbo)\n
    toExternalList(final String listName, final String value, final String siteId, final String orgId)\n
    toExternalList(final String listName, final String[] value)\n
    toExternalList(final String listName, final String[] value, final MboRemote mbo)\n
    toExternalList(final String listName, final String[] value, final String siteId, final String orgId)\n
    '''
def getExternalValues():
    '''returns String[]\n\n
    getExternalValues(final String listName, final String internalValue, final String siteId, final String orgId)\n
    getExternalValues(final String listName, final String internalValue, final MboRemote mbo)\n
    '''
def toExternalDefaultValue():
    '''returns String\n\n
    toExternalDefaultValue(final String listName, final String value)\n
    toExternalDefaultValue(final String listName, final String value, final MboRemote mbo)\n
    toExternalDefaultValue(final String listName, final String value, final String siteId, final String orgId)\n
    '''
def remove():
    '''returns None\n\n
    remove(String listName)\n
    '''
def getSiteOrg():
    '''returns String[]\n\n
    getSiteOrg(final MboRemote mbo)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def reload():
    '''returns None\n\n
    reload()\n
    reload(final String key)\n
    '''
