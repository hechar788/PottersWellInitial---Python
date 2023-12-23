from flask import flash, redirect, url_for

class handler:

    def __init__(self, tup):
        self.valid = tup[0]
        self.msg= tup[1]
        self.state = tup[2]

    def handle_flash(self):
        return flash(self.msg)

def handle(tup):
    instance = handler(tup)

    instance.handle_flash()

    if instance.valid:
        if instance.state:
            return (redirect(url_for('views.home')), instance.msg)
        return (redirect(url_for('views.login')), instance.msg)