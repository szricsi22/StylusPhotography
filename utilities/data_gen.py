def create_photo_list(number):
    photo_list = []

    for i in range(number):
        photo_list.append({
            "title": f"Photo Title{i}",
            "date": "20 09 12",
            "image": f"https://source.unsplash.com/500x500/?nature,water{i}"
        })

    return photo_list


if __name__ == '__main__':
    photo_list = create_photo_list(10)
    pass
