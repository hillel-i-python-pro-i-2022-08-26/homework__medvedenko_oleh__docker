import logging
from typing import Iterator, Protocol, TypeAlias
from faker import Faker

fake = Faker()

T_LOGIN: TypeAlias = str
T_PASSWORD: TypeAlias = str

log = logging.getLogger()
logging.basicConfig(level=logging.DEBUG)


class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password


class UserProtocol(Protocol):
    login: T_LOGIN
    password: T_PASSWORD


def validate(users: list[UserProtocol], amount: int) -> None:
    logins = set(map(lambda user: user.login, users))
    if amount != (amount_of_logins := len(logins)):
        raise ValueError(
            f'Not enough of unique items. Required: "{amount}". Provided: "{amount_of_logins}"'
        )
    return log.info(f"Successfully generated {len(logins)} unique users.")


def generate_users(amount: int) -> Iterator[User]:
    logins: set[str] = set()
    while len(logins) < amount:
        logins.add(fake.user_name())
    passwords: set[str] = {fake.password() for _ in logins}
    log.info(f"Generated {len(logins)} logins.")
    log.info(f"Generated {len(passwords)} passwords.")
    for login, password in zip(logins, passwords):
        yield User(login=login, password=password)


def main():
    amount = 100_000
    users = list(generate_users(amount=amount))
    validate(users=users, amount=amount)


if __name__ == "__main__":
    main()
