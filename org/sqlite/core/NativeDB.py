def NativeDB():
'''public NativeDB(final String url, final String fileName, final SQLiteConfig config)
'''
pass
def load():
'''public static boolean load()
'''
pass
def _exec():
'''public synchronized int _exec(final String sql)
'''
pass
def libversion():
'''public synchronized String libversion()
'''
pass
def column_decltype():
'''public synchronized String column_decltype(final long stmt, final int col)
'''
pass
def column_table_name():
'''public synchronized String column_table_name(final long stmt, final int col)
'''
pass
def column_name():
'''public synchronized String column_name(final long stmt, final int col)
'''
pass
def column_text():
'''public synchronized String column_text(final long stmt, final int col)
'''
pass
def result_text():
'''public synchronized void result_text(final long context, final String val)
'''
pass
def result_error():
'''public synchronized void result_error(final long context, final String err)
'''
pass
def value_text():
'''public synchronized String value_text(final Function f, final int arg)
'''
pass
def create_function():
'''public synchronized int create_function(final String name, final Function func, final int flags)
'''
pass
def destroy_function():
'''public synchronized int destroy_function(final String name)
'''
pass
def backup():
'''public int backup(final String dbName, final String destFileName, final ProgressObserver observer)
'''
pass
def restore():
'''public synchronized int restore(final String dbName, final String sourceFileName, final ProgressObserver observer)
'''
pass
