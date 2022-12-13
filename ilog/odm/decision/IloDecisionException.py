COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
IO_PARAM_COUNT_ERROR = "String  \"IO_PARAM_COUNT_ERROR\""
IO_UNRESOLVED_THIS = "String  \"IO_UNRESOLVED_THIS\""
IO_TYPE_ERROR = "String  \"IO_TYPE_ERROR\""
BAD_PARAM_VALUE = "String  \"BAD_PARAM_VALUE\""
PROP_NOT_FOUND = "String  \"PROP_NOT_FOUND\""
PROP_NOT_SELECTED = "String  \"PROP_NOT_SELECTED\""
TMPL_INST_ERROR = "String  \"TMPL_INST_ERROR\""
ENGINE_MODE_ERROR = "String  \"...\""
RANGE_IN_N_REQS = "String  \"RANGE_IN_N_REQS\""
PROP_ILLEGAL_INDEX = "String  \"PROP_ILLEGAL_INDEX\""
PROP_BAD_VALUE_TYPE = "String  \"PROP_BAD_VALUE_TYPE\""
SVC_OP_NOT_IMPLEMENTED = "String  \"SCV_OP_NOT_IMPLEMENTED\""
INVALID_REQUIREMENT_TYPE = "String  \"INV_REQ_TYPE\""
CONSTRAINT_NOT_FOUND = "String  \"CONSTRAINT_NOT_FOUND\""
INCONSISTENT_PROPS_DEF = "String  \"INCONSISTENT_PROPS_DEF\""
PARALLEL_CPLEX_NOT_SUPPORTED = "String  \"PARALLEL_CPLEX_NOT_SUPPORTED\""
ERRORS_REPORTED_FROM_OPL = "String  \"ERRORS_REPORTED_FROM_OPL\""
def IloDecisionException():
    '''    public IloDecisionException(final String code)
    public IloDecisionException(final String code, final Object param)
    public IloDecisionException(final String code, final Object param1, final Object param2)
    public IloDecisionException(final String code, final Object[] params)
    public IloDecisionException(final Throwable e, final boolean keepStack)
    public IloDecisionException(final String code, final Object[] params, final Throwable e, final boolean keepStack)
    '''
def internalError():
    '''    public static IloDecisionException internalError()
    '''
def multipleParentError():
    '''    public static IloDecisionException multipleParentError(final String childName, final String newParent, final String oldParent)
    '''
def illegalContext():
    '''    public static IloDecisionException illegalContext()
    '''
def badParamValue():
    '''    public static IloDecisionException badParamValue(final int num, final Class<?> type)
    '''
def propertyNotSelected():
    '''    public static IloDecisionException propertyNotSelected(final String name, final Class<?> eltType)
    '''
def propertyNotFound():
    '''    public static IloDecisionException propertyNotFound(final String name, final Class<?> eltType)
    '''
def operationNotImplemented():
    '''    public static IloDecisionException operationNotImplemented(final String name)
    '''
def unknownConstraint():
    '''    public static IloDecisionException unknownConstraint(final String ctName)
    '''
def wrappedError():
    '''    public static IloDecisionException wrappedError(final Exception e)
    '''
def invalidGoalExpression():
    '''    public static IloDecisionException invalidGoalExpression(final String expressionName)
    '''
def modelContainsError():
    '''    public static IloDecisionException modelContainsError()
    '''
def postProcessErrors():
    '''    public static IloDecisionException postProcessErrors()
    '''
def parallelCplexNotSupported():
    '''    public static IloDecisionException parallelCplexNotSupported()
    '''
def getMessage():
    '''    public String getMessage()
    '''
def printStackTrace():
    '''    public void printStackTrace()
    public void printStackTrace(final PrintStream s)
    '''
