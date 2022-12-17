def ():
    '''returns IloIntervalVarArray\n\n
    (final long cPtr, final boolean cMemoryOwn)\n
    (final IloEnv env, final int max)\n
    (final IloEnv env)\n
    '''
def setOwn():
    '''returns None\n\n
    setOwn(final boolean cMemoryOwn)\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def add():
    '''returns None\n\n
    add(final IloIntervalVar v)\n
    add(final ilog.concert.cppimpl.IloIntervalVar x)\n
    add(final int more, final ilog.concert.cppimpl.IloIntervalVar x)\n
    add(final IloIntervalVarArray ax)\n
    '''
def get():
    '''returns IloIntervalVar\n\n
    get(final int index)\n
    '''
def set():
    '''returns None\n\n
    set(final int index, final IloIntervalVar v)\n
    '''
def end():
    '''returns None\n\n
    end()\n
    '''
def getSize():
    '''returns int\n\n
    getSize()\n
    '''
def getEnv():
    '''returns IloEnv\n\n
    getEnv()\n
    '''
def remove():
    '''returns None\n\n
    remove(final int first, final int nb)\n
    remove(final int first)\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def array_set():
    '''returns None\n\n
    array_set(final int index, final ilog.concert.cppimpl.IloIntervalVar val)\n
    '''
