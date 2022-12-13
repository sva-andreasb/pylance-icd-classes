def getEnumMap():
    '''    public static <E extends Enum<E>> Map<String, E> getEnumMap(final Class<E> enumClass)
    '''
def getEnumList():
    '''    public static <E extends Enum<E>> List<E> getEnumList(final Class<E> enumClass)
    '''
def isValidEnum():
    '''    public static <E extends Enum<E>> boolean isValidEnum(final Class<E> enumClass, final String enumName)
    '''
def getEnum():
    '''    public static <E extends Enum<E>> E getEnum(final Class<E> enumClass, final String enumName)
    '''
def generateBitVector():
    '''    public static <E extends Enum<E>> long generateBitVector(final Class<E> enumClass, final Iterable<? extends E> values)
    public static <E extends Enum<E>> long generateBitVector(final Class<E> enumClass, final E... values)
    '''
def generateBitVectors():
    '''    public static <E extends Enum<E>> long[] generateBitVectors(final Class<E> enumClass, final Iterable<? extends E> values)
    public static <E extends Enum<E>> long[] generateBitVectors(final Class<E> enumClass, final E... values)
    '''
def processBitVector():
    '''    public static <E extends Enum<E>> EnumSet<E> processBitVector(final Class<E> enumClass, final long value)
    '''
def processBitVectors():
    '''    public static <E extends Enum<E>> EnumSet<E> processBitVectors(final Class<E> enumClass, final long... values)
    '''
