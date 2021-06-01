def hex_output(hex_as_string):
    dec_num = 0
    for power, digit in enumerate(reversed(hex_as_string)):
        # index, one_letter = power, digit
        # print(f"index: {index}, letter:{one_letter}")
        dec_num += int(digit, 16) * (16 ** power)
    print(f"0x{hex_as_string} is decimal {dec_num}")


hex_output("F")
hex_output("50")
hex_output("5F")
