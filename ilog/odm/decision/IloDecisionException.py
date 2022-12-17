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
def ():
    '''returns IloDecisionException\n\n
    (final String code)\n
    (final String code, final Object param)\n
    (final String code, final Object param1, final Object param2)\n
    (final String code, final Object[] params)\n
    (final Throwable e, final boolean keepStack)\n
    (final String code, final Object[] params, final Throwable e, final boolean keepStack)\n
    '''
def getMessage():
    '''returns String\n\n
    getMessage()\n
    '''
def printStackTrace():
    '''returns None\n\n
    printStackTrace()\n
    printStackTrace(final PrintStream s)\n
    '''
