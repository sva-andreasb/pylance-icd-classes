def getType():
    '''public static RDFDatatype getType(final String s)
    '''
def createAnon():
    '''public static Node createAnon()
    public static Node createAnon(final AnonId id)
    '''
def createLiteral():
    '''public static Node createLiteral(final LiteralLabel lit)
    public static Node createLiteral(final String value)
    public static Node createLiteral(final String lit, final String lang, final boolean isXml)
    public static Node createLiteral(final String lex, final String lang, final RDFDatatype dtype)
    '''
def createURI():
    '''public static Node createURI(final String uri)
    '''
def createVariable():
    '''public static Node createVariable(final String name)
    '''
def createUncachedLiteral():
    '''public static Node createUncachedLiteral(final Object value, final String lang, final RDFDatatype dtype)
    '''
def isLiteral():
    '''public boolean isLiteral()
    '''
def isBlank():
    '''public boolean isBlank()
    '''
def isURI():
    '''public boolean isURI()
    '''
def isVariable():
    '''public boolean isVariable()
    '''
def getBlankNodeId():
    '''public AnonId getBlankNodeId()
    '''
def getBlankNodeLabel():
    '''public String getBlankNodeLabel()
    '''
def getLiteral():
    '''public LiteralLabel getLiteral()
    '''
def getLiteralValue():
    '''public Object getLiteralValue()
    '''
def getLiteralLexicalForm():
    '''public String getLiteralLexicalForm()
    '''
def getLiteralLanguage():
    '''public String getLiteralLanguage()
    '''
def getLiteralDatatypeURI():
    '''public String getLiteralDatatypeURI()
    '''
def getLiteralDatatype():
    '''public RDFDatatype getLiteralDatatype()
    '''
def getLiteralIsXML():
    '''public boolean getLiteralIsXML()
    '''
def getIndexingValue():
    '''public Object getIndexingValue()
    '''
def getURI():
    '''public String getURI()
    '''
def getNameSpace():
    '''public String getNameSpace()
    '''
def getLocalName():
    '''public String getLocalName()
    '''
def getName():
    '''public String getName()
    '''
def hasURI():
    '''public boolean hasURI(final String uri)
    '''
def cache():
    '''public static void cache(final boolean wantCache)
    '''
def create():
    '''public static synchronized Node create(final NodeMaker maker, final Object label)
    '''
def sameValueAs():
    '''public boolean sameValueAs(final Object o)
    '''
def hashCode():
    '''public int hashCode()
    '''
def matches():
    '''public boolean matches(final Node other)
    '''
def toString():
    '''public String toString()
    public String toString(final boolean quoting)
    public String toString(final PrefixMapping pm)
    public String toString(final PrefixMapping pm, final boolean quoting)
    '''
def NotLiteral():
    '''public NotLiteral(final Node it)
    '''
