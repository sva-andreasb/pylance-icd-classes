DONE = "long  -1L"
def compileToStringMinMaxArguments():
    '''    public static String compileToStringMinMaxArguments(final CharSequence pattern, final StringBuilder sb, final int min, final int max)
    '''
def getArgumentLimit():
    '''    public static int getArgumentLimit(final String compiledPattern)
    '''
def formatCompiledPattern():
    '''    public static String formatCompiledPattern(final String compiledPattern, final CharSequence... values)
    '''
def formatRawPattern():
    '''    public static String formatRawPattern(final String pattern, final int min, final int max, final CharSequence... values)
    '''
def formatAndAppend():
    '''    public static StringBuilder formatAndAppend(final String compiledPattern, final StringBuilder appendTo, final int[] offsets, final CharSequence... values)
    '''
def formatAndReplace():
    '''    public static StringBuilder formatAndReplace(final String compiledPattern, final StringBuilder result, final int[] offsets, final CharSequence... values)
    '''
def getTextWithNoArguments():
    '''    public static String getTextWithNoArguments(final String compiledPattern)
    '''
def getLength():
    '''    public static int getLength(final String compiledPattern, final boolean codePoints)
    '''
def getPrefixLength():
    '''    public static int getPrefixLength(final String compiledPattern)
    '''
def formatPrefixSuffix():
    '''    public static int formatPrefixSuffix(final String compiledPattern, final Format.Field field, final int start, final int end, final FormattedStringBuilder output)
    '''
def step():
    '''    public static long step(final long state, final CharSequence compiledPattern, final Appendable output)
    '''
def getArgIndex():
    '''    public static int getArgIndex(final long state)
    '''
