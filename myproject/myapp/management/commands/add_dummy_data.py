from django.core.management.base import BaseCommand
from faker import Faker
from myapp.models import (
    Order, SpecimenType, SpecimenTypeSNOMEDCode, SourceDescription,
    SpecimenSource, SourceSNOMEDCode, Specimen, District, TestLocation,
    OrderingPhysicianNPI, CollectionDate, CollectionTime, Submitter,
    Gender, City, State, Race, Ethnicity, Environment, Patient
)
import random

class Command(BaseCommand):
    help = 'Generate dummy data for the database'

    def handle(self, *args, **kwargs):
        fake = Faker()

        def add_orders():
            unique_order_codes = [fake.unique.word() for _ in range(10)]
            self.stdout.write(self.style.SUCCESS('Generating Orders...'))
            for code in unique_order_codes:
                Order.objects.create(
                    order_code=code,
                    order_name=fake.word(),
                    order_loinc_code=fake.word(),
                    loinc_name=fake.word(),
                    order_loinc_description=fake.text()
                )

        def add_specimen_types():
            unique_specimen_type_codes = [fake.unique.word() for _ in range(10)]
            self.stdout.write(self.style.SUCCESS('Generating Specimen Types...'))
            orders = Order.objects.all()
            for order in orders:
                for code in unique_specimen_type_codes:
                    SpecimenType.objects.create(
                        order=order,
                        specimen_type=code
                    )

        def add_specimen_type_snomed_codes():
            unique_snomed_codes = [fake.unique.word() for _ in range(10)]
            self.stdout.write(self.style.SUCCESS('Generating Specimen Type SNOMED Codes...'))
            specimen_types = SpecimenType.objects.all()
            for specimen_type in specimen_types:
                for code in unique_snomed_codes:
                    SpecimenTypeSNOMEDCode.objects.create(
                        specimen_type=specimen_type,
                        specimen_type_snomed_code=code
                    )

        def add_source_descriptions():
            self.stdout.write(self.style.SUCCESS('Generating Source Descriptions...'))
            snomed_codes = SpecimenTypeSNOMEDCode.objects.all()
            for snomed_code in snomed_codes:
                for _ in range(2):
                    SourceDescription.objects.create(
                        specimen_type_snomed_code=snomed_code,
                        source_description=fake.text()
                    )

        def add_specimen_sources():
            self.stdout.write(self.style.SUCCESS('Generating Specimen Sources...'))
            source_descriptions = SourceDescription.objects.all()
            for source_description in source_descriptions:
                for _ in range(2):
                    SpecimenSource.objects.create(
                        source_description=source_description,
                        specimen_source=fake.word()
                    )

        def add_source_snomed_codes():
            self.stdout.write(self.style.SUCCESS('Generating Source SNOMED Codes...'))
            unique_snomed_codes = [fake.unique.word() for _ in range(10)]
            specimen_sources = SpecimenSource.objects.all()
            for specimen_source in specimen_sources:
                for code in unique_snomed_codes:
                    SourceSNOMEDCode.objects.create(
                        specimen_source=specimen_source,
                        source_snomed_code=code
                    )

        def add_specimens():
            self.stdout.write(self.style.SUCCESS('Generating Specimens...'))
            for _ in range(10):
                Specimen.objects.create(
                    order=fake.random.choice(Order.objects.all()),
                    specimen_type=fake.random.choice(SpecimenType.objects.all()),
                    specimen_type_snomed_code=fake.random.choice(SpecimenTypeSNOMEDCode.objects.all()),
                    source_description=fake.random.choice(SourceDescription.objects.all()),
                    specimen_source=fake.random.choice(SpecimenSource.objects.all()),
                    source_snomed_code=fake.random.choice(SourceSNOMEDCode.objects.all())
                )

        def add_districts():
            self.stdout.write(self.style.SUCCESS('Generating Districts...'))
            for _ in range(5):
                District.objects.create(
                    name=fake.word()
                )

        def add_test_locations():
            self.stdout.write(self.style.SUCCESS('Generating Test Locations...'))
            districts = District.objects.all()
            for district in districts:
                for _ in range(2):
                    TestLocation.objects.create(
                        location_name=fake.word(),
                        district=district
                    )

        def add_ordering_physicians():
            self.stdout.write(self.style.SUCCESS('Generating Ordering Physicians...'))
            test_locations = TestLocation.objects.all()
            for test_location in test_locations:
                for _ in range(2):
                    OrderingPhysicianNPI.objects.create(
                        npi_code=fake.unique.numerify(text='NPI#####'),
                        test_location=test_location
                    )

        def add_collection_dates():
            self.stdout.write(self.style.SUCCESS('Generating Collection Dates...'))
            for _ in range(10):
                CollectionDate.objects.create(
                    date=fake.date()
                )

        def add_collection_times():
            self.stdout.write(self.style.SUCCESS('Generating Collection Times...'))
            for _ in range(10):
                CollectionTime.objects.create(
                    time=fake.time()
                )

        def add_submitters():
            self.stdout.write(self.style.SUCCESS('Generating Submitters...'))
            for _ in range(10):
                Submitter.objects.create(
                    submitter_code=fake.unique.word(),
                    district=fake.random.choice(District.objects.all()),
                    test_location=fake.random.choice(TestLocation.objects.all()),
                    ordering_physician_npi=fake.random.choice(OrderingPhysicianNPI.objects.all()),
                    collection_date=fake.date(),
                    collection_time=fake.time()
                )

        def add_patients():
            self.stdout.write(self.style.SUCCESS('Generating Patients...'))
            genders = [Gender.objects.create(name=g) for g in ["Male", "Female", "Other"]]
            cities = [City.objects.create(name=fake.city()) for _ in range(5)]
            states = [State.objects.create(name=fake.state()) for _ in range(5)]
            races = [Race.objects.create(name=fake.word()) for _ in range(5)]
            ethnicities = [Ethnicity.objects.create(name=fake.word()) for _ in range(5)]
            environments = [Environment.objects.create(name=fake.word()) for _ in range(5)]

            for _ in range(100):
                Patient.objects.create(
                    patient_first_name=fake.first_name(),
                    patient_middle_name=fake.first_name(),
                    patient_last_name=fake.last_name(),
                    patient_gender=random.choice(genders),
                    dob=fake.date_of_birth(minimum_age=0, maximum_age=90),
                    address_line1=fake.street_address(),
                    address_line2=fake.secondary_address(),
                    city=random.choice(cities),
                    state=random.choice(states),
                    zip=fake.zipcode(),
                    email=fake.email(),
                    phone_number=fake.phone_number(),
                    race=random.choice(races),
                    ethnicity=random.choice(ethnicities),
                    entry_number=fake.unique.bothify(text='ENTRY-######'),
                    env=random.choice(environments),
                    extract_flag=fake.boolean()
                )

        # Run all data generation functions
        add_orders()
        add_specimen_types()
        add_specimen_type_snomed_codes()
        add_source_descriptions()
        add_specimen_sources()
        add_source_snomed_codes()
        add_specimens()
        add_districts()
        add_test_locations()
        add_ordering_physicians()
        add_collection_dates()
        add_collection_times()
        add_submitters()
        add_patients()
