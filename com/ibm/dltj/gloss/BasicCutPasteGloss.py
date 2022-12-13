DLT_CASE_CONV_NOCONV = "byte  0"
DLT_CASE_CONV_TOLOWER = "byte  1"
DLT_CASE_CONV_TOUPPER = "byte  2"
DLT_CASE_CONV_CAPITALIZE = "byte  3"
DLT_FUZZY_CASE_SS_IS_ONE_CHAR = "byte  1"
DLT_FUZZY_CASE_FIRST_CHAR_ONLY = "byte  2"
def read():
    '''public void read(final DataInputStream dataInputStream, int capacity)
    '''
def write():
    '''public void write(final DataOutputStream dataOutputStream, final GlossMapper glossMapper)
    '''
def getLemma():
    '''public void getLemma(final CharacterIterator characterIterator, final int index, final int n, final StringBuffer sb)
    public String getLemma(final CharacterIterator characterIterator, final int n, final int n2)
    public String getLemma(final String text)
    '''
def toString():
    '''public String toString(final String text)
    public String toString()
    '''
def equals():
    '''public boolean equals(final Object o)
    '''
def compareTo():
    '''public int compareTo(final BasicCutPasteGloss basicCutPasteGloss)
    '''
def hashCode():
    '''public int hashCode()
    '''
def getMinSourceLength():
    '''public int getMinSourceLength()
    '''
def getConv():
    '''public byte getConv()
    '''
def getCut():
    '''public short getCut()
    '''
def getOptions():
    '''public byte getOptions()
    '''
def process():
    '''public void process(final CharacterIterator characterIterator, final byte b, final StringBuffer sb)
    public void process(final CharacterIterator characterIterator, final byte b, final StringBuffer sb)
    public void process(final CharacterIterator characterIterator, final byte b, final StringBuffer sb)
    '''
