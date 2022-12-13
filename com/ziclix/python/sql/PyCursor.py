def toString():
    '''public String toString()
    '''
def __setattr__():
    '''public void __setattr__(final String name, final PyObject value)
    '''
def __findattr_ex__():
    '''public PyObject __findattr_ex__(final String name)
    '''
def classDictInit():
    '''public static void classDictInit(final PyObject dict)
    '''
def __del__():
    '''public void __del__()
    '''
def close():
    '''public void close()
    '''
def __iter__():
    '''public PyObject __iter__()
    '''
def next():
    '''public PyObject next()
    '''
def __iternext__():
    '''public PyObject __iternext__()
    '''
def getDataHandler():
    '''public DataHandler getDataHandler()
    '''
def callproc():
    '''public void callproc(final PyObject name, final PyObject params, final PyObject bindings, final PyObject maxRows)
    '''
def executemany():
    '''public void executemany(final PyObject sql, final PyObject params, final PyObject bindings, final PyObject maxRows)
    '''
def execute():
    '''public void execute(final PyObject sql, final PyObject params, final PyObject bindings, final PyObject maxRows)
    '''
def fetchone():
    '''public PyObject fetchone()
    '''
def fetchall():
    '''public PyObject fetchall()
    '''
def fetchmany():
    '''public PyObject fetchmany(final int size)
    '''
def nextset():
    '''public PyObject nextset()
    '''
def prepare():
    '''public PyStatement prepare(final PyObject sql)
    '''
def scroll():
    '''public void scroll(final int value, final String mode)
    '''
def warning():
    '''public void warning(final WarningEvent event)
    '''
def isSeq():
    '''public static boolean isSeq(final PyObject object)
    '''
def hasParams():
    '''public static boolean hasParams(final PyObject params)
    '''
def isSeqSeq():
    '''public static boolean isSeqSeq(final PyObject object)
    '''
def __enter__():
    '''public PyObject __enter__(final ThreadState ts)
    public PyObject __enter__()
    '''
def __exit__():
    '''public boolean __exit__(final ThreadState ts, final PyException exception)
    public boolean __exit__(final PyObject type, final PyObject value, final PyObject traceback)
    '''
def traverse():
    '''public int traverse(final Visitproc visit, final Object arg)
    '''
def refersDirectlyTo():
    '''public boolean refersDirectlyTo(final PyObject ob)
    '''
