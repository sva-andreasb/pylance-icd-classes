JAXRPC_METHOD_INFO = "String  \"jaxrpc.method.info\""
def getRoles():
    '''returns String[]\n\n
    getRoles()\n
    '''
def setRoles():
    '''returns None\n\n
    setRoles(final String[] roles)\n
    '''
def init():
    '''returns None\n\n
    init(final Map map)\n
    '''
def ():
    '''returns HandlerChainImpl\n\n
    ()\n
    (final List handlerInfos)\n
    '''
def addNewHandler():
    '''returns None\n\n
    addNewHandler(final String className, final Map config)\n
    '''
def handleFault():
    '''returns boolean\n\n
    handleFault(final MessageContext _context)\n
    '''
def getMessageInfo():
    '''returns ArrayList\n\n
    getMessageInfo(final SOAPMessage message)\n
    '''
def handleRequest():
    '''returns boolean\n\n
    handleRequest(final MessageContext _context)\n
    '''
def handleResponse():
    '''returns boolean\n\n
    handleResponse(final MessageContext context)\n
    '''
def destroy():
    '''returns None\n\n
    destroy()\n
    '''
