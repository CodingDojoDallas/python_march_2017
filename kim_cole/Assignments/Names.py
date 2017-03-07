students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

# Part I:

def show_students(arr):
    for fullName in students:
        print fullName['first_name'], fullName['last_name']

# Part II:        

def all(users):
    for role in users:
        counter = 0
        print role
        for person in users[role]:
            counter += 1
            first_name = person['first_name']
            last_name = person['last_name']
            length = len(person['first_name']) + len(person['last_name'])
            print "{} - {} {} - {}".format(counter, person['first_name'], person['last_name'], length)

show_students(students)
all(users)