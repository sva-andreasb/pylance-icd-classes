PARAM_TAG = "String  \"param\""
LAYOUT_TAG = "String  \"layout\""
NAME_ATTR = "String  \"name\""
VALUE_ATTR = "String  \"value\""
FILTER_TAG = "String  \"filter\""
REF_ATTR = "String  \"ref\""
DEFAULT_DELAY = "long  60000L"
def XmlConfiguration():
    '''public XmlConfiguration(final LoggerContext loggerContext, final ConfigurationSource source, final int monitorIntervalSeconds)
    '''
def addAppenderIfAbsent():
    '''public void addAppenderIfAbsent(final Appender appender)
    '''
def doConfigure():
    '''public void doConfigure()
    '''
def parse():
    '''public Document parse(final DocumentBuilder parser)
    '''
def toString():
    '''public String toString()
    '''
def reconfigure():
    '''public Configuration reconfigure()
    '''
def subst():
    '''public String subst(final String value, final Properties props)
    '''
def setParameter():
    '''public void setParameter(final Element elem, final PropertySetter propSetter, final Properties props)
    '''
def parseElement():
    '''public Object parseElement(final Element element, final Properties props, final Class expectedClass)
    '''
def findAppenderByReference():
    '''public Appender findAppenderByReference(final Element appenderRef)
    '''
def parseAppender():
    '''public Appender parseAppender(final Element appenderElement)
    '''
def parseRewritePolicy():
    '''public RewritePolicy parseRewritePolicy(final Element rewritePolicyElement)
    '''
def parseFilters():
    '''public Filter parseFilters(final Element filterElement)
    '''
def parseLayout():
    '''public Layout parseLayout(final Element layoutElement)
    '''
def forEachElement():
    '''public static void forEachElement(final NodeList list, final Consumer<Element> consumer)
    '''
def error():
    '''public void error(final SAXParseException ex)
    '''
def fatalError():
    '''public void fatalError(final SAXParseException ex)
    '''
def warning():
    '''public void warning(final SAXParseException ex)
    '''
