# myapp/management/commands/add_dummy_data.py

from django.core.management.base import BaseCommand
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Populate the database with dummy data'

    def handle(self, *args, **kwargs):
        from myapp.models import (
            District, TestLocation, OrderingPhysicianNPI, Submitter, Gender, City, 
            State, Race, Ethnicity, Environment, Patient, Order, SpecimenType, 
            SpecimenTypeSNOMEDCode, SourceDescription, SpecimenSource, SourceSNOMEDCode, Specimen
        )

        fake = Faker()

        def add_districts():
            districts = []
            for _ in range(10):
                district = District.objects.create(name=fake.city())
                districts.append(district)
            return districts

        def add_test_locations(districts):
            test_locations = []
            for district in districts:
                for _ in range(5):
                    test_location = TestLocation.objects.create(
                        location_name=fake.company(),
                        district=district
                    )
                    test_locations.append(test_location)
            return test_locations

        def add_ordering_physicians(test_locations):
            physicians = []
            for location in test_locations:
                for _ in range(3):
                    physician = OrderingPhysicianNPI.objects.create(
                        npi_code=fake.unique.bothify(text='????-########'),
                        test_location=location
                    )
                    physicians.append(physician)
            return physicians

        def add_submitters(districts, test_locations, physicians):
            for _ in range(50):
                Submitter.objects.create(
                    submitter_code=fake.unique.bothify(text='SUB-######'),
                    district=random.choice(districts),
                    test_location=random.choice(test_locations),
                    ordering_physician_npi=random.choice(physicians),
                    collection_date=fake.date_this_year(),
                    collection_time=fake.time()
                )

        def add_orders():
            orders = []
            for _ in range(10):
                order = Order.objects.create(
                    order_code=fake.unique.bothify(text='ORD-######'),
                    order_name=fake.sentence(),
                    order_loinc_code=fake.unique.bothify(text='LOINC-######'),
                    loinc_name=fake.sentence(),
                    order_loinc_description=fake.paragraph()
                )
                orders.append(order)
            return orders

        def add_specimen_types(orders):
            specimen_types = []
            for order in orders:
                for _ in range(3):
                    specimen_type = SpecimenType.objects.create(
                        order=order,
                        specimen_type=fake.word()
                    )
                    specimen_types.append(specimen_type)
            return specimen_types

        def add_snomed_codes(specimen_types):
            snomed_codes = []
            for specimen_type in specimen_types:
                for _ in range(2):
                    snomed_code = SpecimenTypeSNOMEDCode.objects.create(
                        specimen_type=specimen_type,
                        specimen_type_snomed_code=fake.unique.bothify(text='SNOMED-######')
                    )
                    snomed_codes.append(snomed_code)
            return snomed_codes

        def add_source_descriptions(snomed_codes):
            descriptions = []
            for code in snomed_codes:
                description = SourceDescription.objects.create(
                    specimen_type_snomed_code=code,
                    source_description=fake.text()
                )
                descriptions.append(description)
            return descriptions

        def add_specimen_sources(descriptions):
            sources = []
            for description in descriptions:
                source = SpecimenSource.objects.create(
                    source_description=description,
                    specimen_source=fake.word()
                )
                sources.append(source)
            return sources

        def add_source_snomed_codes(sources):
            snomed_codes = []
            for source in sources:
                snomed_code = SourceSNOMEDCode.objects.create(
                    specimen_source=source,
                    source_snomed_code=fake.unique.bothify(text='SRC-SNOMED-######')
                )
                snomed_codes.append(snomed_code)
            return snomed_codes

        def add_patients():
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

        def add_specimens(orders, specimen_types, snomed_codes, descriptions, sources, source_snomed_codes):
            for _ in range(50):
                Specimen.objects.create(
                    order=random.choice(orders),
                    specimen_type=random.choice(specimen_types),
                    specimen_type_snomed_code=random.choice(snomed_codes),
                    source_description=random.choice(descriptions),
                    specimen_source=random.choice(sources),
                    source_snomed_code=random.choice(source_snomed_codes)
                )

        # Populate the database
        districts = add_districts()
        test_locations = add_test_locations(districts)
        physicians = add_ordering_physicians(test_locations)
        add_submitters(districts, test_locations, physicians)

        orders = add_orders()
        specimen_types = add_specimen_types(orders)
        snomed_codes = add_snomed_codes(specimen_types)
        descriptions = add_source_descriptions(snomed_codes)
        sources = add_specimen_sources(descriptions)
        source_snomed_codes = add_source_snomed_codes(sources)

        add_patients()
        add_specimens(orders, specimen_types, snomed_codes, descriptions, sources, source_snomed_codes)

        self.stdout.write(self.style.SUCCESS('Dummy data added successfully!'))
