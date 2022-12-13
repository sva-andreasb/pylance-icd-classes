FIRST_SPECIAL_CP = "int  1114112"
INITIAL_VALUE_CP = "int  1114112"
ERROR_VALUE_CP = "int  1114113"
MAX_CP = "int  1114113"
INITIAL_ROWS = "int  4096"
MEDIUM_ROWS = "int  65536"
MAX_ROWS = "int  1114114"
def PropsVectors():
    '''    public PropsVectors(final int numOfColumns)
    '''
def setValue():
    '''    public void setValue(final int start, final int end, int column, int value, int mask)
    '''
def getValue():
    '''    public int getValue(final int c, final int column)
    '''
def getRow():
    '''    public int[] getRow(final int rowIndex)
    '''
def getRowStart():
    '''    public int getRowStart(final int rowIndex)
    '''
def getRowEnd():
    '''    public int getRowEnd(final int rowIndex)
    '''
def compact():
    '''    public void compact(final CompactHandler compactor)
    '''
def compare():
    '''    public int compare(final Integer o1, final Integer o2)
    '''
def getCompactedArray():
    '''    public int[] getCompactedArray()
    '''
def getCompactedRows():
    '''    public int getCompactedRows()
    '''
def getCompactedColumns():
    '''    public int getCompactedColumns()
    '''
def compactToTrieWithRowIndexes():
    '''    public IntTrie compactToTrieWithRowIndexes()
    '''
def getFoldingOffset():
    '''    public int getFoldingOffset(final int value)
    '''
def DefaultGetFoldedValue():
    '''    public DefaultGetFoldedValue(final IntTrieBuilder inBuilder)
    '''
def getFoldedValue():
    '''    public int getFoldedValue(int start, final int offset)
    '''
