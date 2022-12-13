OP_EQUALS = "int  1"
OP_NOT_EQUALS = "int  2"
OP_STARTS_WITH = "int  3"
OP_ENDS_WITH = "int  4"
OP_CONTAINS = "int  5"
OP_REGEXP = "int  6"
OP_IS_NULL = "int  7"
OP_NOT_NULL = "int  8"
OP_EQ = "int  10"
OP_NEQ = "int  20"
OP_GT = "int  30"
OP_GE = "int  40"
OP_LT = "int  50"
OP_LE = "int  60"
OP_NOT = "int  100"
OP_LOWER = "int  200"
OP_UPPER = "int  300"
OP_OR = "int  1000"
OP_AND = "int  2000"
OP_ARRAY_CONTAINS = "int  10000"
OP_INSTANCEOF = "int  100000"
OP_NOOP = "int  0"
def QueryOp():
    '''public QueryOp(final int op, final String arrayClass)
    public QueryOp(final int op)
    '''
def getOp():
    '''public int getOp()
    '''
def getArrayClass():
    '''public String getArrayClass()
    '''
def toString():
    '''public String toString()
    '''
