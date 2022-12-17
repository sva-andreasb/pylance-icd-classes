prefix = "String  \"Attr_\""
postfix = "String  \".att\""
def ():
    '''returns DiskAttribute\n\n
    (final String name)\n
    (final String name, final String baseDir, final boolean deleteOnExit)\n
    (final String name, final long definedSize)\n
    (final String name, final long definedSize, final String baseDir, final boolean deleteOnExit)\n
    (final String name, final Charset charset)\n
    (final String name, final Charset charset, final String baseDir, final boolean deleteOnExit)\n
    (final String name, final long definedSize, final Charset charset)\n
    (final String name, final long definedSize, final Charset charset, final String baseDir, final boolean deleteOnExit)\n
    (final String name, final String value)\n
    (final String name, final String value, final Charset charset)\n
    (final String name, final String value, final Charset charset, final String baseDir, final boolean deleteOnExit)\n
    '''
def getValue():
    '''returns String\n\n
    getValue()\n
    '''
def setValue():
    '''returns None\n\n
    setValue(final String value)\n
    '''
def addContent():
    '''returns None\n\n
    addContent(final ByteBuf buffer, final boolean last)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def compareTo():
    '''returns int\n\n
    compareTo(final InterfaceHttpData o)\n
    compareTo(final Attribute o)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def copy():
    '''returns Attribute\n\n
    copy()\n
    '''
def duplicate():
    '''returns Attribute\n\n
    duplicate()\n
    '''
def retainedDuplicate():
    '''returns Attribute\n\n
    retainedDuplicate()\n
    '''
def replace():
    '''returns Attribute\n\n
    replace(final ByteBuf content)\n
    '''
def retain():
    '''returns Attribute\n\n
    retain(final int increment)\n
    retain()\n
    '''
def touch():
    '''returns Attribute\n\n
    touch()\n
    touch(final Object hint)\n
    '''
