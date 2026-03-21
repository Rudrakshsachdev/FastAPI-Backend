from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.deps import get_db
from schemas.users import UserCreate, UserLogin, UserResponse
from services.auth_services import create_user, login_user

router = APIRouter()


@router.post("/signup", response_model=UserResponse)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)


@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    return login_user(db, user)