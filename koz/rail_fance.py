def en_rail_fance(text, rails):
    rail = [[] for _ in range(rails)]
    rail_num = 0
    direction = 1

    for char in text:
        rail[rail_num].append(char)
        if rail_num == 0:
            direction = 1
        elif rail_num == rails - 1:
            direction = -1
        rail_num += direction

    en_text = ''.join([''.join(rail) for rail in rail])
    return en_text

def de_rail_fance(text, rails):
    rail_len = [0] * rails
    rail_num = 0
    direction = 1

    for i in range(len(text)):
        rail_len[rail_num] += 1
        if rail_num == 0:
            direction = 1
        elif rail_num == rails - 1:
            direction = -1
        rail_num += direction

    rail = [''] * rails
    start = 0

    for i in range(rails):
        rail[i] = text[start:start + rail_len[i]]
        start += rail_len[i]

    rail_num = 0
    direction = 1
    de_text = ''

    for _ in range(len(text)):
        de_text += rail[rail_num][0]
        rail[rail_num] = rail[rail_num][1:]
        if rail_num == 0:
            direction = 1
        elif rail_num == rails - 1:
            direction = -1
        rail_num += direction

    return de_text

text = "lukas baborak smrdi"
rails = 3

en_text = en_rail_fance(text, rails)
print("zašifrovaný text:", en_text)

de_text = de_rail_fance(en_text, rails)
print("dešifrovaný text:", de_text)

