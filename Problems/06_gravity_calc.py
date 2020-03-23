# Universal Gravity Calculator (12pts)
# In physics, the force of gravity between two objects can be calculated using the equation:
# F = G * (m1 * m2) / r ** 2
# F is the force of gravity in Newtons
# G is the universal gravity constant (6.67e-11)
# m1 is the mass of first object in kg
# m2 is the mass of the second object in kg
# r is the center to center distance between the objects in meters

# Make a calculator that does all of the following
# (3pts) takes the inputs for mass 1, mass 2, and distance between the two objects (m1, m2, and r)
# (4pts) contains exceptions for any potential errors (value and dividebyzero).
# (2pts) keeps asking for inputs until they are valid (see while loop from notes)
# (3pts) calculates the force of gravity in Newtons and print the result to the user in scientific notation to two decimals.

done = False
G = 6.67e-11


def force_of_gravity(mass1, mass2, distance):
    answer = G * (mass1 * mass2) / distance ** 2
    return answer


while not done:
    try:
        m1 = float(input("Enter mass one: "))
        m2 = float(input("Enter mass two: "))
        r = float(input("Enter the distance between two objects: "))
        force_of_gravity = force_of_gravity(m1, m2, r)
        print("The force of gravity is {:.2e}".format(force_of_gravity), "newtons.")
        done = True
    except ValueError:
        print("value error")
        done = False
    except ZeroDivisionError:
        print("zero error")
        done = False





