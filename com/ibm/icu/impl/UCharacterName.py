LINES_PER_GROUP_ = "int  32"
def getName():
    '''public String getName(final int ch, final int choice)
    '''
def getCharFromName():
    '''public int getCharFromName(final int choice, final String name)
    '''
def getGroupLengths():
    '''public int getGroupLengths(int index, final char[] offsets, final char[] lengths)
    '''
def getGroupName():
    '''public String getGroupName(int index, int length, final int choice)
    public synchronized String getGroupName(final int ch, final int choice)
    '''
def getExtendedName():
    '''public String getExtendedName(final int ch)
    '''
def getGroup():
    '''public int getGroup(final int codepoint)
    '''
def getExtendedOr10Name():
    '''public String getExtendedOr10Name(final int ch)
    '''
def getGroupMSB():
    '''public int getGroupMSB(final int gindex)
    '''
def getCodepointMSB():
    '''public static int getCodepointMSB(final int codepoint)
    '''
def getGroupLimit():
    '''public static int getGroupLimit(final int msb)
    '''
def getGroupMin():
    '''public static int getGroupMin(final int msb)
    '''
def getGroupOffset():
    '''public static int getGroupOffset(final int codepoint)
    '''
def getGroupMinFromCodepoint():
    '''public static int getGroupMinFromCodepoint(final int codepoint)
    '''
def getAlgorithmLength():
    '''public int getAlgorithmLength()
    '''
def getAlgorithmStart():
    '''public int getAlgorithmStart(final int index)
    '''
def getAlgorithmEnd():
    '''public int getAlgorithmEnd(final int index)
    '''
def getAlgorithmName():
    '''public String getAlgorithmName(final int index, final int codepoint)
    '''
def getMaxCharNameLength():
    '''public int getMaxCharNameLength()
    '''
def getMaxISOCommentLength():
    '''public int getMaxISOCommentLength()
    '''
def getCharNameCharacters():
    '''public void getCharNameCharacters(final UnicodeSet set)
    '''
def getISOCommentCharacters():
    '''public void getISOCommentCharacters(final UnicodeSet set)
    '''
