package main

import (
	"net/http"

	"log"

	"github.com/gin-gonic/gin"
)

// Creates a gin router with default middleware:
// logger and recovery (crash-free) middleware
func createRouter() *gin.Engine {

	r := gin.Default()

	r.POST("/combine-cals", combineCalendars)

	// r.GET("/ping", func(c *gin.Context) {
	// 	c.String(http.StatusOK, "pong")
	// })

	return r
}

func main() {
	r := createRouter()
	r.Run("localhost:3003")
}

func combineCalendars(c *gin.Context) {

	request := c.Request
	log.Println(request)

	c.IndentedJSON(http.StatusOK, gin.H{
		"combine": "This will return an ICS when finished.",
	})

}
