from faker import Faker

fake = Faker()


print(
    f"Hello, my name is {fake.name()}!\nI was born {fake.date()}.\n"
    f"I live at {fake.address()}.\nHave a nice day!"
)
