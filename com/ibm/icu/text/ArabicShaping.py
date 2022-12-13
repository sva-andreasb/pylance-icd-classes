SEEN_TWOCELL_NEAR = "int  2097152"
SEEN_MASK = "int  7340032"
YEHHAMZA_TWOCELL_NEAR = "int  16777216"
YEHHAMZA_MASK = "int  58720256"
TASHKEEL_BEGIN = "int  262144"
TASHKEEL_END = "int  393216"
TASHKEEL_RESIZE = "int  524288"
TASHKEEL_REPLACE_BY_TATWEEL = "int  786432"
TASHKEEL_MASK = "int  917504"
SPACES_RELATIVE_TO_TEXT_BEGIN_END = "int  67108864"
SPACES_RELATIVE_TO_TEXT_MASK = "int  67108864"
SHAPE_TAIL_NEW_UNICODE = "int  134217728"
SHAPE_TAIL_TYPE_MASK = "int  134217728"
LENGTH_GROW_SHRINK = "int  0"
LAMALEF_RESIZE = "int  0"
LENGTH_FIXED_SPACES_NEAR = "int  1"
LAMALEF_NEAR = "int  1"
LENGTH_FIXED_SPACES_AT_END = "int  2"
LAMALEF_END = "int  2"
LENGTH_FIXED_SPACES_AT_BEGINNING = "int  3"
LAMALEF_BEGIN = "int  3"
LAMALEF_AUTO = "int  65536"
LENGTH_MASK = "int  65539"
LAMALEF_MASK = "int  65539"
TEXT_DIRECTION_LOGICAL = "int  0"
TEXT_DIRECTION_VISUAL_RTL = "int  0"
TEXT_DIRECTION_VISUAL_LTR = "int  4"
TEXT_DIRECTION_MASK = "int  4"
LETTERS_NOOP = "int  0"
LETTERS_SHAPE = "int  8"
LETTERS_UNSHAPE = "int  16"
LETTERS_SHAPE_TASHKEEL_ISOLATED = "int  24"
LETTERS_MASK = "int  24"
DIGITS_NOOP = "int  0"
DIGITS_EN2AN = "int  32"
DIGITS_AN2EN = "int  64"
DIGITS_EN2AN_INIT_LR = "int  96"
DIGITS_EN2AN_INIT_AL = "int  128"
DIGITS_MASK = "int  224"
DIGIT_TYPE_AN = "int  0"
DIGIT_TYPE_AN_EXTENDED = "int  256"
DIGIT_TYPE_MASK = "int  256"
def shape():
    '''public int shape(final char[] source, final int sourceStart, final int sourceLength, final char[] dest, final int destStart, final int destSize)
    public void shape(final char[] source, final int start, final int length)
    public String shape(final String text)
    '''
def ArabicShaping():
    '''public ArabicShaping(final int options)
    '''
def equals():
    '''public boolean equals(final Object rhs)
    '''
def hashCode():
    '''public int hashCode()
    '''
def toString():
    '''public String toString()
    '''
