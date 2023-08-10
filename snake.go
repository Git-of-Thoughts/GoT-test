package main

type Snake struct {
	Body []Point
	Dir  Direction
}

func NewSnake() *Snake {
	return &Snake{
		Body: []Point{{5, 5}},
		Dir:  Right,
	}
}

func (s *Snake) Move() {
	// Move the snake in the current direction
}

func (s *Snake) Grow() {
	// Add a new segment to the snake's body
}

func (s *Snake) CollidesWith(p Point) bool {
	// Check if the snake collides with the given point
}

func (s *Snake) CollidesWithSelf() bool {
	// Check if the snake collides with itself
}
