# Function para ayusin ang capitalization ng bawat salita (Proper Case)
def convert_to_proper_case():
    # Humingi ng input sa user (kahit magulo ang malaki/maliit na letra)
    full_name = input("\033[96mEnter your full name in incorrect casing: \033[0m")
    
    # Gamitin ang .title() para gawing capital ang unang letra ng bawat salita
    proper_name = full_name.title()

    # I-print ang maayos na pangalan sa terminal
    print("\033[92mResult:\033[0m", proper_name)

# Ito yung magsisilbing switch para umandar yung script
if __name__ == "__main__":
    convert_to_proper_case()