from unittest import TestCase

from phonespecs import parse_phone_html, Field


class ParsePhoneHtmlTest(TestCase):

    def test_parse_phone_html(self):
        with open('google_pixel_2-8733.php', 'r', encoding='iso-8859-1') as testin:
            testout = parse_phone_html(testin.read(), [Field.CHIPSET])

        self.assertDictEqual(testout, {Field.CHIPSET: 'Qualcomm MSM8998 Snapdragon 835 (10 nm)'},
                             msg="Parsed output didn't match expected")
