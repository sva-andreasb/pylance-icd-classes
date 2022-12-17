DEFAULT_NAMESPACE_PREFIX = "String  \"D\""
NO_NS_PREFIX = "String  \"N\""
def ():
    '''returns WrongEncodingException\n\n
    (final String name, final Reader reader, final Configuration cfg)\n
    (final String name, final String sourceCode, final Configuration cfg)\n
    (final String name, final Reader reader, final Configuration cfg, final String encoding)\n
    (final String name, final String sourceName, final Reader reader, final Configuration cfg)\n
    (final String name, final String sourceName, Reader reader, final Configuration cfg, final String encoding)\n
    (final String name, final Reader reader)\n
    (final String templateSpecifiedEncoding)\n
    (final String templateSpecifiedEncoding, final String constructorSpecifiedEncoding)\n
    '''
def process():
    '''returns None\n\n
    process(final Object dataModel, final Writer out)\n
    process(final Object dataModel, final Writer out, final ObjectWrapper wrapper, final TemplateNodeModel rootNode)\n
    process(final Object dataModel, final Writer out, final ObjectWrapper wrapper)\n
    '''
def createProcessingEnvironment():
    '''returns Environment\n\n
    createProcessingEnvironment(final Object dataModel, final Writer out, ObjectWrapper wrapper)\n
    createProcessingEnvironment(final Object dataModel, final Writer out)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getSourceName():
    '''returns String\n\n
    getSourceName()\n
    '''
def getConfiguration():
    '''returns Configuration\n\n
    getConfiguration()\n
    '''
def setEncoding():
    '''returns None\n\n
    setEncoding(final String encoding)\n
    '''
def getEncoding():
    '''returns String\n\n
    getEncoding()\n
    '''
def getCustomLookupCondition():
    '''returns Object\n\n
    getCustomLookupCondition()\n
    '''
def setCustomLookupCondition():
    '''returns None\n\n
    setCustomLookupCondition(final Object customLookupCondition)\n
    '''
def getActualTagSyntax():
    '''returns int\n\n
    getActualTagSyntax()\n
    '''
def dump():
    '''returns None\n\n
    dump(final PrintStream ps)\n
    dump(final Writer out)\n
    '''
def addMacro():
    '''returns None\n\n
    addMacro(final Macro macro)\n
    '''
def addImport():
    '''returns None\n\n
    addImport(final LibraryLoad ll)\n
    '''
def getSource():
    '''returns String\n\n
    getSource(int beginColumn, int beginLine, int endColumn, int endLine)\n
    '''
def getRootTreeNode():
    '''returns TemplateElement\n\n
    getRootTreeNode()\n
    '''
def getMacros():
    '''returns Map\n\n
    getMacros()\n
    '''
def getImports():
    '''returns List\n\n
    getImports()\n
    '''
def addPrefixNSMapping():
    '''returns None\n\n
    addPrefixNSMapping(final String prefix, final String nsURI)\n
    '''
def getDefaultNS():
    '''returns String\n\n
    getDefaultNS()\n
    '''
def getNamespaceForPrefix():
    '''returns String\n\n
    getNamespaceForPrefix(final String prefix)\n
    '''
def getPrefixForNamespace():
    '''returns String\n\n
    getPrefixForNamespace(final String nsURI)\n
    '''
def getPrefixedName():
    '''returns String\n\n
    getPrefixedName(final String localName, final String nsURI)\n
    '''
def containingElements():
    '''returns TreePath\n\n
    containingElements(final int column, final int line)\n
    '''
def read():
    '''returns int\n\n
    read()\n
    read(final char[] cbuf, final int off, final int len)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def getMessage():
    '''returns String\n\n
    getMessage()\n
    '''
def getTemplateSpecifiedEncoding():
    '''returns String\n\n
    getTemplateSpecifiedEncoding()\n
    '''
def getConstructorSpecifiedEncoding():
    '''returns String\n\n
    getConstructorSpecifiedEncoding()\n
    '''
