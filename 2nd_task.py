cheta = 0
chidera = 0

cheta_height = 50
cheta_mass = 30

chidera_height = 25
chidera_mass = 10

def get_result (mass , height):
    return mass/(height*height);
cheta = get_result(cheta_mass , cheta_height);
print(cheta);
chidera = get_result(chidera_mass , chidera_height);
print(chidera);
if cheta > chidera:
    print("cheta");
else:
    print("chidera")