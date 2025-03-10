package repositories

import (
	"placelists-back/internal/storage"
	"placelists-back/internal/storage/entities"
	"placelists-back/pkg/database"
)

type userRepositoryImpl struct {
	db *database.DB
}

func NewUserRepository(db *database.DB) storage.UserRepository {
	return &userRepositoryImpl{db}
}

func (r *userRepositoryImpl) GetByPublicID(id string) (entities.User, error) {
	var u entities.User
	result := r.db.First(u, "public_id = ?", id)
	return u, result.Error
}

func (r *userRepositoryImpl) GetByPublicIDFull(id string) (entities.User, error) {
	var u entities.User
	result := r.db.Preload("FollwedPlacelists").Preload("CreatedPlacelists").First(u, "public_id = ?", id)
	return u, result.Error
}

func (r *userRepositoryImpl) Create(u entities.User) error {
	result := r.db.Create(u)
	return result.Error
}

func (r *userRepositoryImpl) Update(u entities.User) error {
	result := r.db.Save(u)
	return result.Error
}
