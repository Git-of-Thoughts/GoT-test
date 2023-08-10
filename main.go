package main

import (
	"fmt"
	"time"
)

func main() {
	game := NewGame()
	for !game.GameOver {
		game.Update()
		fmt.Println(game.Render())
		time.Sleep(time.Second / 10)
	}
	fmt.Println("Game over!")
}
