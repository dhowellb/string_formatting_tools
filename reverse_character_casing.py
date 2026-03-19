# Function para pagpalitin ang malalaki at maliliit na letra (Swap Case)
def reverse_character_casing():
    # Humingi ng input sa user
    full_name = input("\033[96mEnter your full name in incorrect casing: \033[0m")
    
    # Gamitin ang .swapcase() para gawing small ang capital, at capital ang small letters
    reversed_case_name = full_name.swapcase()

    # I-print ang baligtad na resulta sa terminal
    print("\033[92mResult:\033[0m", reversed_case_name)

# Ito yung magsisilbing switch para umandar yung script
if __name__ == "__main__":
    reverse_character_casing()