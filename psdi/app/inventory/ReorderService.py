def ReorderService():
    '''    public ReorderService()
    public ReorderService(final MXServer mxServer)
    '''
def changeState():
    '''    public Date changeState(final UserInfo userInfo, final int requestType, final String targetType, final String siteID, final String orgID)
    public synchronized Date changeState(final UserInfo userInfo, final int requestType, final String targetType, final String key, final String siteID, final String orgID)
    '''
def getMutexWhere():
    '''    public String getMutexWhere(final UserInfo userInfo, final String targetType, final String key, final String siteID, final String orgID)
    '''
def whoHasLock():
    '''    public String whoHasLock(final UserInfo userInfo, final int requestType, final String targetType, final String key, final String siteID, final String orgID)
    '''
def monitorThisLock():
    '''    public void monitorThisLock(final UserInfo ui, final String type, final String key, final Date lockDate, final String siteID)
    '''
def getReorderSet():
    '''    public ReorderSetRemote getReorderSet(final UserInfo userInfo, final boolean viewOnly, final InventorySetRemote invs, final String storeRoom, final String siteID, final int allowanceDays, final boolean directOrder)
    public ReorderSetRemote getReorderSet(final UserInfo userInfo, final boolean viewOnly, final InventorySetRemote invs, final String storeRoom, final String siteID, final int allowanceDays, final boolean directOrder, final boolean ignoreReorderPoint)
    public ReorderSetRemote getReorderSet(final UserInfo userInfo, final boolean viewOnly, final InventorySetRemote invs, final String storeRoom, final String siteID, final int allowanceDays, final boolean directOrder, final boolean ignoreReorderPoint, final boolean includeSoftReservations)
    public ReorderSetRemote getReorderSet(final UserInfo userInfo, final boolean viewOnly, final InventoryRemote inv)
    public ReorderSetRemote getReorderSet(final UserInfo userInfo, final boolean viewOnly, final InventoryRemote inv, final boolean ignoreReorderPoint)
    public ReorderSetRemote getReorderSet(final UserInfo userInfo, final boolean viewOnly, final InventorySetRemote invs, final String storeRoom, final String siteID, final int[] selected, final int allowanceDays, final boolean directOrder)
    public ReorderSetRemote getReorderSet(final UserInfo userInfo, final boolean viewOnly, final InventorySetRemote invs, final String storeRoom, final String siteID, final int[] selected, final int allowanceDays, final boolean directOrder, final boolean ignoreReorderPoint)
    public ReorderSetRemote getReorderSet(final UserInfo userInfo, final boolean viewOnly, final InventorySetRemote invs, final String storeRoom, final String siteID, final int[] selected, final int allowanceDays, final boolean directOrder, final boolean ignoreReorderPoint, final boolean includeSoftReservations)
    public ReorderSetRemote getReorderSet(final UserInfo userInfo, final boolean viewOnly, final InventorySetRemote invs, final String storeRoom, final String siteID, final Vector selected, final int allowanceDays, final boolean directOrder)
    public ReorderSetRemote getReorderSet(final UserInfo userInfo, final boolean viewOnly, final InventorySetRemote invs, final String storeRoom, final String siteID, final Vector selected, final int allowanceDays, final boolean directOrder, final boolean ignoreReorderPoint)
    public ReorderSetRemote getReorderSet(final UserInfo userInfo, final boolean viewOnly, final InventorySetRemote invs, final String storeRoom, final String siteID, final Vector selected, final int allowanceDays, final boolean directOrder, final boolean ignoreReorderPoint, final boolean includeSoftReservations)
    '''
def getReorderSetForMR():
    '''    public ReorderSetRemote getReorderSetForMR(final boolean viewOnly, final MRRemote mr)
    '''
def getReorderSetForDirectOrderOnly():
    '''    public ReorderSetRemote getReorderSetForDirectOrderOnly(final UserInfo userInfo, final boolean viewOnly, final String siteID)
    '''
def addFromWPItem():
    '''    public void addFromWPItem(final DBShortcut dbShortcut, final UserInfo userInfo, final String userForThisSet, final int allowanceDays, final String siteIDForThisSet, final String orgIDForThisSet)
    '''
def init():
    '''    public void init()
    '''
def releaseLocks():
    '''    public int releaseLocks(final UserInfo userInfo, final String siteID)
    '''
def ReorderLockMonitor():
    '''    public ReorderLockMonitor(final UserInfo ui, final String targetType, final String keyInput, final Date lockDate, final ReorderService rs, final String siteIDInput, final String orgIDInput)
    '''
def run():
    '''    public void run()
    '''
