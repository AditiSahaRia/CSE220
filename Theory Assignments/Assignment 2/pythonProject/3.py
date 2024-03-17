def hocBuilder(height):
    if height == 1:
        return 8
    else:
        return 5+hocBuilder(height-1)
#TO DO

print(hocBuilder(5))