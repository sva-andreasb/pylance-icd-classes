def ():
    '''returns FileWriterWithEncoding\n\n
    (final String filename, final String encoding)\n
    (final String filename, final String encoding, final boolean append)\n
    (final String filename, final Charset encoding)\n
    (final String filename, final Charset encoding, final boolean append)\n
    (final String filename, final CharsetEncoder encoding)\n
    (final String filename, final CharsetEncoder encoding, final boolean append)\n
    (final File file, final String encoding)\n
    (final File file, final String encoding, final boolean append)\n
    (final File file, final Charset encoding)\n
    (final File file, final Charset encoding, final boolean append)\n
    (final File file, final CharsetEncoder encoding)\n
    (final File file, final CharsetEncoder encoding, final boolean append)\n
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
def close():
    '''returns None\n\n
    close()\n
    '''
