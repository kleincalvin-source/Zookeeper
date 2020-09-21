""" figure out if a movie theatre can hold a given number of
viewers that plan to visit it on a particular day """

# define variables

number_of_halls = int(input())
capacity_of_halls = int(input())
number_of_viewers = int(input())

# define conditions

""" if number of halls and capacity can hold given number of viewers
then print True, else if it cant hold print False """

if (number_of_halls * capacity_of_halls) >= number_of_viewers:
    print(True)
else:
    print(False)










