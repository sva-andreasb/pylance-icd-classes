def accessToString():
    '''    public static final String accessToString(final int access_flags)
    public static final String accessToString(final int access_flags, final boolean for_class)
    '''
def classOrInterface():
    '''    public static final String classOrInterface(final int access_flags)
    '''
def codeToString():
    '''    public static final String codeToString(final byte[] code, final ConstantPool constant_pool, final int index, final int length, final boolean verbose)
    public static final String codeToString(final byte[] code, final ConstantPool constant_pool, final int index, final int length)
    public static final String codeToString(final ByteSequence bytes, final ConstantPool constant_pool, final boolean verbose)
    public static final String codeToString(final ByteSequence bytes, final ConstantPool constant_pool)
    '''
def compactClassName():
    '''    public static final String compactClassName(final String str)
    public static final String compactClassName(String str, final String prefix, final boolean chopit)
    public static final String compactClassName(final String str, final boolean chopit)
    '''
def setBit():
    '''    public static final int setBit(final int flag, final int i)
    '''
def clearBit():
    '''    public static final int clearBit(final int flag, final int i)
    '''
def isSet():
    '''    public static final boolean isSet(final int flag, final int i)
    '''
def methodTypeToSignature():
    '''    public static final String methodTypeToSignature(final String ret, final String[] argv)
    '''
def methodSignatureArgumentTypes():
    '''    public static final String[] methodSignatureArgumentTypes(final String signature)
    public static final String[] methodSignatureArgumentTypes(final String signature, final boolean chopit)
    '''
def methodSignatureReturnType():
    '''    public static final String methodSignatureReturnType(final String signature)
    public static final String methodSignatureReturnType(final String signature, final boolean chopit)
    '''
def methodSignatureToString():
    '''    public static final String methodSignatureToString(final String signature, final String name, final String access)
    public static final String methodSignatureToString(final String signature, final String name, final String access, final boolean chopit)
    public static final String methodSignatureToString(final String signature, final String name, final String access, final boolean chopit, final LocalVariableTable vars)
    '''
def replace():
    '''    public static final String replace(String str, final String old, final String new_)
    '''
def signatureToString():
    '''    public static final String signatureToString(final String signature)
    public static final String signatureToString(final String signature, final boolean chopit)
    '''
def getSignature():
    '''    public static String getSignature(String type)
    '''
def typeOfMethodSignature():
    '''    public static final byte typeOfMethodSignature(final String signature)
    '''
def typeOfSignature():
    '''    public static final byte typeOfSignature(final String signature)
    '''
def searchOpcode():
    '''    public static short searchOpcode(String name)
    '''
def toHexString():
    '''    public static final String toHexString(final byte[] bytes)
    '''
def format():
    '''    public static final String format(final int i, final int length, final boolean left_justify, final char fill)
    '''
def fillup():
    '''    public static final String fillup(final String str, final int length, final boolean left_justify, final char fill)
    '''
def printArray():
    '''    public static final void printArray(final PrintStream out, final Object[] obj)
    public static final void printArray(final PrintWriter out, final Object[] obj)
    public static final String printArray(final Object[] obj)
    public static final String printArray(final Object[] obj, final boolean braces)
    public static final String printArray(final Object[] obj, final boolean braces, final boolean quote)
    '''
def isJavaIdentifierPart():
    '''    public static boolean isJavaIdentifierPart(final char ch)
    '''
def encode():
    '''    public static String encode(byte[] bytes, final boolean compress)
    '''
def decode():
    '''    public static byte[] decode(final String s, final boolean uncompress)
    '''
def convertString():
    '''    public static final String convertString(final String label)
    '''
def JavaReader():
    '''    public JavaReader(final Reader in)
    '''
def read():
    '''    public int read()
    public int read(final char[] cbuf, final int off, final int len)
    '''
def JavaWriter():
    '''    public JavaWriter(final Writer out)
    '''
def write():
    '''    public void write(final int b)
    public void write(final char[] cbuf, final int off, final int len)
    public void write(final String str, final int off, final int len)
    '''
