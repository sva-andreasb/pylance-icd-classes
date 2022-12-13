IMPORTANT_MASK = "short  1"
COMPUTED_MASK = "short  2"
NULL_CASCADED_MASK = "short  4"
INHERITED_MASK = "short  8"
LINE_HEIGHT_RELATIVE_MASK = "short  16"
FONT_SIZE_RELATIVE_MASK = "short  32"
COLOR_RELATIVE_MASK = "short  64"
PARENT_RELATIVE_MASK = "short  128"
BLOCK_WIDTH_RELATIVE_MASK = "short  256"
BLOCK_HEIGHT_RELATIVE_MASK = "short  512"
BOX_RELATIVE_MASK = "short  1024"
ORIGIN_MASK = "short  -8192"
USER_AGENT_ORIGIN = "short  0"
USER_ORIGIN = "short  8192"
NON_CSS_ORIGIN = "short  16384"
AUTHOR_ORIGIN = "short  24576"
INLINE_AUTHOR_ORIGIN = "short  Short.MIN_VALUE"
OVERRIDE_ORIGIN = "short  -24576"
def StyleMap():
    '''    public StyleMap(final int size)
    '''
def hasFixedCascadedValues():
    '''    public boolean hasFixedCascadedValues()
    '''
def setFixedCascadedStyle():
    '''    public void setFixedCascadedStyle(final boolean b)
    '''
def getValue():
    '''    public Value getValue(final int i)
    '''
def getMask():
    '''    public short getMask(final int i)
    '''
def isImportant():
    '''    public boolean isImportant(final int i)
    '''
def isComputed():
    '''    public boolean isComputed(final int i)
    '''
def isNullCascaded():
    '''    public boolean isNullCascaded(final int i)
    '''
def isInherited():
    '''    public boolean isInherited(final int i)
    '''
def getOrigin():
    '''    public short getOrigin(final int i)
    '''
def isColorRelative():
    '''    public boolean isColorRelative(final int i)
    '''
def isParentRelative():
    '''    public boolean isParentRelative(final int i)
    '''
def isLineHeightRelative():
    '''    public boolean isLineHeightRelative(final int i)
    '''
def isFontSizeRelative():
    '''    public boolean isFontSizeRelative(final int i)
    '''
def isBlockWidthRelative():
    '''    public boolean isBlockWidthRelative(final int i)
    '''
def isBlockHeightRelative():
    '''    public boolean isBlockHeightRelative(final int i)
    '''
def putValue():
    '''    public void putValue(final int i, final Value v)
    '''
def putMask():
    '''    public void putMask(final int i, final short m)
    '''
def putImportant():
    '''    public void putImportant(final int i, final boolean b)
    '''
def putOrigin():
    '''    public void putOrigin(final int i, final short val)
    '''
def putComputed():
    '''    public void putComputed(final int i, final boolean b)
    '''
def putNullCascaded():
    '''    public void putNullCascaded(final int i, final boolean b)
    '''
def putInherited():
    '''    public void putInherited(final int i, final boolean b)
    '''
def putColorRelative():
    '''    public void putColorRelative(final int i, final boolean b)
    '''
def putParentRelative():
    '''    public void putParentRelative(final int i, final boolean b)
    '''
def putLineHeightRelative():
    '''    public void putLineHeightRelative(final int i, final boolean b)
    '''
def putFontSizeRelative():
    '''    public void putFontSizeRelative(final int i, final boolean b)
    '''
def putBlockWidthRelative():
    '''    public void putBlockWidthRelative(final int i, final boolean b)
    '''
def putBlockHeightRelative():
    '''    public void putBlockHeightRelative(final int i, final boolean b)
    '''
def toString():
    '''    public String toString(final CSSEngine eng)
    '''
