from django.core.management.base import BaseCommand
from reviews.models import Publisher, Book, Contributor, BookContributor, Review
from django.contrib.auth.models import User
import random
from datetime import date, timedelta


class Command(BaseCommand):
    help = 'Generates dummy data for the reviews app'

    def handle(self, *args, **kwargs):
        # Create a dummy publisher
        publisher = Publisher.objects.create(
            name="Dummy Publishing House",
            website="https://www.dummypublisher.com",
            email="contact@dummypublisher.com"
        )

        # Create dummy contributors
        contributors = [
            Contributor.objects.create(
                first_names=f"First{i}",
                last_names=f"Last{i}",
                email=f"contributor{i}@example.com"
            ) for i in range(1, 6)
        ]

        # Create a dummy user for reviews
        user = User.objects.create_user(
            'dummyuser', 'dummyuser@example.com', 'password123')

        # Book titles
        book_titles = [
            "The Hidden Galaxy", "Whispers of the Wind", "Coding Dreams",
            "The Last Algorithm", "Quantum Leap", "Digital Horizons",
            "The Silicon Saga", "Bytes of Life", "Neural Networks and You",
            "The Blockchain Revolution"
        ]

        # Generate 10 books and 10 reviews for each book
        for i in range(10):
            # Create book
            book = Book.objects.create(
                title=book_titles[i],
                publication_date=date.today() - timedelta(days=random.randint(0, 1000)),
                isbn=f"978-0-{random.randint(10000000,
                                             99999999)}-{random.randint(0, 9)}",
                publisher=publisher
            )

            # Add contributors
            for contributor in random.sample(contributors, 2):
                BookContributor.objects.create(
                    book=book,
                    contributor=contributor,
                    role=random.choice(
                        BookContributor.ContributionRole.choices)[0]
                )

            # Create 10 reviews for each book
            for j in range(10):
                Review.objects.create(
                    content=f"This is a dummy review {
                        j+1} for the book '{book.title}'.",
                    rating=random.randint(1, 5),
                    creator=user,
                    book=book,
                    date_edited=date.today() if random.choice(
                        [True, False]) else None
                )

        self.stdout.write(self.style.SUCCESS(
            'Dummy data generation complete.'))
