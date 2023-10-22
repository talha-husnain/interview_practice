# import png
# import random
# import sys
# import math

# def generate_image(width, height, num_colors=10):
#     image = []

#     # Generate a list of distinct random colors
#     random_colors = {(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(num_colors)}

#     # Calculate the size of each 'cell' in the grid
#     cell_width = width // int(math.sqrt(num_colors))
#     cell_height = height // int(math.sqrt(num_colors))

#     # Create a grid of colors
#     color_grid = [[random.choice(list(random_colors)) for _ in range(int(math.ceil(width / cell_width)))]
#                    for _ in range(int(math.ceil(height / cell_height)))]

#     for y in range(height):
#         row = []
#         for x in range(width):
#             # Determine which cell this pixel belongs to in the grid
#             cell_x = x // cell_width
#             cell_y = y // cell_height

#             # Get the color for this cell
#             red, green, blue = color_grid[cell_y][cell_x]

#             row.extend([red, green, blue])
#         image.append(row)

#     return image

# def save_image(image_data, width, height, filename):
#     with open(filename, 'wb') as f:
#         writer = png.Writer(width=width,
#                             height=height,
#                             bitdepth=8,
#                             greyscale=False)
#         writer.write(f, image_data)

# def main():
#     try:
#         width = int(input("Enter the width of the image: "))
#         height = int(input("Enter the height of the image: "))

#         image_data = generate_image(width, height)
#         save_image(image_data, width, height, 'random_image_with_10_colors.png')

#         print(
#             f"Image generated with dimensions {width}x{height} and saved as 'random_image_with_10_colors.png'"
#         )

#     except MemoryError:
#         print("Out of memory! Try a smaller image size.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# if __name__ == '__main__':
#     main()


import png
import random
import math


def draw_pattern(row, start, end, color1, color2):
    for i in range(start, end, 6):
        row[i:i+3] = color1
        row[i+3:i+6] = color2


def generate_image(width, height, num_colors=10):
    image = []

    random_colors = [(random.randint(0, 255), random.randint(
        0, 255), random.randint(0, 255)) for _ in range(num_colors)]
    cell_width = width // int(math.sqrt(num_colors))
    cell_height = height // int(math.sqrt(num_colors))

    color_grid = [[random.choice(random_colors) for _ in range(width // cell_width)]
                  for _ in range(height // cell_height)]
    pattern_grid = [[random.choice([None, 'checker']) for _ in range(width // cell_width)]
                    for _ in range(height // cell_height)]

    for y in range(height):
        row = []
        for x in range(width):
            cell_x = x // cell_width
            cell_y = y // cell_height

            red, green, blue = color_grid[cell_y][cell_x]

            row.extend([red, green, blue])

            pattern = pattern_grid[cell_y][cell_x]
            if pattern == 'checker':
                if (y % cell_height) < (cell_height // 2):
                    draw_pattern(row, cell_x * cell_width * 3, (cell_x + 1) * cell_width * 3, [
                                 red, green, blue], [255 - red, 255 - green, 255 - blue])

        image.append(row)

    return image


def save_image(image_data, width, height, filename):
    with open(filename, 'wb') as f:
        writer = png.Writer(width=width,
                            height=height,
                            bitdepth=8,
                            greyscale=False)
        writer.write(f, image_data)


def main():
    try:
        width = int(input("Enter the width of the image: "))
        height = int(input("Enter the height of the image: "))

        image_data = generate_image(width, height)
        save_image(image_data, width, height, 'interactive_random_image.png')

        print(
            f"Interactive image generated with dimensions {width}x{height} and saved as 'interactive_random_image.png'")

    except MemoryError:
        print("Out of memory! Try a smaller image size.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    main()
