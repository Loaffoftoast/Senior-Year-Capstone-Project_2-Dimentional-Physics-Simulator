import pygame

'''
keybinds
    i need a settings txt doc that has all keybinds saved
    have the function set to a specific keybind number, then the keybind number can be changed to a specific keybind if that makes sense
    
    *have a JSON file to save the files"
        import JSON
            save_keybinds(keybinds, filename="keybinds.json"):
                    try:
                        with open(filename, "w") as f:
                            # keybinds contains integer constants, which JSON easily handles
                            json.dump(keybinds, f, indent=4)
                        print("Keybinds saved successfully!")
                    except IOError:
                        print("Error: Could not save keybinds.")
    
    *have keybinds array, and just have them be defaults, but also be able to change these so that they dont start like this*
        keybinds = {
            "zoomIn": scroll_wheel_up, 
            "zoomOut": scroll_wheel_down, 
        }
        
    *settings menu*
        waiting_for_key = None
        
        event.get stuff
            if quit
            
            elif user clicks something:
                if user clicks a certain option (zoomIn for example):
                    waiting_for_key = "zoomIn"
                    
            elif user hits a key
                if waiting_for_key:
                    keybinds[waiting_for_key] = keybind
                    waiting_for_key = None
        
    

'''


