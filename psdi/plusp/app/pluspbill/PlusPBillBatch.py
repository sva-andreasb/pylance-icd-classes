def PlusPBillBatch():
    '''public PlusPBillBatch(final MboSet ms)
    '''
def getLogger():
    '''public PlusPLog getLogger()
    '''
def init():
    '''public void init()
    '''
def add():
    '''public void add()
    '''
def modify():
    '''public void modify()
    '''
def setFlagsForStatus():
    '''public void setFlagsForStatus()
    '''
def createBillLines():
    '''public boolean createBillLines()
    public boolean createBillLines(final String s)
    '''
def getService():
    '''public static PlusPCopyServiceRemote getService(final String s)
    '''
def validateTransaction():
    '''public boolean validateTransaction(final MboRemote mboRemote, final MboRemote mboRemote2)
    '''
def calculateTotals():
    '''public void calculateTotals()
    '''
def getTicketSet():
    '''public MboSetRemote getTicketSet(final boolean b)
    '''
def getWOSet():
    '''public MboSetRemote getWOSet(final boolean b)
    '''
def getSOSet():
    '''public MboSetRemote getSOSet(final boolean b)
    '''
def updateBillBatchTotals():
    '''public void updateBillBatchTotals(final MboRemote mboRemote, final String s, final String s2)
    public void updateBillBatchTotals()
    '''
def getBillableStatusWhereClause():
    '''public String getBillableStatusWhereClause(final String listName, final String value, final String s)
    '''
def getStatusListName():
    '''public String getStatusListName()
    '''
def isBilled():
    '''public boolean isBilled()
    '''
def changeStatus():
    '''public void changeStatus(final String val, final Date asOfDate, final String memo, final long accessModifier)
    '''
def setValueCustomerCurrencyTotal():
    '''public void setValueCustomerCurrencyTotal()
    '''
def setRevisionNum():
    '''public void setRevisionNum()
    '''
def canCreateBillLines():
    '''public void canCreateBillLines()
    '''
def hasCopyInProgress():
    '''public boolean hasCopyInProgress()
    '''
def updateCopyHistory():
    '''public void updateCopyHistory(final String errKey, final String... params)
    '''
def getBillBatchCopy():
    '''public MboRemote getBillBatchCopy()
    '''
def canChangeStatus():
    '''public void canChangeStatus(final String changeToStatus, final long accessModifier)
    '''
def setBillBatchFilters():
    '''public void setBillBatchFilters(final MboRemote e)
    '''
def getBillBatchFilters():
    '''public HashSet<MboRemote> getBillBatchFilters()
    '''
