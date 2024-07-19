from handlers_error import input_error

@input_error
def add_contact(args, contacts):
    """
    Add a contact with the specified name and phone number to the contacts dictionary.

    Args:
    - args (list): A list containing two elements: name and phone.
    - contacts (dict): Dictionary containing contacts where the new contact will be added.

    Returns:
    - str: A message indicating whether the contact was successfully added or already exists.

    Raises:
    - KeyError: If the contact name is not found in the dictionary.
    - IndexError: If `args` has fewer than 2 elements.

    Decorators:
    - input_error: Handles exceptions and provides user-friendly error messages.
    """
    name, phone = args
    if name not in contacts:
        contacts[name] = phone
        return "Contact added."
    else:
        return "Contact already added."

@input_error
def change_contact(args, contacts):
    """
    Change the phone number of an existing contact in the contacts dictionary.

    Args:
    - args (list): A list containing two elements: name and phone.
    - contacts (dict): Dictionary containing contacts where the contact will be updated.

    Returns:
    - str: A message indicating whether the contact was successfully updated or not found.

    Raises:
    - ValueError: If the number of arguments in `args` is not equal to 2.
    - IndexError: If `args` has fewer than 2 elements.
    - KeyError: If the contact name is not found in the dictionary.

    Decorators:
    - input_error: Handles exceptions and provides user-friendly error messages.
    """
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact changed."
    else:
        return f"Contact '{name}' not found."

@input_error
def show_phone(args, contacts):
    """
    Retrieve the phone number of a contact from the contacts dictionary.

    Args:
    - args (list): A list containing one element: name.
    - contacts (dict): Dictionary containing contacts.

    Returns:
    - str: The phone number of the contact, or a message indicating the contact was not found.

    Raises:
    - KeyError: If the contact name is not found in the dictionary.
    - ValueError: If `args` is empty or contains more than one element.

    Decorators:
    - input_error: Handles exceptions and provides user-friendly error messages.
    """
    if not args or len(args) != 1:
        raise ValueError()
    
    name = args[0]
    return contacts.get(name, f"Contact '{name}' not found.")

@input_error
def show_all_contacts(contacts):
    """
    Retrieve a formatted string listing all contacts and their phone numbers.

    Args:
    - contacts (dict): Dictionary containing contacts to display.

    Returns:
    - str: A formatted string listing all contacts and their phone numbers, or a message indicating no contacts are available.

    Decorators:
    - input_error: Handles exceptions and provides user-friendly error messages.
    """
    if contacts:
        contact_list = "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
        return f"Contacts:\n{contact_list}"
    else:
        return "No contacts available."