from menu import menu
from enums import Data
from create_save_file import main as create_save
from os import remove as delete

def get_save_data():

    try:
        save = open("save_file.txt")
    except:
        
        print("No save file exists!")

        match menu(['Yes','No'],"Would you like to create a new save?"):
            case 'Yes':
                create_save()
                save = open("save_file.txt")
            case 'No':
                return ''
    
    data = save.readlines()
    save.close()

    return data


def format_data(data):
    
    data_dict = {}
    data_types = {}
    for data_type in Data:
        data_types.update({data_type.value: data_type})

    for datum in data:
        
        datum_split = datum.strip('\n').split(':')

        if datum_split[0] in data_types:
            datum_split[0] = data_types[datum_split[0]]

        data_dict.update({datum_split[0]:datum_split[1]})

    return data_dict


def read_data(data):
    
    options = list(data)
    options.extend(['All','Exit'])
    
    while True:
        
        choice = menu(options, 'What would you like to display?')

        match choice:
            
            case 'All':
                for datum in data:
                    print(f"{datum}: {data[datum]}")
            
            case 'Exit':

                match menu(['Yes','No'],'Would you like to delete your save?'):
                    case 'Yes':
                        delete('save_file.txt')
                    case 'No':
                        pass
                    case _:
                        print('Invalid input!')

                break
            
            case _:
                print(f"{choice}: {data[choice]}")

def main():
    
    data = format_data(get_save_data())
    read_data(data)


main()