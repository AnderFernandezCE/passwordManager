import pymysql
pymysql.install_as_MySQLdb()
from typing import Any
from contextlib import asynccontextmanager

from sqlalchemy import (
  Boolean,
  Column,
  CursorResult,
  DateTime,
  ForeignKey,
  Identity,
  Insert,
  Integer,
  LargeBinary,
  MetaData,
  Select,
  String,
  Table,
  Update,
  Delete,
  func,
)
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.exc import DatabaseError, OperationalError

from src.config import settings
from src.exceptions import DatabaseDown

DATABASE_URL = str(settings.DATABASE_URL)

engine = create_async_engine(DATABASE_URL)
db = async_sessionmaker(engine, expire_on_commit=False)

@asynccontextmanager
async def get_session():
  session = db()
  try:
    yield session
  except DatabaseError as e:
    print(e)
    await session.rollback()
    raise DatabaseDown()
  finally:
    await session.close()

async def fetch_all(select_query: Select | Insert | Update) -> list[dict[str, Any]]:
  async with get_session() as session:
    result: CursorResult = await session.execute(select_query)
    return result.scalars().all()
    
async def fetch_one(select_query: Select | Insert | Update) -> dict[str, Any] | None:
  async with get_session() as session:
    result: CursorResult = await session.execute(select_query)
    return result.scalars().first()

async def insert_update_delete_one(select_query: Insert | Update | Delete) ->  None:
  async with get_session() as session:
    await session.execute(select_query)
    await session.commit()

async def fetch_one_columns(select_query: Select | Insert | Update):
    """Selects one row with partial columns and returns as object."""
    async with get_session() as session:
      result = await session.execute(select_query)
      return result.first()
    
async def fetch_all_columns(select_query: Select | Insert | Update):
  """Selects multiple row with partial columns and returns as dict."""
  async with get_session() as session:
    result: CursorResult = await session.execute(select_query)
    rows = result.mappings().all()
    return [{key: row[key] for key in select_query.columns.keys()} for row in rows]
  
