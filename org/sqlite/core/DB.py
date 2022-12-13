def DB():
'''public DB(final String url, final String fileName, final SQLiteConfig config)
'''
pass
def getUrl():
'''public String getUrl()
'''
pass
def isClosed():
'''public boolean isClosed()
'''
pass
def getConfig():
'''public SQLiteConfig getConfig()
'''
pass
def exec():
'''public final synchronized void exec(final String sql, final boolean autoCommit)
'''
pass
def open():
'''public final synchronized void open(final String file, final int openFlags)
'''
pass
def close():
'''public final synchronized void close()
'''
pass
def prepare():
'''public final synchronized void prepare(final CoreStatement stmt)
'''
pass
def finalize():
'''public final synchronized int finalize(final CoreStatement stmt)
'''
pass
def column_names():
'''public final synchronized String[] column_names(final long stmt)
'''
pass
def execute():
'''public final synchronized boolean execute(final CoreStatement stmt, final Object[] vals)
'''
pass
def executeUpdate():
'''public final synchronized int executeUpdate(final CoreStatement stmt, final Object[] vals)
'''
pass
def throwex():
'''public final void throwex(final int errorCode)
'''
pass
def newSQLException():
'''public static SQLiteException newSQLException(final int errorCode, final String errorMessage)
'''
pass
