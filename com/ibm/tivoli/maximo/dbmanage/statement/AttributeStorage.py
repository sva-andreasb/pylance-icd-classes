def AttributeStorage():
    '''    public AttributeStorage(final String[] names, final AttributeClass[] storage)
    public AttributeStorage(final AttributeStorageDefinition definition)
    public AttributeStorage(final AttributeStorageDefinition asd, final Element element)
    '''
def set():
    '''    public void set(final String attrName, final Object value)
    '''
def get():
    '''    public Object get(final String attrName)
    public Object get(final int n)
    '''
def getInt():
    '''    public final Integer getInt(final String attrName)
    '''
def getBoolean():
    '''    public final Boolean getBoolean(final String attrName)
    '''
def getDouble():
    '''    public final Double getDouble(final String attrName)
    '''
def getLong():
    '''    public final Long getLong(final String attrName)
    '''
def getString():
    '''    public final String getString(final String attrName)
    '''
def isSet():
    '''    public boolean isSet(final String attrName)
    '''
def clear():
    '''    public void clear(final String attrName)
    '''
def loadFromElement():
    '''    public void loadFromElement(final Element fromElement)
    '''
def saveToElement():
    '''    public void saveToElement(final Element toElement)
    public void saveToElement(final String[] columnDefAttributes, final Element toElement)
    '''
def size():
    '''    public int size()
    '''
def getSetAttr():
    '''    public Set<String> getSetAttr()
    '''
def setWithIgnore():
    '''    public void setWithIgnore(final String string, final Object object)
    '''
def copyFromStorage():
    '''    public void copyFromStorage(final AttributeStorage attr)
    '''
def loadFromResultSet():
    '''    public void loadFromResultSet(final ResultSet rs)
    '''
def hasAttribute():
    '''    public boolean hasAttribute(final String attrName)
    '''
def getAttrClass():
    '''    public AttributeClass getAttrClass(final String attr)
    '''
def getNameIterator():
    '''    public Iterator<String> getNameIterator()
    '''
def getValues():
    '''    public Object[] getValues()
    '''
def getDefinition():
    '''    public AttributeStorageDefinition getDefinition()
    '''
def getCommaLine():
    '''    public String getCommaLine()
    '''
def getTimestamp():
    '''    public Timestamp getTimestamp(final String attrName)
    '''
def toString():
    '''    public String toString()
    '''
def hasNoValues():
    '''    public boolean hasNoValues()
    '''
def hashCode():
    '''    public int hashCode()
    '''
