def ItemService():
    '''public ItemService()
    public ItemService(final MXServer mxServer)
    '''
def getInvVendorSql():
    '''public String getInvVendorSql(final UserInfo userInfo, final String itemnum, final String itemsetid, final String vendor, final String manufacturer, final String modelnum)
    public String getInvVendorSql(final UserInfo userInfo, final String itemnum, final String itemsetid, final String vendor, final String manufacturer, final String modelnum, final String conditioncode)
    public String getInvVendorSql(final String vendor, final MboRemote mbo)
    public String getInvVendorSql(final UserInfo userInfo, final String itemnum, final String itemsetid, final String vendor, final String catalogCode)
    '''
def initCriteriaList():
    '''public void initCriteriaList(final Hashtable criteriaTable)
    '''
def isItemRotating():
    '''public boolean isItemRotating(final UserInfo userInfo, final String itemnum, final String itemsetid)
    '''
def isItemLotted():
    '''public boolean isItemLotted(final UserInfo userInfo, final String itemnum, final String itemsetid)
    '''
def isValidItem():
    '''public ItemRemote isValidItem(final UserInfo userInfo, final String itemnum, final String itemsetid)
    '''
def removeSpecialOrderItems():
    '''public MboSetRemote removeSpecialOrderItems(final UserInfo userInfo, final Vector storelocVec)
    '''
def changeStatus():
    '''public void changeStatus(@WSMboKey("ITEM") final ItemRemote item, final String status, final Date date, final String memo)
    '''
def getDefaultItemSet():
    '''public MboRemote getDefaultItemSet(final UserInfo userInfo)
    '''
