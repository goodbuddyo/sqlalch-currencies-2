from typing import List

from sqlalchemy import String, Numeric, create_engine, select, Text, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship

import click
import requests


# this function will combine multiple coin requests into one
# to address the coingecko free account limit

def get_coin_prices(coins, currencies):
    coin_csv = ",".join(coins)
    currency_csv = ",".join(currencies)

    COINGECKO_URL = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_csv}&vs_currencies={currency_csv}"

    data = requests.get(COINGECKO_URL).json()

    return data


class Base(DeclarativeBase):
    pass


class Portfolio(Base):
    __tablename__ = "portfolio"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(256))
    description: Mapped[str] = mapped_column(Text())

    investments: Mapped[List["Investment"]] = relationship(
        back_populates="portfolio")

    def __repr__(self) -> str:
        return f"<Portfolio name: {self.name} with {len(self.investments)} investment(s)>"


class Investment(Base):
    __tablename__ = "investment"

    id: Mapped[int] = mapped_column(primary_key=True)
    coin: Mapped[str] = mapped_column(String(32))
    currency: Mapped[str] = mapped_column(String(3))
    amount: Mapped[float] = mapped_column(Numeric(5, 2))

    portfolio_id: Mapped[int] = mapped_column(ForeignKey("portfolio.id"))
    portfolio: Mapped["Portfolio"] = relationship(
        back_populates="investments")

    def __repr__(self) -> str:
        return f"<Investment coin: {self.coin}, currency: {self.currency}, amount: {self.amount}>"


# engine = create_engine("sqlite:///manager.db")
engine = create_engine("postgresql://postgres:pgpassword@localhost/manager")
Base.metadata.create_all(engine)


@click.group()
def cli():
    pass


if __name__ == "__main__":
    cli()
