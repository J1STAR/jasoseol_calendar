from mongoengine import EmbeddedDocument, Document, DynamicDocument, fields


# Create your models here.
class Todo(DynamicDocument):
    date = fields.DateField()
    event = fields.StringField()