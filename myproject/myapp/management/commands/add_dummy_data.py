from django.core.management.base import BaseCommand
from myapp.models import Order, Specimen, Submitter, Patient
from datetime import date, time
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Add dummy data to the database'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Create dummy data for Order
        orders = []
        for _ in range(5):
            order = Order.objects.create(
                order_code=fake.unique.bothify(text='ORD###'),
                order_name=fake.catch_phrase(),
                order_loinc_code=fake.bothify(text='LOINC#####'),
                loinc_name=fake.word(),
                order_loinc_description=fake.text(max_nb_chars=100)
            )
            orders.append(order)

        # Create dummy data for Specimen
        specimen_types = ['Blood', 'Urine', 'Saliva', 'Tissue', 'Sputum']
        for order in orders:
            for _ in range(5):
                Specimen.objects.create(
                    order=order,
                    specimen_id=fake.unique.bothify(text='SPC###'),
                    specimen_type=random.choice(specimen_types),
                    specimen_type_snomed_code=fake.bothify(text='SNOMED###'),
                    source_description=fake.sentence(),
                    specimen_source=fake.word(),
                    source_snomed_code=fake.bothify(text='SNOMED###')
                )

        # Create dummy data for Submitter
        for _ in range(5):
            Submitter.objects.create(
                submitter_code=fake.unique.bothify(text='SUB###'),
                district=fake.city(),
                orderingphysiciannpi=fake.bothify(text='NPI######'),
                collectiondate=fake.date_between(start_date='-2y', end_date='today'),
                collectiontime=fake.time(),
                testlocation=fake.company()
            )

        # Create dummy data for Patient
        for _ in range(5):
            Patient.objects.create(
                patient_first_name=fake.first_name(),
                patient_middle_name=fake.first_name() if random.choice([True, False]) else None,
                patient_last_name=fake.last_name(),
                patient_gender=random.choice(['Male', 'Female', 'Other']),
                dob=fake.date_of_birth(minimum_age=18, maximum_age=90),
                address_line1=fake.street_address(),
                address_line2=fake.secondary_address() if random.choice([True, False]) else None,
                city=fake.city(),
                state=fake.state_abbr(),
                zip=fake.zipcode(),
                email=fake.email(),
                phone_number=fake.phone_number(),
                race=fake.random_element(elements=('Caucasian', 'African American', 'Asian', 'Hispanic', 'Other')),
                ethnicity=fake.random_element(elements=('Hispanic', 'Non-Hispanic')),
                entry_number=fake.unique.bothify(text='E###'),
                env=fake.word(),
                extract_flag=random.choice([True, False])
            )

        self.stdout.write(self.style.SUCCESS('Successfully added dummy data'))
