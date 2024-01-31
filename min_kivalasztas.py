import sys


def tetel():
    db = 0
    vege = 0
    legkisebb = sys.maxsize
    while (szam := int(input("# "))) != vege:
        if szam < legkisebb:
            legkisebb = szam
        db += 1

    print(f"{db} számból a legkisebb: {legkisebb}")
