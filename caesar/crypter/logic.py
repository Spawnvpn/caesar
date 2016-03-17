def invert_dict(inv_dict):
    inv = dict()
    for key in inv_dict:
        val = inv_dict[key]
        if val not in inv:
            inv[val] = [key]
        else:
            inv[val].append(key)
    return inv


def get_crypt_text(text, number):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    entered_text = text
    displace = number

    if not entered_text:
        return "Enter text"
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

    inv_dict = {}
    alphabet_counter = 0
    for i in alphabet:
        alphabet_counter += 1
        associated_dict = {i: alphabet_counter}
        inv_dict.update(associated_dict)
    et_count = 0
    space_position = []
    letter_position = []
    for i in entered_text:
        et_count += 1
        if i == " ":
            i == i.replace(' ', '')
            space_position.append(et_count)
            continue
        j = inv_dict.get(i)
        letter_position.append(j)

    inv_dict = invert_dict(inv_dict)
    lp_count = 0
    lp_iter = 0
    code_list = []
    for i in letter_position:
        lp_count += 1
        for j in space_position:
            if j == lp_count:
                code_list += ' '
                lp_count += 1
        v = letter_position[lp_iter]
        v += displace
        if v > 26:
            v -= 26
        result = inv_dict.get(v)
        code_list += result
        lp_iter += 1
    crypted_text = ''.join(code_list)
    return crypted_text


def symbol_count(code_text):
    symbols = code_text
    count_dict = {}
    for i in symbols:
        symbols.count(i)
        if not i in count_dict:
            count_dict[i] = 0
        count_dict[i] += 1
        symbols = symbols.split(i)
        t = symbols
        symbols = ''
        for j in t:
            if not j == i:
                symbols += j
    cort = count_dict.items()
    list = []
    res = []
    for i in cort:
        res[:] = i
        list.append(res[:])
    return list

