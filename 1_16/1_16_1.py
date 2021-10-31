import string
pref_allowed_chars = string.ascii_letters + "1234567890" + "-_."
domain_allowed_chars = string.ascii_letters + "1234567890" + "-."


class Email:
    def __init__(self, email):
        print(self.validate(email))

    def validate(self, email):
        if email.count("@") != 1:
            return False
        email_pref, domain = email.split("@")
        if len(email_pref) == 0 or len(domain) == 0:
            return False
        for char in email_pref:
            if char not in pref_allowed_chars:
                return False
        if email_pref[-1] in "-_.":
            return False
        if email_pref[0] in "-_.":
            return False
        if email_pref.find("..") != -1:
            return False

        for char in domain:
            if char not in domain_allowed_chars:
                return False
        if domain.count(".") != 1:
            return False
        domain_pref, domain_suf = domain.split(".")
        if len(domain_suf) < 2:
            return False
        if domain[-1] == "-":
            return False
        if domain[0] == "-":
            return False
        return True


email1 = Email("john.doe@gmail.com")
email2 = Email("-artour.b@ggg.asd")
email3 = Email("zxcvb@asdf.qw")
email4 = Email("@asdfg.com")
email5 = Email("asdfg@asdfg@zxc")
email6 = Email("asdfgh.com")
