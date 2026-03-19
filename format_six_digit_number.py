# Function para lagyan ng zeros sa unahan ang isang number hanggang maging 6 digits
def format_six_digit_number():
    # Humingi ng number mula 0 hanggang 1000
    user_number = input("\033[96mEnter a number (0-1000): \033[0m")
    
    # Gamitin ang .zfill(6) para punuan ng '0' ang left side hanggang maging 6 characters ang haba
    formatted_number = user_number.zfill(6)

    # I-print ang formatted na number sa terminal
    print("\033[92mResult:\033[0m", formatted_number)

# Ito yung magsisilbing switch para umandar yung script
if __name__ == "__main__":
    format_six_digit_number()