package main

type Game struct {
	Snake   *Snake
	Food    *Food
	Score   int
	GameOver bool
}

func NewGame() *Game {
	return &Game{
		Snake:   NewSnake(),
		Food:    NewFood(),
		Score:   0,
		GameOver: false,
	}
}

func (g *Game) Update() {
	if g.Snake.CollidesWith(g.Food) {
		g.Score++
		g.Food = NewFood()
		g.Snake.Grow()
	}
	if g.Snake.CollidesWithSelf() {
		g.GameOver = true
	}
	g.Snake.Move()
}

func (g *Game) Render() string {
	// Render the game state as a string
}
