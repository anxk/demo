# print123

```go
package main

import (
"fmt"
)

func printer(identity int) func(int) {
	return func(x int) {
		fmt.Printf("printer%d, %d\n", identity, x)
	}
}

type Pool struct {
	queue chan func(x int)
}

func newPool(size int) *Pool {
	pool := &Pool{
		queue: make(chan func(int), size),
	}
	for i := 0; i < size; i++ {
		pool.queue <- printer(i)
	}
	return pool
}

func consume(ch chan int, stopCh chan bool) {
	pool := newPool(3)
	for {
		select {
		case x := <-ch:
			g := <-pool.queue
			g(x)
			pool.queue <- g
		case <-stopCh:
			break
		default:
		}
	}
}

func main() {
	ch := make(chan int)
	stopCh := make(chan bool)
	go consume(ch, stopCh)
	for i := 0; i < 100; i++ {
		ch <- i
	}
	stopCh <- true
}
```