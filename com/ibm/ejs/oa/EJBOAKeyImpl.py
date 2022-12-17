HOME_BEAN = "byte  0"
STATELESS_BEAN = "byte  1"
STATEFUL_BEAN = "byte  2"
ENTITY_BEAN = "byte  3"
MESSAGEDRIVEN_BEAN = "byte  4"
USES_BEAN_MANAGED_TX = "byte  16"
def ():
    '''returns EJBOAKeyImpl\n\n
    (final byte[] servantkey)\n
    '''
def getJ2EENameBytes():
    '''returns byte[]\n\n
    getJ2EENameBytes()\n
    '''
def isBeanManagedTransaction():
    '''returns boolean\n\n
    isBeanManagedTransaction()\n
    '''
def getBeanType():
    '''returns byte\n\n
    getBeanType()\n
    '''
def isHome():
    '''returns boolean\n\n
    isHome()\n
    '''
def getPrimaryKeyBytes():
    '''returns byte[]\n\n
    getPrimaryKeyBytes()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
