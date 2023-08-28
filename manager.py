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
    pass


class Investment(Base):
    pass


@click.group()
def cli():
    pass


if __name__ == "__main__":
    cli()
