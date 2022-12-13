def StatefulMbo():
    '''public StatefulMbo(final MboSet ms)
    '''
def getInternalStatus():
    '''public String getInternalStatus()
    '''
def changeMaxStatus():
    '''public void changeMaxStatus(final String internalStatus, final Date date, final String memo, final long accessModifier)
    public void changeMaxStatus(final String internalStatus, final Date date, final String memo)
    '''
def changeStatus():
    '''public void changeStatus(final String status, final Date date, final String memo)
    public void changeStatus(final String status, Date asOfDate, String memo, final long accessModifier)
    public void changeStatus(final String status, final String progressStatus, Date asOfDate, String memo, final long accessModifier)
    '''
def canChangeStatus():
    '''public void canChangeStatus(final String changeToStatus, final String progressStatus, final long accessModifier)
    public void canChangeStatus(final String status)
    public void canChangeStatus(final String changeToStatus, final long accessModifier)
    '''
def checkStatusChangeAuthorization():
    '''public void checkStatusChangeAuthorization(final String changeToStatus, final boolean single)
    '''
def canChangeMaxStatus():
    '''public void canChangeMaxStatus(final String internalStatus)
    '''
def getStatusList():
    '''public MboSetRemote getStatusList()
    '''
def getValidStatusList():
    '''public MboSetRemote getValidStatusList()
    '''
def filterByValidStatusList():
    '''public void filterByValidStatusList(final boolean onlyCanBeChanged, final MboSetRemote values)
    '''
def fireEvent():
    '''public synchronized void fireEvent(final String type)
    '''
def checkForOpenStatus():
    '''public void checkForOpenStatus()
    '''
def getOverridePVStatusException():
    '''public boolean getOverridePVStatusException()
    '''
def setOverridePVStatusException():
    '''public void setOverridePVStatusException(final boolean overridePVStatusException)
    '''
def canDeleteAttachedDocs():
    '''public void canDeleteAttachedDocs()
    '''
def setTargetStatusOption():
    '''public void setTargetStatusOption(final String targetStatusOption)
    '''
def getTargetStatusOption():
    '''public String getTargetStatusOption()
    '''
def setOnListTab():
    '''public void setOnListTab(final boolean onListTab)
    '''
def getOnListTab():
    '''public boolean getOnListTab()
    '''
def setStatusChangeButtonSigoption():
    '''public void setStatusChangeButtonSigoption(final String statusChangeButtonSigoption)
    '''
def getStatusChangeButtonSigoption():
    '''public String getStatusChangeButtonSigoption()
    '''
