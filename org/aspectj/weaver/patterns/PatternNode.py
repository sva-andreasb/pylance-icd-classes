def ():
    '''returns PatternNode\n\n
    ()\n
    '''
def getStart():
    '''returns int\n\n
    getStart()\n
    '''
def getEnd():
    '''returns int\n\n
    getEnd()\n
    '''
def getSourceContext():
    '''returns ISourceContext\n\n
    getSourceContext()\n
    '''
def getFileName():
    '''returns String\n\n
    getFileName()\n
    '''
def setLocation():
    '''returns None\n\n
    setLocation(final ISourceContext sourceContext, final int start, final int end)\n
    '''
def copyLocationFrom():
    '''returns None\n\n
    copyLocationFrom(final PatternNode other)\n
    '''
def getSourceLocation():
    '''returns ISourceLocation\n\n
    getSourceLocation()\n
    '''
def writeLocation():
    '''returns None\n\n
    writeLocation(final DataOutputStream s)\n
    '''
def readLocation():
    '''returns None\n\n
    readLocation(final ISourceContext context, final DataInputStream s)\n
    '''
def traverse():
    '''returns Object\n\n
    traverse(final PatternNodeVisitor visitor, final Object data)\n
    '''
