from faker import Faker

fake = Faker()


def info_generator():
    print(
        f"Hello, my name is {fake.name()}!\nI was born {fake.date()}.\n"
        f"I live at {fake.address()}.\nHave a nice day!"
    )


if __name__ == "__main__":
    info_generator()
