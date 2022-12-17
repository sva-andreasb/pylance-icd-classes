def ():
    '''returns ItemService\n\n
    ()\n
    (final MXServer mxServer)\n
    '''
def getInvVendorSql():
    '''returns String\n\n
    getInvVendorSql(final UserInfo userInfo, final String itemnum, final String itemsetid, final String vendor, final String manufacturer, final String modelnum)\n
    getInvVendorSql(final UserInfo userInfo, final String itemnum, final String itemsetid, final String vendor, final String manufacturer, final String modelnum, final String conditioncode)\n
    getInvVendorSql(final String vendor, final MboRemote mbo)\n
    getInvVendorSql(final UserInfo userInfo, final String itemnum, final String itemsetid, final String vendor, final String catalogCode)\n
    '''
def initCriteriaList():
    '''returns None\n\n
    initCriteriaList(final Hashtable criteriaTable)\n
    '''
def isItemRotating():
    '''returns boolean\n\n
    isItemRotating(final UserInfo userInfo, final String itemnum, final String itemsetid)\n
    '''
def isItemLotted():
    '''returns boolean\n\n
    isItemLotted(final UserInfo userInfo, final String itemnum, final String itemsetid)\n
    '''
def isValidItem():
    '''returns ItemRemote\n\n
    isValidItem(final UserInfo userInfo, final String itemnum, final String itemsetid)\n
    '''
def removeSpecialOrderItems():
    '''returns MboSetRemote\n\n
    removeSpecialOrderItems(final UserInfo userInfo, final Vector storelocVec)\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(@WSMboKey("ITEM") final ItemRemote item, final String status, final Date date, final String memo)\n
    '''
def getDefaultItemSet():
    '''returns MboRemote\n\n
    getDefaultItemSet(final UserInfo userInfo)\n
    '''
