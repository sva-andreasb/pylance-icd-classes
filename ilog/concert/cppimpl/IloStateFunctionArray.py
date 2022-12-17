def ():
    '''returns IloStateFunctionArray\n\n
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
def operator_get():
    '''returns IloStateFunction\n\n
    operator_get(final int i)\n
    '''
def add():
    '''returns None\n\n
    add(final IloStateFunction x)\n
    add(final int more, final IloStateFunction x)\n
    add(final IloStateFunctionArray ax)\n
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
    array_set(final int index, final IloStateFunction val)\n
    '''
def get_IloStateFunction():
    '''returns IloStateFunction\n\n
    get_IloStateFunction(final int index)\n
    '''
