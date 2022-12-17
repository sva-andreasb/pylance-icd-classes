staticFlag = "boolean  false"
def ():
    '''returns JavaCharStream\n\n
    (final Reader dstream, final int startline, final int startcolumn, final int buffersize)\n
    (final Reader dstream, final int startline, final int startcolumn)\n
    (final Reader dstream)\n
    (final InputStream dstream, final int startline, final int startcolumn, final int buffersize)\n
    (final InputStream dstream, final int startline, final int startcolumn)\n
    (final InputStream dstream)\n
    '''
def ReInit():
    '''returns None\n\n
    ReInit(final Reader dstream, final int startline, final int startcolumn, final int buffersize)\n
    ReInit(final Reader dstream, final int startline, final int startcolumn)\n
    ReInit(final Reader dstream)\n
    ReInit(final InputStream dstream, final int startline, final int startcolumn, final int buffersize)\n
    ReInit(final InputStream dstream, final int startline, final int startcolumn)\n
    ReInit(final InputStream dstream)\n
    '''
def Done():
    '''returns None\n\n
    Done()\n
    '''
def adjustBeginLineColumn():
    '''returns None\n\n
    adjustBeginLineColumn(int newLine, final int newCol)\n
    '''
