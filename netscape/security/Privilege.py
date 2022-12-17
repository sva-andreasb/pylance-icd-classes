N_PERMISSIONS = "int  15"
FORBIDDEN = "int  0"
ALLOWED = "int  1"
BLANK = "int  2"
N_DURATIONS = "int  240"
SCOPE = "int  16"
SESSION = "int  32"
FOREVER = "int  64"
def samePermission():
    '''returns boolean\n\n
    samePermission(final Privilege privilege)\n
    samePermission(final int n)\n
    '''
def sameDuration():
    '''returns boolean\n\n
    sameDuration(final Privilege privilege)\n
    sameDuration(final int n)\n
    '''
def isAllowed():
    '''returns boolean\n\n
    isAllowed()\n
    '''
def isForbidden():
    '''returns boolean\n\n
    isForbidden()\n
    '''
def isBlank():
    '''returns boolean\n\n
    isBlank()\n
    '''
def getPermission():
    '''returns int\n\n
    getPermission()\n
    '''
def getDuration():
    '''returns int\n\n
    getDuration()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
