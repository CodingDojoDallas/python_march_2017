def names(arr):
    for each in arr:
        # print each
        print '{} {}'.format(each['first_name'], each['last_name'])


students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

# names(students)


def dictionary_names(obj):
    for key, data in obj.items():
        print key
        count = 1
        for each in data:
            print '{} - {} {} - {}'.format(count, each['first_name'], each['last_name'], len( each['first_name'])+len( each['last_name']))
            count += 1

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

dictionary_names(users)
