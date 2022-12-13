DEFAULT_MAX_INPUT_SIZE = "int  100000"
DEFAULT_MAX_STYLESHEET_IMPORTS = "int  1"
OMIT_XML_DECLARATION = "String  omitXmlDeclaration""
OMIT_DOCTYPE_DECLARATION = "String  omitDoctypeDeclaration""
USE_XHTML = "String  useXHTML""
FORMAT_OUTPUT = "String  formatOutput""
EMBED_STYLESHEETS = "String  embedStyleSheets""
CONNECTION_TIMEOUT = "String  connectionTimeout""
ANCHORS_NOFOLLOW = "String  nofollowAnchors""
VALIDATE_PARAM_AS_EMBED = "String  validateParamAsEmbed""
PRESERVE_SPACE = "String  preserveSpace""
PRESERVE_COMMENTS = "String  preserveComments""
ENTITY_ENCODE_INTL_CHARS = "String  entityEncodeIntlChars""
ALLOW_DYNAMIC_ATTRIBUTES = "String  allowDynamicAttributes""
EXTERNAL_GENERAL_ENTITIES = "String  http://xml.org/sax/features/external-general-entities""
EXTERNAL_PARAM_ENTITIES = "String  http://xml.org/sax/features/external-parameter-entities""
DISALLOW_DOCTYPE_DECL = "String  http://apache.org/xml/features/disallow-doctype-decl""
LOAD_EXTERNAL_DTD = "String  http://apache.org/xml/features/nonvalidating/load-external-dtd""
ACTION_VALIDATE = "String  validate""
ACTION_FILTER = "String  filter""
ACTION_TRUNCATE = "String  truncate""
def getTagByLowercaseName():
'''public Tag getTagByLowercaseName(final String tagName)
'''
pass
def getPropertyByName():
'''public Property getPropertyByName(final String propertyName)
'''
pass
def getInstance():
'''public static Policy getInstance()
public static Policy getInstance(final String filename)
public static Policy getInstance(final InputStream inputStream)
public static Policy getInstance(final File file)
public static Policy getInstance(final URL url)
'''
pass
def cloneWithDirective():
'''public Policy cloneWithDirective(final String name, final String value)
'''
pass
def getGlobalAttributeByName():
'''public Attribute getGlobalAttributeByName(final String name)
'''
pass
def getDynamicAttributeByName():
'''public Attribute getDynamicAttributeByName(final String name)
'''
pass
def getAllowedEmptyTags():
'''public TagMatcher getAllowedEmptyTags()
'''
pass
def getRequiresClosingTags():
'''public TagMatcher getRequiresClosingTags()
'''
pass
def getDirective():
'''public String getDirective(final String name)
'''
pass
def resolveEntity():
'''public static InputSource resolveEntity(final String systemId, final URL baseUrl)
'''
pass
def iterator():
'''public Iterator<Element> iterator()
'''
pass
def hasNext():
'''public boolean hasNext()
'''
pass
def next():
'''public Element next()
'''
pass
def remove():
'''public void remove()
'''
pass
def getCommonRegularExpressions():
'''public AntiSamyPattern getCommonRegularExpressions(final String name)
'''
pass
def resetParamsWhereLastConfigWins():
'''public void resetParamsWhereLastConfigWins()
'''
pass
