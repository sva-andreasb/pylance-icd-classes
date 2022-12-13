def CalendarBuilder():
'''public CalendarBuilder()
public CalendarBuilder(final CalendarParser parser)
public CalendarBuilder(final TimeZoneRegistry tzRegistry)
public CalendarBuilder(final CalendarParser parser, final TimeZoneRegistry tzRegistry)
public CalendarBuilder(final CalendarParser parser, final PropertyFactoryRegistry propertyFactoryRegistry, final ParameterFactoryRegistry parameterFactoryRegistry, final TimeZoneRegistry tzRegistry)
public CalendarBuilder(final CalendarParser parser, final Supplier<List<ParameterFactory<?>>> parameterFactorySupplier, final Supplier<List<PropertyFactory<?>>> propertyFactorySupplier, final Supplier<List<ComponentFactory<?>>> componentFactorySupplier, final TimeZoneRegistry tzRegistry)
'''
pass
def accept():
'''public void accept(final Calendar calendar)
'''
pass
def build():
'''public Calendar build(final InputStream in)
public Calendar build(final Reader in)
public Calendar build(final UnfoldingReader uin)
'''
pass
def getRegistry():
'''public final TimeZoneRegistry getRegistry()
'''
pass
