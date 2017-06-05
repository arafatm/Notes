# A Tour of Go

## Basics

### Packages, variables, and functions.

`package main`

```go
import (
  "fmt"
  "math/rand"
)
```

Only exported names (capitalized) are accessible e.g. `Math.Pi`

Functions can have multiple return values

```go
func split(sum int) (x, y int)
```

Variable type and assignment comes after the name

```go
var i, j int = 1, 2
```

Variables types can be inferred
```go
k := 3 // shorthand for var k int = 3
```
^ can only be used within NOT-top-level scope. At top level must use `var`

Basic types
- `bool` `string`
- `int  int8  int16  int32  int64`
- `uint uint8 uint16 uint32 uint64 uintptr`
- `byte` // alias for uint8
- `rune` // alias for int32 represents a Unicode code point
- `float32 float64`
- `complex64 complex128`

To print type `%T` and value `%v`

```go
fmt.Printf("Type: %T Value: %v\n", z, z)`
```

Default values
- `0`
- `false`
- `""`

Values can be re-typed `x := 3; z := uint(x)`

Constants `const Pi = 3.14`

### Flow control statements: for, if, else, switch and defer

`for i := 0; i < 10; i++ {`

init and post are optional `for i < 1000 {`

stataments can be `defer`ed

```go
func main()
  defer fmt.Println("world")

  fmt.Println("hello")
}
// prints "hello world"
```

[Defer is great to make sure we don't forget to do something like close a 
file](https://blog.golang.org/defer-panic-and-recover)

```go
src := os.Open(srcName)
if err != nil {
  return
}
defer src.Close()
```

### More types: pointers, structs, slices, and maps.

Pointers
```go
i, j := 42, 2701

p := &i         // point to i
fmt.Println(*p) // 42 read i through the pointer
*p = 21         // set i through the pointer
fmt.Println(i)  // 21 see the new value of i

p = &j         // point to j
*p = *p / 37   // divide j through the pointer
fmt.Println(j) // 73 see the new value of j
```

Structs
```go
type Vertex struct {
  X int
  Y int
}
v := Vertex{1, 2}
v.X = 4

p = &v
p.X     // shorthand for (*p).X
```

Arrays in Go can't be resized
```go
primes := [6]int{2, 3, 5, 7, 11, 13}
```

Slices are references to sections of an array. Modifying a slice modifies the 
underlying array
```go
s := primes[1:4] // [3 5 7]
```

- `len(s)` gets length of slice
- `cap(s)` gets length of underlying array

`make` to create dynamically sized arrays
```go
b := make([]int, 2, 5) // make(arr, len, cap)
```

```go
s = append(s, 2, 3, 4) // append 2, 3, 4 to end of slice
```

`range` iterates over `slice` or `map`

```go
for i, v : range arr {

for _, v : range arr { // skip index

for i : range arr { // skip value
```

Maps == hash. Use `make` to init
```go
m = make(map[string]Vertex)

m["Bell Labs"] = Vertex{
  40.68433, -74.39967,
}

var m = map [string] Vertex{
  "Bell Labs": { 40.68433, -74.39967, },
```

insert, update, delete
```go
m := make(map[string]int)

m["Answer"] = 42 // insert

m["Answer"] = 48 // update

delete(m, "Answer")

v, ok := m["Answer"] // read
fmt.Println("The value:", v, "Present?", ok)
```

Functions are values and can be passed

```go
func compute(fn func(float64, float64) float64) float64 {
	return fn(3, 4)
}

func main() {

	hypot := func(x, y float64) float64 {
		return math.Sqrt(x*x + y*y)
	}

	fmt.Println(hypot(5, 12))

	fmt.Println(compute(hypot))
	fmt.Println(compute(math.Pow))
}
```

Functions may also be closures

```go
func adder() func(int) int {
	sum := 0
	return func(x int) int {
		sum += x
		return sum
	}
}

func main() {
	pos, neg := adder(), adder()
	for i := 0; i < 10; i++ {
		fmt.Println(
			pos(i),
			neg(-2*i),
		)
	}
}
```

## Methods and interfaces

### Methods

**method** is a function with a special *receiver* argument

```go
type Vertex struct { }

func (v Vertex) abs() float64 { }

v.abs()
```

methods can also work on other types e.g. `type MyFloat float64`

methods cannot modify the receiver unless it's a pointer
```go
package main

import (
	"fmt"
	"math"
)

type Vertex struct {
	X, Y float64
}

func (v Vertex) Abs() float64 { // pythagorean root
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

// if we change to (v Vertex) then it won't modify v
func (v *Vertex) Scale(f float64) {
	v.X = v.X * f
	v.Y = v.Y * f
}

func main() {
	v := Vertex{3, 4}
	fmt.Println(v.Abs()) // 5
	v.Scale(10)
	fmt.Println(v.Abs()) // 50

}
```

Functions with pointer argument only accepts pointers while methods with
pointer argument will accept either a value or a pointer

```go
func ScaleFunc(v *Vertex, f float64) { }

func (v *Vertex) Scale(f float64) {

ScaleFunc(v, 5)  // Compile error!

v.Scale(5)  // OK
```

### Interfaces

An **interface** is a set of method signatures

```go
type Abser interface {
	Abs() float64
}
```

A type *implicitly* implements an interface by implementing its methods.  This
means that the interface can be implimented in any package

```go
type I interface {	M() }

type T struct {	S string }

// This method means type T implements the interface I,
// but we don't need to explicitly declare that it does so.
func (t T) M() { fmt.Println(t.S) }

func main() { var i I = T{"hello"}; i.M() }
```

Interface values can be thought of as a tuple of value, type.

```go
package main; import ("fmt"; "math")

type I interface { M() }

type T struct { S string }
func (t *T) M() { fmt.Println(t.S) }

type F float64
func (f F) M() { fmt.Println(f) }

func describe(i I) { fmt.Printf("(%v, %T)\n", i, i) }

func main() {
	var i I

	i = &T{"Hello"}
	describe(i)				// (&{Hello}, *main.T)
	i.M()							// Hello 

	i = F(math.Pi)
	describe(i)				// (3.141592653589793, main.F)
	i.M()							// 3.141592653589793
}
```

the receiver can be `nil`

```go
func (t *T) M() {
	if t == nil {
		fmt.Println("<nil>")
		return
	}
}
```

*Empty interface* is one with no methods defined. Used to handle values of unknown types

```go
var i interface{}; describe(i) 	// (<nil>, <nil>)

i = 42; describe(i) 						// (42, int)

i = "hello"; describe(i) 				// (hello, string)
```

We can assert the type  and returns 2 values incl. a boolean if the assertion
succeeds `t, ok := i.(T)`

```go
package main; import "fmt"

func main() {
	var i interface{} = "hello"

	s := i.(string); fmt.Println(s) 					// hello

	s, ok := i.(string); fmt.Println(s, ok)		// hello true

	f, ok := i.(float64); fmt.Println(f, ok)	// 0 false

	f = i.(float64) 													// "panic: interface conversion"
	fmt.Println(f)
}
```

A **type switch** allows assertions on the type (as opposed to value)

```go
func do(i interface{}) {
	switch v := i.(type) {
	case int:			fmt.Printf("Twice %v is %v\n", v, v*2)
	case string:	fmt.Printf("%q is %v bytes long\n", v, len(v))
	default: 			fmt.Printf("I don't know about type %T!\n", v)
	}
}

func main() {
	do(21)
	do("hello")
	do(true)
}
```

Define `func (i Interface) String() type {` to allow printing of values with
`fmt.Println`

```go
type Person struct { Name string; Age  int }

func (p Person) String() string { return fmt.Sprintf("%v (%v years)", p.Name, p.Age) }

func main() {
	a := Person{"Arthur Dent", 42}
	z := Person{"Zaphod Beeblebrox", 9001}
	fmt.Println(a, z)
}
```

### Errors

Most functions return an error value. Test whether the error is nil

```go
i, err := strconv.Atoi("4a")
if err != nil {
  fmt.Printf("couldn't convert number: %v\n", err)
    return
}
fmt.Println("Converted integer:", i) // couldn't convert number... invalid syntax
```

To return an error, add it to return statement and implement customer error type

```go
type MyCustomError float64

func Sqrt(x float64) (float64, error) { return 0, nil }
```

e.g.

```go
package main; import ( "fmt";"math")

type ErrNegativeSqrt float64

func (e ErrNegativeSqrt) Error() string {
  return fmt.Sprint("cannot Sqrt negative number ", float64(e))
}

func Sqrt(f float64) (float64, error) {
  if f < 0 { return f, ErrNegativeSqrt(f) }
  else { return math.Sqrt(f), nil }
}

func main() {
  fmt.Println(Sqrt(2)) // 1.41... <nil>
  fmt.Println(Sqrt(-2)) // -2 cannot Sqrt negative number -2
}
```

## Concurrency

**goroutine** is a lightweight thread managed by Go runtime `go func()`

**channel** is a typed conduit to send/receive values

```go
ch := make(chan int) // create chan

ch <- v    // Send v to channel ch.
v := <-ch  // Receive from ch, and assign value to v.
```

```go
func sum(s []int, c chan int) {
  sum := 0
  for _, v := range s {
    sum += v
  }
  c <- sum // send sum to c
}

func main() {
  s := []int{7, 2, 8, -9, 4, 0}

  c := make(chan int)
  go sum(s[:len(s)/2], c)
  go sum(s[len(s)/2:], c)
  x, y := <-c, <-c // receive from c

  fmt.Println(x, y, x+y)
}
```

Channels can be **buffered** e.g. `ch := make(chan int, 100)` will block buffer
after 100 with a `fatal error: all goroutines are asleep - deadlock!`

:caution: but we can use goroutines that will wait for channel availability
- `c3 := func() { c <- 3 }; go c3()`

`for i := range c` will receive values until closed

`close(c)` 

```go
func fibonacci(n int, c chan int) {
  x, y := 0, 1
  for i := 0; i < n; i++ {
    c <- x
    x, y = y, x+y
  }
  close(c)
}

func main() {
  c := make(chan int, 10) // limit to 10
  go fibonacci(cap(c), c) // close when size limit is reached
  for i := range c {
    fmt.Println(i)
  }
}
```

**select** lets goroutine wait on multiple communication operations

```go
func fibonacci(c, quit chan int) {
  x, y := 0, 1
  for {
    select {
    case c <- x:
      x, y = y, x+y
    case <-quit:
      fmt.Println("quit")
      return
    }
  }
}

func main() {
  c := make(chan int)
  quit := make(chan int)
  go func() {
    for i := 0; i < 10; i++ {
      fmt.Println(<-c)
    }
    quit <- 0
  }()
  fibonacci(c, quit)
}
```

**default** in `select` case runs if no other case is ready
```go
select {
case i := <-c:
    // use i
default:
    // receiving from c would block
}
```

Walking and comparing binary tree

```go
package main

import "golang.org/x/tour/tree"
import "fmt"

func Walk(t *tree.Tree, ch chan int) {
  walkRecur(t, ch)
  close(ch)
}

func walkRecur(t *tree.Tree, ch chan int) {
  if t == nil {
    return
  }
  walkRecur(t.Left, ch)
  ch <- t.Value
  walkRecur(t.Right, ch)
}

func Same(t1, t2 *tree.Tree) bool {
  ch1 := make(chan int)
  go Walk(t1, ch1)

  ch2 := make(chan int)
  go Walk(t2, ch2)

  for n := range ch1 {
    if n != <-ch2 {
      return false
    }
  }
  return true
}

func main() {
  ch := make(chan int)
  go Walk(tree.New(1), ch)
  for n := range ch {
    fmt.Printf("%v ", n)
  }
  fmt.Println()
  fmt.Println(Same(tree.New(1), tree.New(1)))
  fmt.Println(Same(tree.New(1), tree.New(2)))
}
```

**mutex** ensures goroutine can access a variable without need for communication
- `Lock`
- `Unlock`

```go
package main; import ("fmt"; "sync"; "time")

// SafeCounter is safe to use concurrently.
type SafeCounter struct {
  v   map[string]int
  mux sync.Mutex
}

// Inc increments the counter for the given key.
func (c *SafeCounter) Inc(key string) {
  c.mux.Lock()
  // Lock so only one goroutine at a time can access the map c.v.
  c.v[key]++
  c.mux.Unlock()
}

// Value returns the current value of the counter for the given key.
func (c *SafeCounter) Value(key string) int {
  c.mux.Lock()
  // Lock so only one goroutine at a time can access the map c.v.
  defer c.mux.Unlock()
  return c.v[key]
}

func main() {
  c := SafeCounter{v: make(map[string]int)}
  for i := 0; i < 1000; i++ {
    go c.Inc("somekey")
  }

  time.Sleep(time.Second)
  fmt.Println(c.Value("somekey"))
}
```
