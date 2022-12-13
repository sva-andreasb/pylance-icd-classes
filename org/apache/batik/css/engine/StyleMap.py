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
'''public StyleMap(final int size)
'''
pass
def hasFixedCascadedValues():
'''public boolean hasFixedCascadedValues()
'''
pass
def setFixedCascadedStyle():
'''public void setFixedCascadedStyle(final boolean b)
'''
pass
def getValue():
'''public Value getValue(final int i)
'''
pass
def getMask():
'''public short getMask(final int i)
'''
pass
def isImportant():
'''public boolean isImportant(final int i)
'''
pass
def isComputed():
'''public boolean isComputed(final int i)
'''
pass
def isNullCascaded():
'''public boolean isNullCascaded(final int i)
'''
pass
def isInherited():
'''public boolean isInherited(final int i)
'''
pass
def getOrigin():
'''public short getOrigin(final int i)
'''
pass
def isColorRelative():
'''public boolean isColorRelative(final int i)
'''
pass
def isParentRelative():
'''public boolean isParentRelative(final int i)
'''
pass
def isLineHeightRelative():
'''public boolean isLineHeightRelative(final int i)
'''
pass
def isFontSizeRelative():
'''public boolean isFontSizeRelative(final int i)
'''
pass
def isBlockWidthRelative():
'''public boolean isBlockWidthRelative(final int i)
'''
pass
def isBlockHeightRelative():
'''public boolean isBlockHeightRelative(final int i)
'''
pass
def putValue():
'''public void putValue(final int i, final Value v)
'''
pass
def putMask():
'''public void putMask(final int i, final short m)
'''
pass
def putImportant():
'''public void putImportant(final int i, final boolean b)
'''
pass
def putOrigin():
'''public void putOrigin(final int i, final short val)
'''
pass
def putComputed():
'''public void putComputed(final int i, final boolean b)
'''
pass
def putNullCascaded():
'''public void putNullCascaded(final int i, final boolean b)
'''
pass
def putInherited():
'''public void putInherited(final int i, final boolean b)
'''
pass
def putColorRelative():
'''public void putColorRelative(final int i, final boolean b)
'''
pass
def putParentRelative():
'''public void putParentRelative(final int i, final boolean b)
'''
pass
def putLineHeightRelative():
'''public void putLineHeightRelative(final int i, final boolean b)
'''
pass
def putFontSizeRelative():
'''public void putFontSizeRelative(final int i, final boolean b)
'''
pass
def putBlockWidthRelative():
'''public void putBlockWidthRelative(final int i, final boolean b)
'''
pass
def putBlockHeightRelative():
'''public void putBlockHeightRelative(final int i, final boolean b)
'''
pass
def toString():
'''public String toString(final CSSEngine eng)
'''
pass
