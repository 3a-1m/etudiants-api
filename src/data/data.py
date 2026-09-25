STUDENTS = [
    {
        "id": 1,
        "firstName": "Bob",
        "lastName": "Marley",
        "email": "bob.marley@hexagone.fr",
        "grade": 15,
        "field":"chimie"
    },
    {
        "id": 2,
        "firstName": "Alice",
        "lastName": "Merveille",
        "email": "alice.merveille@hexagone.fr",
        "grade": 7,
        "field":"Physique"
    },
    {
        "id": 3,
        "firstName": "Lucas",
        "lastName": "paqueta",
        "email": "lucas.paqueta@hexagone.fr",
        "grade": 12,
        "field":"Physique"
    },
    {
        "id": 4,
        "firstName": "Joseph",
        "lastName": "Joestar",
        "email": "joseph.joestar@hexagone.fr",
        "grade": 10,
        "field":"Informatique"
    },
    {
        "id": 5,
        "firstName": "Mark",
        "lastName": "Evans",
        "email": "mark.evans@hexagone.fr",
        "grade": 20,
        "field":"Mathématiques"
    },
]
next_id = 6

def get_next_id():
    global next_id
    current_id = next_id
    next_id += 1
    return current_id

def reset_data():
    """Réinitialise les données pour les tests."""
    global STUDENTS, next_id
    STUDENTS.clear()
    STUDENTS.extend(
        [
            {
                "id": 1,
                "firstName": "Bob",
                "lastName": "Marley",
                "email": "bob.marley@hexagone.fr",
                "grade": 15,
                "field":"chimie"
            },
            {
                "id": 2,
                "firstName": "Alice",
                "lastName": "Merveille",
                "email": "alice.merveille@hexagone.fr",
                "grade": 7,
                "field":"Physique"
            },
            {
                "id": 3,
                "firstName": "Lucas",
                "lastName": "paqueta",
                "email": "lucas.paqueta@hexagone.fr",
                "grade": 12,
                "field":"Physique"
            },
            {
                "id": 4,
                "firstName": "Joseph",
                "lastName": "Joestar",
                "email": "joseph.joestar@hexagone.fr",
                "grade": 10,
                "field":"Informatique"
            },
            {
                "id": 5,
                "firstName": "Mark",
                "lastName": "Evans",
                "email": "mark.evans@hexagone.fr",
                "grade": 20,
                "field":"Mathématiques"
            },
        ]
    )
next_id = 6
