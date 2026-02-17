import io

image_width = 256
image_height = 256

#Rendering

print("P3")
print(f"{image_width} {image_height}")
print("255")
for (j = 0; j < image_height; j++){
    for (i = 0; i < image_width; i++){
        r = i/(image_height-1)
        g = j/(image_width-1)
        b = 0.0

        ir = (255.999 * r)
        ig = (255.999 * g)
        ib = (255.999 * b)

        print({ir}, " ", {ig}, " ", {ib})
    }
}
