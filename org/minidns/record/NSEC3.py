FLAG_OPT_OUT = "byte  1"
def ():
    '''returns NSEC3\n\n
    (final byte hashAlgorithm, final byte flags, final int iterations, final byte[] salt, final byte[] nextHashed, final Record.TYPE[] types)\n
    '''
def serialize():
    '''returns None\n\n
    serialize(final DataOutputStream dos)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
