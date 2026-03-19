# Function para bilangin kung ilang salita meron sa isang sentence
def count_words_in_statement():
    # Humingi ng buong sentence o statement sa user
    complete_statement = input("\033[96mEnter a complete statement: \033[0m")
    
    # Gamitin ang .split() para hati-hatiin ang sentence by spaces at ilagay sa isang list
    word_list = complete_statement.split()
    
    # Gamitin ang len() (length) para bilangin kung ilang salita ang pumasok sa list
    word_count = len(word_list)

    # I-print ang total na bilang ng salita sa terminal
    print("\033[92mResult:\033[0m", word_count)

# Ito yung magsisilbing switch para umandar yung script
if __name__ == "__main__":
    count_words_in_statement()