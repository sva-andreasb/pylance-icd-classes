def ():
    '''returns Bindings\n\n
    (final BindingPattern[] bindings)\n
    (final int count)\n
    '''
def register():
    '''returns None\n\n
    register(final BindingPattern binding, final IScope scope)\n
    '''
def mergeIn():
    '''returns None\n\n
    mergeIn(final Bindings other, final IScope scope)\n
    '''
def checkEquals():
    '''returns None\n\n
    checkEquals(final Bindings other, final IScope scope)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getUsedFormals():
    '''returns int[]\n\n
    getUsedFormals()\n
    '''
def getUsedFormalTypes():
    '''returns UnresolvedType[]\n\n
    getUsedFormalTypes()\n
    '''
def copy():
    '''returns Bindings\n\n
    copy()\n
    '''
def checkAllBound():
    '''returns None\n\n
    checkAllBound(final IScope scope)\n
    '''
def size():
    '''returns int\n\n
    size()\n
    '''
