import logging

from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from ..dtos.auth import Token, User
from ..services.auth import (
    authenticate_user,
    create_access_token,
    get_current_active_user,
)
from ...core.config import settings
from ...core.database import fake_users_db


router = APIRouter()
logger = logging.getLogger("uvicorn.error")


@router.post(
    "/token",
    response_model=Token,
    status_code=status.HTTP_200_OK,
)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    user = authenticate_user(
        fake_users_db, form_data.username, form_data.password
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


@router.get(
    "/users/me/",
    response_model=User,
    status_code=status.HTTP_200_OK,
)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return current_user
