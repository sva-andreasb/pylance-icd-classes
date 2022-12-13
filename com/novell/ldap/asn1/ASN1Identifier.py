UNIVERSAL = "int  0"
APPLICATION = "int  1"
CONTEXT = "int  2"
PRIVATE = "int  3"
def ASN1Identifier():
    '''    public ASN1Identifier(final int tagClass, final boolean constructed, final int tag)
    public ASN1Identifier(final InputStream inputStream)
    public ASN1Identifier()
    '''
def reset():
    '''    public final void reset(final InputStream inputStream)
    '''
def getASN1Class():
    '''    public final int getASN1Class()
    '''
def getConstructed():
    '''    public final boolean getConstructed()
    '''
def getTag():
    '''    public final int getTag()
    '''
def getEncodedLength():
    '''    public final int getEncodedLength()
    '''
def isUniversal():
    '''    public final boolean isUniversal()
    '''
def isApplication():
    '''    public final boolean isApplication()
    '''
def isContext():
    '''    public final boolean isContext()
    '''
def isPrivate():
    '''    public final boolean isPrivate()
    '''
def clone():
    '''    public Object clone()
    '''
