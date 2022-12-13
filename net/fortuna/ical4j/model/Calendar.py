BEGIN = "String  \"BEGIN\""
VCALENDAR = "String  \"VCALENDAR\""
END = "String  \"END\""
def Calendar():
    '''    public Calendar()
    public Calendar(final ComponentList<CalendarComponent> components)
    public Calendar(final PropertyList<Property> properties, final ComponentList<CalendarComponent> components)
    public Calendar(final PropertyList<Property> p, final ComponentList<CalendarComponent> c, final Validator<Calendar> validator)
    public Calendar(final Calendar c)
    '''
def toString():
    '''    public final String toString()
    '''
def getComponents():
    '''    public final ComponentList<CalendarComponent> getComponents()
    public final <C extends CalendarComponent> ComponentList<C> getComponents(final String name)
    '''
def getComponent():
    '''    public final CalendarComponent getComponent(final String name)
    '''
def getProperties():
    '''    public final PropertyList<Property> getProperties()
    public final PropertyList<Property> getProperties(final String name)
    '''
def getProperty():
    '''    public final <T extends Property> T getProperty(final String name)
    '''
def validate():
    '''    public final void validate()
    public void validate(final boolean recurse)
    '''
def getProductId():
    '''    public final ProdId getProductId()
    '''
def getVersion():
    '''    public final Version getVersion()
    '''
def getCalendarScale():
    '''    public final CalScale getCalendarScale()
    '''
def getMethod():
    '''    public final Method getMethod()
    '''
def equals():
    '''    public final boolean equals(final Object arg0)
    '''
def hashCode():
    '''    public final int hashCode()
    '''
