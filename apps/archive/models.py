from django import forms
from django.forms import ModelForm
from django.db import models

# Create your models here.
# Which I did. At least I tried to...

COLUMN_CHOICES = (
    (0, 'Number'),
    (1, 'Name'),
    (2, 'Text'),
    (3, 'Image'),
    (4, 'File'),
    (5, 'Location'),
)


class Table(models.Model):  # a unit of an archive
    title = models.CharField(
        max_length=55,
    )
    description = models.TextField()
    last_modified = models.DateTimeField(
        auto_now=True,
    )
    column_num = models.IntegerField(
        default=1,
    )
    item_num = models.IntegerField(
        default=1,
    )

    def __str__(self):
        return self.title


class TableForm(ModelForm):
    class Meta:
        model = Table
        fields = [
            'title',
            'description',
        ]


class Column(models.Model):
    serial_no = models.IntegerField(
        default=1,
    )
    column_name = models.CharField(
        max_length=50,
    )
    column_type = models.IntegerField(
        max_length=10,
        choices=COLUMN_CHOICES
    )
    table = models.ForeignKey(
        Table,
        related_name="Columns",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )


class ColumnForm(ModelForm):
    class Meta:
        model = Column
        fields = [
            'column_name',
            'column_type',
        ]


class Item(models.Model): # a row of a table
    serial_no = models.IntegerField(
        default=1
    )
    table = models.ForeignKey(
        Table,
        related_name="Item",
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )


class ColumnNumber(Column):  # column type 0 : numbering (notice : diff with order of each entry)
    content = models.IntegerField()
    item = models.ForeignKey(
        Item,
        related_name="ColumnNumber",
        null=False,
        blank=False,
        on_delete = models.CASCADE
    )

    def __str__(self):
        return self.name


class ColumnName(Column):    # column type 1 : a simple name
    item = models.ForeignKey(
        Item,
        related_name="ColumnName",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name


class ColumnText(Column):    # column type 2 : text without character restriction
    content = models.TextField()
    item = models.ForeignKey(
        Item,
        related_name="ColumnText",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name


class ColumnImage(Column):   # column type 3 : image
    # for future notice : implement a method to generate separate directory as string ex. usr/table/column
    content = models.ImageField(
        upload_to = 'uploaded/',
    )
    item = models.ForeignKey(
        Item,
        related_name="ColumnImage",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name


class ColumnFile(Column): # column type 4 : file upload
    # for future notice : implement a method to generate separate directory as string ex. usr/table/column
    content = models.FileField(
        upload_to = 'uploaded/',
    )
    item = models.ForeignKey(
        Item,
        related_name="ColumnFile",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name


class ColumnLocation(Column): # column type 5 : location using google maps api
    search_str = models.TextField()
    location_str = models.TextField()
    item = models.ForeignKey(
        Item,
        related_name="ColumnLocation",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
