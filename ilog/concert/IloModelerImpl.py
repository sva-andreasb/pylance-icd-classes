def ():
    '''returns IloModelerImpl\n\n
    (final IloEnv env)\n
    (final boolean noModel)\n
    '''
def end():
    '''returns None\n\n
    end()\n
    '''
def numVar():
    '''returns IloNumVar\n\n
    numVar(final double lb, final double ub, final IloNumVarType type)\n
    numVar(final double lb, final double ub, final IloNumVarType type, final String name)\n
    numVar(final double lb, final double ub, final String name)\n
    numVar(final double lb, final double ub)\n
    '''
def numVarArray():
    '''returns IloNumVar[]\n\n
    numVarArray(final int n, final double lb, final double ub, final IloNumVarType type)\n
    numVarArray(final int n, final double lb, final double ub, final IloNumVarType type, final String[] name)\n
    numVarArray(final int n, final double[] lb, final double[] ub, final IloNumVarType[] type)\n
    numVarArray(final int n, final double[] lb, final double[] ub, final IloNumVarType[] type, final String[] name)\n
    numVarArray(final int n, final double lb, final double ub)\n
    numVarArray(final int n, final double[] lb, final double[] ub)\n
    numVarArray(final int n, final double lb, final double ub, final String[] name)\n
    numVarArray(final int n, final double[] lb, final double[] ub, final String[] name)\n
    '''
def numVarArrayO():
    '''returns IloNumVarArray\n\n
    numVarArrayO(final int n, final double[] lb, final double[] ub, final IloNumVarType[] type)\n
    numVarArrayO(final int n, final double lb, final double ub)\n
    '''
def intVar():
    '''returns IloIntVar\n\n
    intVar(final int lb, final int ub, final String name)\n
    intVar(final int lb, final int ub)\n
    '''
def intVarArray():
    '''returns IloIntVar[]\n\n
    intVarArray(final int n, final int lb, final int ub)\n
    intVarArray(final int n, final int[] lb, final int[] ub)\n
    intVarArray(final int n, final int lb, final int ub, final String[] name)\n
    intVarArray(final int n, final int[] lb, final int[] ub, final String[] name)\n
    '''
def boolVar():
    '''returns IloIntVar\n\n
    boolVar(final String name)\n
    boolVar()\n
    '''
def boolVarArray():
    '''returns IloIntVar[]\n\n
    boolVarArray(final int n)\n
    boolVarArray(final int n, final String[] name)\n
    '''
def minimize():
    '''returns IloObjective\n\n
    minimize(final IloNumExpr expr, final String name)\n
    minimize(final IloNumExpr expr)\n
    '''
def maximize():
    '''returns IloObjective\n\n
    maximize(final IloNumExpr expr, final String name)\n
    maximize(final IloNumExpr expr)\n
    '''
def objective():
    '''returns IloObjective\n\n
    objective(final IloObjectiveSense sense, final IloNumExpr expr, final String name)\n
    objective(final IloObjectiveSense sense, final IloNumExpr expr)\n
    '''
def addObjective():
    '''returns IloObjective\n\n
    addObjective(final IloObjectiveSense sense, final IloNumExpr expr, final String name)\n
    addObjective(final IloObjectiveSense sense, final IloNumExpr expr)\n
    '''
def addMinimize():
    '''returns IloObjective\n\n
    addMinimize(final IloNumExpr expr)\n
    addMinimize(final IloNumExpr expr, final String name)\n
    '''
def addMaximize():
    '''returns IloObjective\n\n
    addMaximize(final IloNumExpr expr)\n
    addMaximize(final IloNumExpr expr, final String name)\n
    '''
def linearNumExpr():
    '''returns IloLinearNumExpr\n\n
    linearNumExpr()\n
    linearNumExpr(final double val)\n
    '''
def scalProd():
    '''returns IloNumExpr\n\n
    scalProd(final double[] vals, final IloNumVar[] vars)\n
    scalProd(final IloNumVar[] vars, final double[] vals)\n
    scalProd(final double[] vals, final IloNumVar[] vars, final int start, final int num)\n
    scalProd(final IloNumVar[] vars, final double[] vals, final int start, final int num)\n
    scalProd(final int[] vals, final IloNumVar[] vars)\n
    scalProd(final IloNumVar[] vars, final int[] vals)\n
    scalProd(final int[] vals, final IloIntVar[] vars)\n
    scalProd(final IloIntVar[] vars, final int[] vals)\n
    scalProd(final int[] vals, final IloIntVar[] vars, final int start, final int num)\n
    scalProd(final IloIntVar[] vars, final int[] vals, final int start, final int num)\n
    scalProd(final int[] vals, final IloNumVar[] vars, final int start, final int num)\n
    scalProd(final IloNumVar[] vars, final int[] vals, final int start, final int num)\n
    scalProd(final IloNumVar[] vars1, final IloNumVar[] vars2)\n
    scalProd(final IloNumVar[] vars1, final IloNumVar[] vars2, final int start, final int num)\n
    '''
def linearIntExpr():
    '''returns IloLinearIntExpr\n\n
    linearIntExpr(final int val)\n
    linearIntExpr()\n
    '''
def negative():
    '''returns IloNumExpr\n\n
    negative(final IloNumExpr e)\n
    '''
def sum():
    '''returns IloNumExpr\n\n
    sum(final IloNumExpr e, final double v)\n
    sum(final IloNumExpr e1, final IloNumExpr e2)\n
    sum(final double v, final IloNumExpr e1)\n
    sum(final IloNumExpr expr1, final IloNumExpr expr2, final IloNumExpr expr3)\n
    sum(final IloNumExpr expr1, final IloNumExpr expr2, final IloNumExpr expr3, final IloNumExpr expr4)\n
    sum(final IloNumExpr expr1, final IloNumExpr expr2, final IloNumExpr expr3, final IloNumExpr expr4, final IloNumExpr expr5)\n
    sum(final IloNumExpr expr1, final IloNumExpr expr2, final IloNumExpr expr3, final IloNumExpr expr4, final IloNumExpr expr5, final IloNumExpr expr6)\n
    sum(final IloNumExpr expr1, final IloNumExpr expr2, final IloNumExpr expr3, final IloNumExpr expr4, final IloNumExpr expr5, final IloNumExpr expr6, final IloNumExpr expr7)\n
    sum(final IloNumExpr expr1, final IloNumExpr expr2, final IloNumExpr expr3, final IloNumExpr expr4, final IloNumExpr expr5, final IloNumExpr expr6, final IloNumExpr expr7, final IloNumExpr expr8)\n
    sum(final IloNumExpr[] expr, final int start, final int num)\n
    sum(final IloNumExpr[] expr)\n
    '''
def diff():
    '''returns IloNumExpr\n\n
    diff(final IloNumExpr e, final double v)\n
    diff(final IloNumExpr e1, final IloNumExpr e2)\n
    diff(final double v, final IloNumExpr e1)\n
    '''
def prod():
    '''returns IloNumExpr\n\n
    prod(final double v, final IloNumVar var1, final IloNumVar var2)\n
    prod(final IloNumVar var1, final double v, final IloNumVar var2)\n
    prod(final IloNumVar var1, final IloNumVar var2, final double v)\n
    prod(final IloNumExpr e, final double v)\n
    prod(final IloNumExpr e1, final IloNumExpr e2)\n
    prod(final double v, final IloNumExpr e1)\n
    '''
def max():
    '''returns IloNumExpr\n\n
    max(final IloNumExpr e1, final IloNumExpr e2)\n
    max(final double val, final IloNumExpr e2)\n
    max(final IloNumExpr e1, final double val)\n
    max(final IloNumExpr[] expr)\n
    '''
def min():
    '''returns IloNumExpr\n\n
    min(final IloNumExpr e1, final IloNumExpr e2)\n
    min(final double val, final IloNumExpr e2)\n
    min(final IloNumExpr e1, final double val)\n
    min(final IloNumExpr[] expr)\n
    '''
def square():
    '''returns IloNumExpr\n\n
    square(final IloNumExpr e)\n
    '''
def constant():
    '''returns IloNumExpr\n\n
    constant(final double x)\n
    '''
def addRange():
    '''returns IloRange\n\n
    addRange(final double lb, final IloNumExpr expr, final double ub, final String name)\n
    addRange(final double lb, final IloNumExpr expr, final double ub)\n
    '''
def addEq():
    '''returns IloRange\n\n
    addEq(final IloNumExpr e, final double v)\n
    addEq(final IloNumExpr e, final double v, final String name)\n
    addEq(final IloNumExpr e1, final IloNumExpr e2)\n
    addEq(final IloNumExpr e1, final IloNumExpr e2, final String name)\n
    addEq(final double v, final IloNumExpr e)\n
    addEq(final double v, final IloNumExpr e, final String name)\n
    '''
def addGe():
    '''returns IloRange\n\n
    addGe(final IloNumExpr e, final double v)\n
    addGe(final IloNumExpr e, final double v, final String name)\n
    addGe(final IloNumExpr e1, final IloNumExpr e2)\n
    addGe(final IloNumExpr e1, final IloNumExpr e2, final String name)\n
    addGe(final double v, final IloNumExpr e)\n
    addGe(final double v, final IloNumExpr e, final String name)\n
    '''
def addLe():
    '''returns IloRange\n\n
    addLe(final IloNumExpr e, final double v)\n
    addLe(final IloNumExpr e, final double v, final String name)\n
    addLe(final IloNumExpr e1, final IloNumExpr e2)\n
    addLe(final IloNumExpr e1, final IloNumExpr e2, final String name)\n
    addLe(final double v, final IloNumExpr e)\n
    addLe(final double v, final IloNumExpr e, final String name)\n
    '''
def range():
    '''returns IloRange\n\n
    range(final double lb, final IloNumExpr expr, final double ub, final String name)\n
    range(final double lb, final IloNumExpr expr, final double ub)\n
    '''
def eq():
    '''returns IloRange\n\n
    eq(final IloNumExpr e1, final IloNumExpr e2, final String name)\n
    eq(final IloNumExpr e, final double v)\n
    eq(final IloNumExpr e, final double v, final String name)\n
    eq(final IloNumExpr e1, final IloNumExpr e2)\n
    eq(final double v, final IloNumExpr e)\n
    eq(final double v, final IloNumExpr e, final String name)\n
    '''
def ge():
    '''returns IloRange\n\n
    ge(final IloNumExpr e, final double v)\n
    ge(final IloNumExpr e, final double v, final String name)\n
    ge(final IloNumExpr e1, final IloNumExpr e2)\n
    ge(final IloNumExpr e1, final IloNumExpr e2, final String name)\n
    ge(final int max, final IloCumulFunctionExpr f)\n
    ge(final IloCumulFunctionExpr f, final int min)\n
    ge(final double v, final IloNumExpr e)\n
    ge(final double v, final IloNumExpr e, final String name)\n
    '''
def le():
    '''returns IloRange\n\n
    le(final IloNumExpr e, final double v)\n
    le(final IloNumExpr e, final double v, final String name)\n
    le(final IloNumExpr e1, final IloNumExpr e2)\n
    le(final IloNumExpr e1, final IloNumExpr e2, final String name)\n
    le(final IloCumulFunctionExpr f, final int max)\n
    le(final int min, final IloCumulFunctionExpr f)\n
    le(final double v, final IloNumExpr e)\n
    le(final double v, final IloNumExpr e, final String name)\n
    '''
def abs():
    '''returns IloNumExpr\n\n
    abs(final IloNumExpr e)\n
    '''
def or():
    '''returns IloOr\n\n
    or()\n
    or(final IloConstraint[] cons)\n
    or(final IloConstraint[] cons, final String name)\n
    or(final IloConstraint[] cons, final int start, final int num)\n
    or(final IloConstraint[] cons, final int start, final int num, final String name)\n
    or(final IloConstraint con1, final IloConstraint con2)\n
    or(final IloConstraint con1, final IloConstraint con2, final String name)\n
    '''
def and():
    '''returns IloAnd\n\n
    and()\n
    and(final IloConstraint ct1, final IloConstraint ct2)\n
    and(final IloConstraint[] cons, final String name)\n
    '''
def not():
    '''returns IloConstraint\n\n
    not(final IloConstraint con1)\n
    not(final IloConstraint con1, final String name)\n
    '''
def ifThen():
    '''returns IloConstraint\n\n
    ifThen(final IloConstraint con1, final IloConstraint con2)\n
    ifThen(final IloConstraint con1, final IloConstraint con2, final String name)\n
    '''
def numExpr():
    '''returns IloNumExpr\n\n
    numExpr()\n
    '''
def clearModel():
    '''returns None\n\n
    clearModel()\n
    '''
def intRange():
    '''returns IloIntRange\n\n
    intRange(final int lb, final int ub)\n
    '''
def numSet():
    '''returns IloNumSet\n\n
    numSet()\n
    '''
def getEnvImpl():
    '''returns IloEnv\n\n
    getEnvImpl()\n
    '''
def getEnvImplNoThrow():
    '''returns IloEnv\n\n
    getEnvImplNoThrow()\n
    '''
