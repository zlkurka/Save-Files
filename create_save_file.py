from enums import Data

def get_data():
    
    data = {}

    for data_type in Data:
        
        datum = None

        while not datum:
            datum = input(f"What is your character's {data_type.value}? ")
            
            if data_type == Data.level:
                try:
                    datum = str(int(datum))
                except ValueError:
                    print('Only enter an integer!')
                    datum = None
                    continue
    
            
            if ':' in datum or '\n' in datum:
                print("Line breaks and colons not acceptable!")
                datum = None
                continue
        
        data.update({data_type: datum})

    return data


def clean_data(data):
    
    output = ''

    if type(data) is dict:
        for datum in data:
            output += f"{datum.value.capitalize()}:{data[datum].capitalize()}\n"
    
    return output


def save_file(data):
    save = open("save_file.txt", "w")
    save.write(str(data))
    save.close()

def main():
    
    data = get_data()

    save_file(clean_data(data))