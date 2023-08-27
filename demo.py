from sqlalchemy import String, Numeric, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session


class Base(DeclarativeBase):
    pass


class Investment(Base):
    __tablename__ = "investment"

    id: Mapped[int] = mapped_column(primary_key=True)
    coin: Mapped[str] = mapped_column(String(32))
    currency: Mapped[str] = mapped_column(String(3))
    amount: Mapped[float] = mapped_column(Numeric(5, 2))

    def __repr__(self) -> str:
        return f"<Investment coin: {self.coin}, currency: {self.currency}, amount: {self.amount}>"


engine = create_engine("sqlite:///manager.db")
Base.metadata.create_all(engine)

bitcoin = Investment(coin="bitcoin", currency="USD", amount="1.0")
ethereum = Investment(coin="ethereum", currency="GBP", amount="10.0")
dogecoin = Investment(coin="dogecoin", currency="EUR", amount="100.0")

with Session(engine) as session:

    # --------------------------------
    # -- CRUD EXAMPLES
    # -- uncomment this code to see a single CREATE example

    # session.add(bitcoin)
    # session.commit()

    # --------------------------------
    # -- uncomment this code to see a CREATE many example

    # session.add_all([ethereum, dogecoin])
    # session.commit()

    # --------------------------------
    # -- uncomment this code to see 3 different READ examples

    # stmt = select(Investment).where(Investment.coin == 'bitcoin')
    # print(stmt)

    # investment = session.execute(stmt).scalar_one()
    # print(investment)

    # stmt = select(Investment).where(Investment.amount > 5)
    # investments = session.execute(stmt).scalars().all()

    # for investment in investments:
    #    print(investment)

    # --------------------------------
    # -- uncomment this code to see a CRUD UPDATE example
    # -- The amount attribute of the id = 1 element is updated to 1.234
    # -- notice the dirty attribute

    bitcoin = session.get(Investment, 1)
    bitcoin.amount = 1.234
    print(session.dirty)
    session.commit()

    print(bitcoin)

    # --------------------------------
    # -- uncomment this code to see a CRUD DELETE example
    # -- But first view the db table
    # -- Enter the id of the the row you wish to delete as the 2nd get() param

    dogecoin = session.get(Investment, 3)
    session.delete(dogecoin)
    print(session.deleted)
    session.commit()

    # --------------------------------
    # -- uncomment this code to replace the deleted example

    # session.add(dogecoin)
    # session.commit()

    # --------------------------------
