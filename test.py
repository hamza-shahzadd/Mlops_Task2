from main import StudentsInMLOps
import pytest

@pytest.fixture
def instance():
    return StudentsInMLOps()

def test_enroll_students(instance):
    instance.enrollStudents(5)
    assert instance.getTotalStrength() == 5

def test_drop_students(instance):
    instance.enrollStudents(10)
    instance.dropStudents(3)
    assert instance.getTotalStrength() == 7
