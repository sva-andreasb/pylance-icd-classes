PARAM_TAG = "String  \"param\""
LAYOUT_TAG = "String  \"layout\""
NAME_ATTR = "String  \"name\""
VALUE_ATTR = "String  \"value\""
FILTER_TAG = "String  \"filter\""
REF_ATTR = "String  \"ref\""
DEFAULT_DELAY = "long  60000L"
def ():
    '''returns XmlConfiguration\n\n
    (final LoggerContext loggerContext, final ConfigurationSource source, final int monitorIntervalSeconds)\n
    '''
def addAppenderIfAbsent():
    '''returns None\n\n
    addAppenderIfAbsent(final Appender appender)\n
    '''
def doConfigure():
    '''returns None\n\n
    doConfigure()\n
    '''
def parse():
    '''returns Document\n\n
    parse(final DocumentBuilder parser)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def reconfigure():
    '''returns Configuration\n\n
    reconfigure()\n
    '''
def subst():
    '''returns String\n\n
    subst(final String value, final Properties props)\n
    '''
def setParameter():
    '''returns None\n\n
    setParameter(final Element elem, final PropertySetter propSetter, final Properties props)\n
    '''
def parseElement():
    '''returns Object\n\n
    parseElement(final Element element, final Properties props, final Class expectedClass)\n
    '''
def findAppenderByReference():
    '''returns Appender\n\n
    findAppenderByReference(final Element appenderRef)\n
    '''
def parseAppender():
    '''returns Appender\n\n
    parseAppender(final Element appenderElement)\n
    '''
def parseRewritePolicy():
    '''returns RewritePolicy\n\n
    parseRewritePolicy(final Element rewritePolicyElement)\n
    '''
def parseFilters():
    '''returns Filter\n\n
    parseFilters(final Element filterElement)\n
    '''
def parseLayout():
    '''returns Layout\n\n
    parseLayout(final Element layoutElement)\n
    '''
def error():
    '''returns None\n\n
    error(final SAXParseException ex)\n
    '''
def fatalError():
    '''returns None\n\n
    fatalError(final SAXParseException ex)\n
    '''
def warning():
    '''returns None\n\n
    warning(final SAXParseException ex)\n
    '''
