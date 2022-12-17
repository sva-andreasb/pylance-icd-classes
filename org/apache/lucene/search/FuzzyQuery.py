defaultMaxEdits = "int  2"
defaultPrefixLength = "int  0"
defaultMaxExpansions = "int  50"
defaultTranspositions = "boolean  true"
defaultMinSimilarity = "float  2.0f"
def ():
    '''returns FuzzyQuery\n\n
    (final Term term, final int maxEdits, final int prefixLength, final int maxExpansions, final boolean transpositions)\n
    (final Term term, final int maxEdits, final int prefixLength)\n
    (final Term term, final int maxEdits)\n
    (final Term term)\n
    '''
def getMaxEdits():
    '''returns int\n\n
    getMaxEdits()\n
    '''
def getPrefixLength():
    '''returns int\n\n
    getPrefixLength()\n
    '''
def getTranspositions():
    '''returns boolean\n\n
    getTranspositions()\n
    '''
def getAutomata():
    '''returns CompiledAutomaton\n\n
    getAutomata()\n
    '''
def visit():
    '''returns None\n\n
    visit(final QueryVisitor visitor)\n
    '''
def getTerm():
    '''returns Term\n\n
    getTerm()\n
    '''
def toString():
    '''returns String\n\n
    toString(final String field)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
