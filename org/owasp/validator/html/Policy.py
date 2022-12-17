DEFAULT_MAX_INPUT_SIZE = "int  100000"
DEFAULT_MAX_STYLESHEET_IMPORTS = "int  1"
OMIT_XML_DECLARATION = "String  \"omitXmlDeclaration\""
OMIT_DOCTYPE_DECLARATION = "String  \"omitDoctypeDeclaration\""
USE_XHTML = "String  \"useXHTML\""
FORMAT_OUTPUT = "String  \"formatOutput\""
EMBED_STYLESHEETS = "String  \"embedStyleSheets\""
CONNECTION_TIMEOUT = "String  \"connectionTimeout\""
ANCHORS_NOFOLLOW = "String  \"nofollowAnchors\""
VALIDATE_PARAM_AS_EMBED = "String  \"validateParamAsEmbed\""
PRESERVE_SPACE = "String  \"preserveSpace\""
PRESERVE_COMMENTS = "String  \"preserveComments\""
ENTITY_ENCODE_INTL_CHARS = "String  \"entityEncodeIntlChars\""
ALLOW_DYNAMIC_ATTRIBUTES = "String  \"allowDynamicAttributes\""
EXTERNAL_GENERAL_ENTITIES = "String  \"http://xml.org/sax/features/external-general-entities\""
EXTERNAL_PARAM_ENTITIES = "String  \"http://xml.org/sax/features/external-parameter-entities\""
DISALLOW_DOCTYPE_DECL = "String  \"http://apache.org/xml/features/disallow-doctype-decl\""
LOAD_EXTERNAL_DTD = "String  \"http://apache.org/xml/features/nonvalidating/load-external-dtd\""
ACTION_VALIDATE = "String  \"validate\""
ACTION_FILTER = "String  \"filter\""
ACTION_TRUNCATE = "String  \"truncate\""
def getTagByLowercaseName():
    '''returns Tag\n\n
    getTagByLowercaseName(final String tagName)\n
    '''
def getPropertyByName():
    '''returns Property\n\n
    getPropertyByName(final String propertyName)\n
    '''
def cloneWithDirective():
    '''returns Policy\n\n
    cloneWithDirective(final String name, final String value)\n
    '''
def getGlobalAttributeByName():
    '''returns Attribute\n\n
    getGlobalAttributeByName(final String name)\n
    '''
def getDynamicAttributeByName():
    '''returns Attribute\n\n
    getDynamicAttributeByName(final String name)\n
    '''
def getAllowedEmptyTags():
    '''returns TagMatcher\n\n
    getAllowedEmptyTags()\n
    '''
def getRequiresClosingTags():
    '''returns TagMatcher\n\n
    getRequiresClosingTags()\n
    '''
def getDirective():
    '''returns String\n\n
    getDirective(final String name)\n
    '''
def iterator():
    '''returns Iterator<Element>\n\n
    iterator()\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    '''
def next():
    '''returns Element\n\n
    next()\n
    '''
def remove():
    '''returns None\n\n
    remove()\n
    '''
def getCommonRegularExpressions():
    '''returns AntiSamyPattern\n\n
    getCommonRegularExpressions(final String name)\n
    '''
def resetParamsWhereLastConfigWins():
    '''returns None\n\n
    resetParamsWhereLastConfigWins()\n
    '''
