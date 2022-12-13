def StatefulMbo():
'''public StatefulMbo(final MboSet ms)
'''
pass
def getInternalStatus():
'''public String getInternalStatus()
'''
pass
def changeMaxStatus():
'''public void changeMaxStatus(final String internalStatus, final Date date, final String memo, final long accessModifier)
public void changeMaxStatus(final String internalStatus, final Date date, final String memo)
'''
pass
def changeStatus():
'''public void changeStatus(final String status, final Date date, final String memo)
public void changeStatus(final String status, Date asOfDate, String memo, final long accessModifier)
public void changeStatus(final String status, final String progressStatus, Date asOfDate, String memo, final long accessModifier)
'''
pass
def canChangeStatus():
'''public void canChangeStatus(final String changeToStatus, final String progressStatus, final long accessModifier)
public void canChangeStatus(final String status)
public void canChangeStatus(final String changeToStatus, final long accessModifier)
'''
pass
def checkStatusChangeAuthorization():
'''public void checkStatusChangeAuthorization(final String changeToStatus, final boolean single)
'''
pass
def canChangeMaxStatus():
'''public void canChangeMaxStatus(final String internalStatus)
'''
pass
def getStatusList():
'''public MboSetRemote getStatusList()
'''
pass
def getValidStatusList():
'''public MboSetRemote getValidStatusList()
'''
pass
def filterByValidStatusList():
'''public void filterByValidStatusList(final boolean onlyCanBeChanged, final MboSetRemote values)
'''
pass
def fireEvent():
'''public synchronized void fireEvent(final String type)
'''
pass
def checkForOpenStatus():
'''public void checkForOpenStatus()
'''
pass
def getOverridePVStatusException():
'''public boolean getOverridePVStatusException()
'''
pass
def setOverridePVStatusException():
'''public void setOverridePVStatusException(final boolean overridePVStatusException)
'''
pass
def canDeleteAttachedDocs():
'''public void canDeleteAttachedDocs()
'''
pass
def setTargetStatusOption():
'''public void setTargetStatusOption(final String targetStatusOption)
'''
pass
def getTargetStatusOption():
'''public String getTargetStatusOption()
'''
pass
def setOnListTab():
'''public void setOnListTab(final boolean onListTab)
'''
pass
def getOnListTab():
'''public boolean getOnListTab()
'''
pass
def setStatusChangeButtonSigoption():
'''public void setStatusChangeButtonSigoption(final String statusChangeButtonSigoption)
'''
pass
def getStatusChangeButtonSigoption():
'''public String getStatusChangeButtonSigoption()
'''
pass
