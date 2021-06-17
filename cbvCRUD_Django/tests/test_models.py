from django.test import TestCase

from cbvApp.models import Student

class StudentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Student.objects.create(firstName='Test')
        Student.objects.create(lastName='Tests')
        Student.objects.create(testScore='15')

    def test_first_name_label(self):
        student = Student.objects.get(id=1)
        field_label = student._meta.get_field('firstName').verbose_name
        self.assertEqual(field_label, 'Test')

    def test_last_name_label(self):
        student = Student.objects.get(id=1)
        field_label = student._meta.get_field('lastName').verbose_name
        self.assertEqual(field_label, 'Tests')

    def test_first_name_max_length(self):
        student = Student.objects.get(id=1)
        max_length = student._meta.get_field('firstName').max_length
        self.assertEqual(max_length, 20)


    '''def test_get_absolute_url(self):
        author = Author.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(author.get_absolute_url(), '/catalog/author/1')'''
