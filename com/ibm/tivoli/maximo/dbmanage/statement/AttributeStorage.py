def AttributeStorage():
'''public AttributeStorage(final String[] names, final AttributeClass[] storage)
public AttributeStorage(final AttributeStorageDefinition definition)
public AttributeStorage(final AttributeStorageDefinition asd, final Element element)
'''
pass
def set():
'''public void set(final String attrName, final Object value)
'''
pass
def get():
'''public Object get(final String attrName)
public Object get(final int n)
'''
pass
def getInt():
'''public final Integer getInt(final String attrName)
'''
pass
def getBoolean():
'''public final Boolean getBoolean(final String attrName)
'''
pass
def getDouble():
'''public final Double getDouble(final String attrName)
'''
pass
def getLong():
'''public final Long getLong(final String attrName)
'''
pass
def getString():
'''public final String getString(final String attrName)
'''
pass
def isSet():
'''public boolean isSet(final String attrName)
'''
pass
def clear():
'''public void clear(final String attrName)
'''
pass
def loadFromElement():
'''public void loadFromElement(final Element fromElement)
'''
pass
def saveToElement():
'''public void saveToElement(final Element toElement)
public void saveToElement(final String[] columnDefAttributes, final Element toElement)
'''
pass
def size():
'''public int size()
'''
pass
def getSetAttr():
'''public Set<String> getSetAttr()
'''
pass
def setWithIgnore():
'''public void setWithIgnore(final String string, final Object object)
'''
pass
def copyFromStorage():
'''public void copyFromStorage(final AttributeStorage attr)
'''
pass
def loadFromResultSet():
'''public void loadFromResultSet(final ResultSet rs)
'''
pass
def hasAttribute():
'''public boolean hasAttribute(final String attrName)
'''
pass
def getAttrClass():
'''public AttributeClass getAttrClass(final String attr)
'''
pass
def getNameIterator():
'''public Iterator<String> getNameIterator()
'''
pass
def getValues():
'''public Object[] getValues()
'''
pass
def getDefinition():
'''public AttributeStorageDefinition getDefinition()
'''
pass
def getCommaLine():
'''public String getCommaLine()
'''
pass
def getTimestamp():
'''public Timestamp getTimestamp(final String attrName)
'''
pass
def toString():
'''public String toString()
'''
pass
def hasNoValues():
'''public boolean hasNoValues()
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
