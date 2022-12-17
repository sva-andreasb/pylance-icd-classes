def ():
    '''returns NextItemRetriever\n\n
    (final MboServerInterface ms)\n
    ()\n
    '''
def processQuantity():
    '''returns None\n\n
    processQuantity(final int allowanceDays, final boolean ignoreReorderPoint)\n
    '''
def cancelReorder():
    '''returns None\n\n
    cancelReorder()\n
    '''
def decideVendorAndCost():
    '''returns ReorderSetRemote\n\n
    decideVendorAndCost(final boolean groupByVendor, final boolean considerContract, final int allowanceDays)\n
    '''
def reorder():
    '''returns None\n\n
    reorder(final boolean groupByVendor, final boolean considerContract)\n
    reorder()\n
    '''
def setKey():
    '''returns None\n\n
    setKey(final Object parent, final String key, final String type, final String siteID, final String orgID)\n
    '''
def setInsertDate():
    '''returns None\n\n
    setInsertDate(final Object parent, final Date date)\n
    '''
def setUserName():
    '''returns None\n\n
    setUserName(final Object parent, final String theUserName)\n
    '''
def setViewOnly():
    '''returns None\n\n
    setViewOnly(final Object parent, final boolean viewOnlyFlag)\n
    '''
def addWarning():
    '''returns None\n\n
    addWarning(final MXApplicationException e)\n
    '''
def getReorderWarnings():
    '''returns Vector\n\n
    getReorderWarnings()\n
    '''
def useAgreement():
    '''returns None\n\n
    useAgreement(final boolean useA)\n
    '''
def getReorderResult():
    '''returns Object[]\n\n
    getReorderResult()\n
    '''
def monitorLock():
    '''returns None\n\n
    monitorLock(final String siteID)\n
    '''
def deleteNullOrderUnit():
    '''returns None\n\n
    deleteNullOrderUnit(final UserInfo userInfo, final String siteID)\n
    '''
