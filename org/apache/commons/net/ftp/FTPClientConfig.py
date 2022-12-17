SYST_UNIX = "String  \"UNIX\""
SYST_VMS = "String  \"VMS\""
SYST_NT = "String  \"WINDOWS\""
SYST_OS2 = "String  \"OS/2\""
SYST_OS400 = "String  \"OS/400\""
SYST_MVS = "String  \"MVS\""
def ():
    '''returns FTPClientConfig\n\n
    (final String systemKey)\n
    ()\n
    (final String systemKey, final String defaultDateFormatStr, final String recentDateFormatStr, final String serverLanguageCode, final String shortMonthNames, final String serverTimeZoneId)\n
    '''
def getServerSystemKey():
    '''returns String\n\n
    getServerSystemKey()\n
    '''
def getDefaultDateFormatStr():
    '''returns String\n\n
    getDefaultDateFormatStr()\n
    '''
def getRecentDateFormatStr():
    '''returns String\n\n
    getRecentDateFormatStr()\n
    '''
def getServerTimeZoneId():
    '''returns String\n\n
    getServerTimeZoneId()\n
    '''
def getShortMonthNames():
    '''returns String\n\n
    getShortMonthNames()\n
    '''
def getServerLanguageCode():
    '''returns String\n\n
    getServerLanguageCode()\n
    '''
def setDefaultDateFormatStr():
    '''returns None\n\n
    setDefaultDateFormatStr(final String defaultDateFormatStr)\n
    '''
def setRecentDateFormatStr():
    '''returns None\n\n
    setRecentDateFormatStr(final String recentDateFormatStr)\n
    '''
def setServerTimeZoneId():
    '''returns None\n\n
    setServerTimeZoneId(final String serverTimeZoneId)\n
    '''
def setShortMonthNames():
    '''returns None\n\n
    setShortMonthNames(final String shortMonthNames)\n
    '''
def setServerLanguageCode():
    '''returns None\n\n
    setServerLanguageCode(final String serverLanguageCode)\n
    '''
