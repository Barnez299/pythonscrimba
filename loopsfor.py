
names = ['john ClEEse','Eric IDLE','michael']
names1 = ['graHam chapman', 'TERRY', 'terry jones']

all_friends = names + names1


def party_invites():
    for name in all_friends:
        print(f'Hello {name.upper()} you are invited to my big party this coming saturday')


party_invites()