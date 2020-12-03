# Example 1: How to create a nested dictionary

people = {1: {'name': 'Jhon', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'female'}
}
print(people)

# Example 2: Access the elements using the [] syntax
print(people[1]['name'])
print(people[1]['age'])
print(people[1]['sex'])

# Example 3: How to change or add elements in a nested dictionary?
people[3] = {}

people[3]['name'] = 'Luna'
people[3]['age'] = '24'
people[3]['sex'] = 'Female'
people[3]['married'] = 'No'

print(people[3])
# print(people)

# Example 4: Add another dictionary to the nested dictionary
people[4] = {'name': 'Peter', 'age': '29', 'sex': 'Male', 'married': 'Yes'}
print(people[4])

# Example 5: How to delete elements from a nested dictionary?
del people[3]['married']
del people[4]['married']

print(people[3])
print(people[4])

# Example 6: How to delete dictionary from a nested dictionary?
del people[3], people[4]
print(people)

# Example 7: How to iterate through a Nested dictionary?
for p_id, p_info in people.items():
    print("\nPerson ID: ", p_id)

    for key in p_info:
        print(key + ':', p_info[key])