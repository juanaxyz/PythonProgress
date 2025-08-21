
def greeting_people(people: list[str]) -> None:
    for person in people:
        print(f"Hello, {person.capitalize}!!!")
    return 1

warna = ("merah","kuning")

try:
    warna[0] = "biru"
    print(warna)
except Exception as e:
    print(e)
    print("tupple tidak bisa diubah")