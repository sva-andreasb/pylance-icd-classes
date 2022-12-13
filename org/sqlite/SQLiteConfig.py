DEFAULT_DATE_STRING_FORMAT = "String  \"yyyy-MM-dd HH:mm:ss.SSS\""
def SQLiteConfig():
    '''    public SQLiteConfig()
    public SQLiteConfig(final Properties prop)
    '''
def newConnectionConfig():
    '''    public SQLiteConnectionConfig newConnectionConfig()
    '''
def createConnection():
    '''    public Connection createConnection(final String url)
    '''
def apply():
    '''    public void apply(final Connection conn)
    '''
def isEnabledSharedCache():
    '''    public boolean isEnabledSharedCache()
    '''
def isEnabledLoadExtension():
    '''    public boolean isEnabledLoadExtension()
    '''
def getOpenModeFlags():
    '''    public int getOpenModeFlags()
    '''
def setPragma():
    '''    public void setPragma(final Pragma pragma, final String value)
    '''
def toProperties():
    '''    public Properties toProperties()
    '''
def setOpenMode():
    '''    public void setOpenMode(final SQLiteOpenMode mode)
    '''
def resetOpenMode():
    '''    public void resetOpenMode(final SQLiteOpenMode mode)
    '''
def setSharedCache():
    '''    public void setSharedCache(final boolean enable)
    '''
def enableLoadExtension():
    '''    public void enableLoadExtension(final boolean enable)
    '''
def setReadOnly():
    '''    public void setReadOnly(final boolean readOnly)
    '''
def setCacheSize():
    '''    public void setCacheSize(final int numberOfPages)
    '''
def enableCaseSensitiveLike():
    '''    public void enableCaseSensitiveLike(final boolean enable)
    '''
def enableCountChanges():
    '''    public void enableCountChanges(final boolean enable)
    '''
def setDefaultCacheSize():
    '''    public void setDefaultCacheSize(final int numberOfPages)
    '''
def enableEmptyResultCallBacks():
    '''    public void enableEmptyResultCallBacks(final boolean enable)
    '''
def setEncoding():
    '''    public void setEncoding(final Encoding encoding)
    '''
def enforceForeignKeys():
    '''    public void enforceForeignKeys(final boolean enforce)
    '''
def enableFullColumnNames():
    '''    public void enableFullColumnNames(final boolean enable)
    '''
def enableFullSync():
    '''    public void enableFullSync(final boolean enable)
    '''
def incrementalVacuum():
    '''    public void incrementalVacuum(final int numberOfPagesToBeRemoved)
    '''
def setJournalMode():
    '''    public void setJournalMode(final JournalMode mode)
    '''
def setJounalSizeLimit():
    '''    public void setJounalSizeLimit(final int limit)
    '''
def useLegacyFileFormat():
    '''    public void useLegacyFileFormat(final boolean use)
    '''
def setLockingMode():
    '''    public void setLockingMode(final LockingMode mode)
    '''
def setPageSize():
    '''    public void setPageSize(final int numBytes)
    '''
def setMaxPageCount():
    '''    public void setMaxPageCount(final int numPages)
    '''
def setReadUncommited():
    '''    public void setReadUncommited(final boolean useReadUncommitedIsolationMode)
    '''
def enableRecursiveTriggers():
    '''    public void enableRecursiveTriggers(final boolean enable)
    '''
def enableReverseUnorderedSelects():
    '''    public void enableReverseUnorderedSelects(final boolean enable)
    '''
def enableShortColumnNames():
    '''    public void enableShortColumnNames(final boolean enable)
    '''
def setSynchronous():
    '''    public void setSynchronous(final SynchronousMode mode)
    '''
def setHexKeyMode():
    '''    public void setHexKeyMode(final HexKeyMode mode)
    '''
def setTempStore():
    '''    public void setTempStore(final TempStore storeType)
    '''
def setTempStoreDirectory():
    '''    public void setTempStoreDirectory(final String directoryName)
    '''
def setUserVersion():
    '''    public void setUserVersion(final int version)
    '''
def setApplicationId():
    '''    public void setApplicationId(final int id)
    '''
def setTransactionMode():
    '''    public void setTransactionMode(final TransactionMode transactionMode)
    public void setTransactionMode(final String transactionMode)
    '''
def getTransactionMode():
    '''    public TransactionMode getTransactionMode()
    '''
def setDatePrecision():
    '''    public void setDatePrecision(final String datePrecision)
    '''
def setDateClass():
    '''    public void setDateClass(final String dateClass)
    '''
def setDateStringFormat():
    '''    public void setDateStringFormat(final String dateStringFormat)
    '''
def setBusyTimeout():
    '''    public void setBusyTimeout(final int milliseconds)
    '''
def getBusyTimeout():
    '''    public int getBusyTimeout()
    '''
def getPragmaName():
    '''    public final String getPragmaName()
    '''
def getValue():
    '''    public String getValue()
    public String getValue()
    public String getValue()
    public String getValue()
    public String getValue()
    public String getValue()
    public String getValue()
    public String getValue()
    public String getValue()
    '''
def getEncoding():
    '''    public static Encoding getEncoding(final String value)
    '''
def getMode():
    '''    public static TransactionMode getMode(final String mode)
    '''
def getPrecision():
    '''    public static DatePrecision getPrecision(final String precision)
    '''
def getDateClass():
    '''    public static DateClass getDateClass(final String dateClass)
    '''
