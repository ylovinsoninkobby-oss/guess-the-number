import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'1 から {x} の間の数字を予想してください: '))
        if guess < random_number:
            print('残念、もっと大きい数字です。')
        elif guess > random_number:
            print('残念、もっと小さい数字です。')

    print(f'おめでとうございます！ 正解は {random_number} でした！')

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # low = high の場合はどちらでも同じ
        feedback = input(f'{guess} は高すぎますか (H)、低すぎますか (L)、正解ですか (C)？ ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'やった！ コンピュータはあなたの数字 {guess} を当てました！')


guess(10)
