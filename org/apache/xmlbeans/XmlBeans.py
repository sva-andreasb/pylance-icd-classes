def getTitle():
'''public static final String getTitle()
'''
pass
def getVendor():
'''public static final String getVendor()
'''
pass
def getVersion():
'''public static final String getVersion()
'''
pass
def getQNameCache():
'''public static QNameCache getQNameCache()
'''
pass
def getQName():
'''public static QName getQName(final String localPart)
public static QName getQName(final String namespaceUri, final String localPart)
'''
pass
def compilePath():
'''public static String compilePath(final String pathExpr)
public static String compilePath(final String pathExpr, final XmlOptions options)
'''
pass
def compileQuery():
'''public static String compileQuery(final String queryExpr)
public static String compileQuery(final String queryExpr, final XmlOptions options)
'''
pass
def getContextTypeLoader():
'''public static SchemaTypeLoader getContextTypeLoader()
'''
pass
def getBuiltinTypeSystem():
'''public static SchemaTypeSystem getBuiltinTypeSystem()
'''
pass
def nodeToCursor():
'''public static XmlCursor nodeToCursor(final Node n)
'''
pass
def nodeToXmlObject():
'''public static XmlObject nodeToXmlObject(final Node n)
'''
pass
def nodeToXmlStreamReader():
'''public static XMLStreamReader nodeToXmlStreamReader(final Node n)
'''
pass
def streamToNode():
'''public static Node streamToNode(final XMLStreamReader xs)
'''
pass
def loadXsd():
'''public static SchemaTypeLoader loadXsd(final XmlObject[] schemas)
public static SchemaTypeLoader loadXsd(final XmlObject[] schemas, final XmlOptions options)
'''
pass
def compileXsd():
'''public static SchemaTypeSystem compileXsd(final XmlObject[] schemas, final SchemaTypeLoader typepath, final XmlOptions options)
public static SchemaTypeSystem compileXsd(final SchemaTypeSystem system, final XmlObject[] schemas, final SchemaTypeLoader typepath, final XmlOptions options)
'''
pass
def compileXmlBeans():
'''public static SchemaTypeSystem compileXmlBeans(final String name, final SchemaTypeSystem system, final XmlObject[] schemas, final BindingConfig config, final SchemaTypeLoader typepath, final Filer filer, final XmlOptions options)
'''
pass
def typeLoaderUnion():
'''public static SchemaTypeLoader typeLoaderUnion(final SchemaTypeLoader[] typeLoaders)
'''
pass
def typeLoaderForClassLoader():
'''public static SchemaTypeLoader typeLoaderForClassLoader(final ClassLoader loader)
'''
pass
def typeLoaderForResource():
'''public static SchemaTypeLoader typeLoaderForResource(final ResourceLoader resourceLoader)
'''
pass
def typeSystemForClassLoader():
'''public static SchemaTypeSystem typeSystemForClassLoader(final ClassLoader loader, final String stsName)
'''
pass
def resourceLoaderForPath():
'''public static ResourceLoader resourceLoaderForPath(final File[] path)
'''
pass
def typeForClass():
'''public static SchemaType typeForClass(final Class c)
'''
pass
