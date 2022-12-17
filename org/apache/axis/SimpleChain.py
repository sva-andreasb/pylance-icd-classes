def ():
    '''returns SimpleChain\n\n
    ()\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def cleanup():
    '''returns None\n\n
    cleanup()\n
    '''
def invoke():
    '''returns None\n\n
    invoke(final MessageContext msgContext)\n
    '''
def generateWSDL():
    '''returns None\n\n
    generateWSDL(final MessageContext msgContext)\n
    '''
def onFault():
    '''returns None\n\n
    onFault(final MessageContext msgContext)\n
    '''
def canHandleBlock():
    '''returns boolean\n\n
    canHandleBlock(final QName qname)\n
    '''
def addHandler():
    '''returns None\n\n
    addHandler(final Handler handler)\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final Handler handler)\n
    '''
def getHandlers():
    '''returns Handler[]\n\n
    getHandlers()\n
    '''
def getDeploymentData():
    '''returns Element\n\n
    getDeploymentData(final Document doc)\n
    '''
