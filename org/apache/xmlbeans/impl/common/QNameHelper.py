MAX_NAME_LENGTH = "int  64"
URI_SHA1_PREFIX = "String  \"URI_SHA_1_\""
def getXMLName():
    '''public static XMLName getXMLName(final QName qname)
    '''
def forLNS():
    '''public static QName forLNS(final String localname, String uri)
    '''
def forLN():
    '''public static QName forLN(final String localname)
    '''
def forPretty():
    '''public static QName forPretty(final String pretty, final int offset)
    '''
def pretty():
    '''public static String pretty(final QName name)
    '''
def hexsafe():
    '''public static String hexsafe(final String s)
    '''
def hexsafedir():
    '''public static String hexsafedir(final QName name)
    '''
def readable():
    '''public static String readable(final SchemaType sType)
    public static String readable(final SchemaType sType, final Map nsPrefix)
    public static String readable(final QName name)
    public static String readable(final QName name, final Map prefixes)
    '''
def suggestPrefix():
    '''public static String suggestPrefix(final String namespace)
    '''
def namespace():
    '''public static String namespace(SchemaType sType)
    '''
def getLocalPart():
    '''public static String getLocalPart(final String qname)
    '''
def getPrefixPart():
    '''public static String getPrefixPart(final String qname)
    '''
