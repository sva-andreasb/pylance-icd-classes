PROPER_SUBSET = "int  1"
EQUAL = "int  2"
NO_SUBSET = "int  3"
SIGNED_APPLET_DBNAME = "int  4"
TEMP_FILENAME = "int  5"
def checkPrivilegeEnabled():
    '''returns None\n\n
    checkPrivilegeEnabled(final Target target)\n
    checkPrivilegeEnabled(final Target target, final Object o)\n
    '''
def enablePrivilege():
    '''returns None\n\n
    enablePrivilege(final Target target)\n
    enablePrivilege(final Target target, final Principal principal)\n
    enablePrivilege(final Target target, final Principal principal, final Object o)\n
    '''
def revertPrivilege():
    '''returns None\n\n
    revertPrivilege(final Target target)\n
    '''
def disablePrivilege():
    '''returns None\n\n
    disablePrivilege(final Target target)\n
    disablePrivilege(final String s)\n
    '''
def checkPrivilegeGranted():
    '''returns None\n\n
    checkPrivilegeGranted(final Target target)\n
    checkPrivilegeGranted(final Target target, final Object o)\n
    checkPrivilegeGranted(final Target target, final Principal principal, final Object o)\n
    '''
def isCalledByPrincipal():
    '''returns boolean\n\n
    isCalledByPrincipal(final Principal principal, final int n)\n
    isCalledByPrincipal(final Principal principal)\n
    '''
def hasPrincipal():
    '''returns boolean\n\n
    hasPrincipal(final Class clazz, final Principal principal)\n
    '''
def comparePrincipalArray():
    '''returns int\n\n
    comparePrincipalArray(final Principal[] array, final Principal[] array2)\n
    '''
def checkMatchPrincipal():
    '''returns boolean\n\n
    checkMatchPrincipal(final Class clazz, final int n)\n
    checkMatchPrincipal(final Principal principal, final int n)\n
    checkMatchPrincipal(final Class clazz)\n
    '''
def checkMatchPrincipalAlways():
    '''returns boolean\n\n
    checkMatchPrincipalAlways()\n
    '''
def getClassPrincipalsFromStack():
    '''returns Principal[]\n\n
    getClassPrincipalsFromStack(final int n)\n
    '''
def getPrivilegeTableFromStack():
    '''returns PrivilegeTable\n\n
    getPrivilegeTableFromStack()\n
    '''
