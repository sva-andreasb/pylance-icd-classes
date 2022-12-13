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
def ComparisonQueryHelper():
    '''    public ComparisonQueryHelper(final ReconInfo reconInfo)
    '''
def registerAttribute():
    '''    public ComparisonStatementHelper registerAttribute(final DataSet dS, final String fullyQualifiedName, final String unit, final int type)
    '''
def registerObjectForCount():
    '''    public ComparisonStatementHelper registerObjectForCount(final DataSet dS, final String fullyQualifiedName, final int type)
    '''
def getStatement():
    '''    public ComparisonStatementHelper getStatement(final String objectName)
    '''
def hasStatementsOfType():
    '''    public boolean hasStatementsOfType(final int type)
    '''
def getStatementsOfType():
    '''    public List getStatementsOfType(final int type)
    '''
def getAttributeMatchLeadingSideObjects():
    '''    public List getAttributeMatchLeadingSideObjects()
    '''
def reattachFilterResults():
    '''    public void reattachFilterResults(final ReconCompFilterReturn filterReturn1, final ReconCompFilterReturn filterReturn2)
    '''
def detachResults():
    '''    public List detachResults(final String objectName)
    '''
def attachOneResult():
    '''    public void attachOneResult(final String objectName, final ReconValue value)
    '''
def getMainStatement1():
    '''    public ComparisonStatementHelper getMainStatement1()
    '''
def getMainStatement2():
    '''    public ComparisonStatementHelper getMainStatement2()
    '''
def reset():
    '''    public void reset()
    '''
def setLinkValues():
    '''    public void setLinkValues(final Map linkValue1, final Map linkValue2)
    '''
