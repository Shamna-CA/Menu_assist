from django.conf.urls import url
from django.core.files.storage import FileSystemStorage
from django.db.models import Avg
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from .models import *


# Create your views here.

def admin_home(request):
    return render(request, "admin/index.html")


def login_fun(request):
    return render(request, "login.html")


def login_fun_post(request):
    username = request.POST["username"]
    password = request.POST["pswrd"]

    res = Login.objects.filter(password=password, username=username)
    if res.exists():
        l = Login.objects.get(username=username, password=password)
        request.session["lid"] = l.id
        if l.type == 'admin':
            return redirect('/myapp/admin_home')
        elif l.type == 'Receptionist':
            return redirect('/myapp/r_home')
        else:
            return HttpResponse('''<script>alert("user doesn't exist");history.back()</script>''')
    else:
        return HttpResponse('''<script>alert('user name or password does not match');history.back()</script>''')


def a_change_pswd(request):
    return render(request, "admin/a_change_password.html")


def a_change_pswd_post(request):
    crnt_pswd = request.POST["crnt_pswd"]
    nw_pswd = request.POST["pass"]
    cnfrm_pswd = request.POST["cnfm_pswd"]
    res = Login.objects.filter(password=crnt_pswd, id=request.session['lid'])
    print(res)
    if res.exists():
        if nw_pswd == cnfrm_pswd:
            Login.objects.filter(id=request.session['lid']).update(password=nw_pswd)
            return HttpResponse('''<script>alert('password changed');window.location='/myapp/login_fun/'</script>''')
        else:
            return HttpResponse('''<script>alert('Password does not match');history.back()</script>''')
    else:
        return HttpResponse('''<script>alert('current password does not match');history.back()</script>''')


def add_menu(request):
    return render(request, "admin/Add_menu.html")


def add_menu_post(request):
    name = request.POST["item"]
    price = request.POST["price"]
    duration = request.POST["duration"]
    img = request.FILES["item_img"]
    fs = FileSystemStorage()
    import datetime
    s = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + "/media/" + img.name
    fn = fs.save(s, img)
    obj = Menu()
    obj.item_name = name
    obj.price = price
    obj.img = fs.url(s)
    obj.duration = duration
    obj.save()

    return HttpResponse('''<script>alert('success');window.location='/myapp/v_menu/'</script>''')


def send_reply(request, mid):
    return render(request, "admin/send_reply.html",{'mid':mid})


def send_reply_post(request):
    reply = request.POST["reply"]
    mid=request.POST['mid']
    res=Complaint.objects.filter(pk=mid).update(reply=reply,status="replied")
    return HttpResponse('''<script>alert('success');window.location='/myapp/v_complaint/'</script>''')


def v_menu(request):
    res = Menu.objects.all()
    return render(request, "admin/v_menu.html", {'data': res})


def v_menu_post(request):
    name = request.POST['menu']
    res = Menu.objects.filter(item_name__contains=name)
    return render(request, "admin/v_menu.html", {'data': res})


def delete_menu(request, mid):
    print(mid)
    Menu.objects.get(pk=mid).delete()
    return HttpResponse('''<script>alert('success');window.location='/myapp/v_menu/'</script>''')


def edit_menu(request, mid):
    res = Menu.objects.get(pk=mid)
    return render(request, "admin/edit_menu.html", {'data': res})


def edit_menu_post(request):
    mid = request.POST['mid']
    name = request.POST["item"]
    price = request.POST["price"]
    duration = request.POST["duration"]

    if 'item_img' in request.FILES:
        img = request.FILES["item_img"]
        if img.name != "":
            fs = FileSystemStorage()
            import datetime
            s = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + "/media/" + img.name
            fn = fs.save(s, img)
            obj = Menu.objects.get(pk=mid)
            obj.item_name = name
            obj.price = price
            obj.img = fs.url(s)
            obj.duration = duration
            obj.save()
            return HttpResponse('''<script>alert('success');window.location='/myapp/v_menu/'</script>''')
        else:
            obj = Menu.objects.get(pk=mid)
            obj.item_name = name
            obj.price = price
            obj.duration = duration
            obj.save()
            return HttpResponse('''<script>alert('success');window.location='/myapp/v_menu/'</script>''')
    else:
        obj = Menu.objects.get(pk=mid)
        obj.item_name = name
        obj.price = price
        obj.duration = duration
        obj.save()
        return HttpResponse('''<script>alert('success');window.location='/myapp/v_menu/'</script>''')


def v_feedback(request):
    res = Feedback.objects.all()
    return render(request, "admin/v_feedback.html", {'data': res})


def v_complaint(request):
    res = Complaint.objects.all()
    return render(request, "admin/v_complaint.html", {'data': res})


def v_ordr_rprt(request):
    res = Order.objects.all()
    return render(request, "admin/v_order_report.html", {'data': res})


def v_rating_food(request):
    res = Rating.objects.all()
    return render(request, "admin/v_rating_food.html", {'data': res})


def v_staff(request):
    res = Staff.objects.all()
    return render(request, "admin/v_staff.html", {'data': res})


def v_staff_post(request):
    search = request.POST['staff']
    res = Staff.objects.filter(Name__contains=search)
    return render(request, "admin/v_staff.html", {'data': res})


def delete_staff(request, mid):
    Staff.objects.filter(pk=mid).delete()
    return HttpResponse('''<script>alert('success');window.location='/myapp/v_staff/'</script>''')


def edit_staff(request, mid):
    res = Staff.objects.get(pk=mid)
    return render(request, "admin/e_staff.html", {'data': res})


def edit_staff_post(request):
    mid = request.POST["mid"]
    name = request.POST["name"]
    hs_name = request.POST["hs_name"]
    hs_no = request.POST["hs_no"]
    pin = request.POST["pin"]
    post = request.POST["post"]
    city = request.POST["city"]
    state = request.POST["state"]
    district = request.POST["district"]
    email = request.POST["email"]
    phone = request.POST["phn"]
    age = request.POST["age"]

    gender = request.POST["gender"]
    typ = request.POST["typ"]
    if 'photo' in request.FILES:
        img = request.FILES["photo"]
        if img.name != "":
            fs = FileSystemStorage()
            import datetime
            s = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + "/media/" + img.name
            fn = fs.save(s, img)
            obj = Staff.objects.get(pk=mid)
            obj.Name = name
            obj.hs_name = hs_name
            obj.hs_no = hs_no
            obj.pin = pin
            obj.post = post
            obj.city = city
            obj.State = state
            obj.District = district
            obj.email = email
            obj.Phone = phone
            obj.dob = age
            obj.photo = fs.url(s)
            obj.gender = gender
            obj.typ = typ
            obj.save()
            return HttpResponse('''<script>alert('success');window.location='/myapp/v_staff/'</script>''')
        else:
            obj = Staff.objects.get(pk=mid)
            obj.Name = name
            obj.hs_name = hs_name
            obj.hs_no = hs_no
            obj.pin = pin
            obj.post = post
            obj.city = city
            obj.State = state
            obj.District = district
            obj.email = email
            obj.Phone = phone
            obj.dob = age
            obj.gender = gender
            obj.typ = typ
            obj.save()
            return HttpResponse('''<script>alert('success');window.location='/myapp/v_staff/'</script>''')

    else:
        obj = Staff.objects.get(pk=mid)
        obj.Name = name
        obj.hs_name = hs_name
        obj.hs_no = hs_no
        obj.pin = pin
        obj.post = post
        obj.city = city
        obj.State = state
        obj.District = district
        obj.email = email
        obj.Phone = phone
        obj.dob = age
        obj.gender = gender
        obj.typ = typ
        obj.save()
        return HttpResponse('''<script>alert('success');window.location='/myapp/v_staff/'</script>''')


def add_staff(request):
    return render(request, "admin/a_staff.html")


def add_staff_post(request):
    name = request.POST["name"]
    hs_name = request.POST["hs_name"]
    hs_no = request.POST["hs_no"]
    pin = request.POST["pin"]
    post = request.POST["post"]
    city = request.POST["city"]
    state = request.POST["state"]
    district = request.POST["district"]
    email = request.POST["email"]
    phone = request.POST["phn"]
    dob = request.POST["age"]
    gender = request.POST["gender"]
    typ = request.POST["typ"]
    img = request.FILES["photo"]

    objL = Login.objects.create(username=email, password=phone, type=typ)
    stlid = objL.id

    fs = FileSystemStorage()
    import datetime
    s = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + "/media/" + img.name
    fn = fs.save(s, img)
    obj = Staff()
    obj.Name = name
    obj.hs_name = hs_name
    obj.hs_no = hs_no
    obj.pin = pin
    obj.post = post
    obj.city = city
    obj.State = state
    obj.District = district
    obj.email = email
    obj.Phone = phone
    obj.dob = dob
    obj.photo = fs.url(s)
    obj.gender = gender
    obj.typ = typ
    obj.LOGIN_id = stlid
    obj.save()
    return HttpResponse('''<script>alert('success');window.location='/myapp/v_staff/'</script>''')


def r_home(request):
    return render(request, "receptionist/r_index.html")


def add_tdys_menu(request):
    res = Menu.objects.all()
    res1 = Tdys_menu.objects.all()
    a = ''
    for i in res:
        avgRat = Rating.objects.filter(MENU=i.id).aggregate(Avg('rating'))
        # res1 = Rating.objects.get(MENU=Menu.objects.get(id=i.id))
        a = (avgRat)
    return render(request, "receptionist/add_tdys_menu.html", {'data': res, 'data1': res1, 'rating': a['rating__avg']})


def add_tdys_menu_post(request):
    item_name = request.POST['item_name']
    obj = Tdys_menu()
    obj.MENU = Menu.objects.get(id=item_name)
    obj.save()
    res = Menu.objects.all()
    res1 = Tdys_menu.objects.all()
    a = ''
    for i in res:
        avgRat = Rating.objects.filter(MENU=i.id).aggregate(Avg('rating'))
        # res1 = Rating.objects.get(MENU=Menu.objects.get(id=i.id))
        a = (avgRat)
    return render(request, "receptionist/add_tdys_menu.html", {'data': res, 'data1': res1, 'rating': a['rating__avg']})
    # return HttpResponse('''<script>alert('success');window.location='/myapp/v_tdys_menu/'</script>''')


def v_tdys_menu(request):
    res = Tdys_menu.objects.all()
    a = ''
    for i in res:
        avgRat = Rating.objects.filter(MENU=i.id).aggregate(Avg('rating'))
        # res1 = Rating.objects.get(MENU=Menu.objects.get(id=i.id))
        a = (avgRat)
    return render(request, "receptionist/v_tdys_menu.html", {'data': res, 'rating': a['rating__avg'], "v": ""})


def v_tdys_menu_post(request):
    search = request.POST['tdysmenu']
    res = Tdys_menu.objects.filter(MENU__item_name__icontains=search)
    a = ''
    print(res)
    for i in res:
        avgRat = Rating.objects.filter(MENU=i.id).aggregate(Avg('rating'))
        # res1 = Rating.objects.get(MENU=Menu.objects.get(id=i.id))
        a = (avgRat)
    return render(request, "receptionist/v_tdys_menu.html", {'data': res, 'rating': a['rating__avg'], "v": search})


def delete_tdys_menu(request, mid):
    Tdys_menu.objects.filter(pk=mid).delete()
    return HttpResponse('''<script>alert('success');window.location='/myapp/add_tdys_menu/'</script>''')


def r_change_pswd(request):
    user = request.POST["user"]
    nw_pswd = request.POST["pass"]
    cnfrm_pswd = request.POST["cnfm_pswd"]
    return render(request, "receptionist/r_change_password.html")


def v_bill_tbl_details(request):
    res = Bill.objects.all()
    ttamt = ''
    for i in res:
        print(i.ORDER.total_cost)
        ttamt = int(i.ORDER.TDYS_MENU.MENU.price) * i.ORDER.quantity

    return render(request, "receptionist/v_bill_tbl_dtls.html", {'data': res})


def v_profile(request):
    res = Staff.objects.get(LOGIN_id=request.session["lid"])
    return render(request, "receptionist/v_profile.html", {'data': res})


# ---------------------------------Android-------------------------------------------------------------------------


def and_login_post(request):
    username = request.POST['u_name']
    password = request.POST['pswd']
    res = Login.objects.filter(password=password, username=username)
    if res.exists():
        l = Login.objects.get(username=username, password=password)

        if l.type == 'customer':
            return JsonResponse({'status': "ok", 'type': 'customer'})
        elif l.type == 'Kitchen':
            return JsonResponse({'status': "ok", 'type': 'kitchen'})
        elif l.type == 'service_station':
            return JsonResponse({'status': "ok", 'type': 'Service station'})
        else:
            return JsonResponse({'status': "no"})
    else:
        return JsonResponse({'status': "no"})


# ---------------user-------------------

def and_add_rating_post(request):
    # menu_id = request.POST['menu_id']
    resto_table_id = 1
    menu_id = 12
    rating = request.POST['rating']
    from datetime import datetime
    dates = datetime.now().strftime("%Y-%m-%d")
    obj = Rating()
    obj.RESTO_TABLE_id = resto_table_id
    obj.MENU_id = menu_id
    obj.rating = rating
    obj.date = dates
    obj.save()
    return JsonResponse({'status': "ok"})


def and_add_complaint_post(request):
    # resto_table_id = request.POST['resto_table_id']
    resto_table_id = 1
    complaint = request.POST['cmplnt']
    from datetime import datetime
    dates = datetime.now().strftime("%Y-%m-%d")
    obj = Complaint()
    obj.RESTO_TABLE_id = resto_table_id
    obj.complaint = complaint
    obj.reply = "pending"
    obj.status = "pending"
    obj.date = dates
    obj.save()
    return JsonResponse({'status': "ok"})


def and_add_feedback_post(request):
    # resto_table_id = request.POST['resto_table_id']
    # menu_id = request.POST['menu_id']
    resto_table_id = 1
    menu_id = 8
    feedback = request.POST['feedback']
    from datetime import datetime
    dates = datetime.now().strftime("%Y-%m-%d")
    obj = Feedback()
    obj.MENU_id = menu_id
    obj.RESTO_TABLE_id = resto_table_id
    obj.feedback = feedback
    obj.date = dates
    obj.save()
    return JsonResponse({'status': "ok"})


def and_add_hlp_rqst(request):
    # resto_table_id = request.POST['resto_table_id']
    resto_table_id = 1
    rqst = request.POST['rqst']
    from datetime import datetime
    dates = datetime.now().strftime("%Y-%m-%d")
    from datetime import datetime
    tym = datetime.now().strftime("%H:%M:%S")
    obj = Request()
    obj.RESTO_TABLE_id = resto_table_id
    obj.request = rqst
    obj.date = dates
    obj.time = tym
    obj.save()
    return JsonResponse({'status': "ok"})


def Order_food(request):
    resto_table_id = request.POST['resto_table_id']
    tdys_menu_id = request.POST['tdys_menu_id']
    quantity = request.POST['quantity']
    status = request.POST['status']
    obj = Order()
    obj.resto_table_id = resto_table_id
    obj.tdys_menu_id = tdys_menu_id
    obj.quantity = quantity
    obj.status = status
    obj.save()


def and_v_reply(request):
    # resto_table_id = request.POST['resto_table_id']
    resto_table_id = 1
    res = Complaint.objects.filter(RESTO_TABLE_id=resto_table_id)
    l = []
    for i in res:
        l.append({'id': i.id, 'complaint': i.complaint, 'date': i.date, 'reply': i.reply, 'status': i.status,
                  'resto_tbl_id': i.RESTO_TABLE.id, 'table_no': i.RESTO_TABLE.table_no})
    return JsonResponse({'status': "ok", 'data': l})


def and_v_tdy_menu(request):
    # menu_id = request.POST['MENU_id']
    menu_id = 8
    res = Tdys_menu.objects.filter(MENU_id=menu_id)
    l = []
    for i in res:
        l.append({'id': i.id, 'item_name': i.MENU.item_name, 'img': i.MENU.img, 'price': i.MENU.price, 'duration': i.MENU.duration,
                  'status': i.MENU.status})
    print(l)
    return JsonResponse({'status': "ok", 'data': l})


def and_Cust_v_tdy_spcl(request):
    menu_id = request.POST['menu_id']
    res = Tdys_menu.objects.filter(menu_id=menu_id)
    l = []
    for i in res:
        l.append({'id': i.id, 'item_name': i.item_name, 'img': i.img, 'price': i.price, 'duration': i.duration,
                  'status': i.status})
    return JsonResponse({'status': "ok", 'data': l})


def and_v_ordr_status(request):
    # tdys_menu_id = request.POST['tdys_menu_id']
    # resto_table_id = request.POST['resto_table_id']
    resto_table_id = 1
    res = Order.objects.filter(RESTO_TABLE_id=resto_table_id)
    # res1 =Order.objects.filter(tdys_meni_d = tdys_menu_id)
    l = []
    for i in res:
        l.append({'id': i.id, 'quantity': i.quantity, 'status': i.status, 'date': i.date,
                  'item_name': i.TDYS_MENU.MENU.item_name,
                  'img': i.TDYS_MENU.MENU.img, 'price': i.TDYS_MENU.MENU.price, 'duration': i.TDYS_MENU.MENU.duration,
                  'mstatus': i.TDYS_MENU.MENU.status,
                  'resto_tbl_no': i.RESTO_TABLE.table_no, 'resto_tbl_id': i.RESTO_TABLE.id})
    print(l)
    return JsonResponse({'status': "ok", 'data': l})


def and_v_bill(request):
    # order_id = request.POST['order_id']
    # tdys_menu_id = request.POST['tdys_menu_id']
    # res1 = Bill.objects.filter(tdys_menu_id=tdys_menu_id)
    # res3 = Bill.objects.filter(order_id=order_id)
    resto_table_id = 1
    # resto_table_id = request.POST['resto_table_id']
    res = Bill.objects.filter(RESTO_TABLE_id=resto_table_id)
    l = []
    for i in res:
        ttamt = int(i.ORDER.TDYS_MENU.MENU.price) * i.ORDER.quantity
        l.append({'id': i.id, 'total_amnt': ttamt, 'item_name': i.TDYS_MENU.MENU.item_name, 'img': i.TDYS_MENU.MENU.img,
                  'price': i.TDYS_MENU.MENU.price, 'duration': i.TDYS_MENU.MENU.duration,
                  'mstatus': i.TDYS_MENU.MENU.status, 'quantity': i.ORDER.quantity,
                  'status': i.ORDER.status, 'date': i.ORDER.date, 'resto_tbl_id': i.RESTO_TABLE.id,
                  'table_no': i.RESTO_TABLE.table_no})
    return JsonResponse({'status': "ok", 'data': l})


def and_v_toplist(request):
    return JsonResponse({'status': "ok"})


def and_Cust_v_assin_order(request):
    # staff_id = request.POST['staff_id']
    order_id = 4
    # order_id = request.POST['order_id']
    res = Asign.objects.filter(ORDER_id=order_id)
    l = []
    for i in res:
        ttamt = int(i.ORDER.TDYS_MENU.MENU.price) * i.ORDER.quantity

        l.append({'Name': i.STAFF.Name, 'STAFF': i.STAFF_id, 'item_name': i.ORDER.TDYS_MENU.MENU.item_name,
                  'TDYS_MENU': i.ORDER.TDYS_MENU.MENU.item_name,
                  'img': i.ORDER.TDYS_MENU.MENU.img, 'price': i.ORDER.TDYS_MENU.MENU.price,
                  'quantity': i.ORDER.quantity,
                  'table_no': i.ORDER.RESTO_TABLE.table_no, 'duration': i.ORDER.TDYS_MENU.MENU.duration,
                  'status': i.ORDER.status,
                  'resto_tbl_id': i.ORDER.RESTO_TABLE_id, 'total_amnt': ttamt})
    return JsonResponse({'status': "ok", 'data': l})


# ------------kitchen--------------------------

def and_K_v_order(request):
    resto_table_id = request.POST['resto_table_id']
    res = Order.objects.filter(RESTO_TABLE_id=resto_table_id)
    l = []
    for i in res:
        l.append({'id': i.id, 'quantity': i.quantity, 'item_name': i.MENU.item_name, 'img': i.MENU.img,
                  'price': i.MENU.price, 'duration': i.MENU.duration})
    return JsonResponse({'status': "ok", 'data': l})


def and_k_add_odr_sts(request):
    order_id = request.POST['order_id']
    Order.objects.filter(pk=order_id).update(status='Completed')
    return JsonResponse({'status': "ok"})


# ------------Service Station------------------

def and_srvStn_v_help_rqst(request):
    resto_table_id = request.POST['resto_table_id']
    res = Request.objects.filter(RESTO_TABLE_id=resto_table_id)
    l = []
    for i in res:
        l.append({'id': i.id, 'request': i.request, 'date': i.date, 'time': i.time})
    return JsonResponse({'status': "ok", 'data': l})


def and_srvStn_v_all_ordr_status(request):
    # tdys_menu_id = request.POST['tdys_menu_id']
    resto_table_id = request.POST['resto_table_id']
    res = Order.objects.filter(RESTO_TABLE_id=resto_table_id)
    # res1 =Order.objects.filter(tdys_meni_d = tdys_menu_id)
    l = []
    for i in res:
        l.append({'id': i.id, 'quantity': i.quantity, 'status': i.status, 'date': i.date, 'item_name': i.MENU.item_name,
                  'img': i.MENU.img, 'price': i.MENU.price, 'duration': i.MENU.duration, 'status': i.MENU.status,
                  'resto_tbl_no': i.RESTO_TABLE.table_no})
    return JsonResponse({'status': "ok", 'data': l})


def and_srvStn_asign_order(request):
    staff_id = request.POST['staff_id']
    order_id = request.POST['order_id']
    obj = Asign()
    obj.STAFF_id = staff_id
    obj.ORDER_id = order_id
    obj.save()
    return JsonResponse({'status': "ok"})


def and_srvStn_v_assin_order(request):
    staff_id = request.POST['staff_id']
    order_id = request.POST['order_id']
    res = Asign.objects.filter(ORDER_id=order_id)
    l = []
    for i in res:
        l.append({'Name': i.STAFF.Name, 'item_name': i.MENU.item_name,
                  'img': i.MENU.img, 'price': i.MENU.price, 'quantity': i.ORDER.quantity, 'status': i.ORDER.status,
                  'resto_tbl_no': i.RESTO_TABLE.table_no})
    return JsonResponse({'status': "ok", 'data': l})


def and_srvStn_add_tdy_spcl(request):
    menu_id = request.POST['menu_id']
    obj = Tdys_spcl()
    obj.MENU_id = menu_id
    obj.save()
    return JsonResponse({'status': "ok"})


def and_Srvstn_v_tdys_spcl(request):
    menu_id = request.POST['menu_id']
    res = Tdys_spcl.objects.filter(menu_id=menu_id)
    l = []
    for i in res:
        l.append({'id': i.id, 'item_name': i.item_name, 'img': i.img, 'price': i.price, 'duration': i.duration,
                  'status': i.status})
        return JsonResponse({'status': "ok", 'data': l})
