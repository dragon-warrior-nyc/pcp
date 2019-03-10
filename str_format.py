# basics
s1 = "so much depends upon {}".format("a red wheel barrow")
s2 = "glazed with {} water beside the {} chickens".format("rain", "white")
print(s1)
print(s2)

# formatting a floating point number
pi = 3.14159
print(" pi = %1.2f" % pi) # old
print(" pi = {:.2f}".format(pi)) # new

# multiple substitutions
s1 = 'cats'
s2 = 'dogs'
s3 = '%s and %s living together' % (s1, s2)
s4 = '{} and {} living together'.format(s1, s2)

set = " ({0}, {1}) ".format(s1, s2)

# named arguments
madlib = " I {verb} the {object} off the {place} ".format(verb="took", object="cheese", place="table")
print(madlib)

# use {} inside {}
pi = 3.1415926
precision = 4
print("{:.{}f}".format(pi, precision))

# convert values to different bases
print("{0:d} - {0:x} - {0:o} - {0:b}".format(21))
print("{0:d} - {0:x} - {0:o} - {0:b}".format(-21))

# use format as a function
email_f = "Your email address was {email}.".format
print(email_f(email="bob@example.com"))

# escaping braces
print(" The {} set is often represented as {{0}}".format("empty"))

# https://mkaz.blog/code/python-string-format-cookbook/
