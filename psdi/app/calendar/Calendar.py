def Calendar():
'''public Calendar(final MboSet ms)
'''
pass
def init():
'''public void init()
'''
pass
def generateAutoKey():
'''public void generateAutoKey()
'''
pass
def isAvailable():
'''public boolean isAvailable(final Date date)
'''
pass
def appValidate():
'''public void appValidate()
'''
pass
def duplicate():
'''public MboRemote duplicate()
'''
pass
def canDelete():
'''public void canDelete()
'''
pass
def delete():
'''public void delete(final long accessModifier)
'''
pass
def canApplyShift():
'''public void canApplyShift(final ShiftRemote shift)
public void canApplyShift(final String shiftname)
'''
pass
def applyShift():
'''public void applyShift(final Vector shiftSet)
public void applyShift(final String shiftname)
public void applyShift(final String shiftname, final Date startdate, final Date enddate)
'''
pass
def setWPIncrement():
'''public void setWPIncrement(final int i)
'''
pass
def applyNonWorkTime():
'''public boolean applyNonWorkTime(final MboSetRemote nonWorkTimeSet)
public void applyNonWorkTime(final String nonWorkType, final String description, final Date startDate, final Date endDate)
'''
pass
def calculateAvailability():
'''public double calculateAvailability()
public double calculateAvailability(final Date startDate, final Date endDate)
'''
pass
def calculateHours():
'''public double calculateHours(final Date date1, final Date date2)
'''
pass
def calculateDownTime():
'''public double calculateDownTime(final Date lastChangeDate, final Date currentChangeDate)
'''
pass
def getDownTime():
'''public double getDownTime(final Date currentChangeDate, final Date lastChangeDate)
public double getDownTime(final Date currentChangeDate, final Date lastChangeDate, final TimeZone tz)
'''
pass
def getWorkPeriodData():
'''public double getWorkPeriodData(final WorkPeriodSet workPeriodSet, final Date lastChangeDate, final Date currentChangeDate)
public double getWorkPeriodData(final WorkPeriodSet workPeriodSet, final Date lastChangeDate, final Date currentChangeDate, final TimeZone tz)
'''
pass
def addDates():
'''public Date addDates(final Date date, final int days)
'''
pass
def combineDateTime():
'''public Date combineDateTime(final Date date, final Date time)
public Date combineDateTime(final Date date, final Date time, final TimeZone tz)
'''
pass
def deleteWorkPeriod():
'''public void deleteWorkPeriod(final Date startDate, final Date endDate)
'''
pass
def calculateWorkHours():
'''public double calculateWorkHours(final Date workDate)
'''
pass
def getWorkPeriodSet():
'''public WorkPeriodSetRemote getWorkPeriodSet(final Date workDate)
'''
pass
def getMonthsAvailableHours():
'''public String[][] getMonthsAvailableHours(final com.ibm.icu.util.Calendar cal)
'''
pass
def add():
'''public void add()
'''
pass
