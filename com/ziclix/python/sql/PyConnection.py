def ():
    '''returns PyConnection\n\n
    (final Connection connection)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def __setattr__():
    '''returns None\n\n
    __setattr__(final String name, final PyObject value)\n
    '''
def __findattr_ex__():
    '''returns PyObject\n\n
    __findattr_ex__(final String name)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def commit():
    '''returns None\n\n
    commit()\n
    '''
def rollback():
    '''returns None\n\n
    rollback()\n
    '''
def nativesql():
    '''returns PyObject\n\n
    nativesql(final PyObject nativeSQL)\n
    '''
def cursor():
    '''returns PyCursor\n\n
    cursor()\n
    cursor(final boolean dynamicFetch)\n
    cursor(final boolean dynamicFetch, final PyObject rsType, final PyObject rsConcur)\n
    '''
def __enter__():
    '''returns PyObject\n\n
    __enter__(final ThreadState ts)\n
    __enter__()\n
    '''
def __exit__():
    '''returns boolean\n\n
    __exit__(final ThreadState ts, final PyException exception)\n
    __exit__(final PyObject type, final PyObject value, final PyObject traceback)\n
    '''
def traverse():
    '''returns int\n\n
    traverse(final Visitproc visit, final Object arg)\n
    '''
def refersDirectlyTo():
    '''returns boolean\n\n
    refersDirectlyTo(final PyObject ob)\n
    '''
