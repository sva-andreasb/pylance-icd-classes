def ():
    '''returns CoreParser\n\n
    (final Analyzer analyzer, final QueryParser parser)\n
    (final String defaultField, final Analyzer analyzer)\n
    '''
def parse():
    '''returns Query\n\n
    parse(final InputStream xmlStream)\n
    '''
def addQueryBuilder():
    '''returns None\n\n
    addQueryBuilder(final String nodeName, final QueryBuilder builder)\n
    '''
def addSpanBuilder():
    '''returns None\n\n
    addSpanBuilder(final String nodeName, final SpanQueryBuilder builder)\n
    '''
def addSpanQueryBuilder():
    '''returns None\n\n
    addSpanQueryBuilder(final String nodeName, final SpanQueryBuilder builder)\n
    '''
def getQuery():
    '''returns Query\n\n
    getQuery(final Element e)\n
    '''
def getSpanQuery():
    '''returns SpanQuery\n\n
    getSpanQuery(final Element e)\n
    '''
