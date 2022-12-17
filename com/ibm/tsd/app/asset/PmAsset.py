def ():
    '''returns PmAsset\n\n
    (final MboSet ms)\n
    '''
def recordAssetStatusChange():
    '''returns None\n\n
    recordAssetStatusChange(final MboRemote woMbo, final Date changeDate, final String code, final boolean operational)\n
    '''
def reportDowntime():
    '''returns None\n\n
    reportDowntime(final MboRemote mbo, final Date startDate, final Date endDate, final double hoursDown, final String code, final boolean operational)\n
    '''
def calculateDownTime():
    '''returns double\n\n
    calculateDownTime(final Date lastChangeDate, final Date currentChangeDate)\n
    '''
def hasMeters():
    '''returns None\n\n
    hasMeters()\n
    '''
def isReportingDownTime():
    '''returns boolean\n\n
    isReportingDownTime()\n
    '''
def getDowntimeReportUpperDateLimit():
    '''returns Date\n\n
    getDowntimeReportUpperDateLimit()\n
    '''
def setDowntimeReportUpperDateLimit():
    '''returns None\n\n
    setDowntimeReportUpperDateLimit(final Date ULDate)\n
    '''
def lastAssetStatusForAssetnum():
    '''returns MboRemote\n\n
    lastAssetStatusForAssetnum()\n
    '''
