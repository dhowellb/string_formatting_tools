# Function para gawing maliliit na letra (lowercase) ang lahat ng ita-type na text
def convert_to_lower_case():
    # Humingi ng input sa user (yung buong pangalan nila)
    full_name = input("\033[96mEnter your full name: \033[0m")
    
    # Gamitin ang .lower() para i-convert lahat ng letters to lowercase
    lowercased_name = full_name.lower()

    # I-print ang naka-lowercase na resulta sa terminal
    print("\033[92mResult:\033[0m", lowercased_name)

# Ito yung magsisilbing switch para umandar yung script
if __name__ == "__main__":
    convert_to_lower_case()