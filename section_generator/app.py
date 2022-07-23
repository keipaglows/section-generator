from PIL import Image


_SECTION_WIDTH = 3


def draw_variants(result_image: Image, section: Image, row: int):
    for offset, angle in enumerate([0, 90, 180, 270]):
        rotated = section.rotate(angle)
        result_image.paste(rotated, (
            _SECTION_WIDTH * offset,
            _SECTION_WIDTH * row
        ))


def create_whole_set():
    s_image = Image.open('data/sections.png')
    variant_row = 0
    section_width = s_image.width // 3
    section_height = s_image.height // 3
    result_image = Image.new('RGBA', (
        _SECTION_WIDTH * 4,  # number of rotations
        _SECTION_WIDTH * section_height * section_width
    ))

    for x_section in range(section_width):
        for y_section in range(section_height):
            x = x_section * _SECTION_WIDTH
            y = y_section * _SECTION_WIDTH

            section = s_image.crop((
                x,
                y,
                x + _SECTION_WIDTH,
                y + _SECTION_WIDTH
            ))
            draw_variants(result_image, section, variant_row)
            variant_row += 1

    result_image.save('data/generated.png')


if __name__ == '__main__':
    create_whole_set()
