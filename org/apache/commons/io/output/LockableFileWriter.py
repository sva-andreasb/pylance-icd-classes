def ():
    '''returns LockableFileWriter\n\n
    (final String fileName)\n
    (final String fileName, final boolean append)\n
    (final String fileName, final boolean append, final String lockDir)\n
    (final File file)\n
    (final File file, final boolean append)\n
    (final File file, final boolean append, final String lockDir)\n
    (final File file, final Charset encoding)\n
    (final File file, final String encoding)\n
    (File file, final Charset encoding, final boolean append, String lockDir)\n
    (final File file, final String encoding, final boolean append, final String lockDir)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def write():
    '''returns None\n\n
    write(final int idx)\n
    write(final char[] chr)\n
    write(final char[] chr, final int st, final int end)\n
    write(final String str)\n
    write(final String str, final int st, final int end)\n
    '''
def flush():
    '''returns None\n\n
    flush()\n
    '''
