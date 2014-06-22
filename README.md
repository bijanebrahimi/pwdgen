pwdgen
======

This is a very simple Python/GTK frontend to my previouse password generator script also called [pwdgen](https://gitorious.org/pwdgen). the Idea is to never remember any password or write it down. **any good password should be hard to remember but easy to regenerate at anytime**.

screenshot:
------

TO BE ADDED SOON

Concepts
------

with a given **master password** and a **salt** we can create countless strong and unique passwords. to do things a little complex for a better password, we added an **offset** and **length** number which acts as even a more unique filter on the output.

**FOR EXAMPLE**: to create a password for your gmail account you can use the following inputs.

    Master password = 123456
    Salt/Domain = gmail.com
    offset = 1
    length = 20
    
    OUTPUT = DQwYzc2NjVjNDg5YzBiY

as you may figure it by now, the length is actually the length of the password you desire. it could any number between 1 and 99 (i can't see any reason why not even more than 99 since you don't need to remember it).

* Tip #1: you can use a **fixed phrase for your master password**, but use a reasonable and unique phrases for salt key. that should be one of many strategies you may want to use to create your passwords.

* Tip #2: also you can **change the offset number every 6 months** or so to change your password periodically over time. you can a use formula of your choice for the ofset number.

Issues:
------

* the generated password is only consists of alpha numerical characters plus = sign (0-9A-Za-z=). any more complex password is beyond the capabilities of this script. but it can be easily added ;)

