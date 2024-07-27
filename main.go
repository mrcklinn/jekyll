package main

import (
	"flag"
	"fmt"
	"log"
	"net/http"
)

type Server struct {
	listenAddr string
}

func NewServer(listenAddr string) *Server {
	return &Server{
		listenAddr: listenAddr,
	}
}

func (s *Server) Start() error {
	// Serve static files from the "static" directory
	fs := http.FileServer(http.Dir("./"))
	http.Handle("/", fs)

	return http.ListenAndServe(s.listenAddr, nil)
}

func main() {
	listenAddr := flag.String("listenaddr", ":3000", "the server address")
	flag.Parse()
	server := NewServer(*listenAddr)
	fmt.Println("Server running on", *listenAddr)
	log.Fatal(server.Start())
}
