list_stud = ["Безкоровайний Павло Миколайович",
             "Грицюк Юлія Володимирівна",
             "Носаченко Олег Юрійович",
             "Носаченко Олег Юрійович",
             "Ричков Дмитро Сергійович",
             "Грицюк Юлія Володимирівна",
             ]
def discount(list_var):
    # dict_var = {}
    # for element in list_var:
    #     dict_var[element] = f'{element}, місце - {list_var.index(element)}, кількість повторень - {list_var.count(element)}'
    # return dict_var
    return {element:f'місце - {list_var.index(element)}, кількість повторень - {list_var.count(element)}'for element in list_var}
print(discount(list_var = list_stud))