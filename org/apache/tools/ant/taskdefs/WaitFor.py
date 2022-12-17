ONE_MILLISECOND = "long  1L"
ONE_SECOND = "long  1000L"
ONE_MINUTE = "long  60000L"
ONE_HOUR = "long  3600000L"
ONE_DAY = "long  86400000L"
ONE_WEEK = "long  604800000L"
DEFAULT_MAX_WAIT_MILLIS = "long  180000L"
DEFAULT_CHECK_MILLIS = "long  500L"
MILLISECOND = "String  \"millisecond\""
SECOND = "String  \"second\""
MINUTE = "String  \"minute\""
HOUR = "String  \"hour\""
DAY = "String  \"day\""
WEEK = "String  \"week\""
def ():
    '''returns Unit\n\n
    ()\n
    (final String taskName)\n
    ()\n
    '''
def setMaxWait():
    '''returns None\n\n
    setMaxWait(final long time)\n
    '''
def setMaxWaitUnit():
    '''returns None\n\n
    setMaxWaitUnit(final Unit unit)\n
    '''
def setCheckEvery():
    '''returns None\n\n
    setCheckEvery(final long time)\n
    '''
def setCheckEveryUnit():
    '''returns None\n\n
    setCheckEveryUnit(final Unit unit)\n
    '''
def setTimeoutProperty():
    '''returns None\n\n
    setTimeoutProperty(final String p)\n
    '''
def execute():
    '''returns None\n\n
    execute()\n
    '''
def calculateCheckEveryMillis():
    '''returns long\n\n
    calculateCheckEveryMillis()\n
    '''
def calculateMaxWaitMillis():
    '''returns long\n\n
    calculateMaxWaitMillis()\n
    '''
def getMultiplier():
    '''returns long\n\n
    getMultiplier()\n
    '''
def getValues():
    '''returns String[]\n\n
    getValues()\n
    '''
