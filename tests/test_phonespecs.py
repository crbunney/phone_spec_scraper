from unittest import TestCase

from phonespecs import parse_phone_html, Field


class ParsePhoneHtmlTest(TestCase):

    @classmethod
    def setUpClass(cls):
        with open('google_pixel_2-8733.html', 'r', encoding='iso-8859-1') as fixture_file:
            cls.TESTIN = fixture_file.read()

    def test_battery_cap(self):
        testout = parse_phone_html(self.TESTIN, [Field.BATTERY_SIZE])
        self.assertDictEqual(testout, {Field.BATTERY_SIZE: '2700'}, msg="Parsed output didn't match expected")

    def test_battery_tech(self):
        testout = parse_phone_html(self.TESTIN, [Field.BATTERY_TECH])
        self.assertDictEqual(testout, {Field.BATTERY_TECH: 'Li-Ion'}, msg="Parsed output didn't match expected")

    def test_camera_main(self):
        testout = parse_phone_html(self.TESTIN, [Field.CAMERA_MAIN])
        self.assertDictEqual(testout, {Field.CAMERA_MAIN: '12'}, msg="Parsed output didn't match expected")

    def test_camera_front(self):
        testout = parse_phone_html(self.TESTIN, [Field.CAMERA_FRONT])
        self.assertDictEqual(testout, {Field.CAMERA_FRONT: '8'}, msg="Parsed output didn't match expected")

    def test_chipset(self):
        testout = parse_phone_html(self.TESTIN, [Field.CHIPSET])
        self.assertDictEqual(testout, {Field.CHIPSET: 'Qualcomm MSM8998 Snapdragon 835 (10 nm)'},
                             msg="Parsed output didn't match expected")

    def test_model(self):
        testout = parse_phone_html(self.TESTIN, [Field.MODEL])
        self.assertDictEqual(testout, {Field.MODEL: 'Google Pixel 2'}, msg="Parsed output didn't match expected")

    def test_price(self):
        testout = parse_phone_html(self.TESTIN, [Field.PRICE])
        self.assertDictEqual(testout, {Field.PRICE: '~€550'}, msg="Parsed output didn't match expected")

    def test_ram(self):
        testout = parse_phone_html(self.TESTIN, [Field.RAM])
        self.assertDictEqual(testout, {Field.RAM: '4'}, msg="Parsed output didn't match expected")

    def test_released(self):
        testout = parse_phone_html(self.TESTIN, [Field.RELEASED])
        self.assertDictEqual(
            testout, {Field.RELEASED: 'Released 2017, October'}, msg="Parsed output didn't match expected")

    def test_resolution(self):
        testout = parse_phone_html(self.TESTIN, [Field.RESOLUTION])
        self.assertDictEqual(testout, {Field.RESOLUTION: '1080x1920 pixels'}, msg="Parsed output didn't match expected")

    def test_size(self):
        testout = parse_phone_html(self.TESTIN, [Field.SIZE])
        self.assertDictEqual(testout, {Field.SIZE: '5.0"'}, msg="Parsed output didn't match expected")

    def test_storage(self):
        testout = parse_phone_html(self.TESTIN, [Field.STORAGE])
        self.assertDictEqual(
            testout, {Field.STORAGE: '64/128GB storage, no card slot'}, msg="Parsed output didn't match expected")

    def test_all(self):
        testout = parse_phone_html(self.TESTIN, list(Field))

        expected = {
            Field.BATTERY_SIZE: '2700',
            Field.BATTERY_TECH: 'Li-Ion',
            Field.CAMERA_MAIN: '12',
            Field.CAMERA_FRONT: '8',
            Field.CHIPSET: 'Qualcomm MSM8998 Snapdragon 835 (10 nm)',
            Field.MODEL: 'Google Pixel 2',
            Field.PRICE: '~€550',
            Field.RAM: '4',
            Field.RELEASED: 'Released 2017, October',
            Field.RESOLUTION: '1080x1920 pixels',
            Field.SIZE: '5.0"',
            Field.STORAGE: '64/128GB storage, no card slot',
        }
        self.assertDictEqual(testout, expected, msg="Parsed output didn't match expected")
