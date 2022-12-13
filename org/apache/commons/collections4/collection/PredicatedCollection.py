def builder():
    '''public static <E> Builder<E> builder(final Predicate<? super E> predicate)
    '''
def notNullBuilder():
    '''public static <E> Builder<E> notNullBuilder()
    '''
def predicatedCollection():
    '''public static <T> PredicatedCollection<T> predicatedCollection(final Collection<T> coll, final Predicate<? super T> predicate)
    '''
def add():
    '''public boolean add(final E object)
    public Builder<E> add(final E item)
    '''
def addAll():
    '''public boolean addAll(final Collection<? extends E> coll)
    public Builder<E> addAll(final Collection<? extends E> items)
    '''
def Builder():
    '''public Builder(final Predicate<? super E> predicate)
    '''
def createPredicatedList():
    '''public List<E> createPredicatedList()
    public List<E> createPredicatedList(final List<E> list)
    '''
def createPredicatedSet():
    '''public Set<E> createPredicatedSet()
    public Set<E> createPredicatedSet(final Set<E> set)
    '''
def createPredicatedMultiSet():
    '''public MultiSet<E> createPredicatedMultiSet()
    public MultiSet<E> createPredicatedMultiSet(final MultiSet<E> multiset)
    '''
def createPredicatedBag():
    '''public Bag<E> createPredicatedBag()
    public Bag<E> createPredicatedBag(final Bag<E> bag)
    '''
def createPredicatedQueue():
    '''public Queue<E> createPredicatedQueue()
    public Queue<E> createPredicatedQueue(final Queue<E> queue)
    '''
def rejectedElements():
    '''public Collection<E> rejectedElements()
    '''
