ENTITY_RESOLVER = "String  \"http://apache.org/xml/properties/internal/entity-resolver\""
ERROR_REPORTER = "String  \"http://apache.org/xml/properties/internal/error-reporter\""
XMLGRAMMAR_POOL = "String  \"http://apache.org/xml/properties/internal/grammar-pool\""
SYMBOL_TABLE = "String  \"http://apache.org/xml/properties/internal/symbol-table\""
REDEF_IDENTIFIER = "String  \"_fn3dktizrknc9pi\""
def ():
    '''returns XSDHandler\n\n
    ()\n
    (final XSGrammarBucket fGrammarBucket)\n
    '''
def parseSchema():
    '''returns SchemaGrammar\n\n
    parseSchema(final XMLInputSource xmlInputSource, final XSDDescription xsdDescription, final Hashtable fLocationPairs)\n
    '''
def schemaDocument2SystemId():
    '''returns String\n\n
    schemaDocument2SystemId(final XSDocumentInfo xsDocumentInfo)\n
    '''
def setDeclPool():
    '''returns None\n\n
    setDeclPool(final XSDeclarationPool fDeclPool)\n
    '''
def setDVFactory():
    '''returns None\n\n
    setDVFactory(final SchemaDVFactory fdvFactory)\n
    '''
def reset():
    '''returns None\n\n
    reset(final XMLComponentManager xmlComponentManager)\n
    '''
def element2Locator():
    '''returns boolean\n\n
    element2Locator(final Element element)\n
    element2Locator(final Element element, final SimpleLocator simpleLocator)\n
    '''
def setGenerateSyntheticAnnotations():
    '''returns None\n\n
    setGenerateSyntheticAnnotations(final boolean b)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def retrieveInitialGrammarSet():
    '''returns Grammar[]\n\n
    retrieveInitialGrammarSet(final String s)\n
    '''
def cacheGrammars():
    '''returns None\n\n
    cacheGrammars(final String s, final Grammar[] array)\n
    '''
def retrieveGrammar():
    '''returns Grammar\n\n
    retrieveGrammar(final XMLGrammarDescription xmlGrammarDescription)\n
    '''
def refreshGrammars():
    '''returns None\n\n
    refreshGrammars(final XSGrammarBucket fGrammarBucket)\n
    '''
def lockPool():
    '''returns None\n\n
    lockPool()\n
    '''
def unlockPool():
    '''returns None\n\n
    unlockPool()\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
