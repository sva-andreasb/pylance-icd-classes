DEFAULT_SHADOW_SYMBOL_TABLE = "boolean  false"
DEFAULT_SHADOW_GRAMMAR_POOL = "boolean  false"
def ():
    '''returns SynchronizedGrammarPool\n\n
    ()\n
    (final SymbolTable symbolTable, final XMLGrammarPool xmlGrammarPool)\n
    (final XMLGrammarPool fGrammarPool)\n
    (final XMLGrammarPool fGrammarPool)\n
    '''
def getSymbolTable():
    '''returns SymbolTable\n\n
    getSymbolTable()\n
    '''
def getXMLGrammarPool():
    '''returns XMLGrammarPool\n\n
    getXMLGrammarPool()\n
    '''
def setShadowSymbolTable():
    '''returns None\n\n
    setShadowSymbolTable(final boolean fShadowSymbolTable)\n
    '''
def createDOMParser():
    '''returns DOMParser\n\n
    createDOMParser()\n
    '''
def createSAXParser():
    '''returns SAXParser\n\n
    createSAXParser()\n
    '''
def retrieveInitialGrammarSet():
    '''returns Grammar[]\n\n
    retrieveInitialGrammarSet(final String s)\n
    retrieveInitialGrammarSet(final String s)\n
    '''
def retrieveGrammar():
    '''returns Grammar\n\n
    retrieveGrammar(final XMLGrammarDescription xmlGrammarDescription)\n
    retrieveGrammar(final XMLGrammarDescription xmlGrammarDescription)\n
    '''
def cacheGrammars():
    '''returns None\n\n
    cacheGrammars(final String s, final Grammar[] array)\n
    cacheGrammars(final String s, final Grammar[] array)\n
    '''
def getGrammar():
    '''returns Grammar\n\n
    getGrammar(final XMLGrammarDescription xmlGrammarDescription)\n
    '''
def containsGrammar():
    '''returns boolean\n\n
    containsGrammar(final XMLGrammarDescription xmlGrammarDescription)\n
    '''
def lockPool():
    '''returns None\n\n
    lockPool()\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def unlockPool():
    '''returns None\n\n
    unlockPool()\n
    '''
