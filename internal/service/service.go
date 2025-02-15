package service

import "placelists/internal/service/models"

type Service struct {
	Place     PlaceService
	Placelist PlacelistService
	User      UserService
}

type PlaceService interface {
	GetByID(placeID string, userID string) (models.Place, error)
	GetByNameOrAddress(query string, userID string) ([]models.Place, error)
	Create(userID string, pc models.PlaceCreate) error
	UpdateByID(placeID string, userID string, pu models.PlaceUpdate) error
}

type PlacelistService interface {
	GetByID(placelistID string, userID string) (models.Placelist, error)
	GetByNameOrAuthor(query string, userID string) ([]models.Placelist, error)
	GetFollowedByUserID(userID string) ([]models.Placelist, error)
	GetCreatedByUserID(userID string) ([]models.Placelist, error)
	GetPlacesByID(placelistID string, userID string) ([]models.Place, error)
	Create(userID string, pc models.PlacelistCreate) error
	UpdateByID(placelistID string, userID string, pu models.PlacelistUpdate) error
}

type UserService interface {
	GetByID(id string) (models.User, error)
	UpdateByID(id string, uu models.UserUpdate) error
}
