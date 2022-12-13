def PyConnection():
    '''    public PyConnection(final Connection connection)
    '''
def toString():
    '''    public String toString()
    '''
def classDictInit():
    '''    public static void classDictInit(final PyObject dict)
    '''
def __setattr__():
    '''    public void __setattr__(final String name, final PyObject value)
    '''
def __findattr_ex__():
    '''    public PyObject __findattr_ex__(final String name)
    '''
def close():
    '''    public void close()
    '''
def commit():
    '''    public void commit()
    '''
def rollback():
    '''    public void rollback()
    '''
def nativesql():
    '''    public PyObject nativesql(final PyObject nativeSQL)
    '''
def cursor():
    '''    public PyCursor cursor()
    public PyCursor cursor(final boolean dynamicFetch)
    public PyCursor cursor(final boolean dynamicFetch, final PyObject rsType, final PyObject rsConcur)
    '''
def __enter__():
    '''    public PyObject __enter__(final ThreadState ts)
    public PyObject __enter__()
    '''
def __exit__():
    '''    public boolean __exit__(final ThreadState ts, final PyException exception)
    public boolean __exit__(final PyObject type, final PyObject value, final PyObject traceback)
    '''
def traverse():
    '''    public int traverse(final Visitproc visit, final Object arg)
    '''
def refersDirectlyTo():
    '''    public boolean refersDirectlyTo(final PyObject ob)
    '''
