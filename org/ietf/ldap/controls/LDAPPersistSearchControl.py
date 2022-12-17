ADD = "int  1"
DELETE = "int  2"
MODIFY = "int  4"
MODDN = "int  8"
ANY = "int  15"
def ():
    '''returns LDAPPersistSearchControl\n\n
    ()\n
    (final int changeTypes, final boolean changesOnly, final boolean returnControls, final boolean b)\n
    '''
def getChangeTypes():
    '''returns int\n\n
    getChangeTypes()\n
    '''
def setChangeTypes():
    '''returns None\n\n
    setChangeTypes(final int changeTypes)\n
    '''
def getReturnControls():
    '''returns boolean\n\n
    getReturnControls()\n
    '''
def setReturnControls():
    '''returns None\n\n
    setReturnControls(final boolean returnControls)\n
    '''
def getChangesOnly():
    '''returns boolean\n\n
    getChangesOnly()\n
    '''
def setChangesOnly():
    '''returns None\n\n
    setChangesOnly(final boolean changesOnly)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
