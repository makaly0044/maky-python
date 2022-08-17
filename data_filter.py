DATA = [
    {
        "name": "Anthony",
        "last name": "Justiniano",
        "age": 27,
        "Ingeniería": "Ing. Redes y Telecomunicaciones"
    },
    {
        "name": "Makaly",
        "last name": "Amutari",
        "age": 22,
        "Ingeniería": "Ing. Sistemas"
    },
    {
        "name": "Maky",
        "last name": "mk4",
        "age": 19,
        "Ingeniería": "Ing. Electrónica"
    }
]

def run():
    # Filtrado por edad traer nombre
    age_filter_name = list(filter(lambda people: people["age"] >= 20, DATA))
    age_filter_name = list(map(lambda name: name["name"], age_filter_name))
    
    for name in age_filter_name:
        print(name)




if __name__== '__main__':
    run()