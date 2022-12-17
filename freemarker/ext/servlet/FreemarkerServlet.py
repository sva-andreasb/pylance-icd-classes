serialVersionUID = "long  -2440216393145762479L"
INIT_PARAM_TEMPLATE_PATH = "String  \"TemplatePath\""
INIT_PARAM_NO_CACHE = "String  \"NoCache\""
INIT_PARAM_CONTENT_TYPE = "String  \"ContentType\""
INIT_PARAM_BUFFER_SIZE = "String  \"BufferSize\""
INIT_PARAM_META_INF_TLD_LOCATIONS = "String  \"MetaInfTldSources\""
INIT_PARAM_EXCEPTION_ON_MISSING_TEMPLATE = "String  \"ExceptionOnMissingTemplate\""
INIT_PARAM_CLASSPATH_TLDS = "String  \"ClasspathTlds\""
SYSTEM_PROPERTY_META_INF_TLD_SOURCES = "String  \"org.freemarker.jsp.metaInfTldSources\""
SYSTEM_PROPERTY_CLASSPATH_TLDS = "String  \"org.freemarker.jsp.classpathTlds\""
META_INF_TLD_LOCATION_WEB_INF_PER_LIB_JARS = "String  \"webInfPerLibJars\""
META_INF_TLD_LOCATION_CLASSPATH = "String  \"classpath\""
META_INF_TLD_LOCATION_CLEAR = "String  \"clear\""
KEY_REQUEST = "String  \"Request\""
KEY_INCLUDE = "String  \"include_page\""
KEY_REQUEST_PRIVATE = "String  \"__FreeMarkerServlet.Request__\""
KEY_REQUEST_PARAMETERS = "String  \"RequestParameters\""
KEY_SESSION = "String  \"Session\""
KEY_APPLICATION = "String  \"Application\""
KEY_APPLICATION_PRIVATE = "String  \"__FreeMarkerServlet.Application__\""
KEY_JSP_TAGLIBS = "String  \"JspTaglibs\""
def ():
    '''returns InitParamValueException\n\n
    ()\n
    (final String initParamName, final String initParamValue, final String cause)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def doGet():
    '''returns None\n\n
    doGet(final HttpServletRequest request, final HttpServletResponse response)\n
    '''
def doPost():
    '''returns None\n\n
    doPost(final HttpServletRequest request, final HttpServletResponse response)\n
    '''
