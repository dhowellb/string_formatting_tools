# Function para tanggalin ang mga sobrang spaces sa unahan ng text
def remove_leading_spaces():
    # Humingi ng input sa user (name na may spaces sa unahan)
    user_input = input("\033[96mEnter your full name with leading spaces: \033[0m")
    
    # Gamitin ang .lstrip() (Left Strip) para linisin yung left side ng string
    formatted_name = user_input.lstrip()

    # I-print yung malinis na resulta
    print("\033[92mResult:\033[0m", formatted_name)

# Ang ating start button para umandar yung script
if __name__ == "__main__":
    remove_leading_spaces()