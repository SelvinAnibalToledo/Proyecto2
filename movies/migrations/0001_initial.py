# Generated by Django 4.1.10 on 2023-10-04 03:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Studio",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="Movie",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("release_date", models.DateField()),
                ("country", models.CharField(max_length=60)),
                ("description", models.TextField()),
                (
                    "genre",
                    models.CharField(
                        choices=[
                            ("Adventure", "Adventure"),
                            ("Drama", "Drama"),
                            ("Sci-Fi", "Sci-Fi"),
                            ("Comedy", "Comedy"),
                            ("Action", "Action"),
                            ("Fantasy", "Fantasy"),
                            ("Horror", "Horror"),
                        ],
                        max_length=18,
                    ),
                ),
                (
                    "studio",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="movies.studio",
                    ),
                ),
            ],
        ),
    ]
