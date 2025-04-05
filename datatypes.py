x=2
print(x,type(x))# integer type of number

#next number type float
x=5.4
print(x,type(x))

#next number type complex

x=2-12j
print(x,type(x))

#STRING DATATYPE

s='hello#23'
print(s,type(s))

p=("hi@19")
print(p,type(p))

u='''my name si string 123'''
print(u,type(u))

q=''''this is not a string 0000'''
print(q,type(q))

#multi line data type they are immutable '''
o='''adi123
atu98
haha0000
hi'''
print(o,type(o))

s=10 # now 10 is integer because there is no any quotation
print(s,type(s))#o/p is integer

s='10' #coz of single quotation data type changed
print(s,type(s))#o/p is string



#list data type (muted datatype)

l=[12,'atish',7.5,1+2j]
l[0]=1 #index is 0 sho 12 will be replaced by 1
print(l,type(l))

#TUPLE DATA TYPE (IMMUTABLE)

t=(5,'program',1+3j)
print(t,type(t))

#Dictionary Data type
#eg:1

d={
    'course_name':'python',
    'course_duration':'2 Months'
}
print(d,type(d))
print(d['course_name'])
print(d['course_duration'])

#eg:2
c={
    'package_name':'BCA',
    'package_duration':'4 Years'
}
print(c['package_name'])
print(c,type(c))
print(c['package_duration'])


#eg:3

a={
    'students_name':'toilet',
    'students_address':'my house 123 ',
    'students_class':'bachelor 1st semister'
}
print(a['students_name'])
print(a['students_address'])

#eg:4 meri maya
m={
    'meri maya_name':'Chandra Bhatt',
    'meri maya_address':'Attariya',
    'meri maya ko ghar_name':'mero mutu ma',
    'meri maya mobile_no.':'98********'

}
print(m['meri maya_name'])
print(m['meri maya_address'])
print(m['meri maya ko ghar_name'])
print(m['meri maya mobile_no.'])

# data type set(immutable)

s={10,30,30,19,29}
print(s,type(s))
