import mod.title
import mod.to_text as to_text

def main():
    form = to_text.formatter()
    print("""1. Varsayılan(CSV)
2. Nokta ile ayrılmış
3. Parantez ile ayrılmış
4. Özel""")
    opt = input("Format Tipini Seçiniz: ")

    match opt:
        case 1:
            form.configure("data/default.json")
        case 2:
            form.configure("data/dot-sep.json")
        case 3:
            form.configure("data/para-sep.json")
        case 4:
            data = input("dosya yerini girin(\\ yerine / kullanın): ")
            form.configure(data)
        case _:
            form.configure("data/default.json")

    input_file = input("Formatlanmamış dosya(input.txt): ")
    output_file = input("Formatlanmış dosya(out.txt): ")

    if input_file == "":
        input_file = "input.txt"

    if output_file == "":
        output_file = "out.txt"

    un_f = open(input_file)
    unform_txt = un_f.read()
    un_f.close()

    formatted_txt = form.format(unform_txt)

    f = open(output_file, "w+")
    if opt == "" or opt == 1:
        f.write("Soru,Cevap\n")
    f.write(formatted_txt)

    f.write("\nCevap Anahtarı Formatter tarafından oluşturuldu\n")
    f.write("KDEV Programs")

    f.close()

    print("Formatlama Tamamlandı")



if __name__ == "__main__":
    main()