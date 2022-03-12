from django.test import LiveServerTestCase
from django.test import TestCase
from selenium.webdriver import Chrome

# Create your tests here.

class TestAccount(LiveServerTestCase):
    def setUp(self):
        self.driver = Chrome("C:/Users/5225s/Desktop/SEPP/lab/chromedriver.exe")

    def test_login(self):
        driver = self.driver
        driver.get('http://127.0.0.1:8000/accounts/login')
        driver.find_element_by_name('username').send_keys('Sumit123')
        #driver.find_element_by_name('username').send_keys('sumit123') checking for wrong username
        driver.find_element_by_name('password').send_keys('1234')
        #driver.find_element_by_name('password').send_keys('1111') checkin for wrong password

        driver.find_element_by_name("submit").click()

    def test_register(self):
        driver = self.driver
        driver.get('http://127.0.0.1:8000/accounts/register')
        driver.find_element_by_name('first_name').send_keys('Sumit')
        driver.find_element_by_name('last_name').send_keys('Patel')
        driver.find_element_by_name('username').send_keys('Sumit123')
        #driver.find_element_by_name('username').send_keys('jay')checking for username that  is already taken
        driver.find_element_by_name('email').send_keys('Patel123@gmail.com')
        driver.find_element_by_name('password1').send_keys('1234')
        driver.find_element_by_name('password2').send_keys('1234')
        #driver.find_element_by_name('password2').send_keys('1232')checking for wrong password

        driver.find_element_by_name("submit").click()

    def test_adminlogin(self):
        driver = self.driver
        driver.get('http://127.0.0.1:8000/accounts/adminlogin')
        driver.find_element_by_name('username').send_keys('admin')
        #driver.find_element_by_name('username').send_keys('admin12') checking for wrong admin username
        driver.find_element_by_name('password').send_keys('1234')
        #driver.find_element_by_name('password').send_keys('1111') checkin for wrong password

        driver.find_element_by_name("submit").click()
    

    def test_addroom(self):
        driver = self.driver
        driver.get('http://127.0.0.1:8000/accounts/addrooms')
        driver.find_element_by_name('name').send_keys('Sumit')
        #driver.find_element_by_name('username').send_keys('admin12') checking for wrong admin username
        driver.find_element_by_name('lname').send_keys('Patel')
        #driver.find_element_by_name('password').send_keys('1111') checkin for wrong password
        driver.find_element_by_name('sem').send_keys('1')
        driver.find_element_by_name('branch').send_keys('CE')
        driver.find_element_by_name('roomno').send_keys('105')

        driver.find_element_by_name("submit").click()

    def test_addstudent(self):
        driver = self.driver
        driver.get('http://127.0.0.1:8000/accounts/addstudent')
        driver.find_element_by_name('studentname').send_keys('Smit')
        driver.find_element_by_name('fathername').send_keys('Vinodkumar')
        driver.find_element_by_name('birthdate').send_keys("2002-05-06")
        driver.find_element_by_name('gender').send_keys('Male')
        driver.find_element_by_name('mobileno').send_keys('7856457856')
        driver.find_element_by_name('branch').send_keys('CE')
        driver.find_element_by_name('age').send_keys('18')
        driver.find_element_by_name('area').send_keys('dfssa')
        driver.find_element_by_name('city').send_keys('fdsgv')
        driver.find_element_by_name('state').send_keys('hdgfc')
        driver.find_element_by_name('email').send_keys('smit@gmail.com')
        driver.find_element_by_name('semester').send_keys('4')

        driver.find_element_by_name("submit").click()

    def test_payment(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/accounts/payment")
        driver.find_elements_by_name('year').send_keys('2021')
        driver.find_elements_by_name('amount').send_keys('78000')
        driver.find_elements_by_name('paytype').send_keys('Case')
        driver.find_elements_by_name('paydetails').send_keys('')
        driver.find_elements_by_name('roomno').send_keys('1109')
        driver.find_elements_by_name('paymentdate').send_keys('23-03-2021')

        driver.find_element_by_name("save").click()

    def test_notice(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/accounts/notice")
        driver.find_element_by_name('notice').send_keys('About rules and ragulations')
        driver.find_element_by_name('description').send_keys('You have to follow all the rule and the regulations')

        driver.find_element_by_name("submit").click()

    def test_notice_back(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/accounts/notice")
        

        driver.find_element_by_name("back").click()

    def test_studentapply(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/accounts/mainpage")
        

        driver.find_element_by_name("apply").click()

    def test_student(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/accounts/mainpage")
        

        driver.find_element_by_name("student").click()
    
    def test_admin(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/accounts/mainpage")
        

        driver.find_element_by_name("admin").click()

    def test_home(self):
        driver = self.driver
        driver.get("http://127.0.0.1:8000/accounts/mainpage")
        

        driver.find_element_by_name("home").click()