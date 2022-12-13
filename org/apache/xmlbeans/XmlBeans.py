def getTitle():
    '''public static final String getTitle()
    '''
def getVendor():
    '''public static final String getVendor()
    '''
def getVersion():
    '''public static final String getVersion()
    '''
def getQNameCache():
    '''public static QNameCache getQNameCache()
    '''
def getQName():
    '''public static QName getQName(final String localPart)
    public static QName getQName(final String namespaceUri, final String localPart)
    '''
def compilePath():
    '''public static String compilePath(final String pathExpr)
    public static String compilePath(final String pathExpr, final XmlOptions options)
    '''
def compileQuery():
    '''public static String compileQuery(final String queryExpr)
    public static String compileQuery(final String queryExpr, final XmlOptions options)
    '''
def getContextTypeLoader():
    '''public static SchemaTypeLoader getContextTypeLoader()
    '''
def getBuiltinTypeSystem():
    '''public static SchemaTypeSystem getBuiltinTypeSystem()
    '''
def nodeToCursor():
    '''public static XmlCursor nodeToCursor(final Node n)
    '''
def nodeToXmlObject():
    '''public static XmlObject nodeToXmlObject(final Node n)
    '''
def nodeToXmlStreamReader():
    '''public static XMLStreamReader nodeToXmlStreamReader(final Node n)
    '''
def streamToNode():
    '''public static Node streamToNode(final XMLStreamReader xs)
    '''
def loadXsd():
    '''public static SchemaTypeLoader loadXsd(final XmlObject[] schemas)
    public static SchemaTypeLoader loadXsd(final XmlObject[] schemas, final XmlOptions options)
    '''
def compileXsd():
    '''public static SchemaTypeSystem compileXsd(final XmlObject[] schemas, final SchemaTypeLoader typepath, final XmlOptions options)
    public static SchemaTypeSystem compileXsd(final SchemaTypeSystem system, final XmlObject[] schemas, final SchemaTypeLoader typepath, final XmlOptions options)
    '''
def compileXmlBeans():
    '''public static SchemaTypeSystem compileXmlBeans(final String name, final SchemaTypeSystem system, final XmlObject[] schemas, final BindingConfig config, final SchemaTypeLoader typepath, final Filer filer, final XmlOptions options)
    '''
def typeLoaderUnion():
    '''public static SchemaTypeLoader typeLoaderUnion(final SchemaTypeLoader[] typeLoaders)
    '''
def typeLoaderForClassLoader():
    '''public static SchemaTypeLoader typeLoaderForClassLoader(final ClassLoader loader)
    '''
def typeLoaderForResource():
    '''public static SchemaTypeLoader typeLoaderForResource(final ResourceLoader resourceLoader)
    '''
def typeSystemForClassLoader():
    '''public static SchemaTypeSystem typeSystemForClassLoader(final ClassLoader loader, final String stsName)
    '''
def resourceLoaderForPath():
    '''public static ResourceLoader resourceLoaderForPath(final File[] path)
    '''
def typeForClass():
    '''public static SchemaType typeForClass(final Class c)
    '''
