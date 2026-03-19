# Function para bilangin lahat ng characters (kasama ang spaces) sa pangalan
def count_characters_in_name():
    # Humingi ng buong pangalan sa user
    full_name = input("\033[96mEnter your full name: \033[0m")
    
    # Gamitin ang len() (length) direkta sa string para bilangin lahat ng letra at spaces
    character_count = len(full_name)

    # I-print ang total na bilang ng characters sa terminal
    print("\033[92mResult:\033[0m", character_count)

# Ito yung magsisilbing switch para umandar yung script
if __name__ == "__main__":
    count_characters_in_name()