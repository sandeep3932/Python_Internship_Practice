updated_list = []
def learn_enumeratefunc(colors_list, remove_list):
    for index, color in enumerate(colors_list):
        if index not in remove_list:
            updated_list.append(color)
    return updated_list

colors_list = ['Red', 'Green', 'Pink', 'Blue', 'Black', 'Purple', 'Yellow', 'Magenta', 'Brown']
remove_list = [0, 2, 5]

def main():
    print(f"Updated list with the removed elements is: {learn_enumeratefunc(colors_list, remove_list)}")

main()


