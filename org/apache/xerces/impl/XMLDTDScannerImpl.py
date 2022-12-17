def ():
    '''returns XMLDTDScannerImpl\n\n
    ()\n
    (final SymbolTable fSymbolTable, final XMLErrorReporter fErrorReporter, final XMLEntityManager fEntityManager)\n
    '''
def setInputSource():
    '''returns None\n\n
    setInputSource(final XMLInputSource xmlInputSource)\n
    '''
def scanDTDExternalSubset():
    '''returns boolean\n\n
    scanDTDExternalSubset(final boolean b)\n
    '''
def scanDTDInternalSubset():
    '''returns boolean\n\n
    scanDTDInternalSubset(final boolean b, final boolean fStandalone, final boolean b2)\n
    '''
def reset():
    '''returns None\n\n
    reset(final XMLComponentManager xmlComponentManager)\n
    reset()\n
    '''
def getRecognizedFeatures():
    '''returns String[]\n\n
    getRecognizedFeatures()\n
    '''
def getRecognizedProperties():
    '''returns String[]\n\n
    getRecognizedProperties()\n
    '''
def getFeatureDefault():
    '''returns Boolean\n\n
    getFeatureDefault(final String anObject)\n
    '''
def getPropertyDefault():
    '''returns Object\n\n
    getPropertyDefault(final String anObject)\n
    '''
def setDTDHandler():
    '''returns None\n\n
    setDTDHandler(final XMLDTDHandler fdtdHandler)\n
    '''
def getDTDHandler():
    '''returns XMLDTDHandler\n\n
    getDTDHandler()\n
    '''
def setDTDContentModelHandler():
    '''returns None\n\n
    setDTDContentModelHandler(final XMLDTDContentModelHandler fdtdContentModelHandler)\n
    '''
def getDTDContentModelHandler():
    '''returns XMLDTDContentModelHandler\n\n
    getDTDContentModelHandler()\n
    '''
def startEntity():
    '''returns None\n\n
    startEntity(final String s, final XMLResourceIdentifier xmlResourceIdentifier, final String s2, final Augmentations augmentations)\n
    '''
def endEntity():
    '''returns None\n\n
    endEntity(final String s, final Augmentations augmentations)\n
    '''
