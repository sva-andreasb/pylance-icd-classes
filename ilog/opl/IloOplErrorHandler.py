def ():
    '''returns IloOplErrorHandler\n\n
    (final long cPtr, final boolean cMemoryOwn)\n
    (final IloOplErrorHandlerBaseI impl)\n
    (final IloEnv env)\n
    (final IloEnv env, final ostream outs)\n
    '''
def setOwn():
    '''returns None\n\n
    setOwn(final boolean cMemoryOwn)\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def keepRefOnOutputStreamAdapter():
    '''returns None\n\n
    keepRefOnOutputStreamAdapter(final JavaToCppOutputStreamAdapter stream)\n
    '''
def end():
    '''returns None\n\n
    end()\n
    '''
def fatal():
    '''returns None\n\n
    fatal(final IloOplMessage message, final IloOplLocation location)\n
    '''
def error():
    '''returns None\n\n
    error(final IloOplMessage message, final IloOplLocation location)\n
    '''
def warning():
    '''returns None\n\n
    warning(final IloOplMessage message, final IloOplLocation location)\n
    warning(final String id, final String param1, final String param2, final String param3)\n
    '''
def ok():
    '''returns boolean\n\n
    ok()\n
    '''
def abort():
    '''returns None\n\n
    abort()\n
    '''
def setImpl():
    '''returns None\n\n
    setImpl(final IloOplErrorHandlerBaseI impl)\n
    '''
