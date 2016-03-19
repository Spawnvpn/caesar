SYMBOLS_TO_IGNORE = "~!@#$%^&*()_-=+{}|:\"?<>[];'/.,0123456789 "


def get_crypt_text(text, number):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    entered_text = text
    displace = number

    # Validation of displace and text entered by user
    if not entered_text:
        return "Enter text"
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

    # Finding and storing the positions of symbols in the entered text
    et_count = 0
    symbol_position = {}
    letter_position = []
    for char in entered_text:
        et_count += 1
        if char in SYMBOLS_TO_IGNORE:
            tempo = dict.fromkeys([et_count], char)
            symbol_position.update(tempo)
            continue
        j = associated_dict.get(char)
        letter_position.append(j)

    associated_dict = invert_dict(associated_dict)
    # Counter for the return of symbols to its position in the ciphertext
    lp_count = 0
    lp_iter = 0
    code_list = []  # List to collect the ciphertext and symbols
    dynamic_sp = symbol_position.copy()
    for i in letter_position:
        lp_count += 1
        for j in symbol_position:  # Cycle for the return symbols
            if j == lp_count:      # to its position in the ciphertext
                code_list += dynamic_sp.pop(j)
                lp_count += 1
        v = letter_position[lp_iter]  # Take the position of each
        v += displace                 # letter and add the displace
        if v > 26:
            v -= 26
        result = associated_dict.get(v)  # Get the letter displace
        code_list += result              # from the associated_dict
        lp_iter += 1
    crypted_text = ''.join(code_list)  # Transfer list in a string
    for i in dynamic_sp:
        crypted_text += symbol_position[i]
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

    for char in code_text:  # Cycle to count the number of letters
        if char not in SYMBOLS_TO_IGNORE:
            count_dict[char] = code_text.count(char)

    # To obtain an acceptable format for the list of chart
    cort = count_dict.items()
    final_list = []
    for i in cort:
        res = list(i)
        final_list.append(res)
    return final_list

