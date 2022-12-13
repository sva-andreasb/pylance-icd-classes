def helo():
'''public static SmtpRequest helo(final CharSequence hostname)
'''
pass
def ehlo():
'''public static SmtpRequest ehlo(final CharSequence hostname)
'''
pass
def empty():
'''public static SmtpRequest empty(final CharSequence... parameter)
'''
pass
def auth():
'''public static SmtpRequest auth(final CharSequence... parameter)
'''
pass
def noop():
'''public static SmtpRequest noop()
'''
pass
def data():
'''public static SmtpRequest data()
'''
pass
def rset():
'''public static SmtpRequest rset()
'''
pass
def help():
'''public static SmtpRequest help(final String cmd)
'''
pass
def quit():
'''public static SmtpRequest quit()
'''
pass
def mail():
'''public static SmtpRequest mail(final CharSequence sender, final CharSequence... mailParameters)
'''
pass
def rcpt():
'''public static SmtpRequest rcpt(final CharSequence recipient, final CharSequence... rcptParameters)
'''
pass
def expn():
'''public static SmtpRequest expn(final CharSequence mailingList)
'''
pass
def vrfy():
'''public static SmtpRequest vrfy(final CharSequence user)
'''
pass
