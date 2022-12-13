DEFAULT_EXTENSION_FIELD_DELIMITER = "char  ':'"
def Extensions():
    '''public Extensions()
    public Extensions(final char extensionFieldDelimiter)
    '''
def add():
    '''public void add(final String key, final ParserExtension extension)
    '''
def getExtension():
    '''public final ParserExtension getExtension(final String key)
    '''
def getExtensionFieldDelimiter():
    '''public char getExtensionFieldDelimiter()
    '''
def splitExtensionField():
    '''public Pair<String, String> splitExtensionField(final String defaultField, final String field)
    '''
def escapeExtensionField():
    '''public String escapeExtensionField(final String extfield)
    '''
def buildExtensionField():
    '''public String buildExtensionField(final String extensionKey)
    public String buildExtensionField(final String extensionKey, final String field)
    '''
def Pair():
    '''public Pair(final Cur cur, final Cud cud)
    '''
