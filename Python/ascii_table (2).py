from prettytable import PrettyTable

a = PrettyTable()
b = PrettyTable()
a._validate_field_names = lambda *a, **k: None

print("Ascii Table 1")
a.field_names = ["  0", "NUL", " 16", "DLE", " 32", "", " 48", "0"]
a.add_row(["  1", "SOH", " 17", "DC1", " 33", "!", " 49", "1"], divider=True)
a.add_row(["  2", "STX", " 18", "DC2", " 34", '"', " 50", "2"], divider=True)
a.add_row(["  3", "ETX", " 19", "DC3", " 35", "#", " 51", "3"], divider=True)
a.add_row(["  4", "EOT", " 20", "DC4", " 36", "$", " 52", "4"], divider=True)
a.add_row(["  5", "ENQ", " 21", "NAK", " 37", "%", " 53", "5"], divider=True)
a.add_row(["  6", "ACK", " 22", "SYN", " 38", "&", " 54", "6"], divider=True)
a.add_row(["  7", "BEL", " 23", "ETB", " 39", "'", " 55", "7"], divider=True)
a.add_row(["  8", "BS ", " 24", "CAN", " 40", "(", " 56", "8"], divider=True)
a.add_row(["  9", "HT ", " 25", "EM ", " 41", ")", " 57", "9"], divider=True)
a.add_row([" 10", "LF ", " 26", "SUB", " 42", "*", " 58", ":"], divider=True)
a.add_row([" 11", "VT ", " 27", "ESC", " 43", "+", " 59", ";"], divider=True)
a.add_row([" 12", "FF ", " 28", "FS ", " 44", ",", " 60", "<"], divider=True)
a.add_row([" 13", "CR ", " 29", "GS ", " 45", "-", " 61", "="], divider=True)
a.add_row([" 14", "SO ", " 30", "RS ", " 46", ".", " 62", ">"], divider=True)
a.add_row([" 15", "SI ", " 31", "US ", " 47", " / ", " 63", " ? "], divider=True)

print(a)
print()

print("Ascii Table 2")
b.field_names = [" 16", "DLE", " 48", 0, " 80", " P ", 112, "p"]
b.add_row([" 17", "DC1", " 49", 1, " 81", "Q", 113, "q"], divider=True)
b.add_row([" 18", "DC2", " 50", 2, " 82", "R", 114, "r"], divider=True)
b.add_row([" 19", "DC3", " 51", 3, " 83", "S", 115, "s"], divider=True)
b.add_row([" 20", "DC4", " 52", 4, " 84", "T", 116, "t"], divider=True)
b.add_row([" 21", "NAK", " 53", 5, " 85", "U", 117, "u"], divider=True)
b.add_row([" 22", "SYN", " 54", 6, " 86", "V", 118, "v"], divider=True)
b.add_row([" 23", "ETB", " 55", 7, " 87", "W", 119, "w"], divider=True)
b.add_row([" 24", "CAN", " 56", 8, " 88", "X", 120, "x"], divider=True)
b.add_row([" 25", "EM ", " 57", 9, " 89", "Y", 121, "y"], divider=True)
b.add_row([" 26", "SUB", " 58", ":", " 90", "Z", 122, "z"], divider=True)
b.add_row([" 27", "ESC", " 59", ";", " 91", "[", 123, "{"], divider=True)
b.add_row([" 28", "FS ", " 60", "<", " 92", "\\", 124, "|"], divider=True)
b.add_row([" 29", "GS ", " 61", "=", " 93", "]", 125, "}"], divider=True)
b.add_row([" 30", "RS ", " 62", ">", " 94", "^", 126, "~"], divider=True)
b.add_row([" 31", "US ", " 63", " ? ", " 95", "_", 127, "DEL"], divider=True)

print(b)