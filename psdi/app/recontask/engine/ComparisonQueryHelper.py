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
'''public ComparisonQueryHelper(final ReconInfo reconInfo)
'''
pass
def registerAttribute():
'''public ComparisonStatementHelper registerAttribute(final DataSet dS, final String fullyQualifiedName, final String unit, final int type)
'''
pass
def registerObjectForCount():
'''public ComparisonStatementHelper registerObjectForCount(final DataSet dS, final String fullyQualifiedName, final int type)
'''
pass
def getStatement():
'''public ComparisonStatementHelper getStatement(final String objectName)
'''
pass
def hasStatementsOfType():
'''public boolean hasStatementsOfType(final int type)
'''
pass
def getStatementsOfType():
'''public List getStatementsOfType(final int type)
'''
pass
def getAttributeMatchLeadingSideObjects():
'''public List getAttributeMatchLeadingSideObjects()
'''
pass
def reattachFilterResults():
'''public void reattachFilterResults(final ReconCompFilterReturn filterReturn1, final ReconCompFilterReturn filterReturn2)
'''
pass
def detachResults():
'''public List detachResults(final String objectName)
'''
pass
def attachOneResult():
'''public void attachOneResult(final String objectName, final ReconValue value)
'''
pass
def getMainStatement1():
'''public ComparisonStatementHelper getMainStatement1()
'''
pass
def getMainStatement2():
'''public ComparisonStatementHelper getMainStatement2()
'''
pass
def reset():
'''public void reset()
'''
pass
def setLinkValues():
'''public void setLinkValues(final Map linkValue1, final Map linkValue2)
'''
pass
