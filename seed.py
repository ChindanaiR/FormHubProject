import django
import os

# Django settings module environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FormHub.settings")
django.setup()

from authentication.models import *
from userprofile.models import *
from authentication.models import *
from form_management.models import *
from django.core.management import call_command

def flush_remaining_data():
    try:
        call_command("flush", "--no-input")
        print("[+] Database flushed successfully.")
    except Exception as e:
        print("[!] Error flushing the database:", str(e))


def create_point_range():
    if not Point.objects.all().exists():
        try:
            Point.objects.create(
                form_size = "S",
                context = "SEL",
                point = 10,
                description = "Buying small form",
                lower_bound = 1,
                upper_bound = 3,
            )
            Point.objects.create(
                form_size = "S",
                context = "ANS",
                point = 10,
                description = "Answering small form",
                lower_bound = 1,
                upper_bound = 3,
            )
            Point.objects.create(
                form_size = "M",
                context = "SEL",
                point = 20,
                description = "Buying medium form",
                lower_bound = 4,
                upper_bound = 7,
            )
            Point.objects.create(
                form_size = "M",
                context = "ANS",
                point = 20,
                description = "Answering medium form",
                lower_bound = 4,
                upper_bound = 7,
            )
            Point.objects.create(
                form_size = "L",
                context = "SEL",
                point = 30,
                description = "Buying large form",
                lower_bound = 8,
                upper_bound = 999,
            )
            Point.objects.create(
                form_size = "L",
                context = "ANS",
                point = 30,
                description = "Answering large form",
                lower_bound = 8,
                upper_bound = 999,
            )
            print("[+] Point table has been created.")
        except Exception as e:
            print("[!] Something went wrong with Point script.", str(e))
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
        except Exception as e:
            print("[!] Something went wrong with creating superuser script.", str(e))
    else:
        print("[!] Creating superuser script is already run.")

def create_normal_users():
    if not User.objects.filter(is_superuser = False).exists():
        try:
            User.objects.create_user(
                first_name = "John",
                last_name = "Doe",
                username = "john",
                email = "john@mail.com",
                student_id = "6441111126",
                password = "123",
            )
            User.objects.create_user(
                first_name = "Jimmy",
                last_name = "Doe",
                username = "jimmy",
                email = "jimmy@mail.com",
                student_id = "6442222226",
                password = "123",
            )
            User.objects.create_user(
                first_name = "Jane",
                last_name = "Doe",
                username = "jane",
                email = "jane@mail.com",
                student_id = "6443333326",
                password = "123",
            )
            print("[+] Normal user has been created.")
        except Exception as e:
            print("[!] Something went wrong with creating normal user script.", str(e))
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
        except Exception as e:
            print("[!] Something went wrong with creating redeem item script.", str(e))
    else:
        print("[!] Creating ReedeemItem script is already run.")

def create_forms():
    if not Form.objects.all().exists():
        try:
            Form.objects.create(
                form_name = "Future career",
                description = "This form is designed to gather information about your future career aspirations and background.",
                design = [
                    {
                        "section": 1,
                        "type": "radio",
                        "question": "What industry are you most interested in pursuing a career in?",
                        "options": ["Technology", "Healthcare", "Finance", "Education", "Hospitality", "Other"]
                    },
                    {
                        "section": 2,
                        "type": "long",
                        "question": "Describe your key skills and strengths that you believe are relevant to your future career."
                    },
                    {
                        "section": 3,
                        "type": "short",
                        "question": "What is your highest level of education completed?"
                    },
                    {
                        "section": 4,
                        "type": "long",
                        "question": "What are your short-term and long-term career goals?"
                    },
                    {
                        "section": 5,
                        "type": "long",
                        "question": "Please describe your relevant work experience, if any."
                    },
                    {
                        "section": 6,
                        "type": "checkbox",
                        "question": "What type of work environment do you prefer?",
                        "options": ["Remote", "Office", "Team-based", "Independent", "Flexible Hours"]
                    }
                ],
                owner = User.objects.get(pk = 2),
                form_point = Point.objects.get(context = "ANS", form_size = "M"),
                is_open = True,
            )
            Form.objects.create(
                form_name = "Reading behavior",
                description = "This form aims to understand your reading habits and preferences. Please answer the following questions.",
                design = [
                    {
                        "section": 1,
                        "type": "checkbox",
                        "question": "Which genres of books do you enjoy reading?",
                        "options": ["Fiction", "Non-fiction", "Mystery/Thriller", "Science Fiction/Fantasy", "Biography/Memoir", "Other"]
                    },
                    {
                        "section": 2,
                        "type": "short",
                        "question": "How often do you typically read in a week?"
                    },
                    {
                        "section": 3,
                        "type": "long",
                        "question": "Describe your favorite reading environment or routine."
                    },
                    {
                        "section": 4,
                        "type": "radio",
                        "question": "What motivates you to pick up a new book?",
                        "options": ["Recommendations from friends or family", "Bestseller lists", "Interest in the author", "Subject matter or topic", "Cover design", "Other"]
                    },
                    {
                        "section": 5,
                        "type": "long",
                        "question": "Share a memorable reading experience or book that has had a significant impact on you, and explain why."
                    }
                ],
                owner = User.objects.get(pk = 2),
                form_point = Point.objects.get(context = "ANS", form_size = "M"),
                is_open = True,
            )
            Form.objects.create(
                form_name = "Eating Behavior - CP Bolona Products",
                description = "Please provide information about your eating behavior related to CP Bolona products.",
                design = [
                    {
                        "section": 1,
                        "type": "radio",
                        "question": "How often do you consume CP Bolona products?",
                        "options": [
                            "Daily",
                            "Weekly",
                            "Monthly",
                            "Rarely",
                            "Never"
                        ]
                    },
                    {
                        "section": 2,
                        "type": "dropdown",
                        "question": "Which CP Bolona product do you consume most frequently?",
                        "options": [
                            "CP Bolona Sausage",
                            "CP Bolona Ham",
                            "CP Bolona Chicken"
                        ]
                    },
                    {
                        "section": 3,
                        "type": "checkbox",
                        "question": "What are your reasons for consuming CP Bolona products? (Select all that apply)",
                        "options": [
                            "Convenience",
                            "Taste",
                            "Price",
                            "Nutritional Value",
                            "Brand Preference"
                        ]
                    },
                    {
                        "section": 4,
                        "type": "short",
                        "question": "How would you describe your overall satisfaction with CP Bolona products?"
                    },
                    {
                        "section": 5,
                        "type": "long",
                        "question": "Please share any additional comments or feedback about CP Bolona products."
                    },
                    {
                        "section": 6,
                        "type": "date",
                        "question": "When did you first try CP Bolona products?"
                    },
                    {
                        "section": 7,
                        "type": "radio",
                        "question": "Would you recommend CP Bolona products to others?",
                        "options": [
                            "Definitely yes",
                            "Probably yes",
                            "Not sure",
                            "Probably not",
                            "Definitely not"
                        ]
                    },
                    {
                        "section": 8,
                        "type": "checkbox",
                        "question": "Which other processed meat products do you consume?",
                        "options": [
                            "Sausages",
                            "Ham",
                            "Bacon",
                            "Hotdogs"
                        ]
                    },
                    {
                        "section": 9,
                        "type": "dropdown",
                        "question": "Where do you usually purchase CP Bolona products?",
                        "options": [
                            "Supermarket",
                            "Convenience Store",
                            "Online",
                            "Specialty Store",
                            "Others"
                        ]
                    },
                    {
                        "section": 10,
                        "type": "short",
                        "question": "What improvements would you like to see in CP Bolona products?"
                    }
                ],
                owner = User.objects.get(pk = 3),
                form_point = Point.objects.get(context = "ANS", form_size = "L"),
                is_open = True,
            )
            Form.objects.create(
                form_name = "The point of view toward the e-learning trends",
                description = "This survey aims to gather valuable insights into your perspective on current e-learning trends. Your input will help us understand your habits, preferences, and expectations regarding e-learning activities and platforms. Please take a moment to share your thoughts and experiences to contribute to the ongoing evolution of online learning.",
                design = [
                    {
                        "section": 1,
                        "type": "radio",
                        "question": "How often do you participate in e-learning activities?",
                        "options": [
                            "Daily",
                            "Weekly",
                            "Monthly",
                            "Rarely",
                            "Never"
                        ]
                    },
                    {
                        "section": 2,
                        "type": "short",
                        "question": "What are the primary reasons for your participation in e-learning?"
                    },
                    {
                        "section": 3,
                        "type": "long",
                        "question": "Please describe your experience with e-learning platforms."
                    },
                    {
                        "section": 4,
                        "type": "checkbox",
                        "question": "Which e-learning formats do you prefer? (Select all that apply)",
                        "options": [
                            "Video lectures",
                            "Interactive modules",
                            "Live webinars",
                            "Text-based materials",
                            "Quizzes/Assessments"
                        ]
                    },
                    {
                        "section": 5,
                        "type": "dropdown",
                        "question": "What is your preferred device for accessing e-learning content?",
                        "options": [
                            "Desktop/Laptop",
                            "Smartphone",
                            "Tablet",
                            "Others"
                        ]
                    },
                    {
                        "section": 6,
                        "type": "short",
                        "question": "How would you rate the effectiveness of e-learning compared to traditional classroom learning?"
                    },
                    {
                        "section": 7,
                        "type": "radio",
                        "question": "Do you believe that e-learning will continue to grow in popularity in the future?",
                        "options": [
                            "Strongly agree",
                            "Agree",
                            "Neutral",
                            "Disagree",
                            "Strongly disagree"
                        ]
                    },
                    {
                        "section": 8,
                        "type": "long",
                        "question": "What improvements would you suggest for e-learning platforms or content?"
                    },
                    {
                        "section": 9,
                        "type": "short",
                        "question": "What are your expectations for future e-learning trends?"
                    }
                ],
                owner = User.objects.get(pk = 3),
                form_point = Point.objects.get(context = "ANS", form_size = "L"),
                is_open = True,
            )
            Form.objects.create(
                form_name = "Feedback from using FormHub",
                description = "We value your feedback on your experience with this platform. Your input helps us improve and enhance our services to better meet your needs. Please take a moment to share your thoughts with us.",
                design = [
                    {
                        "section": 1,
                        "type": "radio",
                        "question": "How satisfied are you with the user interface of this platform?",
                        "options": [
                            "Very satisfied",
                            "Satisfied",
                            "Neutral",
                            "Dissatisfied",
                            "Very dissatisfied"
                        ]
                    },
                    {
                        "section": 2,
                        "type": "short",
                        "question": "What features do you find most useful on this platform?"
                    },
                    {
                        "section": 3,
                        "type": "long",
                        "question": "Please share any suggestions or improvements you have for this platform."
                    },
                    {
                        "section": 4,
                        "type": "radio",
                        "question": "How likely are you to recommend this platform to others?",
                        "options": [
                            "Very likely",
                            "Likely",
                            "Neutral",
                            "Unlikely",
                            "Very unlikely"
                        ]
                    },
                    {
                        "section": 5,
                        "type": "short",
                        "question": "Is there anything else you would like to tell us about your experience with this platform?"
                    }
                ],
                owner = User.objects.get(pk = 1),
                form_point = Point.objects.get(context = "ANS", form_size = "M"),
                is_open = True,
            )
            print("[+] Forms has been created.")
        except Exception as e:
            print("[!] Something went wrong with creating forms script.", str(e))
    else:
        print("[!] Creating forms script is already run.")


if __name__ == "__main__":
    print("[*] Initializing the database\n")
    flush_remaining_data()
    create_point_range()
    create_superuser()
    create_normal_users()
    create_redeem_items()
    create_forms()