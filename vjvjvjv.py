def game():
    progress = True
    word = ['привет','сус','превысокомногорассмотрительствующий','несколько','слово']
    lifes = 10
    word_in_play = get_word(word)
    template = start_template(word_in_play)
    welcome_speech(template)
    while progress:
        user_guess = input('введите букву:')
        template = build_template(template, word_in_play, user_guess)
        print(template)
        progress = check_win(template)
        if user_guess not in word_in_play:
            lifes -= 1
            print(f'осталось {lifes} осталось попытки')
        if lifes == 0:
            print('ВЫ ПРОИГРАЛИ ХОХОХОХОХОХХОХОХОХОХОХОХОХО')
            break
def get_word(w):
    return w[0]
def start_template(w):
    return len(w)*'_'
def welcome_speech(t):
    print(f'''Здравствуй сырник загаданное слово состоит из {len(t)}' букв {t}''') 
def build_template(t, w, usges):
    t = list(t)
    for i in range(len(w)):
        if t[i] == '_':
            if w[i] == usges:
                t[i] = w[i]
            else:
                t[i] = '_'
    return t 
def check_win(t):
    if '_' not in t:
        return False
    else:
        return True

game()