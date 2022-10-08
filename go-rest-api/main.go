package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func main() {
	router := gin.Default()

	router.GET("/hello-world", helloWorld)
	router.GET("/hello-world/:id", helloWorldWithID)

	router.Run("localhost:3000")
}

func helloWorld(c *gin.Context) {
	c.IndentedJSON(http.StatusOK, "Hello World!")
}

func helloWorldWithID(c *gin.Context) {
	// id := c.Param("id")

	c.IndentedJSON(http.StatusNotFound, gin.H{"error": "World not found"})
}
