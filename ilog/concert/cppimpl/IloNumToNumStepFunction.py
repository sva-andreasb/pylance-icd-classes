def ():
    '''returns IloNumToNumStepFunction\n\n
    (final long cPtr, final boolean cMemoryOwn)\n
    (final IloEnv env, final double xmin, final double xmax, final double dval, final String name)\n
    (final IloEnv env, final double xmin, final double xmax, final double dval)\n
    (final IloEnv env, final double xmin, final double xmax)\n
    (final IloEnv env, final double xmin)\n
    (final IloEnv env)\n
    (final IloEnv env, final ilog.concert.cppimpl.IloNumArray x, final ilog.concert.cppimpl.IloNumArray v, final double xmin, final double xmax, final String name)\n
    (final IloEnv env, final ilog.concert.cppimpl.IloNumArray x, final ilog.concert.cppimpl.IloNumArray v, final double xmin, final double xmax)\n
    (final IloEnv env, final ilog.concert.cppimpl.IloNumArray x, final ilog.concert.cppimpl.IloNumArray v, final double xmin)\n
    (final IloEnv env, final ilog.concert.cppimpl.IloNumArray x, final ilog.concert.cppimpl.IloNumArray v)\n
    (final IloEnv env, final double yl, final ilog.concert.cppimpl.IloNumArray x, final ilog.concert.cppimpl.IloNumArray y, final String name)\n
    (final IloEnv env, final double yl, final ilog.concert.cppimpl.IloNumArray x, final ilog.concert.cppimpl.IloNumArray y)\n
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
    add(final ilog.concert.IloNumToNumStepFunction f)\n
    '''
def sub():
    '''returns None\n\n
    sub(final ilog.concert.IloNumToNumStepFunction f)\n
    '''
def prod():
    '''returns None\n\n
    prod(final double k)\n
    '''
def setSteps():
    '''returns None\n\n
    setSteps(final IloNumArray x, final IloNumArray v)\n
    setSteps(final ilog.concert.cppimpl.IloNumArray x, final ilog.concert.cppimpl.IloNumArray v)\n
    '''
def setPeriodic():
    '''returns None\n\n
    setPeriodic(final ilog.concert.IloNumToNumStepFunction f, final double x0, final double n, final double dval)\n
    setPeriodic(final ilog.concert.IloNumToNumStepFunction f, final double x0, final double n)\n
    setPeriodic(final ilog.concert.IloNumToNumStepFunction f, final double x0)\n
    setPeriodic(final IloNumToNumStepFunction f, final double x0, final double n, final double dval)\n
    setPeriodic(final IloNumToNumStepFunction f, final double x0, final double n)\n
    setPeriodic(final IloNumToNumStepFunction f, final double x0)\n
    '''
def setPeriodicValue():
    '''returns None\n\n
    setPeriodicValue(final double x1, final double x2, final ilog.concert.IloNumToNumStepFunction f, final double offset)\n
    setPeriodicValue(final double x1, final double x2, final ilog.concert.IloNumToNumStepFunction f)\n
    setPeriodicValue(final double x1, final double x2, final IloNumToNumStepFunction f, final double offset)\n
    setPeriodicValue(final double x1, final double x2, final IloNumToNumStepFunction f)\n
    '''
def setMin():
    '''returns None\n\n
    setMin(final ilog.concert.IloNumToNumStepFunction fct)\n
    setMin(final double x1, final double x2, final double v)\n
    setMin(final IloNumToNumStepFunction fct)\n
    '''
def setMax():
    '''returns None\n\n
    setMax(final ilog.concert.IloNumToNumStepFunction fct)\n
    setMax(final double x1, final double x2, final double v)\n
    setMax(final IloNumToNumStepFunction fct)\n
    '''
def copyImpl():
    '''returns IloNumToNumStepFunction\n\n
    copyImpl()\n
    '''
def setValue():
    '''returns None\n\n
    setValue(final double x1, final double x2, final double v)\n
    '''
def addValue():
    '''returns None\n\n
    addValue(final double x1, final double x2, final double v)\n
    '''
def shift():
    '''returns None\n\n
    shift(final double dx, final double dval)\n
    shift(final double dx)\n
    '''
def getDefinitionIntervalMin():
    '''returns double\n\n
    getDefinitionIntervalMin()\n
    '''
def getDefinitionIntervalMax():
    '''returns double\n\n
    getDefinitionIntervalMax()\n
    '''
def getValue():
    '''returns double\n\n
    getValue(final double x)\n
    '''
def getMax():
    '''returns double\n\n
    getMax(final double x1, final double x2)\n
    '''
def getMin():
    '''returns double\n\n
    getMin(final double x1, final double x2)\n
    '''
def getArea():
    '''returns double\n\n
    getArea(final double x1, final double x2)\n
    '''
def operator_prod_equal():
    '''returns None\n\n
    operator_prod_equal(final double k)\n
    '''
def operator_sum_equal():
    '''returns None\n\n
    operator_sum_equal(final IloNumToNumStepFunction fct)\n
    '''
def operator_diff_equal():
    '''returns None\n\n
    operator_diff_equal(final IloNumToNumStepFunction fct)\n
    '''
def dilate():
    '''returns None\n\n
    dilate(final double k)\n
    '''
