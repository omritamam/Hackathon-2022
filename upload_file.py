from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui


class Form:
    def __init__(self, path: str, course : str, year : str, questions : str, comments : str):
        """

        :param path:
        :param course: 83151
        :param year: 2005
        :param questions: 134
        :param comments:
        """
        self.path = path
        self.course = course
        self.year = year
        self.questions = questions
        self.comments = comments

id_dict =\
    {
    "80131": "227",
    "67101": "176",
    "80181": "235",
    "80133": "229",
    "67109": "237",
    "67521": "239",
    "80135": "233",

    "83312": "289",
    "80153": "283",
    "80114": "279",
    "80177": "287",
    "80154": "285",
    "80134": "231",
    "80157": "281",
    "83313": "291"}

prop_dict = {
    "80131" : "cs-year-1",
    "80131": "cs-year-1",
    "67101": "cs-year-1",
    "80181": "cs-year-1",
    "80133": "cs-year-1",
    "67109": "cs-year-1",
    "67521": "cs-year-1",
    "80135": "cs-year-1",
    "80134": "cs-year-1",
    "83312": "electrical-engineering-cs",
    "80153": "electrical-engineering-cs",
    "80114": "electrical-engineering-cs",
    "80177": "electrical-engineering-cs",
    "80154": "electrical-engineering-cs",
    "83313": "electrical-engineering-cs"
}

driver = webdriver.Chrome('C:\\Users\\otamam\\Downloads\\chromedriver_win32\\chromedriver.exe')


def wp_login( website , username , password ):

    driver.get( website )

    user_field = driver.find_element_by_id('usernameOrEmail')
    user_field.send_keys( username )
    submitButton = driver.find_element_by_class_name("login__form-action")
    submitButton.click()

    time.sleep(1)
    pass_field = driver.find_element_by_id('password')
    pass_field.send_keys( password )
    time.sleep(1)
    submitButton = driver.find_element_by_class_name("login__form-action")
    submitButton.click()

    time.sleep(1)


def upload_file(form : Form):

    print("https://up-grade.online/all-courses/{0}/{1}-2/".format(prop_dict[form.course], form.course))
    driver.get("https://up-grade.online/all-courses/{0}/{1}-2/".format(prop_dict[form.course], form.course))
    time.sleep(2)

    title_field = driver.find_element_by_name("bbp_topic_title")
    title = form.year[:4] + " " + form.year[-1] + " (" + ",".join(list(form.questions)) + ")"
    title_field.send_keys(title)
    time.sleep(1)

    body_field = driver.find_element_by_id("bbp_topic_content")
    body_field.send_keys(form.comments)
    time.sleep(1)

    upload_click = driver.find_element_by_name("d4p_attachment[]")
    upload_click.send_keys(form.path)
    time.sleep(1)

    submit_bottum = driver.find_element_by_id("bbp_topic_submit")
    submit_bottum.click()
    driver.close()


def full_upload(file_dict):
    file_dict['year'] = file_dict['year'] + file_dict['moed'][-1]
    file_dict['path'] = 'C:\\Users\\otamam\\source\\repos\\Studies\\Hackathon2022\\' + file_dict['path']
    file_dict['questions'] = "1348"
    wp_login("https://up-grade.online/wp-login.php", "idoazulai", "TipoIsBetter")
    upload_file(Form(file_dict["path"], file_dict["course"], file_dict["year"], file_dict["questions"], file_dict["comments"]))


# full_upload({"path":"C:\\Users\\User\\Downloads\\complex3.pdf",
#              "course":"80153",
#              "year":"2008A",
#              "questions":"1348",
#              "comments":"auisdfiuerhgh"})