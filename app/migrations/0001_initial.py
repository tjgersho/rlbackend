# Generated by Django 4.1.3 on 2022-11-04 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('X', models.FloatField()),
                ('Y', models.FloatField()),
                ('Z', models.FloatField()),
                ('created', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Rocket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mission', models.CharField(max_length=1000)),
                ('launch_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Velocity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Vx', models.FloatField()),
                ('Vy', models.FloatField()),
                ('Vz', models.FloatField()),
                ('created', models.FloatField()),
                ('position', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='velocity', to='app.position')),
            ],
        ),
        migrations.AddField(
            model_name='position',
            name='rocket',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='position', to='app.rocket'),
        ),
        migrations.CreateModel(
            name='Acceleration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ax', models.FloatField()),
                ('Ay', models.FloatField()),
                ('Az', models.FloatField()),
                ('created', models.FloatField()),
                ('position', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='acceleration', to='app.position')),
            ],
        ),
    ]
