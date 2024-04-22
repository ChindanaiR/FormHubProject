import django
import sys
import subprocess
import os

# Django settings module environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FormHub.settings")
django.setup()

from authentication.models import *
from userprofile.models import *
from authentication.models import *
from form_management.models import *

def create_point_range():
    if not Point.objects.all().exists():
        try:
            Point.objects.create(
                form_size = "S",
                context = "SEL",
                point = 10,
                description = "Buying small form",
                lower_bound = 1,
                upper_bound = 1,
            )
            Point.objects.create(
                form_size = "S",
                context = "ANS",
                point = 10,
                description = "Answering small form",
                lower_bound = 1,
                upper_bound = 1,
            )
            Point.objects.create(
                form_size = "M",
                context = "SEL",
                point = 20,
                description = "Buying medium form",
                lower_bound = 2,
                upper_bound = 2,
            )
            Point.objects.create(
                form_size = "M",
                context = "ANS",
                point = 20,
                description = "Answering medium form",
                lower_bound = 2,
                upper_bound = 2,
            )
            Point.objects.create(
                form_size = "L",
                context = "SEL",
                point = 30,
                description = "Buying large form",
                lower_bound = 3,
                upper_bound = 3,
            )
            Point.objects.create(
                form_size = "L",
                context = "ANS",
                point = 30,
                description = "Answering large form",
                lower_bound = 3,
                upper_bound = 3,
            )
            print("[+] Point table has been created.")
        except:
            print("[-] Something went wrong with Point script.")
    else:
        print("[!] Creating Point script is already run.")

def create_superuser():
    if not User.objects.filter(is_superuser = True).exists():
        try:
            User.objects.create_superuser(
                "admin",
                "admin@admin.com", 
                "admin",
            )
            print("[+] Superuser has been created.")
        except:
            print("[-] Something went wrong with creating superuser script.")
    else:
        print("[!] Creating superuser script is already run.")

def create_normal_users():
    if not User.objects.filter(is_superuser = False).exists():
        try:
            User.objects.create_user(
                first_name = "John",
                last_name = "Doe",
                username = "John D.",
                email = "john@mail.com",
                student_id = "6441111126",
                password = "123",
            )
            User.objects.create_user(
                first_name = "Jimmy",
                last_name = "Doe",
                username = "Jimmy D.",
                email = "jimmy@mail.com",
                student_id = "6442222226",
                password = "123",
            )
            User.objects.create_user(
                first_name = "Jane",
                last_name = "Doe",
                username = "Jane D.",
                email = "jane@mail.com",
                student_id = "6443333326",
                password = "123",
            )
            print("[+] Normal user has been created.")
        except:
            print("[-] Something went wrong with creating normal user script.")
    else:
        print("[!] Creating normal user script is already run.")

def create_redeem_items():
    if not RedeemItem.objects.all().exists():
        try:
            RedeemItem.objects.create(
                redeem_code = "DCT",
                description = "Momo 10%",
                point = 40,
            )
            RedeemItem.objects.create(
                redeem_code = "PRZ",
                description = "iPod",
                point = 200,
            )
            RedeemItem.objects.create(
                redeem_code = "PRZ",
                description = "iPhone Case",
                point = 20,
            )
            RedeemItem.objects.create(
                redeem_code = "PRZ",
                description = "Airpods Case",
                point = 25,
            )
            RedeemItem.objects.create(
                redeem_code = "DCT",
                description = "จุฬา 48 discount 15%",
                point = 10,
            )
            RedeemItem.objects.create(
                redeem_code = "DCT",
                description = "TUCU T-shirt 10% discount",
                point = 10,
            )
            RedeemItem.objects.create(
                redeem_code = "CSH",
                description = "Convert 100 points to 100THB",
                point = 10,
            )
            RedeemItem.objects.create(
                redeem_code = "CSH",
                description = "Convert 300 points to 100THB",
                point = 30,
            )
            RedeemItem.objects.create(
                redeem_code = "CSH",
                description = "Convert 500 points to 100THB",
                point = 50,
            )
            print("[+] RedeemItem table has been created.")
        except:
            print("[-] Something went wrong with creating redeem item script.")
    else:
        print("[!] Creating ReedeemItem script is already run.")

def create_forms():
    if not Form.objects.all().exists():
        try:
            Form.objects.create(
                form_name = "Form",
                description = "This is a description",
                design = [],
                owner = User.objects.get(pk = 1),
                form_point = Point.object.get(context = "ANS", form_size = "S")
            )
            print("[+] Forms has been created.")
        except:
            print("[-] Something went wrong with creating forms script.")
    else:
        print("[!] Creating forms script is already run.")


if __name__ == "__main__":
    print("[*] Initializing the database")
    create_point_range()
    create_superuser()
    create_normal_users()
    create_redeem_items()