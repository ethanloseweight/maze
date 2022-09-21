Project structure
    
    maze
        main.py
        web_app.py
        map.txt
        map_hard.txt
        scores.json
    
    
        models
            maze.py
            player.py
            score.py
            score_manager.py
        
        controllers
            app.py
            keyboardcontroller.py
            gamecontroller.py
            gameovercontroller.py
            welcomecontroller.py
            welldonecontroller.py
        
        views
            gameview.py
            gameoverview.py
            welcomeview.py
            welldoneview.py
        
        tests
            models
                test_maze.py
                test_player.py  
                test_score.py
                test_score_manager.py  
            controllers
                test_app.py
                test_game_controller.py
            views
                test_game_view.py
    web
        app.py
        models
            score.py
            score_manager.py
        templates
            base.html
            list.html

Dependencies

    - pygame
    - pygame (if you are running the test files)
    - flask
    
How to  run pytest

    1. In terminal, set your current working directory to maze_game/maze folder.
    
    2. Type "pytest"
    
 
 How to run the code
 
    1. In terminal, set your current working directory to maze_game/maze folder.
    
    2. Make sure that you have required dependency(ies) installed
       in your computer.
    
    3. Type "main.py" in terminal.
        
 
 How to control the game
 
    UP = w key on keyboard
    DOWN = s key on keyboard
    LEFT = a key on keyboard
    RIGHT = d key on keyboard
    
 
 How to check your score
    
    1. Close the pygame window OR open another terminal
    
    2. In terminal, set your current working directory to maze_game/web folder.
    
    3. Type app.py
    
    4. Click "http://127.0.0.1:5000/" in your terminal OR type "http://127.0.0.1:5000/" in your browser