def get_crypt_text(text, number):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    symbols = "~!@#$%^&*()_-=+{}|:\"?<>[];'/.,0123456789"
    entered_text = text
    displace = number

# Validation of displace and text entered by user
    if not entered_text:
        crypted_text = "Enter text"
        return crypted_text
    for char in entered_text:
        if char in symbols:
            crypted_text = "Only english character are allowed"
            return crypted_text
    entered_text = entered_text.replace("\r\n", " ")
    if not entered_text.islower():
        entered_text = entered_text.lower()
    if not displace:
        displace = 0
    if not displace.isdigit():
        return "Invalid displacement"
    displace = int(displace)
    if displace < 0:
        displace = abs(displace)
    if displace > 26:
        displace %= 26

# Associating dict with the position in the alphabet
    associated_dict = {}
    alphabet_counter = 0
    for i in alphabet:
        alphabet_counter += 1
        collect_dict = {i: alphabet_counter}
        associated_dict.update(collect_dict)

# Finding and storing the positions of whitespace in the entered text
    et_count = 0
    space_position = []
    letter_position = []
    for i in entered_text:
        et_count += 1
        if i == " ":
            i == i.replace(' ', '')
            space_position.append(et_count)
            continue
        j = associated_dict.get(i)
        letter_position.append(j)

    associated_dict = invert_dict(associated_dict)
    lp_count = 0  # Counter for the return of whitespaces to its position in the ciphertext
    lp_iter = 0
    code_list = []  # List to collect the ciphertext and whitespaces
    for i in letter_position:
        lp_count += 1
        for j in space_position:  # Cycle for the return whitespaces
            if j == lp_count:     # to its position in the ciphertext
                code_list += ' '
                lp_count += 1
        v = letter_position[lp_iter]  # Take the position of each
        v += displace                 # letter and add the displace
        if v > 26:
            v -= 26
        result = associated_dict.get(v)  # Get the letter displace
        code_list += result              # from the associated_dict
        lp_iter += 1
    crypted_text = ''.join(code_list)  # Transfer list in a string
    return crypted_text


def invert_dict(inv_dict):
    inv = dict()
    for key in inv_dict:
        val = inv_dict[key]
        if val not in inv:
            inv[val] = [key]
        else:
            inv[val].append(key)
    return inv


def symbol_count(code_text):
    count_dict = {}
    code_text = code_text.replace(' ', '')
    for char in code_text:  # Cycle to count the number of letters
        count_dict[char] = code_text.count(char)

    # To obtain an acceptable format for the list of chart
    cort = count_dict.items()
    final_list = []
    for i in cort:
        res = list(i)
        final_list.append(res)
    return final_list

