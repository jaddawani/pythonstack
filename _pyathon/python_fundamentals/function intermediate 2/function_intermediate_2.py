x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
x[1][0]=15
print(x[1])
students[0]['last_name']='bryan'
print (students[0])

sports_directory['soccer'][0]='ronaldo'
print(sports_directory['soccer'])

z[0]['y']=30
print(z[0])




students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
     

print(students)

def iterate(students):
    for i in range(0,len(students),1):
    	for key,value in students[i].items():
        	print(f" {key} - {value}", end=",")
            
            
           
        	
    return students
iterate(students)



students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
     

print(students)

def iterate(students):
    for i in range(0,len(students),1):
    	for key,value in students[i].items():
        	print( value )
            
            
           
        	
    return students
iterate(students)



students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
     

print(students)

def iterate(students):
    for i in range(0,len(students),1):
    	
        	print( students[i]['first_name'] )
            
            
           
        	
    return students
iterate(students)



students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
     

print(students)

def iterate(students):
    for i in range(0,len(students),1):
    	
        	print( students[i]['last_name'] )
            
            
           
        	
    return students
iterate(students)




dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def hello(dict):
    for key in dict:
        print(len(key))    	
    return dict
hello(dojo)




dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def hello(dict):
    for key in dict:
        print(len(dict[key]), key.upper()) 
        for value in dict[key]:
        	print(value)
        
    return dict
hello(dojo)