obj = {"name": "Thrall", "class": "Shaman", "level": 50}
print(
    f"Nombre de personaje: { {key: value for key, value in obj.items() if key == 'name'}}"
)

list = ["Marine", "Ventormenta Guard", "Mecha Robot"]
print(f"lista de personajes: {[char for char in list if len(char) < 10]}")