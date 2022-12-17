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
def ():
    '''returns StyleMap\n\n
    (final int size)\n
    '''
def hasFixedCascadedValues():
    '''returns boolean\n\n
    hasFixedCascadedValues()\n
    '''
def setFixedCascadedStyle():
    '''returns None\n\n
    setFixedCascadedStyle(final boolean b)\n
    '''
def getValue():
    '''returns Value\n\n
    getValue(final int i)\n
    '''
def getMask():
    '''returns short\n\n
    getMask(final int i)\n
    '''
def isImportant():
    '''returns boolean\n\n
    isImportant(final int i)\n
    '''
def isComputed():
    '''returns boolean\n\n
    isComputed(final int i)\n
    '''
def isNullCascaded():
    '''returns boolean\n\n
    isNullCascaded(final int i)\n
    '''
def isInherited():
    '''returns boolean\n\n
    isInherited(final int i)\n
    '''
def getOrigin():
    '''returns short\n\n
    getOrigin(final int i)\n
    '''
def isColorRelative():
    '''returns boolean\n\n
    isColorRelative(final int i)\n
    '''
def isParentRelative():
    '''returns boolean\n\n
    isParentRelative(final int i)\n
    '''
def isLineHeightRelative():
    '''returns boolean\n\n
    isLineHeightRelative(final int i)\n
    '''
def isFontSizeRelative():
    '''returns boolean\n\n
    isFontSizeRelative(final int i)\n
    '''
def isBlockWidthRelative():
    '''returns boolean\n\n
    isBlockWidthRelative(final int i)\n
    '''
def isBlockHeightRelative():
    '''returns boolean\n\n
    isBlockHeightRelative(final int i)\n
    '''
def putValue():
    '''returns None\n\n
    putValue(final int i, final Value v)\n
    '''
def putMask():
    '''returns None\n\n
    putMask(final int i, final short m)\n
    '''
def putImportant():
    '''returns None\n\n
    putImportant(final int i, final boolean b)\n
    '''
def putOrigin():
    '''returns None\n\n
    putOrigin(final int i, final short val)\n
    '''
def putComputed():
    '''returns None\n\n
    putComputed(final int i, final boolean b)\n
    '''
def putNullCascaded():
    '''returns None\n\n
    putNullCascaded(final int i, final boolean b)\n
    '''
def putInherited():
    '''returns None\n\n
    putInherited(final int i, final boolean b)\n
    '''
def putColorRelative():
    '''returns None\n\n
    putColorRelative(final int i, final boolean b)\n
    '''
def putParentRelative():
    '''returns None\n\n
    putParentRelative(final int i, final boolean b)\n
    '''
def putLineHeightRelative():
    '''returns None\n\n
    putLineHeightRelative(final int i, final boolean b)\n
    '''
def putFontSizeRelative():
    '''returns None\n\n
    putFontSizeRelative(final int i, final boolean b)\n
    '''
def putBlockWidthRelative():
    '''returns None\n\n
    putBlockWidthRelative(final int i, final boolean b)\n
    '''
def putBlockHeightRelative():
    '''returns None\n\n
    putBlockHeightRelative(final int i, final boolean b)\n
    '''
def toString():
    '''returns String\n\n
    toString(final CSSEngine eng)\n
    '''
