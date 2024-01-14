import sys
import game

def main():
    Game = game.game()
    
    Game.setUp()
    while Game.isRunning() == True:
        for i in range(0, 10):
            Game.HandleEvents()
            Game.Update()   
        Game.Render()
        Game.FinishCalculations()
    Game.Exit()
    return 0

sys.exit(main())