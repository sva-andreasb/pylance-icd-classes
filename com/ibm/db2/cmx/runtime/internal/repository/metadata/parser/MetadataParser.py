def ():
    '''returns StatementInfo\n\n
    ()\n
    (final String expression, final String sql, final String processedSql, final HashMap<Constants.SourceOpType, List<List<SourceInfo>>> sourceInfoMap, final boolean isBindable, final char expressionType, final char queryTextType, final int sectionNumber, final String id, final Integer executionCount, final String lastUsedTimestamp, final String incrementalSpecialRegValuesUsed)\n
    '''
def parse():
    '''returns None\n\n
    parse(final InputStream is, final MetadataListener listener, final boolean insertOnly)\n
    '''
def startDocument():
    '''returns None\n\n
    startDocument()\n
    '''
def startElement():
    '''returns None\n\n
    startElement(final String s, final String s2, final String queryNameType, final Attributes attributes)\n
    '''
def characters():
    '''returns None\n\n
    characters(final char[] str, final int offset, final int len)\n
    '''
def endElement():
    '''returns None\n\n
    endElement(final String s, final String s2, final String s3)\n
    '''
def getExpression():
    '''returns String\n\n
    getExpression()\n
    '''
def getSql():
    '''returns String\n\n
    getSql()\n
    '''
def getProcessedSql():
    '''returns String\n\n
    getProcessedSql()\n
    '''
def isBindable():
    '''returns boolean\n\n
    isBindable()\n
    '''
def getExpressionType():
    '''returns char\n\n
    getExpressionType()\n
    '''
def getQueryTextType():
    '''returns char\n\n
    getQueryTextType()\n
    '''
def getSectionNumber():
    '''returns int\n\n
    getSectionNumber()\n
    '''
def setSectionNumber():
    '''returns None\n\n
    setSectionNumber(final int sectionNumber)\n
    '''
def getId():
    '''returns String\n\n
    getId()\n
    '''
def getExecutionCount():
    '''returns Integer\n\n
    getExecutionCount()\n
    '''
def getLastUsedTimestamp():
    '''returns String\n\n
    getLastUsedTimestamp()\n
    '''
def getIncrementalSpecialRegValuesUsed():
    '''returns String\n\n
    getIncrementalSpecialRegValuesUsed()\n
    '''
