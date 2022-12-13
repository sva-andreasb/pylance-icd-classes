def getType():
'''public static RDFDatatype getType(final String s)
'''
pass
def createAnon():
'''public static Node createAnon()
public static Node createAnon(final AnonId id)
'''
pass
def createLiteral():
'''public static Node createLiteral(final LiteralLabel lit)
public static Node createLiteral(final String value)
public static Node createLiteral(final String lit, final String lang, final boolean isXml)
public static Node createLiteral(final String lex, final String lang, final RDFDatatype dtype)
'''
pass
def createURI():
'''public static Node createURI(final String uri)
'''
pass
def createVariable():
'''public static Node createVariable(final String name)
'''
pass
def createUncachedLiteral():
'''public static Node createUncachedLiteral(final Object value, final String lang, final RDFDatatype dtype)
'''
pass
def isLiteral():
'''public boolean isLiteral()
'''
pass
def isBlank():
'''public boolean isBlank()
'''
pass
def isURI():
'''public boolean isURI()
'''
pass
def isVariable():
'''public boolean isVariable()
'''
pass
def getBlankNodeId():
'''public AnonId getBlankNodeId()
'''
pass
def getBlankNodeLabel():
'''public String getBlankNodeLabel()
'''
pass
def getLiteral():
'''public LiteralLabel getLiteral()
'''
pass
def getLiteralValue():
'''public Object getLiteralValue()
'''
pass
def getLiteralLexicalForm():
'''public String getLiteralLexicalForm()
'''
pass
def getLiteralLanguage():
'''public String getLiteralLanguage()
'''
pass
def getLiteralDatatypeURI():
'''public String getLiteralDatatypeURI()
'''
pass
def getLiteralDatatype():
'''public RDFDatatype getLiteralDatatype()
'''
pass
def getLiteralIsXML():
'''public boolean getLiteralIsXML()
'''
pass
def getIndexingValue():
'''public Object getIndexingValue()
'''
pass
def getURI():
'''public String getURI()
'''
pass
def getNameSpace():
'''public String getNameSpace()
'''
pass
def getLocalName():
'''public String getLocalName()
'''
pass
def getName():
'''public String getName()
'''
pass
def hasURI():
'''public boolean hasURI(final String uri)
'''
pass
def cache():
'''public static void cache(final boolean wantCache)
'''
pass
def create():
'''public static synchronized Node create(final NodeMaker maker, final Object label)
'''
pass
def sameValueAs():
'''public boolean sameValueAs(final Object o)
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
def matches():
'''public boolean matches(final Node other)
'''
pass
def toString():
'''public String toString()
public String toString(final boolean quoting)
public String toString(final PrefixMapping pm)
public String toString(final PrefixMapping pm, final boolean quoting)
'''
pass
def NotLiteral():
'''public NotLiteral(final Node it)
'''
pass
