try:
    open("abc.txt","r")
except IOError:
    pass

try:
    print aa
except NameError:
    pass


try:
    print aas
except NameError,msg:
    print msg
    
print "pass"

