def clean(text: str) -> str:
    """
    returns a string with numbers removed, then edge whitespace trimmed, for user readability
    """
    builder = ''
    for c in text:
        if not c.isdigit():
            builder += c
    return builder.strip()


def get_file_contents(name: str) -> str:
    with open(name, 'r') as file:
        return file.read()


def create_dict(text: str, before: str = '{', after: str = '}') -> dict:
    """
    creates a dictionary of keys with the strings between 'before' and 'after' within the provided text
    the values of the dictionary are set to None
    note: 'before' and 'after' must be only one character long
    """
    dictionary = {}
    within = False
    for c in text:
        if c == before:
            within = True
            current_key = ''
        elif within:
            if c == after:
                within = False
                # noinspection PyUnboundLocalVariable
                dictionary[current_key] = None
            else:
                current_key += c
    return dictionary


def get_values_from_user(dictionary: dict) -> None:
    """
    goes through the dictionary's keys and asks the user for the values
    runs keys through the clean function before prompting the user with them.
    """
    for k in dictionary:
        dictionary[k] = input("Enter a " + clean(k) + ": ")


def replace_keys_with_values(text: str, dictionary: dict, prepend: str = '{', append: str = '}') -> str:
    for k, v in dictionary.items():
        text = text.replace(prepend + k + append, v)
    return text


def handle_mad_lib(file_name: str):
    mad_lib = get_file_contents(file_name)
    mad_lib_dict = create_dict(mad_lib)
    get_values_from_user(mad_lib_dict)
    mad_lib = replace_keys_with_values(mad_lib, mad_lib_dict)
    print(mad_lib)


handle_mad_lib("Lib.txt")
