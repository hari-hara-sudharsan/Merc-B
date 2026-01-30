from faker import Faker

fake = Faker("en_IN")

def mock_competitors():
    return [
        {
            "name": fake.company(),
            "strength": "Strong local presence",
            "weakness": "Low tech adoption"
        }
        for _ in range(3)
    ]

def mock_trends():
    return [
        "Kerala student startup boom",
        "AI adoption in MSMEs",
        "EdTech demand in tier-2 cities"
    ]
