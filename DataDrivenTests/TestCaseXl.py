
from .LibraryXL import CommonXl


def test_post_multiple_student_data():
    post_api_url = 'http://thetestingworldapi.com/api/studentsDetails'
    xl_path = './students.xlsx'
    xl_sheet = 'students'

    student = CommonXl(xl_path, xl_sheet)
    for person in student.students_data:
        response = student.send_post_request(post_api_url, person)
        code = response.status_code
        assert code == 201 and student.assert_success(), 'Wrong status code, should be 201'

