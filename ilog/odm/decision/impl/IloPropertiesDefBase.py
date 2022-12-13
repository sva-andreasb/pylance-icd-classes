COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def IloPropertiesDefBase():
    '''    public IloPropertiesDefBase()
    '''
def getPropertyIndex():
    '''    public int getPropertyIndex(String name)
    '''
def getPropertyName():
    '''    public String getPropertyName(final int index)
    '''
def getPropertyGetter():
    '''    public Getter getPropertyGetter(final int index)
    '''
def getPropertySetter():
    '''    public Setter getPropertySetter(final int index)
    '''
def addProperty():
    '''    public void addProperty(final String propName, final Class<?> propType, final boolean isMandatory, final boolean isStored, final boolean isExported, final Getter getter, final Setter setter)
    '''
def selectProperty():
    '''    public void selectProperty(final String propName)
    '''
def propertyCount():
    '''    public int propertyCount(final Selector select)
    '''
def exportedProperties():
    '''    public Property[] exportedProperties()
    '''
def equals():
    '''    public boolean equals(final Object o)
    '''
