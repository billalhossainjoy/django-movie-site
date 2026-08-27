#!/usr/bin/env bash

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

cd "$PROJECT_ROOT"

python manage.py shell <<'PY'

import random

from django.contrib.auth import get_user_model

from movies.models import Movie, Genre


User = get_user_model()


# --------------------------------
# Get a user for created_by
# --------------------------------

user = (
    User.objects
    .filter(is_superuser=True)
    .first()
)

if user is None:
    user = User.objects.first()

if user is None:
    raise Exception(
        "No user exists. Create a user first."
    )


# --------------------------------
# Genres
# --------------------------------

genre_names = [
    "Action",
    "Adventure",
    "Comedy",
    "Drama",
    "Horror",
    "Sci-Fi",
    "Thriller",
    "Romance",
    "Fantasy",
    "Mystery",
]


genres = []

for name in genre_names:
    genre, _ = Genre.objects.get_or_create(
        name=name
    )

    genres.append(genre)


# --------------------------------
# Random data
# --------------------------------

adjectives = [
    "Dark",
    "Silent",
    "Last",
    "Lost",
    "Infinite",
    "Hidden",
    "Final",
    "Broken",
    "Golden",
    "Secret",
    "Midnight",
    "Burning",
]

nouns = [
    "World",
    "Empire",
    "Journey",
    "Planet",
    "Shadow",
    "Dream",
    "Storm",
    "Kingdom",
    "Mission",
    "Legacy",
    "Signal",
    "Memory",
]

directors = [
    "Christopher Nolan",
    "Denis Villeneuve",
    "James Cameron",
    "Steven Spielberg",
    "Ridley Scott",
    "David Fincher",
    "Martin Scorsese",
    "Greta Gerwig",
    "Jordan Peele",
    "Quentin Tarantino",
]


# --------------------------------
# Create movies
# --------------------------------

for i in range(1, 101):

    title = (
        f"{random.choice(adjectives)} "
        f"{random.choice(nouns)} {i}"
    )

    movie = Movie.objects.create(
        title=title,

        description=(
            f"{title} is a generated movie used "
            f"for testing the MovieSite application."
        ),

        release_year=random.randint(
            1980,
            2026,
        ),

        director=random.choice(
            directors
        ),

        created_by=user,
    )


    # Give each movie 1-3 genres

    movie.genres.set(
        random.sample(
            genres,
            random.randint(1, 3),
        )
    )


print("Successfully created 100 movies.")

PY