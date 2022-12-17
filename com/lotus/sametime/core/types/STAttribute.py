def ():
    '''returns STAttribute\n\n
    (final int key, final byte[] val)\n
    (final int key, final String str)\n
    (final int key, final int v)\n
    (final int key, final long v)\n
    (final int key, final boolean v)\n
    (final NdrInputStream ndrInputStream)\n
    '''
def dump():
    '''returns None\n\n
    dump(final NdrOutputStream ndrOutputStream)\n
    dump(final NdrOutputStream ndrOutputStream, final boolean b)\n
    '''
def load():
    '''returns None\n\n
    load(final NdrInputStream ndrInputStream, final boolean b)\n
    '''
def getKey():
    '''returns int\n\n
    getKey()\n
    '''
def getValue():
    '''returns byte[]\n\n
    getValue()\n
    '''
def getInt():
    '''returns int\n\n
    getInt()\n
    '''
def getLong():
    '''returns long\n\n
    getLong()\n
    '''
def getString():
    '''returns String\n\n
    getString()\n
    '''
def getBoolean():
    '''returns boolean\n\n
    getBoolean()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty()\n
    '''
