distance_mi = 25
is_raining = True
has_bike = False
has_car = True
has_ride_share_app = False

if distance_mi:
    print(False)
else:
    print(True)

if distance_mi >= 1 and is_raining:
    print('True')
else:
    print('False')

if distance_mi > 1 and distance_mi <= 6 and has_bike and is_raining == False:
    print('True')
else:
    print('False')

if distance_mi > 6 and has_car:
    print('True')
elif has_ride_share_app:
    print('True')
else:
    print('False')