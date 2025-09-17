def array_of_names(persons):
    result = []
    for first, last in persons.items():
        fullname = first.capitalize() + " " + last.capitalize()
        result.append(fullname)
    return result

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))
