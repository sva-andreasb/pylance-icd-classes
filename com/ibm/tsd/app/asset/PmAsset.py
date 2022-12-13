def PmAsset():
    '''public PmAsset(final MboSet ms)
    '''
def recordAssetStatusChange():
    '''public void recordAssetStatusChange(final MboRemote woMbo, final Date changeDate, final String code, final boolean operational)
    '''
def reportDowntime():
    '''public void reportDowntime(final MboRemote mbo, final Date startDate, final Date endDate, final double hoursDown, final String code, final boolean operational)
    '''
def calculateDownTime():
    '''public double calculateDownTime(final Date lastChangeDate, final Date currentChangeDate)
    '''
def hasMeters():
    '''public void hasMeters()
    '''
def isReportingDownTime():
    '''public boolean isReportingDownTime()
    '''
def getDowntimeReportUpperDateLimit():
    '''public Date getDowntimeReportUpperDateLimit()
    '''
def setDowntimeReportUpperDateLimit():
    '''public void setDowntimeReportUpperDateLimit(final Date ULDate)
    '''
def lastAssetStatusForAssetnum():
    '''public MboRemote lastAssetStatusForAssetnum()
    '''
