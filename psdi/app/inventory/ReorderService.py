def ():
    '''returns ReorderLockMonitor\n\n
    ()\n
    (final MXServer mxServer)\n
    (final UserInfo ui, final String targetType, final String keyInput, final Date lockDate, final ReorderService rs, final String siteIDInput, final String orgIDInput)\n
    '''
def changeState():
    '''returns Date\n\n
    changeState(final UserInfo userInfo, final int requestType, final String targetType, final String siteID, final String orgID)\n
    '''
def getMutexWhere():
    '''returns String\n\n
    getMutexWhere(final UserInfo userInfo, final String targetType, final String key, final String siteID, final String orgID)\n
    '''
def whoHasLock():
    '''returns String\n\n
    whoHasLock(final UserInfo userInfo, final int requestType, final String targetType, final String key, final String siteID, final String orgID)\n
    '''
def monitorThisLock():
    '''returns None\n\n
    monitorThisLock(final UserInfo ui, final String type, final String key, final Date lockDate, final String siteID)\n
    '''
def getReorderSet():
    '''returns ReorderSetRemote\n\n
    getReorderSet(final UserInfo userInfo, final boolean viewOnly, final InventorySetRemote invs, final String storeRoom, final String siteID, final int allowanceDays, final boolean directOrder)\n
    getReorderSet(final UserInfo userInfo, final boolean viewOnly, final InventorySetRemote invs, final String storeRoom, final String siteID, final int allowanceDays, final boolean directOrder, final boolean ignoreReorderPoint)\n
    getReorderSet(final UserInfo userInfo, final boolean viewOnly, final InventorySetRemote invs, final String storeRoom, final String siteID, final int allowanceDays, final boolean directOrder, final boolean ignoreReorderPoint, final boolean includeSoftReservations)\n
    getReorderSet(final UserInfo userInfo, final boolean viewOnly, final InventoryRemote inv)\n
    getReorderSet(final UserInfo userInfo, final boolean viewOnly, final InventoryRemote inv, final boolean ignoreReorderPoint)\n
    getReorderSet(final UserInfo userInfo, final boolean viewOnly, final InventorySetRemote invs, final String storeRoom, final String siteID, final int[] selected, final int allowanceDays, final boolean directOrder)\n
    getReorderSet(final UserInfo userInfo, final boolean viewOnly, final InventorySetRemote invs, final String storeRoom, final String siteID, final int[] selected, final int allowanceDays, final boolean directOrder, final boolean ignoreReorderPoint)\n
    getReorderSet(final UserInfo userInfo, final boolean viewOnly, final InventorySetRemote invs, final String storeRoom, final String siteID, final int[] selected, final int allowanceDays, final boolean directOrder, final boolean ignoreReorderPoint, final boolean includeSoftReservations)\n
    getReorderSet(final UserInfo userInfo, final boolean viewOnly, final InventorySetRemote invs, final String storeRoom, final String siteID, final Vector selected, final int allowanceDays, final boolean directOrder)\n
    getReorderSet(final UserInfo userInfo, final boolean viewOnly, final InventorySetRemote invs, final String storeRoom, final String siteID, final Vector selected, final int allowanceDays, final boolean directOrder, final boolean ignoreReorderPoint)\n
    getReorderSet(final UserInfo userInfo, final boolean viewOnly, final InventorySetRemote invs, final String storeRoom, final String siteID, final Vector selected, final int allowanceDays, final boolean directOrder, final boolean ignoreReorderPoint, final boolean includeSoftReservations)\n
    '''
def getReorderSetForMR():
    '''returns ReorderSetRemote\n\n
    getReorderSetForMR(final boolean viewOnly, final MRRemote mr)\n
    '''
def getReorderSetForDirectOrderOnly():
    '''returns ReorderSetRemote\n\n
    getReorderSetForDirectOrderOnly(final UserInfo userInfo, final boolean viewOnly, final String siteID)\n
    '''
def addFromWPItem():
    '''returns None\n\n
    addFromWPItem(final DBShortcut dbShortcut, final UserInfo userInfo, final String userForThisSet, final int allowanceDays, final String siteIDForThisSet, final String orgIDForThisSet)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def releaseLocks():
    '''returns int\n\n
    releaseLocks(final UserInfo userInfo, final String siteID)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    '''
