def VFreeBusy():
'''public VFreeBusy()
public VFreeBusy(final boolean initialise)
public VFreeBusy(final PropertyList properties)
public VFreeBusy(final DateTime start, final DateTime end)
public VFreeBusy(final DateTime start, final DateTime end, final TemporalAmount duration)
public VFreeBusy(final VFreeBusy request, final ComponentList<CalendarComponent> components)
'''
pass
def validate():
'''public final void validate(final boolean recurse)
'''
pass
def getContact():
'''public final Contact getContact()
'''
pass
def getStartDate():
'''public final DtStart getStartDate()
'''
pass
def getEndDate():
'''public final DtEnd getEndDate()
'''
pass
def getDuration():
'''public final Duration getDuration()
'''
pass
def getDateStamp():
'''public final DtStamp getDateStamp()
'''
pass
def getOrganizer():
'''public final Organizer getOrganizer()
'''
pass
def getUrl():
'''public final Url getUrl()
'''
pass
def getUid():
'''public final Uid getUid()
'''
pass
def start():
'''public BusyTimeBuilder start(final DateTime start)
public FreeTimeBuilder start(final DateTime start)
'''
pass
def end():
'''public BusyTimeBuilder end(final DateTime end)
public FreeTimeBuilder end(final DateTime end)
'''
pass
def components():
'''public BusyTimeBuilder components(final ComponentList<CalendarComponent> components)
public FreeTimeBuilder components(final ComponentList<CalendarComponent> components)
'''
pass
def build():
'''public FreeBusy build()
public FreeBusy build()
'''
pass
def Factory():
'''public Factory()
'''
pass
def createComponent():
'''public VFreeBusy createComponent()
public VFreeBusy createComponent(final PropertyList properties)
public VFreeBusy createComponent(final PropertyList properties, final ComponentList subComponents)
'''
pass
