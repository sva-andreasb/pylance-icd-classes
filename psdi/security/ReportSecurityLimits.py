REPORT_STOP_LIMIT = "String  \"reportstoplimit\""
MAX_SCHEDULED_REPORT = "String  \"maxschedreport\""
ADHOC_CREATE_LIMIT = "String  \"adhoccreatelimit\""
def ReportSecurityLimits():
    '''public ReportSecurityLimits(final UserInfo loginUserInfo, final UserInfo systemUserInfo, final boolean isMaxLimitParam)
    public ReportSecurityLimits(final UserInfo loginUserInfo, final UserInfo systemUserInfo)
    '''
def getReportLimit():
    '''public Integer getReportLimit(final String attributeName)
    '''
def refreshReportLimits():
    '''public void refreshReportLimits(final boolean isMaxLimitParam)
    '''
def clearCachedValues():
    '''public void clearCachedValues()
    '''
def getLoginUserInfo():
    '''public UserInfo getLoginUserInfo()
    '''
