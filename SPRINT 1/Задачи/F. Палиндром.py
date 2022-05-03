seq = input()
seq_1 = "".join(i for i in seq if i.isalpha())
seq_l = seq_1.lower()
seq_l_reversed = seq_l[::-1]

if seq_l == seq_l_reversed:
    print("True")
else:
    print("False")