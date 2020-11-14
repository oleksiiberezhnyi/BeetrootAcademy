caffe = dict(
    name = "Super Cafe",
    location = "Kyiv",
    work_time = (9, 18),
    staff = [
        dict(
            name = "Ivan",
            position = "Barista"
        ),
        dict(
            name = "Jana",
            position = "Barista"
        )
    ]
)

print(f"caffe type is {type(caffe)}\n{caffe}")

for number in [1, 2, 0, 5, 3, ]:
    print(number)

for key in caffe.values():
    print(key)
