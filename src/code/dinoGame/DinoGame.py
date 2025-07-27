from src.code.dinoGame.scenes.MainDinoScene import MainDinoScene
from src.code.framework.MainGame import MainGame

game = MainGame(title='Dino Game', width=1280, height=640)
game.current_scene = MainDinoScene()
game.run_game()

# Clean up resources
del game