from django.core.management.base import BaseCommand
from myapp.models import Order, Specimen, Submitter, Patient, SpecimenType, SpecimenTypeSNOMEDCode, SourceDescription, SpecimenSource, SourceSNOMEDCode
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Add dummy data to the database'

    def add_arguments(self, parser):
        parser.add_argument(
            '--reset',
            action='store_true',
            help='Delete all existing data before generating new dummy data',
        )

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Check if the reset flag was provided
        if kwargs['reset']:
            self.stdout.write('Resetting database... Deleting all existing records.')
            Order.objects.all().delete()
            Specimen.objects.all().delete()
            Submitter.objects.all().delete()
            Patient.objects.all().delete()
            SpecimenType.objects.all().delete()
            SpecimenTypeSNOMEDCode.objects.all().delete()
            SourceDescription.objects.all().delete()
            SpecimenSource.objects.all().delete()
            SourceSNOMEDCode.objects.all().delete()

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

        # Create dummy data for SpecimenType
        specimen_types = {}
        specimen_type_names = ['Blood', 'Urine', 'Saliva', 'Tissue', 'Sputum']
        for name in specimen_type_names:
            specimen_type = SpecimenType.objects.create(
                order=random.choice(orders),  # Assigning a random order to the SpecimenType
                specimen_type=name
            )
            specimen_types[name] = specimen_type

        # Create dummy data for SpecimenTypeSNOMEDCode
        for specimen_type in specimen_types.values():
            for _ in range(3):  # Create 3 SNOMED codes for each SpecimenType
                SpecimenTypeSNOMEDCode.objects.create(
                    specimen_type=specimen_type,
                    specimen_type_snomed_code=fake.bothify(text='SNOMED###')
                )

        # Create dummy data for SourceDescription
        for snomed_code in SpecimenTypeSNOMEDCode.objects.all():
            for _ in range(2):  # Create 2 Source Descriptions for each SNOMED code
                SourceDescription.objects.create(
                    specimen_type_snomed_code=snomed_code,
                    source_description=fake.sentence()
                )

        # Create dummy data for SpecimenSource
        for description in SourceDescription.objects.all():
            SpecimenSource.objects.create(
                source_description=description,
                specimen_source=fake.word()
            )

        # Create dummy data for SourceSNOMEDCode
        for specimen_source in SpecimenSource.objects.all():
            SourceSNOMEDCode.objects.create(
                specimen_source=specimen_source,
                source_snomed_code=fake.bothify(text='SNOMED###')
            )

        # Create dummy data for Specimen
        for order in orders:
            for _ in range(5):
                specimen_type = random.choice(list(specimen_types.values()))
                specimen_type_snomed_code = random.choice(specimen_type.snomed_codes.all())
                source_description = random.choice(specimen_type_snomed_code.source_descriptions.all())
                specimen_source = source_description.specimen_sources.first()
                source_snomed_code = specimen_source.snomed_codes.first()

                Specimen.objects.create(
                    order=order,
                    specimen_type=specimen_type,
                    specimen_type_snomed_code=specimen_type_snomed_code,
                    source_description=source_description,
                    specimen_source=specimen_source,
                    source_snomed_code=source_snomed_code
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
