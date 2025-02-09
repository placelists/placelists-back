package repositories

import (
	"placelists/internal/storage/database"
	"placelists/internal/storage/entities"
)

type userRepositoryImpl struct {
	db *database.DB
}

func NewUserRepository(db *database.DB) *userRepositoryImpl {
	return &userRepositoryImpl{db}
}

func (r *userRepositoryImpl) GetByPublicID(publicID string) (*entities.User, error) {
	var u *entities.User
	result := r.db.First(&u, "public_id = ? AND deleted_at IS NULL", publicID)
	return u, result.Error
}

func (r *userRepositoryImpl) Create(u *entities.User) error {
	result := r.db.Create(&u)
	return result.Error
}

func (r *userRepositoryImpl) Update(u *entities.User) error {
	result := r.db.Save(&u)
	return result.Error
}
