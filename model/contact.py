from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, id = None, nickname=None, title=None, company=None, address=None, homephone=None,
                       mobilephone=None, workphone=None, fax=None, email1=None, email2=None, email3=None,
                 homepage=None, address2=None, phone2=None, notes=None, all_phones_from_home_page = None, all_emails_from_home_page = None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.fax = fax
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page


    def __repr__(self):
        return("%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s" % (self.id, self.firstname, self.lastname, self.middlename, self.nickname, self.title, self.company, self.address,
                                                        self.homephone, self.mobilephone, self.workphone, self.fax, self.email1, self.email2, self.email3,
                                                           self.address2, self.phone2, self.notes))

    def __eq__(self, other):
        return self.id == other.id and self.lastname == other.lastname, self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize