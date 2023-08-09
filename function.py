import file_operation
import Note
import prime

number = 6

def add(text):
    note = prime.generate_note(number)
    array = file_operation.read_file()
    for notes in array:
        if Note.Note.get_id(note) == Note.Note.get_id(notes):
            Note.Note.set_id(note)
    array.append(note)
    file_operation.write_file(array, "a")
    print("Заметка добавлена.")

def display(text):
    logic = True
    array = file_operation.read_file()
    if text == "date":
        date = input("Введите дату в формате dd.mm.yyyy: ")
    for notes in array:
        if text == "all":
            logic = False
            print(Note.Note.map_note(notes))
        if text == "id":
            logic = False
            print("ID: " + Note.Note.get_id(notes))
        if text == "date":
            logic = False
            if date in Note.Note.get_date(notes):
                print(Note.Note.map_note(notes))
    if logic == True:
        print("Нет ни одной заметки. ")

def id_edit_del_display(text):
    id = input("Введите id нужной заметки: ")
    array = file_operation.read_file()
    logic = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            logic = False
            if text == "edit":
                note = prime.generate_note(number)
                Note.Note.set_title(notes, note.get_title())
                Note.Note.set_body(notes, note.get_body())
                Note.Note.set_date(notes)
                print("Заметка изменена. ")
            if text == "del":
                array.remove(notes)
                print("Заметка удалена. ")
            if text == "display":
                print(Note.Note.map_note(notes))
    if logic == True:
        print("Такой заметки не существует, вы ввели неверный id ")
    file_operation.write_file(array, "a")
