# Function para gawing snake_case ang text (small letters lahat at underscores ang spaces)
def convert_to_snake_case():
    # Humingi ng input sa user
    full_name = input("\033[96mEnter your full name in incorrect casing: \033[0m")
    
    # Step 1: Gawing small letters lahat gamit ang .lower()
    lower_cased_name = full_name.lower()
    
    # Step 2: Palitan ang lahat ng spaces ng underscore (_) gamit ang .replace()
    snake_case_name = lower_cased_name.replace(" ", "_")

    # I-print ang snake_case na resulta sa terminal
    print("\033[92mResult:\033[0m", snake_case_name)

# Ito yung magsisilbing switch para umandar yung script
if __name__ == "__main__":
    convert_to_snake_case()