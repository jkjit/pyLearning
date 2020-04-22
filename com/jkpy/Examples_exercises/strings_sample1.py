

x = "car bat ball apple"
y = x.split()

print(y)
x = "car,bat,ball,apple"
y=x.split(',')
y = x.split()
print(type(y))
print(y)


a,b,c,d  = x.split(',')

print(a,b,c,d)

data = "6,8 2,6,2,6 3,0,6,4 7,8,6,4 4,3,3,0 4,3"
data_1 = data.split(',')
print(data_1)


input_list = [1,2.5,'A', 'R', 23, 55.5]

int_list =[]
char_list =[]
float_list =[]
for entry in input_list:
    print("entry :{} and its type is :{}".format(entry,type(entry)))
    if type(entry) == int:
        int_list.append(entry)
    elif type(entry) == float:
        float_list.append(entry)
    elif type(entry) == str:
        char_list.append(entry)


print(int_list,char_list,float_list)


x1=[y for y in input_list if type(y)==int]

print(x1)

y1=[y for y in input_list if type(y)==float]
print(y1)



data2= ""