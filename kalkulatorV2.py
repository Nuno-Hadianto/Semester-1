# This property belongs to nuno
RESET = "\033[0m"
BOLD = "\033[1m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
PURPLE = "\033[95m"
CYAN = "\033[96m"

def stoner():
    rossi = 46
    marquez = 93

    # // Operator Penugasan
    c = rossi + marquez
    d = rossi - marquez
    e = rossi * marquez
    f = rossi / marquez

    # // Operator Perbandingan
    g = rossi == marquez
    h = rossi != marquez
    i = rossi < marquez
    j = rossi > marquez
    k = rossi <= marquez
    l = rossi >= marquez

    # // Operator Logika
    q = rossi and marquez
    x = rossi or marquez
    z =  rossi ,not marquez

    
    print(BOLD + YELLOW + "rossi = " + RESET, rossi)
    print(BOLD + RED + "marquez = " + RESET, marquez)
    print(BOLD + GREEN + "................................................" + RESET)
    print(BOLD + BLUE + " Ini Adalah Program Kalkulator Sederhana " + RESET)

    print(BOLD + GREEN + "................................................" + RESET)
    print(BOLD + BLUE + "Operator Penugasan = " + RESET)
    print(BOLD + CYAN + "c = rossi + marquez = " + RESET, c)
    print(BOLD + CYAN + "d = rossi - marquez = " + RESET, d)
    print(BOLD + CYAN + "e = rossi * marquez = " + RESET, e)
    print(BOLD + CYAN + "f = rossi / marquez = " + RESET, f)
    print(BOLD + GREEN + "................................................" + RESET)
    
    print(BOLD + BLUE + "Operator Perbandingan = " + RESET)
    print(BOLD + CYAN + "g = rossi == marquez = " + RESET, g)
    print(BOLD + CYAN + "h = rossi != marquez = " + RESET, h)
    print(BOLD + CYAN + "i = rossi < marquez = " + RESET, i)
    print(BOLD + CYAN + "j = rossi > marquez = " + RESET, j)
    print(BOLD + CYAN + "k = rossi <= marquez = " + RESET, k)
    print(BOLD + CYAN + "l = rossi >= marquez = " + RESET, l)
    print(BOLD + GREEN + "................................................" + RESET)

    print(BOLD + BLUE + " Operator Logika = " + RESET)
    print(BOLD + CYAN + "q = rossi and marquez = " + RESET, q)
    print(BOLD + CYAN + " 93 Belongs to Marc Marquez " + RESET)
    print(BOLD + CYAN + "x = rossi or marquez = " + RESET, x)
    print(BOLD + CYAN + " 46 Belongs to Valentino Rossi " + RESET)
    print(BOLD + CYAN + "z = rossi = " + RESET, z)
    print(BOLD + RED + " False if the number for Marc Marquez " + RESET)
    print(BOLD + GREEN + "................................................" + RESET)

stoner()