def getObject():
'''public static <K, V> V getObject(final Map<? super K, V> map, final K key)
public static <K, V> V getObject(final Map<K, V> map, final K key, final V defaultValue)
'''
pass
def getString():
'''public static <K> String getString(final Map<? super K, ?> map, final K key)
public static <K> String getString(final Map<? super K, ?> map, final K key, final String defaultValue)
'''
pass
def getBoolean():
'''public static <K> Boolean getBoolean(final Map<? super K, ?> map, final K key)
public static <K> Boolean getBoolean(final Map<? super K, ?> map, final K key, final Boolean defaultValue)
'''
pass
def getNumber():
'''public static <K> Number getNumber(final Map<? super K, ?> map, final K key)
public static <K> Number getNumber(final Map<? super K, ?> map, final K key, final Number defaultValue)
'''
pass
def getByte():
'''public static <K> Byte getByte(final Map<? super K, ?> map, final K key)
public static <K> Byte getByte(final Map<? super K, ?> map, final K key, final Byte defaultValue)
'''
pass
def getShort():
'''public static <K> Short getShort(final Map<? super K, ?> map, final K key)
public static <K> Short getShort(final Map<? super K, ?> map, final K key, final Short defaultValue)
'''
pass
def getInteger():
'''public static <K> Integer getInteger(final Map<? super K, ?> map, final K key)
public static <K> Integer getInteger(final Map<? super K, ?> map, final K key, final Integer defaultValue)
'''
pass
def getLong():
'''public static <K> Long getLong(final Map<? super K, ?> map, final K key)
public static <K> Long getLong(final Map<? super K, ?> map, final K key, final Long defaultValue)
'''
pass
def getFloat():
'''public static <K> Float getFloat(final Map<? super K, ?> map, final K key)
public static <K> Float getFloat(final Map<? super K, ?> map, final K key, final Float defaultValue)
'''
pass
def getDouble():
'''public static <K> Double getDouble(final Map<? super K, ?> map, final K key)
public static <K> Double getDouble(final Map<? super K, ?> map, final K key, final Double defaultValue)
'''
pass
def getBooleanValue():
'''public static <K> boolean getBooleanValue(final Map<? super K, ?> map, final K key)
public static <K> boolean getBooleanValue(final Map<? super K, ?> map, final K key, final boolean defaultValue)
'''
pass
def getByteValue():
'''public static <K> byte getByteValue(final Map<? super K, ?> map, final K key)
public static <K> byte getByteValue(final Map<? super K, ?> map, final K key, final byte defaultValue)
'''
pass
def getShortValue():
'''public static <K> short getShortValue(final Map<? super K, ?> map, final K key)
public static <K> short getShortValue(final Map<? super K, ?> map, final K key, final short defaultValue)
'''
pass
def getIntValue():
'''public static <K> int getIntValue(final Map<? super K, ?> map, final K key)
public static <K> int getIntValue(final Map<? super K, ?> map, final K key, final int defaultValue)
'''
pass
def getLongValue():
'''public static <K> long getLongValue(final Map<? super K, ?> map, final K key)
public static <K> long getLongValue(final Map<? super K, ?> map, final K key, final long defaultValue)
'''
pass
def getFloatValue():
'''public static <K> float getFloatValue(final Map<? super K, ?> map, final K key)
public static <K> float getFloatValue(final Map<? super K, ?> map, final K key, final float defaultValue)
'''
pass
def getDoubleValue():
'''public static <K> double getDoubleValue(final Map<? super K, ?> map, final K key)
public static <K> double getDoubleValue(final Map<? super K, ?> map, final K key, final double defaultValue)
'''
pass
def toProperties():
'''public static <K, V> Properties toProperties(final Map<K, V> map)
'''
pass
def toMap():
'''public static Map<String, Object> toMap(final ResourceBundle resourceBundle)
'''
pass
def verbosePrint():
'''public static void verbosePrint(final PrintStream out, final Object label, final Map<?, ?> map)
'''
pass
def debugPrint():
'''public static void debugPrint(final PrintStream out, final Object label, final Map<?, ?> map)
'''
pass
def invertMap():
'''public static <K, V> Map<V, K> invertMap(final Map<K, V> map)
'''
pass
def safeAddToMap():
'''public static <K> void safeAddToMap(final Map<? super K, Object> map, final K key, final Object value)
'''
pass
def putAll():
'''public static <K, V> Map<K, V> putAll(final Map<K, V> map, final Object[] array)
'''
pass
def emptyIfNull():
'''public static <K, V> Map<K, V> emptyIfNull(final Map<K, V> map)
'''
pass
def isEmpty():
'''public static boolean isEmpty(final Map<?, ?> map)
'''
pass
def isNotEmpty():
'''public static boolean isNotEmpty(final Map<?, ?> map)
'''
pass
def synchronizedMap():
'''public static <K, V> Map<K, V> synchronizedMap(final Map<K, V> map)
'''
pass
def unmodifiableMap():
'''public static <K, V> Map<K, V> unmodifiableMap(final Map<? extends K, ? extends V> map)
'''
pass
def predicatedMap():
'''public static <K, V> IterableMap<K, V> predicatedMap(final Map<K, V> map, final Predicate<? super K> keyPred, final Predicate<? super V> valuePred)
'''
pass
def transformedMap():
'''public static <K, V> IterableMap<K, V> transformedMap(final Map<K, V> map, final Transformer<? super K, ? extends K> keyTransformer, final Transformer<? super V, ? extends V> valueTransformer)
'''
pass
def fixedSizeMap():
'''public static <K, V> IterableMap<K, V> fixedSizeMap(final Map<K, V> map)
'''
pass
def lazyMap():
'''public static <K, V> IterableMap<K, V> lazyMap(final Map<K, V> map, final Factory<? extends V> factory)
public static <K, V> IterableMap<K, V> lazyMap(final Map<K, V> map, final Transformer<? super K, ? extends V> transformerFactory)
'''
pass
def orderedMap():
'''public static <K, V> OrderedMap<K, V> orderedMap(final Map<K, V> map)
'''
pass
def multiValueMap():
'''public static <K, V> MultiValueMap<K, V> multiValueMap(final Map<K, ? super Collection<V>> map)
public static <K, V, C extends Collection<V>> MultiValueMap<K, V> multiValueMap(final Map<K, C> map, final Class<C> collectionClass)
public static <K, V, C extends Collection<V>> MultiValueMap<K, V> multiValueMap(final Map<K, C> map, final Factory<C> collectionFactory)
'''
pass
def synchronizedSortedMap():
'''public static <K, V> SortedMap<K, V> synchronizedSortedMap(final SortedMap<K, V> map)
'''
pass
def unmodifiableSortedMap():
'''public static <K, V> SortedMap<K, V> unmodifiableSortedMap(final SortedMap<K, ? extends V> map)
'''
pass
def predicatedSortedMap():
'''public static <K, V> SortedMap<K, V> predicatedSortedMap(final SortedMap<K, V> map, final Predicate<? super K> keyPred, final Predicate<? super V> valuePred)
'''
pass
def transformedSortedMap():
'''public static <K, V> SortedMap<K, V> transformedSortedMap(final SortedMap<K, V> map, final Transformer<? super K, ? extends K> keyTransformer, final Transformer<? super V, ? extends V> valueTransformer)
'''
pass
def fixedSizeSortedMap():
'''public static <K, V> SortedMap<K, V> fixedSizeSortedMap(final SortedMap<K, V> map)
'''
pass
def lazySortedMap():
'''public static <K, V> SortedMap<K, V> lazySortedMap(final SortedMap<K, V> map, final Factory<? extends V> factory)
public static <K, V> SortedMap<K, V> lazySortedMap(final SortedMap<K, V> map, final Transformer<? super K, ? extends V> transformerFactory)
'''
pass
def populateMap():
'''public static <K, V> void populateMap(final Map<K, V> map, final Iterable<? extends V> elements, final Transformer<V, K> keyTransformer)
public static <K, V, E> void populateMap(final Map<K, V> map, final Iterable<? extends E> elements, final Transformer<E, K> keyTransformer, final Transformer<E, V> valueTransformer)
public static <K, V> void populateMap(final MultiMap<K, V> map, final Iterable<? extends V> elements, final Transformer<V, K> keyTransformer)
public static <K, V, E> void populateMap(final MultiMap<K, V> map, final Iterable<? extends E> elements, final Transformer<E, K> keyTransformer, final Transformer<E, V> valueTransformer)
'''
pass
def iterableMap():
'''public static <K, V> IterableMap<K, V> iterableMap(final Map<K, V> map)
'''
pass
def iterableSortedMap():
'''public static <K, V> IterableSortedMap<K, V> iterableSortedMap(final SortedMap<K, V> sortedMap)
'''
pass
