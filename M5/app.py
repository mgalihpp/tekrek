from random import choice

# Membuat dictionary untuk menyimpan pola-pola yang telah ditemukan
patterns = {}

# Fungsi untuk membuat pola dari pilihan pemain sebelumnya
def create_pattern(history):
    return tuple(history)

# Fungsi untuk memprediksi pilihan selanjutnya berdasarkan pola yang ada
def predict_next_move(history):
    pattern = create_pattern(history)
    if pattern in patterns:
        # Jika pola telah ditemukan sebelumnya, pilih pilihan yang paling sering muncul setelah pola tersebut
        next_moves = patterns[pattern]
        return max(next_moves, key=next_moves.get)
    else:
        # Jika pola belum ditemukan sebelumnya, pilih secara acak
        return choice(["rock", "paper", "scissors"])

# Fungsi untuk menambahkan pilihan pemain ke dalam history dan memperbarui dictionary patterns
def update_patterns(history, player_move):
    pattern = create_pattern(history)
    next_move = history[-1] if history else None
    if pattern not in patterns:
        patterns[pattern] = {next_move: 1}
    else:
        if next_move not in patterns[pattern]:
            patterns[pattern][next_move] = 1
        else:
            patterns[pattern][next_move] += 1

# Fungsi utama untuk bermain
def main():
    history = []
    while True:
        ai_move = predict_next_move(history)
        player_move = input("Masukkan pilihan Anda (rock/paper/scissors): ").lower()
        if player_move not in ["rock", "paper", "scissors"]:
            print("Masukkan tidak valid. Silakan masukkan rock, paper, atau scissors.")
            continue
        print("Pilihan Anda:", player_move)
        print("Pilihan AI:", ai_move)
        if player_move == ai_move:
            print("Hasil: Draw!")
        elif (player_move == "rock" and ai_move == "scissors") or \
             (player_move == "paper" and ai_move == "rock") or \
             (player_move == "scissors" and ai_move == "paper"):
            print("Hasil: Anda menang!")
        else:
            print("Hasil: Anda kalah!")
        update_patterns(history, player_move)
        history.append(player_move)
        history = history[-2:]

        play_again = input("Ingin bermain lagi? (y/n): ").lower()
        if play_again != "y":
            break

if __name__ == "__main__":
    main()
