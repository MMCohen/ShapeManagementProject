from shape_manager import ShapeManager

def menu():
    menu =f"""{"=" * 45}
= {"welcome to Shape Crud v.0.0.1 ":=<43}
{"=" * 45}
Menu:
1. Add shape
2. Show all shapes
3. Update shape
4. Delete shape
5. Exit
    """
    return menu


def shape_menu(object: ShapeManager) -> dict:
    while True:
        menu =f"""{"=" * 45}
= {"welcome to add shape menu: ":=<43}
{"=" * 45}
which shape do you want?
1. square
2. circle
3. rectangle
        """
        object.clear_screen()
        object.print_to_screen(menu)

        choice = input("Please enter your choice: ")

        if choice not in "123":
            object.print_to_screen("you did not enter a number from the menu,\nplease try again...")
            continue
        choice = int(choice)

        match choice:
            case 1:
                side = input("please enter side: ")
                dimensions = [side]
                shape_dict = {"id": None, "type": "square", "dimensions": dimensions}
            case 2:
                radius = input("please enter radius: ")
                dimensions = [radius]
                shape_dict = {"id": None, "type": "circle", "dimensions": dimensions}
            case 3:
                length = input("please enter length: ")
                width = input("please enter width: ")
                dimensions = [length, width]
                shape_dict = {"id": None, "type": "rectangle", "dimensions": dimensions}
        try:
            shape_dict["dimensions"] = [int(num) for num in shape_dict["dimensions"]]
        except ValueError as e:
            object.print_to_screen(f"{e} you did not enter legit dimensions. only numbers!\nPlease try again..")
            continue


        return shape_dict


def main():
    s1 = ShapeManager()
    want_to_exit = False

    while not want_to_exit:
        # s1.clear_screen()
        s1.print_to_screen(menu())

        try:
            choice = int(input("Please enter your choice: "))
        except ValueError:
            s1.print_to_screen("Please enter numbers only")
            continue

        match choice:
            case 1:
                shape = shape_menu(s1)
                s1.create_shape(shape)
            case 2:
                s1.get_all_shapes()
            case 3:
                while True:
                    shape_id = input("please enter shape id: ")
                    try:
                        shape_id = int(shape_id)
                        break
                    except ValueError:
                        s1.print_to_screen("please enter numbers only")
                        continue
                shape_type = s1.get_shape_type(shape_id)
                while True:
                    match shape_type:
                        case "square":
                            dimensions = [input("please enter side: ")]
                        case "circle":
                            dimensions = [input("please enter radius: ")]
                        case "rectangle":
                            dimensions = [input("please enter length: "),input("please enter width: ")]
                        case _:
                            s1.print_to_screen("we didn't find shape id")
                            continue
                    try:
                        dimensions = [int(num) for num in dimensions]
                    except ValueError:
                        s1.print_to_screen("you didnt enter legit dimensions numbers")
                        continue
                    else:
                        s1.update_shape(shape_id, dimensions)
                        break
            case 4:
                is_a_number = False
                while not is_a_number:
                    try:
                        shape_id = int(input("please enter shape id: "))
                        is_a_number = True
                    except ValueError:
                        s1.print_to_screen("please enter numbers only")

                s1.delete_shape(shape_id)

            case 5:
                want_to_exit = True
                s1.print_to_screen("Good bye!")
            case _:
                s1.print_to_screen("you did not enter a number from the menu,\nplease try again...")


if __name__ == "__main__":
    main()