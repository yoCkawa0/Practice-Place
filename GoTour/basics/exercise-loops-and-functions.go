package main

import (
	"fmt"
	"math"
)

func Squrt(x float64) float64 {
	z := 1.0
	for i := 1; i <= 10; i++ {
		z -= (z*z - x) / (2 * z)
		fmt.Println(i, z)

		if math.Sqrt(x) == z {
			fmt.Println(i, "回で一致")
			break
		}
	}
	return z
}

func main() {
	x := float64(100)

	fmt.Printf("%vの平方根の近似値は%v\n", int(x), int(Squrt(x)))
}
