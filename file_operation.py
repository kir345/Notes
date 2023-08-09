import Note

def write_file(array, mode):
    file = open("annotation.csv", mode= "w", encoding= "utf-8")
    file.seek(0)
    file.close()
    file = open("annotation.csv", mode=mode, encoding="utf-8")
    for annotation in array:
        file.write(Note.Note.to_string(annotation))
        file.write("\n")
    file.close

def read_file():
    try:
        array = []
        file = open("annotation.csv", "r", encoding="utf-8")
        annotation = file.read().strip().split("\n")
        for n in annotation:
            split_n = n.split(";")
            annotation = Note.Note(id = split_n[0], title = split_n[1], body = split_n[2], date = split_n[3])
            array.append(annotation)
    except Exception:
        print("Нет сохраненных заметок. ")
    finally:
        return array