import random as r;
import string as s;
special = "!@#$%^&*()_+:<>?;,.|~";
passw = r.sample(s.ascii_letters+s.digits+special,10);
password = "".join(passw);
print(passw);
print(password);