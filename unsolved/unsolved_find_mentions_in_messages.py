"""
Find mentions of users in messages
single mention @id7
multi mention @id7,id8

First mention doesn't have to be valid
Only count once per message
"""
messages = ['hi @id1,id2 how are you? @id2 go fuck yourself',
            'id1,@id2']
users = ['id1', 'id2', 'id3']
# def solution(users, mentions):
counts = {}
for user in users:
    counts[user] = 0

for message in messages:
    # find all @'s in message
    indices = [i for i, letter in enumerate(message) if letter == '@']
