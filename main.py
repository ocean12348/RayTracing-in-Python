import io
import sys

image_width = 256
image_height = 256

#Rendering

print("P3")
print(f"{image_width} {image_height}")
print("255")
for j in range(image_height):

    sys.stderr.write(f"\rScanlines remaining: {(image_height - j)}    ")
    sys.stderr.flush()

    for i in range(image_width):
        r = i/(image_height-1)
        g = j/(image_width-1)
        b = 0.0

        ir = int(255.999 * r)
        ig = int(255.999 * g)
        ib = int(255.999 * b)

        print(ir, ig, ib)
