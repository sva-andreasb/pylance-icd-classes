def ():
    '''returns FieldGen\n\n
    (final int access_flags, final Type type, final String name, final ConstantPoolGen cp)\n
    (final Field field, final ConstantPoolGen cp)\n
    '''
def setInitValue():
    '''returns None\n\n
    setInitValue(final String str)\n
    setInitValue(final long l)\n
    setInitValue(final int i)\n
    setInitValue(final short s)\n
    setInitValue(final char c)\n
    setInitValue(final byte b)\n
    setInitValue(final boolean b)\n
    setInitValue(final float f)\n
    setInitValue(final double d)\n
    '''
def cancelInitValue():
    '''returns None\n\n
    cancelInitValue()\n
    '''
def getField():
    '''returns Field\n\n
    getField()\n
    '''
def getSignature():
    '''returns String\n\n
    getSignature()\n
    '''
def addObserver():
    '''returns None\n\n
    addObserver(final FieldObserver o)\n
    '''
def removeObserver():
    '''returns None\n\n
    removeObserver(final FieldObserver o)\n
    '''
def update():
    '''returns None\n\n
    update()\n
    '''
def getInitValue():
    '''returns String\n\n
    getInitValue()\n
    '''
def copy():
    '''returns FieldGen\n\n
    copy(final ConstantPoolGen cp)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    equals(final Object o1, final Object o2)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    hashCode(final Object o)\n
    '''
