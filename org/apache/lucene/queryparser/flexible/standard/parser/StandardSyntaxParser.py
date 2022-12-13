def StandardSyntaxParser():
    '''    public StandardSyntaxParser()
    public StandardSyntaxParser(final CharStream stream)
    public StandardSyntaxParser(final StandardSyntaxParserTokenManager tm)
    '''
def parse():
    '''    public QueryNode parse(final CharSequence query, final CharSequence field)
    '''
def TopLevelQuery():
    '''    public final QueryNode TopLevelQuery(final CharSequence field)
    '''
def Query():
    '''    public final QueryNode Query(final CharSequence field)
    '''
def DisjQuery():
    '''    public final QueryNode DisjQuery(final CharSequence field)
    '''
def ConjQuery():
    '''    public final QueryNode ConjQuery(final CharSequence field)
    '''
def ModClause():
    '''    public final QueryNode ModClause(final CharSequence field)
    '''
def Clause():
    '''    public final QueryNode Clause(CharSequence field)
    '''
def Term():
    '''    public final QueryNode Term(final CharSequence field)
    '''
def ReInit():
    '''    public void ReInit(final CharStream stream)
    public void ReInit(final StandardSyntaxParserTokenManager tm)
    '''
def getNextToken():
    '''    public final Token getNextToken()
    '''
def getToken():
    '''    public final Token getToken(final int index)
    '''
def generateParseException():
    '''    public ParseException generateParseException()
    '''
def enable_tracing():
    '''    public final void enable_tracing()
    '''
def disable_tracing():
    '''    public final void disable_tracing()
    '''
