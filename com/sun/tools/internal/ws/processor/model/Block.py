UNBOUND = "int  0"
BODY = "int  1"
HEADER = "int  2"
ATTACHMENT = "int  3"
def ():
    '''returns Block\n\n
    (final QName name, final AbstractType type, final Entity entity)\n
    '''
def getName():
    '''returns QName\n\n
    getName()\n
    '''
def getType():
    '''returns AbstractType\n\n
    getType()\n
    '''
def setType():
    '''returns None\n\n
    setType(final AbstractType type)\n
    '''
def getLocation():
    '''returns int\n\n
    getLocation()\n
    '''
def setLocation():
    '''returns None\n\n
    setLocation(final int i)\n
    '''
def accept():
    '''returns None\n\n
    accept(final ModelVisitor visitor)\n
    '''
