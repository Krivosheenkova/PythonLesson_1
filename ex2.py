# Ex. 2
user_seconds = (input('Enter time(sec): '))
hours = int(user_seconds) // 3600
minutes = int(user_seconds) // 60
seconds = int(user_seconds) % 60

print('{0}:{1}:{2}'.format(hours, minutes, seconds))
