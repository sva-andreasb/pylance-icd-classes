REPORT_STOP_LIMIT = "String  \"reportstoplimit\""
MAX_SCHEDULED_REPORT = "String  \"maxschedreport\""
ADHOC_CREATE_LIMIT = "String  \"adhoccreatelimit\""
def ():
    '''returns ReportSecurityLimits\n\n
    (final UserInfo loginUserInfo, final UserInfo systemUserInfo, final boolean isMaxLimitParam)\n
    (final UserInfo loginUserInfo, final UserInfo systemUserInfo)\n
    '''
def getReportLimit():
    '''returns Integer\n\n
    getReportLimit(final String attributeName)\n
    '''
def refreshReportLimits():
    '''returns None\n\n
    refreshReportLimits(final boolean isMaxLimitParam)\n
    '''
def clearCachedValues():
    '''returns None\n\n
    clearCachedValues()\n
    '''
def getLoginUserInfo():
    '''returns UserInfo\n\n
    getLoginUserInfo()\n
    '''
