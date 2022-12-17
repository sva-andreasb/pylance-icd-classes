GET_CONSTANT = "byte  1"
GET_VARIABLE = "byte  2"
UNIFY_VARIABLE = "byte  3"
GET_TEMP = "byte  4"
UNIFY_TEMP = "byte  18"
PUT_CONSTANT = "byte  5"
PUT_NEW_VARIABLE = "byte  6"
PUT_VARIABLE = "byte  7"
PUT_DEREF_VARIABLE = "byte  20"
PUT_TEMP = "byte  8"
CALL_PREDICATE = "byte  9"
GET_FUNCTOR = "byte  10"
CALL_PREDICATE_INDEX = "byte  23"
CALL_TRIPLE_MATCH = "byte  17"
LAST_CALL_PREDICATE = "byte  19"
CALL_TABLED = "byte  24"
CALL_WILD_TABLED = "byte  25"
PROCEED = "byte  11"
MAKE_FUNCTOR = "byte  12"
CALL_BUILTIN = "byte  13"
CLEAR_VARIABLE = "byte  14"
CLEAR_TEMP = "byte  15"
CLEAR_ARG = "byte  16"
ALLOCATE = "byte  22"
TEST_BOUND = "byte  32"
TEST_UNBOUND = "byte  33"
MAX_PERMANENT_VARS = "int  15"
MAX_ARGUMENT_VARS = "int  8"
MAX_TEMPORARY_VARS = "int  8"
def ():
    '''returns RuleClauseCodeList\n\n
    (final Rule rule)\n
    (final List<RuleClauseCode> list)\n
    '''
def getCode():
    '''returns byte[]\n\n
    getCode()\n
    '''
def getArgs():
    '''returns Object[]\n\n
    getArgs()\n
    '''
def getRule():
    '''returns Rule\n\n
    getRule()\n
    '''
def compile():
    '''returns None\n\n
    compile(final LPRuleStore ruleStore)\n
    '''
def termIndex():
    '''returns int\n\n
    termIndex(final int pc)\n
    '''
def print():
    '''returns None\n\n
    print(final PrintStream out)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
