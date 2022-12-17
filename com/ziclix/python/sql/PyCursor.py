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
def __del__():
    '''returns None\n\n
    __del__()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def __iter__():
    '''returns PyObject\n\n
    __iter__()\n
    '''
def next():
    '''returns PyObject\n\n
    next()\n
    '''
def __iternext__():
    '''returns PyObject\n\n
    __iternext__()\n
    '''
def getDataHandler():
    '''returns DataHandler\n\n
    getDataHandler()\n
    '''
def callproc():
    '''returns None\n\n
    callproc(final PyObject name, final PyObject params, final PyObject bindings, final PyObject maxRows)\n
    '''
def executemany():
    '''returns None\n\n
    executemany(final PyObject sql, final PyObject params, final PyObject bindings, final PyObject maxRows)\n
    '''
def execute():
    '''returns None\n\n
    execute(final PyObject sql, final PyObject params, final PyObject bindings, final PyObject maxRows)\n
    '''
def fetchone():
    '''returns PyObject\n\n
    fetchone()\n
    '''
def fetchall():
    '''returns PyObject\n\n
    fetchall()\n
    '''
def fetchmany():
    '''returns PyObject\n\n
    fetchmany(final int size)\n
    '''
def nextset():
    '''returns PyObject\n\n
    nextset()\n
    '''
def prepare():
    '''returns PyStatement\n\n
    prepare(final PyObject sql)\n
    '''
def scroll():
    '''returns None\n\n
    scroll(final int value, final String mode)\n
    '''
def warning():
    '''returns None\n\n
    warning(final WarningEvent event)\n
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
