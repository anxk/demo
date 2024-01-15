# wait group

```go
func TestWaitgroup(t *testing.T) {
   var wg sync.WaitGroup
   wg.Add(2)

   go func() {
      sendHttpRequest("https://baidu.com")
      wg.Done()
   }()

   go func() {
      sendHttpRequest("https://baidu.com")
      wg.Done()
   }()
   wg.Wait()
}
```