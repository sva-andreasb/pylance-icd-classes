MILLIS_KEY = "String  \"millis\""
DATETIME_KEY = "String  \"datetime\""
CHECKDIRS_KEY = "String  \"checkdirs\""
GRANULARITY_KEY = "String  \"granularity\""
WHEN_KEY = "String  \"when\""
PATTERN_KEY = "String  \"pattern\""
def ():
    '''returns DateSelector\n\n
    ()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def setMillis():
    '''returns None\n\n
    setMillis(final long millis)\n
    '''
def getMillis():
    '''returns long\n\n
    getMillis()\n
    '''
def setDatetime():
    '''returns None\n\n
    setDatetime(final String dateTime)\n
    '''
def setCheckdirs():
    '''returns None\n\n
    setCheckdirs(final boolean includeDirs)\n
    '''
def setGranularity():
    '''returns None\n\n
    setGranularity(final int granularity)\n
    '''
def setWhen():
    '''returns None\n\n
    setWhen(final TimeComparisons tcmp)\n
    setWhen(final TimeComparison t)\n
    '''
def setPattern():
    '''returns None\n\n
    setPattern(final String pattern)\n
    '''
def setParameters():
    '''returns None\n\n
    setParameters(final Parameter[] parameters)\n
    '''
def verifySettings():
    '''returns None\n\n
    verifySettings()\n
    '''
def isSelected():
    '''returns boolean\n\n
    isSelected(final File basedir, final String filename, final File file)\n
    '''
