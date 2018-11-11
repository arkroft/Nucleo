print('Введите последовательность нуклеотидов')
st = input()
my_file = 'NucIn.txt'
f = open(my_file, "w")
f.write(st)
f.close()


st = ''
f = open(my_file)
st = f.read().upper()
f.close()
nkt = ""
if st != '':
    if 'U' in st or 'У' in st:
        nkt = "RNA -> DNA"
        st = st.replace('U', 'T')
        st = st.replace('У', 'T')
    else:
        nkt = "DNA -> RNA"
        st = st.replace('T', 'U')
        st = st.replace('Т', 'У')

    my_file = 'NucOut.txt'
    f = open(my_file, "w")
    f.write(nkt)
    f.write(": ")
    f.write(st)
    f.close()
else:
    print('Файл пустой!')