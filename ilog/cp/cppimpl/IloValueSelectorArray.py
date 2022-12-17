def ():
    '''returns IloValueSelectorArray\n\n
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
    add(final IloValueSelector v)\n
    add(final ilog.cp.cppimpl.IloValueSelector x)\n
    add(final int more, final ilog.cp.cppimpl.IloValueSelector x)\n
    add(final IloValueSelectorArray ax)\n
    '''
def get():
    '''returns IloValueSelector\n\n
    get(final int index)\n
    '''
def set():
    '''returns None\n\n
    set(final int index, final IloValueSelector v)\n
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
    array_set(final int index, final ilog.cp.cppimpl.IloValueSelector val)\n
    '''
