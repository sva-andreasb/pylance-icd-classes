def ():
    '''returns StatefulMbo\n\n
    (final MboSet ms)\n
    '''
def getInternalStatus():
    '''returns String\n\n
    getInternalStatus()\n
    '''
def changeMaxStatus():
    '''returns None\n\n
    changeMaxStatus(final String internalStatus, final Date date, final String memo, final long accessModifier)\n
    changeMaxStatus(final String internalStatus, final Date date, final String memo)\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(final String status, final Date date, final String memo)\n
    changeStatus(final String status, Date asOfDate, String memo, final long accessModifier)\n
    changeStatus(final String status, final String progressStatus, Date asOfDate, String memo, final long accessModifier)\n
    '''
def canChangeStatus():
    '''returns None\n\n
    canChangeStatus(final String changeToStatus, final String progressStatus, final long accessModifier)\n
    canChangeStatus(final String status)\n
    canChangeStatus(final String changeToStatus, final long accessModifier)\n
    '''
def checkStatusChangeAuthorization():
    '''returns None\n\n
    checkStatusChangeAuthorization(final String changeToStatus, final boolean single)\n
    '''
def canChangeMaxStatus():
    '''returns None\n\n
    canChangeMaxStatus(final String internalStatus)\n
    '''
def getStatusList():
    '''returns MboSetRemote\n\n
    getStatusList()\n
    '''
def getValidStatusList():
    '''returns MboSetRemote\n\n
    getValidStatusList()\n
    '''
def filterByValidStatusList():
    '''returns None\n\n
    filterByValidStatusList(final boolean onlyCanBeChanged, final MboSetRemote values)\n
    '''
def checkForOpenStatus():
    '''returns None\n\n
    checkForOpenStatus()\n
    '''
def getOverridePVStatusException():
    '''returns boolean\n\n
    getOverridePVStatusException()\n
    '''
def setOverridePVStatusException():
    '''returns None\n\n
    setOverridePVStatusException(final boolean overridePVStatusException)\n
    '''
def canDeleteAttachedDocs():
    '''returns None\n\n
    canDeleteAttachedDocs()\n
    '''
def setTargetStatusOption():
    '''returns None\n\n
    setTargetStatusOption(final String targetStatusOption)\n
    '''
def getTargetStatusOption():
    '''returns String\n\n
    getTargetStatusOption()\n
    '''
def setOnListTab():
    '''returns None\n\n
    setOnListTab(final boolean onListTab)\n
    '''
def getOnListTab():
    '''returns boolean\n\n
    getOnListTab()\n
    '''
def setStatusChangeButtonSigoption():
    '''returns None\n\n
    setStatusChangeButtonSigoption(final String statusChangeButtonSigoption)\n
    '''
def getStatusChangeButtonSigoption():
    '''returns String\n\n
    getStatusChangeButtonSigoption()\n
    '''
