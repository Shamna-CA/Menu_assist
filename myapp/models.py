# import dateutil.utils
from django.db import models


# Create your models here.

class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    type = models.CharField(max_length=50)

    class Meta:
        db_table = "login"


class Menu(models.Model):
    item_name = models.CharField(max_length=50)
    img = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    duration = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    class Meta:
        db_table = "Menu"


class Tdys_menu(models.Model):
    MENU = models.ForeignKey(Menu, on_delete=models.CASCADE)

    class Meta:
        db_table = "Tdys_menu"


class Resto_table(models.Model):
    table_no = models.CharField(max_length=10)


class Order(models.Model):
    RESTO_TABLE = models.ForeignKey(Resto_table, on_delete=models.CASCADE,default=0)
    TDYS_MENU = models.ForeignKey(Tdys_menu, on_delete=models.CASCADE)
    quantity = models.IntegerField(max_length=10, default=1)
    status = models.CharField(max_length=50)
    date = models.DateField(default='2023-04-03')

    @property
    def total_cost(self):
        return self.quantity * self.TDYS_MENU.MENU.price

    def __unicode__(self):
        return self.TDYS_MENU.MENU.item_name
    class Meta:
        db_table = "Order"


class Bill(models.Model):
    bill_no = models.CharField(max_length=50)
    ORDER = models.ForeignKey(Order, on_delete=models.CASCADE)
    TDYS_MENU = models.ForeignKey(Tdys_menu, on_delete=models.CASCADE)
    total_amnt = models.CharField(max_length=50)
    RESTO_TABLE = models.ForeignKey(Resto_table, on_delete=models.CASCADE)

    class Meta:
        db_table = "Bill"


class Rating(models.Model):
    MENU = models.ForeignKey(Menu, on_delete=models.CASCADE)
    RESTO_TABLE = models.ForeignKey(Resto_table, on_delete=models.CASCADE, default=0)
    rating = models.CharField(max_length=50)
    date = models.DateField()

    class Meta:
        db_table = "Rating"


class Complaint(models.Model):
    RESTO_TABLE = models.ForeignKey(Resto_table, on_delete=models.CASCADE)
    complaint = models.CharField(max_length=50)
    date = models.DateField()
    reply = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    class Meta:
        db_table = "Complaint"


class Feedback(models.Model):
    RESTO_TABLE = models.ForeignKey(Resto_table, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=100)
    MENU = models.ForeignKey(Menu, on_delete=models.CASCADE)
    date = models.DateField(auto_now=False, auto_now_add=False, null=True)

    class Meta:
        db_table = "Feedback"


class Staff(models.Model):
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    hs_name = models.CharField(max_length=100)
    hs_no = models.CharField(max_length=10)
    pin = models.CharField(max_length=10)
    post = models.CharField(max_length=100)
    place = models.CharField(max_length=150, default='place')
    city = models.CharField(max_length=100)
    District = models.CharField(max_length=100)
    State = models.CharField(max_length=100)
    email = models.CharField(max_length=20)
    Phone = models.CharField(max_length=10)
    photo = models.CharField(max_length=200)
    gender = models.CharField(max_length=100)
    typ = models.CharField(max_length=50)
    dob = models.DateField(auto_now=False, auto_now_add=False, null=True)

    class Meta:
        db_table = "Staff"


# ----------------------------------------------------------------


class Request(models.Model):
    RESTO_TABLE = models.ForeignKey(Resto_table, on_delete=models.CASCADE)
    request = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        db_table = "Request"


class Tdys_spcl(models.Model):
    MENU = models.ForeignKey(Menu, on_delete=models.CASCADE)

    class Meta:
        db_table = "Tdys_spcl"


class Order_sub(models.Model):
    MENU = models.ForeignKey(Menu, on_delete=models.CASCADE)
    ORDER = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=20)

    class Meta:
        db_table = "Order_sub"


class Asign(models.Model):
    STAFF = models.ForeignKey(Staff, on_delete=models.CASCADE)
    ORDER = models.ForeignKey(Order, on_delete=models.CASCADE)

    class Meta:
        db_table = "Asign"