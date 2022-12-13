def StandardSyntaxParser():
'''public StandardSyntaxParser()
public StandardSyntaxParser(final CharStream stream)
public StandardSyntaxParser(final StandardSyntaxParserTokenManager tm)
'''
pass
def parse():
'''public QueryNode parse(final CharSequence query, final CharSequence field)
'''
pass
def TopLevelQuery():
'''public final QueryNode TopLevelQuery(final CharSequence field)
'''
pass
def Query():
'''public final QueryNode Query(final CharSequence field)
'''
pass
def DisjQuery():
'''public final QueryNode DisjQuery(final CharSequence field)
'''
pass
def ConjQuery():
'''public final QueryNode ConjQuery(final CharSequence field)
'''
pass
def ModClause():
'''public final QueryNode ModClause(final CharSequence field)
'''
pass
def Clause():
'''public final QueryNode Clause(CharSequence field)
'''
pass
def Term():
'''public final QueryNode Term(final CharSequence field)
'''
pass
def ReInit():
'''public void ReInit(final CharStream stream)
public void ReInit(final StandardSyntaxParserTokenManager tm)
'''
pass
def getNextToken():
'''public final Token getNextToken()
'''
pass
def getToken():
'''public final Token getToken(final int index)
'''
pass
def generateParseException():
'''public ParseException generateParseException()
'''
pass
def enable_tracing():
'''public final void enable_tracing()
'''
pass
def disable_tracing():
'''public final void disable_tracing()
'''
pass
