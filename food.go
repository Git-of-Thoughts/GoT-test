package main

type Food struct {
	Pos Point
}

func NewFood() *Food {
	return &Food{
		Pos: RandomPoint(),
	}
}
