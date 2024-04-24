afro_beat_artists = ('Davido', 'Wizkid', 'Tiwa Savage', 'Flavor', 'Phyno')
print(afro_beat_artists[3])
print(afro_beat_artists[-3:])
print(afro_beat_artists[0:2])

y = list(afro_beat_artists)
y.append('Omah Lay')
afro_beat_artists = tuple(y)
print(afro_beat_artists)
another_afro_beat_artist = ('Odumuodu Black',)
afro_beat_artists += another_afro_beat_artist
print(afro_beat_artists)

artist1, artist2, artist3, artist4, artist5, artist6, artist7 = afro_beat_artists
# print(artist1)
# print(artist2)

for i in afro_beat_artists:
    print(i)

for x in afro_beat_artists:
    print(range(len(x)))

for m in range(len(afro_beat_artists)):
    print(afro_beat_artists[m])
print('6666666666666666666666666666666')
a = 0
while a < len(afro_beat_artists):
    print(afro_beat_artists[a])
    a+= 1

afro_beat_artists *= 3
print(afro_beat_artists)
print(afro_beat_artists.count('Phyno'))
print(afro_beat_artists.index('Phyno'))
