import crcmod

crc32_func = crcmod.mkCrcFun(0x104c11db7, initCrc=0xFFFFFFFF, xorOut=0x00000000)


while True:
    # Benutzer zur Eingabe auffordern
    input_string = input("Please enter the code: ")
    # Exit Funktion
    if input_string.lower() == 'exit':
        print("Exiting..")
        break

    # Aufteilen der Eingabe in Blöcke
    blocks = input_string.split('-')

    # Überprüfe, ob die Eingabe die richtige Länge hat
    if len(blocks) == 6 and len(blocks[0])<=4 and len(blocks[1])<=4 and len(blocks[2])<=4 and len(blocks[3])<=4 and len(blocks[4])<=4 and len(blocks[5])<=4:
        # Überprüfe, ob die ersten beiden Blöcke übereinstimmen
        if blocks[0] == "203c" and blocks[1] == "d001":
            # Verbinde die restlichen Blöcke ohne Bindestriche
            result_string = "".join(blocks[2:])
            # Entferne alle Bindestriche aus der Zeichenfolge
            result_string = result_string.replace("-", "")
            # Ausgabe der Zeichenfolge
            print("Input ok.")
            # Ändere die Eingabe zu hexadezimal
            hex_result = hex(int(result_string, 16))[2:].encode('utf-8')
            crc_sum = hex(crc32_func(bytearray(hex_result)))
            
            #Colors for better visability
            TGREEN = '\033[32m'
            RESET = '\033[m'
            
            print("The master password is: ", TGREEN + crc_sum[2:] + RESET)
            print("Please note that the password is encoded for US QWERTY keyboard layouts.")
            break # Beende die Schleife, da die Eingabe gültig ist
        else:
            print("Wrong Input! The first two blocks must be '203c' and 'd001'.")
    else:
        print("Wrong Input! 6x4 blocks required.")

