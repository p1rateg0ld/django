# TODO Make dynamic and not company specific
# TODO Write email parser script so someone can send me an email with their info and it will auto make them a signature
# TODO: write try except wrapper for all the keys that might not exist
# TODO: add other departments

# Create a ?.htm file for Outlook signature.
# Takes parameters: FirstName, LastName, Title, EmailAddress, WorkPhone, direct, LinkToCustomImage

# Original html output
# <table cellpadding="0" cellspacing="0" border="0" style="background: none; border-width: 0px; border: 0px; margin: 0; padding: 0;">
# <tr><td colspan="2" style="padding-bottom: 5px; color: #159558; font-size: 18px; font-family: Arial, Helvetica, sans-serif;">NAME</td></tr>
# <tr><td colspan="2" style="color: #333333; font-size: 14px; font-family: Arial, Helvetica, sans-serif;"><i>TITLE</i></td></tr>
# <tr><td colspan="2" style="color: #333333; font-size: 14px; font-family: Arial, Helvetica, sans-serif;"><strong>COMPANY</strong></td></tr>
# <tr><td width="20" valign="top" style="vertical-align: top; width: 20px; color: #159558; font-size: 14px; font-family: Arial, Helvetica, sans-serif;">W:</td><td valign="top" style="vertical-align: top; color: #333333; font-size: 14px; font-family: Arial, Helvetica, sans-serif;">WORKPHONE&nbsp;&nbsp;<span style="color: #159558;">M:&nbsp;</span>z</td></tr>
# <tr><td width="20" valign="top" style="vertical-align: top; width: 20px; color: #159558; font-size: 14px; font-family: Arial, Helvetica, sans-serif;">w:</td><td valign="top" style="vertical-align: top; color: #333333; font-size: 14px; font-family: Arial, Helvetica, sans-serif;"><a href="WEBSITELINK" style=" color: #1da1db; text-decoration: none; font-weight: normal; font-size: 14px;">WEBSITE</a>&nbsp;&nbsp;<span style="color: #159558;">e:&nbsp;</span><a href="mailto:EMAILADDRESSLINK" style="color: #1da1db; text-decoration: none; font-weight: normal; font-size: 14px;">EMAILADDRESS</a></td></tr>
# <tr><td colspan="2" style="padding-bottom: 8px; padding-top: 5px;"><a href="SIGNATUREIMAGELINK"><img src="SIGNATUREIMAGELINK"></a></td></tr>
# </table>
# <body style="color: #333333; font-size: 14px; font-family: Arial, Helvetica, sans-serif;"><h4>EMAIL CONFIDENTIALITY NOTICE</h4>
# <p>
# This communication contains information which is confidential and may also be privileged. It is for the exclusive use of the intended recipient(s). If you are not the intended recipient(s) please note that any distribution, copying or use of this communication or the information in it is strictly prohibited. If you have received this communication in error please notify us by email CustomerService@EasyPayfinance.com or by telephone 800 438 8372 and then delete the email and any copies of it.
# </p>
# </body>

from sys import argv
import argparse
from re import match

# Default URL for image
DEFAULTURL = "https://i.imgur.com/6NCyQgi.jpg"
DEFAULTWEBSITE = "https://www.youtube.com/watch?v=4Rc-NGWEHdU"
DEFAULTFILEPATH = "./Signature.htm"


class info():
    firstname = ''
    lastname = ''
    title = ''
    emailaddress = ''
    workphone = ''
    direct = ''
    department = ''
    linkaddress = ''
    filepath = ''
    websitelink = ''
    

# Gets user info from terminal and returns a dictionary.
def getUserInfo(info):
    for key in info:
        if not info[key]:
            info[key] = input(("please enter {}:").format(key))

    return info


def parseArguments():

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--firstname", default=None, help="Your First Name")
    parser.add_argument("-l", "--lastname", default=None, help="Your Last Name")
    parser.add_argument("-t", "--title", default=None, help="Your Title")
    parser.add_argument("-e", "--emailaddress", default=None, help="Your Email Address")
    parser.add_argument("-w", "--workphone", default=None, help="Your Work Phone")
    parser.add_argument("-c", "--direct", default=None, help="Your direct line")
    parser.add_argument("-d", "--department", default=None, help="Your Department")
    parser.add_argument("-a", "--linkaddress", default=DEFAULTURL, help="URL to a custom signature image")
    parser.add_argument("-p", "--filepath", default=DEFAULTFILEPATH, help="Filepath and name of file to write to (ex: C:/Users/FlashGordon/Documents/ImASignature.html)")
    parser.add_argument("-s", "--websitelink", default=DEFAULTWEBSITE, help="Website address for the image link")
    parser.add_argument("-x", "--noprompt", action="store_true", help="Run silently")

    return vars(parser.parse_args())


def make_HTML(info):
    print (info["filepath"])
    with open(info["filepath"], 'w') as file:

        html_str = """<!DOCTYPE html>"""
        html_str += """\n<table cellpadding="0" cellspacing="0" border="0" style="background: none; border-width: 0px; border: 0px; margin: 0; padding: 0;">"""
        html_str += """\n<tr><td colspan="2" style="padding-bottom: 5px; color: #159558; font-size: 18px; font-family: Arial, Helvetica, sans-serif;">%s %s</td></tr>""" % (info["firstname"], info["lastname"])
        if info["title"]:
            html_str += """\n<tr><td colspan="2" style="color: #333333; font-size: 14px; font-family: Arial, Helvetica, sans-serif;"><i>%s</i></td></tr>""" % (info["title"])
    
        temp = None
        if info["workphone"]:
            temp = """\n<tr><td width="20" valign="top" style="vertical-align: top; width: 20px;"><span style="color: #159558; font-size: 14px; font-family: Arial, Helvetica, sans-serif;">W:&nbsp</span>%s</td></tr>""" % (info["workphone"])
        if info["direct"]:
            temp = temp[:-10] + """&nbsp;&nbsp;<span style="color: #159558;">M:&nbsp;</span>%s</td></tr>""" % (info["direct"])
        if temp:
            html_str += temp
    
        if info["emailaddress"]:
            html_str += """\n<tr><td valign="top" style="vertical-align: top; color: #333333; font-size: 14px; font-family: Arial, Helvetica, sans-serif;"><span style="color: #159558;">E:&nbsp;</span><a href="mailto:%s" style="color: #1da1db; text-decoration: none; font-weight: normal; font-size: 14px;">%s</a></td></tr>""" % (info["emailaddress"], info["emailaddress"])
    
        html_str += """\n<tr><td colspan="2" style="padding-bottom: 8px; padding-top: 5px;"><a href="%s"><img src="%s"></a></td></tr>""" % (info["websitelink"],info["linkaddress"])
        html_str += """\n</table>"""
        
        html_str += department_output(info['department'])
        
        
        html_str += """\n<p style="color: #333333; font-size: 14px; font-family: Arial, Helvetica, sans-serif;"><h4>EMAIL CONFIDENTIALITY NOTICE</h4>
    This communication contains information which is confidential and may also be privileged. It is for the exclusive use of the intended recipient(s). If you are not the intended recipient(s) please note that any distribution, copying or use of this communication or the information in it is strictly prohibited. If you have received this communication in error please notify us by email CustomerService@EasyPayfinance.com or by telephone 800 438 8372 and then delete the email and any copies of it.</p>"""
        
        return html_str
        
def create_file (html_str):
    file.write(html_str)


def department_output(department):
    return_string = ''
    if match('(C|c)ustomer( |)(S|s)ervice', department):
        print('matched customer service')
        return_string = """
        <p style="color: #333333; font-size: 14px; font-family: Arial, Helvetica, sans-serif;">
        Phone: <br>
        Fax: <br>
        
        <h4>Department Hours:</h4><br>
        Monday - Friday: 5am PT - 7pm PT<br>
        Saturday: 8am PT - 4pm PT<br>
        Sunday: Closed<br>
        </p>
        """
    
    elif match(department, '(M|m)erchant( |)(S|s)ervices'):
        pass
    elif match(department, '(S|s)ales'):
        pass
    else:
        pass
    return return_string


if __name__ == "__main__":
    args = parseArguments()
    make_HTML(getUserInfo(args))