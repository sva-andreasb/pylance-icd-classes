INVALID = "int  -1"
FILTER_DATASET1 = "int  0"
FILTER_DATASET2 = "int  1"
CARDINALITY_STATEMENT = "int  2"
CARDINALITY_STATEMENT_DATASET1 = "int  21"
CARDINALITY_STATEMENT_DATASET2 = "int  22"
ATTRIBUTE_EQUALITY_STATEMENT = "int  3"
ATTRIBUTE_EQUALITY_STATEMENT_DATASET1 = "int  31"
ATTRIBUTE_EQUALITY_STATEMENT_DATASET2 = "int  32"
STATEMENT_MAIN = "int  4"
def ():
    '''returns ComparisonQueryHelper\n\n
    (final ReconInfo reconInfo)\n
    '''
def registerAttribute():
    '''returns ComparisonStatementHelper\n\n
    registerAttribute(final DataSet dS, final String fullyQualifiedName, final String unit, final int type)\n
    '''
def registerObjectForCount():
    '''returns ComparisonStatementHelper\n\n
    registerObjectForCount(final DataSet dS, final String fullyQualifiedName, final int type)\n
    '''
def getStatement():
    '''returns ComparisonStatementHelper\n\n
    getStatement(final String objectName)\n
    '''
def hasStatementsOfType():
    '''returns boolean\n\n
    hasStatementsOfType(final int type)\n
    '''
def getStatementsOfType():
    '''returns List\n\n
    getStatementsOfType(final int type)\n
    '''
def getAttributeMatchLeadingSideObjects():
    '''returns List\n\n
    getAttributeMatchLeadingSideObjects()\n
    '''
def reattachFilterResults():
    '''returns None\n\n
    reattachFilterResults(final ReconCompFilterReturn filterReturn1, final ReconCompFilterReturn filterReturn2)\n
    '''
def detachResults():
    '''returns List\n\n
    detachResults(final String objectName)\n
    '''
def attachOneResult():
    '''returns None\n\n
    attachOneResult(final String objectName, final ReconValue value)\n
    '''
def getMainStatement1():
    '''returns ComparisonStatementHelper\n\n
    getMainStatement1()\n
    '''
def getMainStatement2():
    '''returns ComparisonStatementHelper\n\n
    getMainStatement2()\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
def setLinkValues():
    '''returns None\n\n
    setLinkValues(final Map linkValue1, final Map linkValue2)\n
    '''
