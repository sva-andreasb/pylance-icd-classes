STATEMENT_STATIC = "int  2"
STATEMENT_PREPARED = "int  4"
STATEMENT_CALLABLE = "int  8"
def ():
    '''returns PyStatement\n\n
    (final Statement statement, final Object sql, final int style)\n
    (final Statement statement, final Procedure procedure)\n
    '''
def __unicode__():
    '''returns PyUnicode\n\n
    __unicode__()\n
    '''
def __str__():
    '''returns PyString\n\n
    __str__()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def __findattr_ex__():
    '''returns PyObject\n\n
    __findattr_ex__(final String name)\n
    '''
def __del__():
    '''returns None\n\n
    __del__()\n
    '''
def execute():
    '''returns None\n\n
    execute(final PyCursor cursor, final PyObject params, final PyObject bindings)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def traverse():
    '''returns int\n\n
    traverse(final Visitproc visit, final Object arg)\n
    '''
def refersDirectlyTo():
    '''returns boolean\n\n
    refersDirectlyTo(final PyObject ob)\n
    '''
