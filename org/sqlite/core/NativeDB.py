def NativeDB():
    '''    public NativeDB(final String url, final String fileName, final SQLiteConfig config)
    '''
def load():
    '''    public static boolean load()
    '''
def _exec():
    '''    public synchronized int _exec(final String sql)
    '''
def libversion():
    '''    public synchronized String libversion()
    '''
def column_decltype():
    '''    public synchronized String column_decltype(final long stmt, final int col)
    '''
def column_table_name():
    '''    public synchronized String column_table_name(final long stmt, final int col)
    '''
def column_name():
    '''    public synchronized String column_name(final long stmt, final int col)
    '''
def column_text():
    '''    public synchronized String column_text(final long stmt, final int col)
    '''
def result_text():
    '''    public synchronized void result_text(final long context, final String val)
    '''
def result_error():
    '''    public synchronized void result_error(final long context, final String err)
    '''
def value_text():
    '''    public synchronized String value_text(final Function f, final int arg)
    '''
def create_function():
    '''    public synchronized int create_function(final String name, final Function func, final int flags)
    '''
def destroy_function():
    '''    public synchronized int destroy_function(final String name)
    '''
def backup():
    '''    public int backup(final String dbName, final String destFileName, final ProgressObserver observer)
    '''
def restore():
    '''    public synchronized int restore(final String dbName, final String sourceFileName, final ProgressObserver observer)
    '''
