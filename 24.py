def pokeGo(name, numberOfPokemon = 0):
    if numberOfPokemon == 0:
        return "You have caught no Pokemon, " + name
    elif numberOfPokemon < 5:
        return "You are just starting out, " + name
    elif numberOfPokemon < 250:
        return "You are getting better, " + name
    else:
        return "You are the very best, like no one ever was, " + name
print(pokeGo("NewGamer98"))
print(pokeGo("PokeMASTER222", numberOfPokemon = 100))
print(pokeGo("GaryFOak", 250))
