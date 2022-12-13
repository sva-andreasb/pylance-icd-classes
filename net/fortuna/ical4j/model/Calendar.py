BEGIN = "String  BEGIN""
VCALENDAR = "String  VCALENDAR""
END = "String  END""
def Calendar():
'''public Calendar()
public Calendar(final ComponentList<CalendarComponent> components)
public Calendar(final PropertyList<Property> properties, final ComponentList<CalendarComponent> components)
public Calendar(final PropertyList<Property> p, final ComponentList<CalendarComponent> c, final Validator<Calendar> validator)
public Calendar(final Calendar c)
'''
pass
def toString():
'''public final String toString()
'''
pass
def getComponents():
'''public final ComponentList<CalendarComponent> getComponents()
public final <C extends CalendarComponent> ComponentList<C> getComponents(final String name)
'''
pass
def getComponent():
'''public final CalendarComponent getComponent(final String name)
'''
pass
def getProperties():
'''public final PropertyList<Property> getProperties()
public final PropertyList<Property> getProperties(final String name)
'''
pass
def getProperty():
'''public final <T extends Property> T getProperty(final String name)
'''
pass
def validate():
'''public final void validate()
public void validate(final boolean recurse)
'''
pass
def getProductId():
'''public final ProdId getProductId()
'''
pass
def getVersion():
'''public final Version getVersion()
'''
pass
def getCalendarScale():
'''public final CalScale getCalendarScale()
'''
pass
def getMethod():
'''public final Method getMethod()
'''
pass
def equals():
'''public final boolean equals(final Object arg0)
'''
pass
def hashCode():
'''public final int hashCode()
'''
pass
