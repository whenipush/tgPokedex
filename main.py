import pokebase as pb



def print_info(id):
    pokemon = pb.pokemon(id)
    a = f'{pokemon}'.title()
    return a

def print_img(id):
    img = pb.SpriteResource('pokemon', id)
    img = img.url
    return img

print(print_info(1))
print(print_img(1))