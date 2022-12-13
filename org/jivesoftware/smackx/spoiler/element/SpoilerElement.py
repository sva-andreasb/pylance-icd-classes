ELEMENT = "String  \"spoiler\""
NAMESPACE = "String  \"urn:xmpp:spoiler:0\""
def SpoilerElement():
    '''public SpoilerElement(final String language, final String hint)
    '''
def getHint():
    '''public String getHint()
    '''
def addSpoiler():
    '''public static void addSpoiler(final Message message)
    public static void addSpoiler(final Message message, final String hint)
    public static void addSpoiler(final Message message, final String lang, final String hint)
    '''
def containsSpoiler():
    '''public static boolean containsSpoiler(final Message message)
    '''
def getSpoilers():
    '''public static Map<String, String> getSpoilers(final Message message)
    '''
def getLanguage():
    '''public String getLanguage()
    '''
def getNamespace():
    '''public String getNamespace()
    '''
def getElementName():
    '''public String getElementName()
    '''
def toXML():
    '''public CharSequence toXML(final String enclosingNamespace)
    '''
