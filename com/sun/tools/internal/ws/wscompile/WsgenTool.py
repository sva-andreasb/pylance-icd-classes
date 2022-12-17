def ():
    '''returns WsgenTool\n\n
    (final OutputStream out, final Container container)\n
    (final OutputStream out)\n
    '''
def run():
    '''returns boolean\n\n
    run(final String[] args)\n
    '''
def buildModel():
    '''returns boolean\n\n
    buildModel(final String endpoint, final Listener listener)\n
    '''
def getWSDL():
    '''returns Result\n\n
    getWSDL(final String suggestedFilename)\n
    '''
def getSchemaOutput():
    '''returns Result\n\n
    getSchemaOutput(final String namespace, final String suggestedFilename)\n
    getSchemaOutput(final String namespace, final Holder<String> filename)\n
    '''
def getAbstractWSDL():
    '''returns Result\n\n
    getAbstractWSDL(final Holder<String> filename)\n
    '''
def generatedFile():
    '''returns None\n\n
    generatedFile(final String fileName)\n
    '''
def message():
    '''returns None\n\n
    message(final String msg)\n
    '''
def error():
    '''returns None\n\n
    error(final SAXParseException exception)\n
    '''
def fatalError():
    '''returns None\n\n
    fatalError(final SAXParseException exception)\n
    '''
def warning():
    '''returns None\n\n
    warning(final SAXParseException exception)\n
    '''
def info():
    '''returns None\n\n
    info(final SAXParseException exception)\n
    '''
