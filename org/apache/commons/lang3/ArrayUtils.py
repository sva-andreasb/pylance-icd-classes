INDEX_NOT_FOUND = "int  -1"
def toString():
'''public static String toString(final Object array)
public static String toString(final Object array, final String stringIfNull)
'''
pass
def hashCode():
'''public static int hashCode(final Object array)
'''
pass
def isEquals():
'''public static boolean isEquals(final Object array1, final Object array2)
'''
pass
def toMap():
'''public static Map<Object, Object> toMap(final Object[] array)
'''
pass
def toArray():
'''public static <T> T[] toArray(final T... items)
'''
pass
def clone():
'''public static <T> T[] clone(final T[] array)
public static long[] clone(final long[] array)
public static int[] clone(final int[] array)
public static short[] clone(final short[] array)
public static char[] clone(final char[] array)
public static byte[] clone(final byte[] array)
public static double[] clone(final double[] array)
public static float[] clone(final float[] array)
public static boolean[] clone(final boolean[] array)
'''
pass
def nullToEmpty():
'''public static Object[] nullToEmpty(final Object[] array)
public static String[] nullToEmpty(final String[] array)
public static long[] nullToEmpty(final long[] array)
public static int[] nullToEmpty(final int[] array)
public static short[] nullToEmpty(final short[] array)
public static char[] nullToEmpty(final char[] array)
public static byte[] nullToEmpty(final byte[] array)
public static double[] nullToEmpty(final double[] array)
public static float[] nullToEmpty(final float[] array)
public static boolean[] nullToEmpty(final boolean[] array)
public static Long[] nullToEmpty(final Long[] array)
public static Integer[] nullToEmpty(final Integer[] array)
public static Short[] nullToEmpty(final Short[] array)
public static Character[] nullToEmpty(final Character[] array)
public static Byte[] nullToEmpty(final Byte[] array)
public static Double[] nullToEmpty(final Double[] array)
public static Float[] nullToEmpty(final Float[] array)
public static Boolean[] nullToEmpty(final Boolean[] array)
'''
pass
def subarray():
'''public static <T> T[] subarray(final T[] array, int startIndexInclusive, int endIndexExclusive)
public static long[] subarray(final long[] array, int startIndexInclusive, int endIndexExclusive)
public static int[] subarray(final int[] array, int startIndexInclusive, int endIndexExclusive)
public static short[] subarray(final short[] array, int startIndexInclusive, int endIndexExclusive)
public static char[] subarray(final char[] array, int startIndexInclusive, int endIndexExclusive)
public static byte[] subarray(final byte[] array, int startIndexInclusive, int endIndexExclusive)
public static double[] subarray(final double[] array, int startIndexInclusive, int endIndexExclusive)
public static float[] subarray(final float[] array, int startIndexInclusive, int endIndexExclusive)
public static boolean[] subarray(final boolean[] array, int startIndexInclusive, int endIndexExclusive)
'''
pass
def isSameLength():
'''public static boolean isSameLength(final Object[] array1, final Object[] array2)
public static boolean isSameLength(final long[] array1, final long[] array2)
public static boolean isSameLength(final int[] array1, final int[] array2)
public static boolean isSameLength(final short[] array1, final short[] array2)
public static boolean isSameLength(final char[] array1, final char[] array2)
public static boolean isSameLength(final byte[] array1, final byte[] array2)
public static boolean isSameLength(final double[] array1, final double[] array2)
public static boolean isSameLength(final float[] array1, final float[] array2)
public static boolean isSameLength(final boolean[] array1, final boolean[] array2)
'''
pass
def getLength():
'''public static int getLength(final Object array)
'''
pass
def isSameType():
'''public static boolean isSameType(final Object array1, final Object array2)
'''
pass
def reverse():
'''public static void reverse(final Object[] array)
public static void reverse(final long[] array)
public static void reverse(final int[] array)
public static void reverse(final short[] array)
public static void reverse(final char[] array)
public static void reverse(final byte[] array)
public static void reverse(final double[] array)
public static void reverse(final float[] array)
public static void reverse(final boolean[] array)
public static void reverse(final boolean[] array, final int startIndexInclusive, final int endIndexExclusive)
public static void reverse(final byte[] array, final int startIndexInclusive, final int endIndexExclusive)
public static void reverse(final char[] array, final int startIndexInclusive, final int endIndexExclusive)
public static void reverse(final double[] array, final int startIndexInclusive, final int endIndexExclusive)
public static void reverse(final float[] array, final int startIndexInclusive, final int endIndexExclusive)
public static void reverse(final int[] array, final int startIndexInclusive, final int endIndexExclusive)
public static void reverse(final long[] array, final int startIndexInclusive, final int endIndexExclusive)
public static void reverse(final Object[] array, final int startIndexInclusive, final int endIndexExclusive)
public static void reverse(final short[] array, final int startIndexInclusive, final int endIndexExclusive)
'''
pass
def indexOf():
'''public static int indexOf(final Object[] array, final Object objectToFind)
public static int indexOf(final Object[] array, final Object objectToFind, int startIndex)
public static int indexOf(final long[] array, final long valueToFind)
public static int indexOf(final long[] array, final long valueToFind, int startIndex)
public static int indexOf(final int[] array, final int valueToFind)
public static int indexOf(final int[] array, final int valueToFind, int startIndex)
public static int indexOf(final short[] array, final short valueToFind)
public static int indexOf(final short[] array, final short valueToFind, int startIndex)
public static int indexOf(final char[] array, final char valueToFind)
public static int indexOf(final char[] array, final char valueToFind, int startIndex)
public static int indexOf(final byte[] array, final byte valueToFind)
public static int indexOf(final byte[] array, final byte valueToFind, int startIndex)
public static int indexOf(final double[] array, final double valueToFind)
public static int indexOf(final double[] array, final double valueToFind, final double tolerance)
public static int indexOf(final double[] array, final double valueToFind, int startIndex)
public static int indexOf(final double[] array, final double valueToFind, int startIndex, final double tolerance)
public static int indexOf(final float[] array, final float valueToFind)
public static int indexOf(final float[] array, final float valueToFind, int startIndex)
public static int indexOf(final boolean[] array, final boolean valueToFind)
public static int indexOf(final boolean[] array, final boolean valueToFind, int startIndex)
'''
pass
def lastIndexOf():
'''public static int lastIndexOf(final Object[] array, final Object objectToFind)
public static int lastIndexOf(final Object[] array, final Object objectToFind, int startIndex)
public static int lastIndexOf(final long[] array, final long valueToFind)
public static int lastIndexOf(final long[] array, final long valueToFind, int startIndex)
public static int lastIndexOf(final int[] array, final int valueToFind)
public static int lastIndexOf(final int[] array, final int valueToFind, int startIndex)
public static int lastIndexOf(final short[] array, final short valueToFind)
public static int lastIndexOf(final short[] array, final short valueToFind, int startIndex)
public static int lastIndexOf(final char[] array, final char valueToFind)
public static int lastIndexOf(final char[] array, final char valueToFind, int startIndex)
public static int lastIndexOf(final byte[] array, final byte valueToFind)
public static int lastIndexOf(final byte[] array, final byte valueToFind, int startIndex)
public static int lastIndexOf(final double[] array, final double valueToFind)
public static int lastIndexOf(final double[] array, final double valueToFind, final double tolerance)
public static int lastIndexOf(final double[] array, final double valueToFind, int startIndex)
public static int lastIndexOf(final double[] array, final double valueToFind, int startIndex, final double tolerance)
public static int lastIndexOf(final float[] array, final float valueToFind)
public static int lastIndexOf(final float[] array, final float valueToFind, int startIndex)
public static int lastIndexOf(final boolean[] array, final boolean valueToFind)
public static int lastIndexOf(final boolean[] array, final boolean valueToFind, int startIndex)
'''
pass
def contains():
'''public static boolean contains(final Object[] array, final Object objectToFind)
public static boolean contains(final long[] array, final long valueToFind)
public static boolean contains(final int[] array, final int valueToFind)
public static boolean contains(final short[] array, final short valueToFind)
public static boolean contains(final char[] array, final char valueToFind)
public static boolean contains(final byte[] array, final byte valueToFind)
public static boolean contains(final double[] array, final double valueToFind)
public static boolean contains(final double[] array, final double valueToFind, final double tolerance)
public static boolean contains(final float[] array, final float valueToFind)
public static boolean contains(final boolean[] array, final boolean valueToFind)
'''
pass
def toPrimitive():
'''public static char[] toPrimitive(final Character[] array)
public static char[] toPrimitive(final Character[] array, final char valueForNull)
public static long[] toPrimitive(final Long[] array)
public static long[] toPrimitive(final Long[] array, final long valueForNull)
public static int[] toPrimitive(final Integer[] array)
public static int[] toPrimitive(final Integer[] array, final int valueForNull)
public static short[] toPrimitive(final Short[] array)
public static short[] toPrimitive(final Short[] array, final short valueForNull)
public static byte[] toPrimitive(final Byte[] array)
public static byte[] toPrimitive(final Byte[] array, final byte valueForNull)
public static double[] toPrimitive(final Double[] array)
public static double[] toPrimitive(final Double[] array, final double valueForNull)
public static float[] toPrimitive(final Float[] array)
public static float[] toPrimitive(final Float[] array, final float valueForNull)
public static boolean[] toPrimitive(final Boolean[] array)
public static boolean[] toPrimitive(final Boolean[] array, final boolean valueForNull)
'''
pass
def toObject():
'''public static Character[] toObject(final char[] array)
public static Long[] toObject(final long[] array)
public static Integer[] toObject(final int[] array)
public static Short[] toObject(final short[] array)
public static Byte[] toObject(final byte[] array)
public static Double[] toObject(final double[] array)
public static Float[] toObject(final float[] array)
public static Boolean[] toObject(final boolean[] array)
'''
pass
def isEmpty():
'''public static boolean isEmpty(final Object[] array)
public static boolean isEmpty(final long[] array)
public static boolean isEmpty(final int[] array)
public static boolean isEmpty(final short[] array)
public static boolean isEmpty(final char[] array)
public static boolean isEmpty(final byte[] array)
public static boolean isEmpty(final double[] array)
public static boolean isEmpty(final float[] array)
public static boolean isEmpty(final boolean[] array)
'''
pass
def isNotEmpty():
'''public static <T> boolean isNotEmpty(final T[] array)
public static boolean isNotEmpty(final long[] array)
public static boolean isNotEmpty(final int[] array)
public static boolean isNotEmpty(final short[] array)
public static boolean isNotEmpty(final char[] array)
public static boolean isNotEmpty(final byte[] array)
public static boolean isNotEmpty(final double[] array)
public static boolean isNotEmpty(final float[] array)
public static boolean isNotEmpty(final boolean[] array)
'''
pass
def addAll():
'''public static <T> T[] addAll(final T[] array1, final T... array2)
public static boolean[] addAll(final boolean[] array1, final boolean... array2)
public static char[] addAll(final char[] array1, final char... array2)
public static byte[] addAll(final byte[] array1, final byte... array2)
public static short[] addAll(final short[] array1, final short... array2)
public static int[] addAll(final int[] array1, final int... array2)
public static long[] addAll(final long[] array1, final long... array2)
public static float[] addAll(final float[] array1, final float... array2)
public static double[] addAll(final double[] array1, final double... array2)
'''
pass
def add():
'''public static <T> T[] add(final T[] array, final T element)
public static boolean[] add(final boolean[] array, final boolean element)
public static byte[] add(final byte[] array, final byte element)
public static char[] add(final char[] array, final char element)
public static double[] add(final double[] array, final double element)
public static float[] add(final float[] array, final float element)
public static int[] add(final int[] array, final int element)
public static long[] add(final long[] array, final long element)
public static short[] add(final short[] array, final short element)
public static <T> T[] add(final T[] array, final int index, final T element)
public static boolean[] add(final boolean[] array, final int index, final boolean element)
public static char[] add(final char[] array, final int index, final char element)
public static byte[] add(final byte[] array, final int index, final byte element)
public static short[] add(final short[] array, final int index, final short element)
public static int[] add(final int[] array, final int index, final int element)
public static long[] add(final long[] array, final int index, final long element)
public static float[] add(final float[] array, final int index, final float element)
public static double[] add(final double[] array, final int index, final double element)
'''
pass
def remove():
'''public static <T> T[] remove(final T[] array, final int index)
public static boolean[] remove(final boolean[] array, final int index)
public static byte[] remove(final byte[] array, final int index)
public static char[] remove(final char[] array, final int index)
public static double[] remove(final double[] array, final int index)
public static float[] remove(final float[] array, final int index)
public static int[] remove(final int[] array, final int index)
public static long[] remove(final long[] array, final int index)
public static short[] remove(final short[] array, final int index)
'''
pass
def removeElement():
'''public static <T> T[] removeElement(final T[] array, final Object element)
public static boolean[] removeElement(final boolean[] array, final boolean element)
public static byte[] removeElement(final byte[] array, final byte element)
public static char[] removeElement(final char[] array, final char element)
public static double[] removeElement(final double[] array, final double element)
public static float[] removeElement(final float[] array, final float element)
public static int[] removeElement(final int[] array, final int element)
public static long[] removeElement(final long[] array, final long element)
public static short[] removeElement(final short[] array, final short element)
'''
pass
def removeAll():
'''public static <T> T[] removeAll(final T[] array, final int... indices)
public static byte[] removeAll(final byte[] array, final int... indices)
public static short[] removeAll(final short[] array, final int... indices)
public static int[] removeAll(final int[] array, final int... indices)
public static char[] removeAll(final char[] array, final int... indices)
public static long[] removeAll(final long[] array, final int... indices)
public static float[] removeAll(final float[] array, final int... indices)
public static double[] removeAll(final double[] array, final int... indices)
public static boolean[] removeAll(final boolean[] array, final int... indices)
'''
pass
def removeElements():
'''public static <T> T[] removeElements(final T[] array, final T... values)
public static byte[] removeElements(final byte[] array, final byte... values)
public static short[] removeElements(final short[] array, final short... values)
public static int[] removeElements(final int[] array, final int... values)
public static char[] removeElements(final char[] array, final char... values)
public static long[] removeElements(final long[] array, final long... values)
public static float[] removeElements(final float[] array, final float... values)
public static double[] removeElements(final double[] array, final double... values)
public static boolean[] removeElements(final boolean[] array, final boolean... values)
'''
pass
def compare():
'''public int compare(final T o1, final T o2)
'''
pass
def isSorted():
'''public static <T> boolean isSorted(final T[] array, final Comparator<T> comparator)
public static boolean isSorted(final int[] array)
public static boolean isSorted(final long[] array)
public static boolean isSorted(final short[] array)
public static boolean isSorted(final double[] array)
public static boolean isSorted(final float[] array)
public static boolean isSorted(final byte[] array)
public static boolean isSorted(final char[] array)
public static boolean isSorted(final boolean[] array)
'''
pass