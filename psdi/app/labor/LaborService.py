def LaborService():
    '''public LaborService()
    public LaborService(final MXServer mxServer)
    '''
def init():
    '''public void init()
    '''
def destroy():
    '''public void destroy()
    '''
def initCriteriaList():
    '''public void initCriteriaList(final Hashtable criteriaTable)
    '''
def getServReceiptSet():
    '''public MboSetRemote getServReceiptSet(final UserInfo ui, final String ponum)
    '''
def createServiceReceipts():
    '''public final void createServiceReceipts(final UserInfo userinfo, final MboRemote forLabor, final boolean createSummary, final Date startDate, final Date endDate)
    public void createServiceReceipts(final UserInfo userinfo, final Vector forLabor, final boolean createSummary, final Date startDate, final Date endDate)
    '''
def createInvoiceForLabTrans():
    '''public void createInvoiceForLabTrans(final MboRemote labTransMbo, final UserInfo userInfo)
    '''
def updateHours():
    '''public synchronized void updateHours(final UserInfo userinfo, final String laborcode, final String orgid, final double regHours, final double otHours)
    '''
