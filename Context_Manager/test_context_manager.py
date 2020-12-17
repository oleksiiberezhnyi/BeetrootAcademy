from unittest import TestCase
import context_manager


class TestOpenFile(TestCase):

    def test_get_counter(self):
        with context_manager.OpenFile("testfile.txt"):
            test_counter = context_manager.OpenFile.get_counter()
        with context_manager.OpenFile("testfile2.txt", "w+"):
            test_counter2 = context_manager.OpenFile.get_counter()
        self.assertEqual(test_counter, 1)
        self.assertEqual(test_counter2, 2)

    def test_get_log(self):
        test_log = context_manager.OpenFile.get_log()
        self.assertListEqual(test_log, [["testfile.txt", "r"],
                                        ["testfile2.txt", "w+"]]
                             )
