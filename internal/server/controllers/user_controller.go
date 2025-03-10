package controllers

import (
	"net/http"
	"placelists-back/internal/server"
	"placelists-back/internal/server/dtos"
	"placelists-back/internal/service"
	"placelists-back/internal/service/models"
	"placelists-back/pkg/api"

	"github.com/gin-gonic/gin"
	"github.com/jinzhu/copier"
)

type userControllerImpl struct {
	service service.UserService
}

func NewUserController(service service.UserService) server.UserController {
	return &userControllerImpl{service}
}

// GetUsers return list of all users from the database
// @Summary return list of all
// @Description return list of all users from the database
// @Tags Users
// @Router /users [get]
func (c *userControllerImpl) GetUserMy(ctx *gin.Context) {
	userID := ctx.GetString("userID")
	if len(userID) == 0 {
		errors := []dtos.Error{{Message: "Some error", Code: "000"}}
		api.ErrorResponse(ctx, http.StatusBadRequest, errors)
		return
	}

	user, err := c.service.GetByID(userID)
	if err != nil {
		errors := []dtos.Error{{Message: "Some error", Code: "000"}}
		api.ErrorResponse(ctx, http.StatusBadRequest, errors)
		return
	}

	userDTO := dtos.User{}
	err = copier.Copy(&user, &userDTO)
	if err != nil {
		errors := []dtos.Error{{Message: "Some error", Code: "000"}}
		api.ErrorResponse(ctx, http.StatusBadRequest, errors)
		return
	}

	api.SuccessResponse(ctx, http.StatusOK, userDTO)
}

func (c *userControllerImpl) GetUserByID(ctx *gin.Context) {
	userID := ctx.Param("id")

	user, err := c.service.GetByID(userID)
	if err != nil {
		errors := []dtos.Error{{Message: "Some error", Code: "000"}}
		api.ErrorResponse(ctx, http.StatusBadRequest, errors)
		return
	}

	userDTO := dtos.User{}
	err = copier.Copy(&user, &userDTO)
	if err != nil {
		errors := []dtos.Error{{Message: "Some error", Code: "000"}}
		api.ErrorResponse(ctx, http.StatusBadRequest, errors)
		return
	}

	api.SuccessResponse(ctx, http.StatusOK, userDTO)
}

func (c *userControllerImpl) PutUserByID(ctx *gin.Context) {
	userID := ctx.Param("id")

	var userUpdateDTO dtos.UserUpdate
	err := ctx.ShouldBindJSON(&userUpdateDTO)
	if err != nil {
		errors := []dtos.Error{{Message: "Some error", Code: "000"}}
		api.ErrorResponse(ctx, http.StatusBadRequest, errors)
		return
	}

	userUpdate := models.UserUpdate{}
	err = copier.Copy(&userUpdateDTO, &userUpdate)
	if err != nil {
		errors := []dtos.Error{{Message: "Some error", Code: "000"}}
		api.ErrorResponse(ctx, http.StatusBadRequest, errors)
		return
	}

	user, err := c.service.UpdateByID(userID, userUpdate)
	if err != nil {
		errors := []dtos.Error{{Message: "Some error", Code: "000"}}
		api.ErrorResponse(ctx, http.StatusBadRequest, errors)
		return
	}

	userDTO := dtos.User{}
	err = copier.Copy(&user, &userDTO)
	if err != nil {
		errors := []dtos.Error{{Message: "Some error", Code: "000"}}
		api.ErrorResponse(ctx, http.StatusBadRequest, errors)
		return
	}

	api.SuccessResponse(ctx, http.StatusOK, userDTO)
}
