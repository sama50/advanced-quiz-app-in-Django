# Generated by Django 4.2.4 on 2023-10-30 14:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='TypeQuiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('number_of_queation', models.IntegerField(default=0)),
                ('quiz_id', models.UUIDField(default=uuid.UUID('2cb5407b-1814-48e1-9489-39d02baf6238'))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QuizQuestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('typequiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.typequiz')),
            ],
        ),
        migrations.CreateModel(
            name='OptionsOfQuiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=256)),
                ('quiz_questions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.quizquestions')),
            ],
        ),
        migrations.CreateModel(
            name='CandidatesAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=256)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.candidates')),
                ('queation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.quizquestions')),
                ('quiz_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.typequiz')),
            ],
        ),
        migrations.AddField(
            model_name='candidates',
            name='quiz_type',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.typequiz'),
        ),
    ]
