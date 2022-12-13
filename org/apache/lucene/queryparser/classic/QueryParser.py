DEFAULT_SPLIT_ON_WHITESPACE = "boolean  false"
def QueryParser():
'''public QueryParser(final String f, final Analyzer a)
'''
pass
def setAutoGeneratePhraseQueries():
'''public void setAutoGeneratePhraseQueries(final boolean value)
'''
pass
def getSplitOnWhitespace():
'''public boolean getSplitOnWhitespace()
'''
pass
def setSplitOnWhitespace():
'''public void setSplitOnWhitespace(final boolean splitOnWhitespace)
'''
pass
def Conjunction():
'''public final int Conjunction()
'''
pass
def Modifiers():
'''public final int Modifiers()
'''
pass
def TopLevelQuery():
'''public final Query TopLevelQuery(final String field)
'''
pass
def Query():
'''public final Query Query(final String field)
'''
pass
def Clause():
'''public final Query Clause(String field)
'''
pass
def Term():
'''public final Query Term(final String field)
'''
pass
def MultiTerm():
'''public final Query MultiTerm(final String field, final List<BooleanClause> clauses)
'''
pass
def ReInit():
'''public void ReInit(final CharStream stream)
public void ReInit(final QueryParserTokenManager tm)
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
