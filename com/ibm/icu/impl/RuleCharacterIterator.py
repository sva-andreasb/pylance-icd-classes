DONE = "int  -1"
PARSE_VARIABLES = "int  1"
PARSE_ESCAPES = "int  2"
SKIP_WHITESPACE = "int  4"
def RuleCharacterIterator():
    '''    public RuleCharacterIterator(final String text, final SymbolTable sym, final ParsePosition pos)
    '''
def atEnd():
    '''    public boolean atEnd()
    '''
def next():
    '''    public int next(final int options)
    '''
def isEscaped():
    '''    public boolean isEscaped()
    '''
def inVariable():
    '''    public boolean inVariable()
    '''
def getPos():
    '''    public Object getPos(final Object p)
    '''
def setPos():
    '''    public void setPos(final Object p)
    '''
def skipIgnored():
    '''    public void skipIgnored(final int options)
    '''
def lookahead():
    '''    public String lookahead()
    '''
def jumpahead():
    '''    public void jumpahead(final int count)
    '''
def toString():
    '''    public String toString()
    '''
