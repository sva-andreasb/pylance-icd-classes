def DB():
    '''    public DB(final String url, final String fileName, final SQLiteConfig config)
    '''
def getUrl():
    '''    public String getUrl()
    '''
def isClosed():
    '''    public boolean isClosed()
    '''
def getConfig():
    '''    public SQLiteConfig getConfig()
    '''
def exec():
    '''    public final synchronized void exec(final String sql, final boolean autoCommit)
    '''
def open():
    '''    public final synchronized void open(final String file, final int openFlags)
    '''
def close():
    '''    public final synchronized void close()
    '''
def prepare():
    '''    public final synchronized void prepare(final CoreStatement stmt)
    '''
def finalize():
    '''    public final synchronized int finalize(final CoreStatement stmt)
    '''
def column_names():
    '''    public final synchronized String[] column_names(final long stmt)
    '''
def execute():
    '''    public final synchronized boolean execute(final CoreStatement stmt, final Object[] vals)
    '''
def executeUpdate():
    '''    public final synchronized int executeUpdate(final CoreStatement stmt, final Object[] vals)
    '''
def throwex():
    '''    public final void throwex(final int errorCode)
    '''
def newSQLException():
    '''    public static SQLiteException newSQLException(final int errorCode, final String errorMessage)
    '''
