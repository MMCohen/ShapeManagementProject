# https://github.com/MMCohen/ShapeManagementProject

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


def get_int_input(text):
    while True:
        try:
            return int(input(text))
        except ValueError:
            print("Please enter numbers only")


def shape_menu(shape_manager: ShapeManager) -> dict:
    while True:
        menu =f"""{"=" * 45}
= {"welcome to add shape menu: ":=<43}
{"=" * 45}
which shape do you want?
1. square
2. circle
3. rectangle
        """
        shape_manager.clear_screen()
        shape_manager.print_to_screen(menu)

        choice = get_int_input("Please enter your choice: ")

        if choice not in (1, 2, 3):
            shape_manager.print_to_screen("you did not enter a number from the menu,\nplease try again...")
            continue

        match choice:
            case 1:
                side = get_int_input("please enter side: ")
                dimensions = [side]
                shape_dict = {"id": None, "type": "square", "dimensions": dimensions}
            case 2:
                radius = get_int_input("please enter radius: ")
                dimensions = [radius]
                shape_dict = {"id": None, "type": "circle", "dimensions": dimensions}
            case 3:
                length = get_int_input("please enter length: ")
                width = get_int_input("please enter width: ")
                dimensions = [length, width]
                shape_dict = {"id": None, "type": "rectangle", "dimensions": dimensions}

        return shape_dict


def main():
    s1 = ShapeManager()
    want_to_exit = False

    while not want_to_exit:
        # s1.clear_screen()
        s1.print_to_screen(menu())

        choice = get_int_input("Please enter your choice: ")

        match choice:
            case 1: # Add shape
                shape = shape_menu(s1)
                s1.create_shape(shape)
            case 2: # Show all shapes
                s1.get_all_shapes()
            case 3: # Update shape
                shape_id = get_int_input("please enter shape id: ")

                shape_type = s1.get_shape_type(shape_id)
                if not shape_type:
                    s1.print_to_screen("Shape ID not found")
                    continue
                match shape_type:
                    case "square":
                        dimensions = [get_int_input("please enter side: ")]
                    case "circle":
                        dimensions = [get_int_input("please enter radius: ")]
                    case "rectangle":
                        dimensions = [get_int_input("please enter length: "),get_int_input("please enter width: ")]

                s1.update_shape(shape_id, dimensions)

            case 4: # Delete shape
                shape_id = get_int_input("please enter shape id: ")
                s1.delete_shape(shape_id)

            case 5: # Exit
                want_to_exit = True
                s1.print_to_screen("Good bye!")
            case _:
                s1.print_to_screen("you did not enter a number from the menu,\nplease try again...")


if __name__ == "__main__":
    main()