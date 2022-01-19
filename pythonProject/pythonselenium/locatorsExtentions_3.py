from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.maximize_window()
driver.get("https://login.salesforce.com/")

# CSS Selecter also works in this way for only ID tag
# tagename#ID eg : input#username  and tagname is optional so #username will also work
driver.find_element_by_css_selector("#username").send_keys("manu")

# Another Method for only class is tagname.classname  eg : .password
driver.find_element_by_css_selector("input.password").send_keys("1234")

# CSS is Farset locator then any other locator in selenium , for identifying obj on web page
# To clear the box
driver.find_element_by_css_selector(".password").clear()

#link Text locator
#if there is a link in webpage its tagname will be "a" as per html standerds if a tag is not there then first confirm its link or not
driver.find_element_by_link_text("Forgot Your Password?").click()

driver.find_element_by_name("cancel").click()

# generate xpath based on test xpath
# //tagname[text()='xxx']

# Creating X path and CSS by Traversing Tags  if there is no usinque atribute for this label
# xpath : ParetnTag/ChildTag        //div[@id='usernamegroup']/label
# css : ParentTag ChildTag              div[id='usernamegroup'] label

#xpath : ParetnTag/ChildTag you want from grand parent level //form[@name='login']/div[@id="usernamegroup"]/labe
# css : ParentTag ChildTag form[name='login'] div[id="usernamegroup"] label
# if yo have multiple div then go with xpath

print(driver.find_element_by_xpath("//form[@name='login']/div[@id='usernamegroup']/label").text)

print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(3)").text)

# absutulte xpath vs relative xpath , abs xpath start from from beging html ->boday->then trevesr down but rel path is like on target 