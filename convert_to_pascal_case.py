# Function para gawing PascalCase ang text (Capital ang simula ng bawat salita at walang spaces)
def convert_to_pascal_case():
    # Humingi ng input sa user (kahit magulo ang malaki/maliit na letra)
    full_name = input("\033[96mEnter your full name in incorrect casing: \033[0m")
    
    # Step 1: Gawing capital ang simula ng bawat salita gamit ang .title()
    title_cased_name = full_name.title()
    
    # Step 2: Tanggalin ang lahat ng spaces gamit ang .replace(" ", "")
    pascal_case_name = title_cased_name.replace(" ", "")

    # I-print ang PascalCase na resulta sa terminal
    print("\033[92mResult:\033[0m", pascal_case_name)

# Ito yung magsisilbing switch para umandar yung script
if __name__ == "__main__":
    convert_to_pascal_case()