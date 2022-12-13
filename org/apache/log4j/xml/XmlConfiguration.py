PARAM_TAG = "String  param""
LAYOUT_TAG = "String  layout""
NAME_ATTR = "String  name""
VALUE_ATTR = "String  value""
FILTER_TAG = "String  filter""
REF_ATTR = "String  ref""
DEFAULT_DELAY = "long  60000L"
def XmlConfiguration():
'''public XmlConfiguration(final LoggerContext loggerContext, final ConfigurationSource source, final int monitorIntervalSeconds)
'''
pass
def addAppenderIfAbsent():
'''public void addAppenderIfAbsent(final Appender appender)
'''
pass
def doConfigure():
'''public void doConfigure()
'''
pass
def parse():
'''public Document parse(final DocumentBuilder parser)
'''
pass
def toString():
'''public String toString()
'''
pass
def reconfigure():
'''public Configuration reconfigure()
'''
pass
def subst():
'''public String subst(final String value, final Properties props)
'''
pass
def setParameter():
'''public void setParameter(final Element elem, final PropertySetter propSetter, final Properties props)
'''
pass
def parseElement():
'''public Object parseElement(final Element element, final Properties props, final Class expectedClass)
'''
pass
def findAppenderByReference():
'''public Appender findAppenderByReference(final Element appenderRef)
'''
pass
def parseAppender():
'''public Appender parseAppender(final Element appenderElement)
'''
pass
def parseRewritePolicy():
'''public RewritePolicy parseRewritePolicy(final Element rewritePolicyElement)
'''
pass
def parseFilters():
'''public Filter parseFilters(final Element filterElement)
'''
pass
def parseLayout():
'''public Layout parseLayout(final Element layoutElement)
'''
pass
def forEachElement():
'''public static void forEachElement(final NodeList list, final Consumer<Element> consumer)
'''
pass
def error():
'''public void error(final SAXParseException ex)
'''
pass
def fatalError():
'''public void fatalError(final SAXParseException ex)
'''
pass
def warning():
'''public void warning(final SAXParseException ex)
'''
pass
