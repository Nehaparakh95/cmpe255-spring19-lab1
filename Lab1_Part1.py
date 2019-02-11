users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}
]

friendship = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (6, 7),
    (6, 8),
    (7, 8),
    (8, 9)
]


def num_of_friends(user):
    number = 0
    id = 0

    for k in users:
        if k["name"] == user:
            id = k["id"]

    for j in friendship:
        for i in j:
            if i == id:
                number += 1
    return number


def sort_by_num():
    friends = []
    for i in users:
        friends.append((num_of_friends(i["name"]), i["name"]))
    friends.sort(reverse=True)
    return friends


list_friends = sort_by_num()
for i in list_friends:
    print('{} has {} friends'.format(i[1], i[0]))
