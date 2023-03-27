def draw_triangle(height):
    for i in range(height-1):
        print(" "*(height-i-1) + "/" + " "*i + " "*i + "\\")
    print("/" + "_"*(2*height-2) + "\\")

draw_triangle(10)