students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
# Print all the students by first and last name
for i in students:
    print i['first_name'], i['last_name']
print "\n"      # Separate from second problem below

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
# Print all the students and instructors by first and last name, char count, and number
for key, data in users.items():
    print key
    count = 0
    for value in data:
        count += 1
        name = value['first_name'] + " " + value['last_name']
        print count, "-", name.upper() , "-", len(name)-1


# ALTERNATE METHOD

# def show_students(arr):
#     for x in students:
#         print x['first_name'], x['last_name']
#
# def show_all(users):
#     for role in users:
#         counter = 0
#         print role
#         for person in users[role]:
#             counter += 1
#             first_name = person['first_name']
#             last_name = person['last_name']
#             length = len(person['first_name']) + len(person['last_name'])
#             print "{} - {} {} - {}".format(counter, person['first_name'], person['last_name'], length)
#
# show_students(students)
# show_all(users)
