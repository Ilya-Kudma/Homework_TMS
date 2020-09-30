pupils = [
    {
        'firstname': 'Ilya',
        'group': '743',
        'physics': 3,
        'informatics': 4,
        'history': 3,
    },
    {
        'firstname': 'Alex',
        'group': '74',
        'physics': 8,
        'informatics': 10,
        'history': 4,
    },
    {
        'firstname': 'Darya',
        'group': '45',
        'physics': 5,
        'informatics': 4,
        'history': 2,
    },
    {
        'firstname': 'Marya',
        'group': '93',
        'physics': 6,
        'informatics': 4,
        'history': 7,
    },
    {
        'firstname': 'Polina',
        'group': '43',
        'physics': 7,
        'informatics': 7,
        'history': 8,
    },
    {
        'firstname': 'Andrei',
        'group': '116',
        'physics': 6,
        'informatics': 8,
        'history': 7,
    },
]
for element in pupils:
    for elem in element:
        physics = element['physics']
        informatics = element['informatics']
        history = element['history']
        average = (physics + informatics + history) / 3
    if average > 4.0:
        print(element, f'Average: {average}')
