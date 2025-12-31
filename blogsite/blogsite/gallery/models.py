from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    #automatically sets the field to the current date and time only when the model instance is first created
    created_at = models.DateTimeField(auto_now_add=True)
    #automatically sets the field's value to the current date and time every time the model instance's save() method is called
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def edit(self, name, description, image):
        self.name = name
        self.description = description
        self.image = image
        self.save()


    def short_description(self):
        # Split the description into words
        words = self.description.split()
        if len(words) > 50:
            # Join the first 50 words and add "..." at the end
            return ' '.join(words[:30]) + '...'
        else:
            # If the description is already less than 50 words, return it as is
            return self.description