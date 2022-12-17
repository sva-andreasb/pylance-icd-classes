ANON_TOKEN = "String  \">\""
def ():
    '''returns SymbolTable\n\n
    (final BaseTypeMapping btm, final boolean addImports, final boolean verbose, final boolean nowrap)\n
    '''
def isQuiet():
    '''returns boolean\n\n
    isQuiet()\n
    '''
def setQuiet():
    '''returns None\n\n
    setQuiet(final boolean quiet)\n
    '''
def getHashMap():
    '''returns HashMap\n\n
    getHashMap()\n
    '''
def getSymbols():
    '''returns Vector\n\n
    getSymbols(final QName qname)\n
    '''
def get():
    '''returns SymTabEntry\n\n
    get(final QName qname, final Class cls)\n
    '''
def getTypeEntry():
    '''returns TypeEntry\n\n
    getTypeEntry(final QName qname, final boolean wantElementType)\n
    '''
def getType():
    '''returns Type\n\n
    getType(final QName qname)\n
    '''
def getElement():
    '''returns Element\n\n
    getElement(final QName qname)\n
    '''
def getMessageEntry():
    '''returns MessageEntry\n\n
    getMessageEntry(final QName qname)\n
    '''
def getPortTypeEntry():
    '''returns PortTypeEntry\n\n
    getPortTypeEntry(final QName qname)\n
    '''
def getBindingEntry():
    '''returns BindingEntry\n\n
    getBindingEntry(final QName qname)\n
    '''
def getServiceEntry():
    '''returns ServiceEntry\n\n
    getServiceEntry(final QName qname)\n
    '''
def getTypes():
    '''returns Vector\n\n
    getTypes()\n
    '''
def getElementIndex():
    '''returns Map\n\n
    getElementIndex()\n
    '''
def getTypeIndex():
    '''returns Map\n\n
    getTypeIndex()\n
    '''
def getTypeEntryCount():
    '''returns int\n\n
    getTypeEntryCount()\n
    '''
def getDefinition():
    '''returns Definition\n\n
    getDefinition()\n
    '''
def getWSDLURI():
    '''returns String\n\n
    getWSDLURI()\n
    '''
def isWrapped():
    '''returns boolean\n\n
    isWrapped()\n
    '''
def setWrapped():
    '''returns None\n\n
    setWrapped(final boolean wrapped)\n
    '''
def dump():
    '''returns None\n\n
    dump(final PrintStream out)\n
    '''
def populate():
    '''returns None\n\n
    populate(final String uri)\n
    populate(String uri, final String username, final String password)\n
    populate(final String context, final Document doc)\n
    '''
def isKnownNamespace():
    '''returns boolean\n\n
    isKnownNamespace(final String namespace)\n
    '''
def populateTypes():
    '''returns None\n\n
    populateTypes(final URL context, final Document doc)\n
    '''
def getOperationParameters():
    '''returns Parameters\n\n
    getOperationParameters(final Operation operation, final String namespace, final BindingEntry bindingEntry)\n
    '''
def getParametersFromParts():
    '''returns None\n\n
    getParametersFromParts(final Vector v, final Collection parts, final boolean literal, final String opName, final BindingEntry bindingEntry)\n
    '''
def getMessageEntries():
    '''returns List\n\n
    getMessageEntries()\n
    '''
def setWrapArrays():
    '''returns None\n\n
    setWrapArrays(final boolean wrapArrays)\n
    '''
def getElementFormDefaults():
    '''returns Map\n\n
    getElementFormDefaults()\n
    '''
