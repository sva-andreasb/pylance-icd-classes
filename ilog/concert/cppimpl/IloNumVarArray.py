def ():
    '''returns IloNumVarArray\n\n
    (final long cPtr, final boolean cMemoryOwn)\n
    (final SWIGTYPE_p_IloDefaultArrayI i)\n
    ()\n
    (final IloEnv env, final int n)\n
    (final IloEnv env)\n
    (final IloEnv env, final IloNumArray lb, final IloNumArray ub, final ilog.concert.cppimpl.IloNumVar.CppType type)\n
    (final IloEnv env, final IloNumArray lb, final IloNumArray ub)\n
    (final IloEnv env, final double lb, final IloNumArray ub, final ilog.concert.cppimpl.IloNumVar.CppType type)\n
    (final IloEnv env, final double lb, final IloNumArray ub)\n
    (final IloEnv env, final IloNumArray lb, final double ub, final ilog.concert.cppimpl.IloNumVar.CppType type)\n
    (final IloEnv env, final IloNumArray lb, final double ub)\n
    (final IloEnv env, final int n, final double lb, final double ub, final ilog.concert.cppimpl.IloNumVar.CppType type)\n
    (final IloEnv env, final int n, final double lb, final double ub)\n
    (final IloEnv env, final IloNumColumnArray columnarray, final ilog.concert.cppimpl.IloNumVar.CppType type)\n
    (final IloEnv env, final IloNumColumnArray columnarray)\n
    (final IloEnv env, final IloNumColumnArray columnarray, final IloNumArray lb, final IloNumArray ub, final ilog.concert.cppimpl.IloNumVar.CppType type)\n
    (final IloEnv env, final IloNumColumnArray columnarray, final IloNumArray lb, final IloNumArray ub)\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def get():
    '''returns Object\n\n
    get(final int index)\n
    '''
def getNumVar():
    '''returns IloNumVar\n\n
    getNumVar(final int index)\n
    '''
def set():
    '''returns None\n\n
    set(final int index, final Object v)\n
    '''
def setNumVar():
    '''returns None\n\n
    setNumVar(final int index, final IloNumVar v)\n
    '''
def add():
    '''returns None\n\n
    add(final IloNumVar x)\n
    add(final int more, final IloNumVar x)\n
    add(final ilog.concert.IloNumVarArray ax)\n
    add(final IloNumVarArray array)\n
    add(final ilog.concert.cppimpl.IloNumVar x)\n
    add(final int more, final ilog.concert.cppimpl.IloNumVar x)\n
    '''
def operator_get():
    '''returns IloNumExprArg\n\n
    operator_get(final IloIntExprArg anIntegerExpr)\n
    '''
def setBounds():
    '''returns None\n\n
    setBounds(final IloNumArray lb, final IloNumArray ub)\n
    '''
def toNumExprArray():
    '''returns IloNumExprArray\n\n
    toNumExprArray()\n
    '''
def toIntExprArray():
    '''returns IloIntExprArray\n\n
    toIntExprArray()\n
    '''
def toIntVarArray():
    '''returns IloIntVarArray\n\n
    toIntVarArray()\n
    '''
def set_int():
    '''returns None\n\n
    set_int(final int index, final ilog.concert.cppimpl.IloNumVar val)\n
    '''
