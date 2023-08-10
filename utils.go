package main

import (
	"math/rand"
	"time"
)

func RandomPoint() Point {
	rand.Seed(time.Now().UnixNano())
	return Point{rand.Intn(10), rand.Intn(10)}
}
