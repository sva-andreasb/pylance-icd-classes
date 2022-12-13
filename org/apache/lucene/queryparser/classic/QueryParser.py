DEFAULT_SPLIT_ON_WHITESPACE = "boolean  false"
def QueryParser():
    '''public QueryParser(final String f, final Analyzer a)
    '''
def setAutoGeneratePhraseQueries():
    '''public void setAutoGeneratePhraseQueries(final boolean value)
    '''
def getSplitOnWhitespace():
    '''public boolean getSplitOnWhitespace()
    '''
def setSplitOnWhitespace():
    '''public void setSplitOnWhitespace(final boolean splitOnWhitespace)
    '''
def Conjunction():
    '''public final int Conjunction()
    '''
def Modifiers():
    '''public final int Modifiers()
    '''
def TopLevelQuery():
    '''public final Query TopLevelQuery(final String field)
    '''
def Query():
    '''public final Query Query(final String field)
    '''
def Clause():
    '''public final Query Clause(String field)
    '''
def Term():
    '''public final Query Term(final String field)
    '''
def MultiTerm():
    '''public final Query MultiTerm(final String field, final List<BooleanClause> clauses)
    '''
def ReInit():
    '''public void ReInit(final CharStream stream)
    public void ReInit(final QueryParserTokenManager tm)
    '''
def getNextToken():
    '''public final Token getNextToken()
    '''
def getToken():
    '''public final Token getToken(final int index)
    '''
def generateParseException():
    '''public ParseException generateParseException()
    '''
def enable_tracing():
    '''public final void enable_tracing()
    '''
def disable_tracing():
    '''public final void disable_tracing()
    '''
