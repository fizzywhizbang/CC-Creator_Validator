#!/usr/bin/env python3

#imports
from faker import Faker


fake = Faker()

Faker.seed(0)
for _ in range(5):
    print(fake.credit_card_full('visa'))