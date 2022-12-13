def builder():
'''public static <E> Builder<E> builder(final Predicate<? super E> predicate)
'''
pass
def notNullBuilder():
'''public static <E> Builder<E> notNullBuilder()
'''
pass
def predicatedCollection():
'''public static <T> PredicatedCollection<T> predicatedCollection(final Collection<T> coll, final Predicate<? super T> predicate)
'''
pass
def add():
'''public boolean add(final E object)
public Builder<E> add(final E item)
'''
pass
def addAll():
'''public boolean addAll(final Collection<? extends E> coll)
public Builder<E> addAll(final Collection<? extends E> items)
'''
pass
def Builder():
'''public Builder(final Predicate<? super E> predicate)
'''
pass
def createPredicatedList():
'''public List<E> createPredicatedList()
public List<E> createPredicatedList(final List<E> list)
'''
pass
def createPredicatedSet():
'''public Set<E> createPredicatedSet()
public Set<E> createPredicatedSet(final Set<E> set)
'''
pass
def createPredicatedMultiSet():
'''public MultiSet<E> createPredicatedMultiSet()
public MultiSet<E> createPredicatedMultiSet(final MultiSet<E> multiset)
'''
pass
def createPredicatedBag():
'''public Bag<E> createPredicatedBag()
public Bag<E> createPredicatedBag(final Bag<E> bag)
'''
pass
def createPredicatedQueue():
'''public Queue<E> createPredicatedQueue()
public Queue<E> createPredicatedQueue(final Queue<E> queue)
'''
pass
def rejectedElements():
'''public Collection<E> rejectedElements()
'''
pass
