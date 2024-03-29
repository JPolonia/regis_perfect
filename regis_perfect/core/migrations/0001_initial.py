# Generated by Django 2.2.10 on 2020-02-20 23:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bangs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50, verbose_name='Valor')),
            ],
            options={
                'verbose_name': 'Franja',
                'verbose_name_plural': 'Tipos de franja',
            },
        ),
        migrations.CreateModel(
            name='BangsSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50, verbose_name='Valor')),
            ],
            options={
                'verbose_name': 'Tamanho da franja',
                'verbose_name_plural': 'Tamanhos da franja',
            },
        ),
        migrations.CreateModel(
            name='Beard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50, verbose_name='Valor')),
            ],
            options={
                'verbose_name': 'Barba',
                'verbose_name_plural': 'Tipos de barba',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('sex', models.CharField(choices=[('m', 'Masculino'), ('f', 'Feminino')], max_length=1, verbose_name='Sexo')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Data de nascimento')),
                ('email', models.CharField(blank=True, max_length=30, null=True, verbose_name='Email')),
                ('referral', models.CharField(blank=True, max_length=200, null=True, verbose_name='Como nos conheceu')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Coloring',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50, verbose_name='Valor')),
            ],
            options={
                'verbose_name': 'Coloração',
                'verbose_name_plural': 'Tipos de coloração',
            },
        ),
        migrations.CreateModel(
            name='CutType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50, verbose_name='Valor')),
            ],
            options={
                'verbose_name': 'Tipo de corte',
                'verbose_name_plural': 'Tipos de corte',
            },
        ),
        migrations.CreateModel(
            name='HaircutSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50, verbose_name='Valor')),
            ],
            options={
                'verbose_name': 'Tamanho de corte',
                'verbose_name_plural': 'Tamanhos de corte',
            },
        ),
        migrations.CreateModel(
            name='HaircutType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50, verbose_name='Valor')),
            ],
            options={
                'verbose_name': 'Tipo de corte',
                'verbose_name_plural': 'Tipos de corte',
            },
        ),
        migrations.CreateModel(
            name='HairStyle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50, verbose_name='Valor')),
            ],
            options={
                'verbose_name': 'Penteado',
                'verbose_name_plural': 'Tipos de penteado',
            },
        ),
        migrations.CreateModel(
            name='Laterals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50, verbose_name='Valor')),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.CutType', verbose_name='Tipo')),
            ],
            options={
                'verbose_name': 'Laterais',
                'verbose_name_plural': 'Tipos de Laterais',
            },
        ),
        migrations.CreateModel(
            name='Locks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50, verbose_name='Valor')),
            ],
            options={
                'verbose_name': 'Madeixas',
                'verbose_name_plural': 'Tipos de madeixa',
            },
        ),
        migrations.CreateModel(
            name='Straightening',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50, verbose_name='Valor')),
            ],
            options={
                'verbose_name': 'Alisamento',
                'verbose_name_plural': 'Tipos de alisamento',
            },
        ),
        migrations.CreateModel(
            name='TopTechnique',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50, verbose_name='Valor')),
            ],
            options={
                'verbose_name': 'Topo técnica',
                'verbose_name_plural': 'Técnicas de topo',
            },
        ),
        migrations.CreateModel(
            name='Top',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50, verbose_name='Valor')),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.CutType', verbose_name='Tipo')),
            ],
            options={
                'verbose_name': 'Laterais',
                'verbose_name_plural': 'Tipos de laterais',
            },
        ),
        migrations.CreateModel(
            name='MaleHaircut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data')),
                ('price', models.IntegerField(verbose_name='Valor do serviço')),
                ('record', models.TextField(blank=True, null=True, verbose_name='Registo')),
                ('beard', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.Beard', verbose_name='Barba')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Client', verbose_name='Cliente')),
                ('coloring', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.Coloring', verbose_name='Coloração')),
                ('hairstyle', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.HairStyle', verbose_name='Penteado')),
                ('laterals', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.Laterals', verbose_name='Laterais')),
                ('locks', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.Locks', verbose_name='Madeixas')),
                ('professional', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('straightening', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.Straightening', verbose_name='Alisamento')),
                ('top', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.Top', verbose_name='Topo')),
                ('top_technique', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.TopTechnique', verbose_name='Topo técnica')),
            ],
            options={
                'verbose_name': 'Corte Masculino',
                'verbose_name_plural': 'Corte Masculino',
            },
        ),
        migrations.CreateModel(
            name='FemaleHaircut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data')),
                ('price', models.IntegerField(verbose_name='Valor do serviço')),
                ('record', models.TextField(blank=True, null=True, verbose_name='Registo')),
                ('bangs', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.Bangs', verbose_name='Franja')),
                ('bangs_size', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.BangsSize', verbose_name='Tamanho da franja')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Client', verbose_name='Cliente')),
                ('haircut_size', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.HaircutSize', verbose_name='Tamanho do corte')),
                ('haircut_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.HaircutType', verbose_name='Tipo de corte')),
                ('professional', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Corte Feminino',
                'verbose_name_plural': 'Corte Feminino',
            },
        ),
    ]
