import random

def choose_difficulty():
    print("\nВыбери уровень сложности:")
    print("1. Легкий (1-50, 10 попыток)")
    print("2. Средний (1-100, 7 попыток)")
    print("3. Сложный (1-200, 5 попыток)")
    
    while True:
        choice = input("Твой выбор (1/2/3): ")
        if choice == "1":
            return 50, 10
        elif choice == "2":
            return 100, 7
        elif choice == "3":
            return 200, 5
        else:
            print("Введи 1, 2 или 3.")

def play_game():
    print("=" * 40)
    print("   ИГРА 'УГАДАЙ ЧИСЛО'")
    print("=" * 40)
    
    max_number, max_attempts = choose_difficulty()
    secret = random.randint(1, max_number)
    attempts = 0
    
    print(f"\nЯ загадал число от 1 до {max_number}.")
    print(f"У тебя {max_attempts} попыток. Удачи!\n")
    
    while attempts < max_attempts:
        attempts += 1
        remaining = max_attempts - attempts
        
        try:
            guess = int(input(f"Попытка {attempts}/{max_attempts}. Введи число: "))
        except ValueError:
            print("Это не число! Попробуй снова.")
            attempts -= 1
            continue
        
        if guess < 1 or guess > max_number:
            print(f"Число должно быть от 1 до {max_number}!")
            attempts -= 1
            continue
        
        if guess < secret:
            print(f"Больше! Осталось попыток: {remaining}")
        elif guess > secret:
            print(f"Меньше! Осталось попыток: {remaining}")
        else:
            print(f"\n🎉 Поздравляю! Ты угадал число {secret} за {attempts} попыток!")
            return True
    
    print(f"\n😔 Попытки закончились. Было загадано число {secret}.")
    return False

def main():
    wins = 0
    games = 0
    
    while True:
        games += 1
        if play_game():
            wins += 1
        
        print(f"\nСчёт: {wins} побед из {games} игр.")
        again = input("Сыграть ещё? (да/нет): ").lower()
        if again not in ("да", "д", "yes", "y"):
            print("Спасибо за игру! До встречи!")
            break

if __name__ == "__main__":
    main()
