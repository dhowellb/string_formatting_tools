# Function para gawing malalaking letra (all caps) ang lahat ng ita-type na text
def convert_to_all_caps():
    # Humingi ng input sa user (yung buong pangalan nila)
    full_name = input("\033[96mEnter your full name: \033[0m")
    
    # Gamitin ang .upper() para i-convert lahat ng letters to uppercase
    capitalized_name = full_name.upper()

    # I-print ang naka-all caps na resulta sa terminal
    print("\033[92mResult:\033[0m", capitalized_name)

# Ito yung magsisilbing switch para umandar yung script
if __name__ == "__main__":
    convert_to_all_caps()