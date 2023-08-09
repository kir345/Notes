import function as f
import prime

def run():
    input_from_user = " "
    while input_from_user != "7":
        prime.menu()
        input_from_user = input().strip()
        if input_from_user == "1":
            f.display("all")
        if input_from_user == "2":
            f.add("all")
        if input_from_user == "3":
            f.display("all")
            f.id_edit_del_display("del")
        if input_from_user == "4":
            f.display("all")
            f.id_edit_del_display("edit")
        if input_from_user == "5":
            f.display("date")
        if input_from_user == "6":
            f.display("id")
            f.id_edit_del_display("display")
        if input_from_user == "7":
            prime.buy()
            break
    