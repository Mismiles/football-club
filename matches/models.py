from django.contrib.auth.models import User
from django.db import models


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Match(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='match_s')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    man_of_the_match = models.CharField(max_length=200, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(blank=True, null=True)

    class Meta:
        ordering = ['-created_on']
        verbose_name_plural = "Matches"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("match_detail", kwargs={"slug": str(self.slug)})
