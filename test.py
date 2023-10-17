import secrets
import numpy as np

random_number = secrets.SystemRandom()

numElements = 100

print(random_number.randrange(numElements))


#########################################

MIN_ENTROPY = 128
def calculate_entropy(numOptions, length):
    # Entropy = L × log2(R)
    return length * np.log2(numOptions)

def calc_num_years_from_bits_entropy(bits_entropy):
    CHECKS_PER_SEC = 1000000000
    classical_entropy = 2 ** bits_entropy
    class_seconds = classical_entropy / CHECKS_PER_SEC
    class_minutes = class_seconds / 60
    class_hours = class_minutes / 60
    class_days = class_hours / 24
    class_years = class_days / 365

    quantum_entropy = int(classical_entropy ** (1 / 2))
    quant_seconds = quantum_entropy / CHECKS_PER_SEC
    quant_minutes = quant_seconds / 60
    quant_hours = quant_minutes / 60
    quant_days = quant_hours / 24
    quant_years = quant_days / 365

    # print("Entropy: ", entropy)
    # print(f"Seconds at {checks_per_sec} checks per second: ", seconds)
    # print("Minutes: ", minutes)
    # print("Hours: ", hours)
    # print("Days: ", days)
    # print("Years: ", class_years)
    return class_years, quant_years


### From: https://docs.python.org/3/library/secrets.html
import secrets
# On standard Linux systems, use a convenient dictionary file.
# Other platforms may need to provide their own word-list.
with open('/usr/share/dict/words') as f:
    words = [word.strip() for word in f]
    print(len(words))

    numWords = 0
    bits_entropy = 0
    password = ''
    while bits_entropy < MIN_ENTROPY:
        password += secrets.choice(words) + " "
        numWords += 1
        bits_entropy = calculate_entropy(len(words), numWords)

    password.strip()
    bits_entropy = int(bits_entropy)

    years = calc_num_years_from_bits_entropy(bits_entropy)
    print(f"Years at {bits_entropy} bits entropy on classical computer: ", years[0],"\n"
           "Years on quantum computer: ", years[1])
    
    # bits_entropy = 128
    # years = calc_num_years_from_bits_entropy(bits_entropy)
    # print(f"Years at {bits_entropy} bits entropy on classical computer: ", years[0],
    #       "\n Years on quantum computer: ", years[1])
    print(password)
