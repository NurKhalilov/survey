from django.db import models


class Region(models.Model):
    region_name = models.CharField(max_length=25)
    slug = models.SlugField(max_length=25)

    def __str__(self):
        return self.region_name


class Salesman(models.Model):
    region = models.ForeignKey(Region, related_name='region', on_delete=models.CASCADE)
    name = models.CharField(max_length=35)
    surname = models.CharField(max_length=35)

    class Meta:
        verbose_name = 'Salesman'
        verbose_name_plural = 'Salesmen'

    def __str__(self):
        return f"{self.name} {self.surname}"


class Rating(models.Model):
    RATING_CHOICES = (
        ("a'lo", "A'lo"),
        ("yaxshi", "Yaxshi"),
        ("qoniqarli", "Qoniqarli"),
        ("yomon", "Yomon"),
    )
    salesman = models.ForeignKey(Salesman, related_name='salesman', on_delete=models.CASCADE)
    purchase_price = models.IntegerField(blank=True, default=100000)
    rating = models.CharField(max_length=9, choices=RATING_CHOICES)
    sent_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.salesman.name


class ExtraQuestion(models.Model):
    TYPE_CHOICES = (
        ('checkbox', 'Checkbox'),
        ('radio', 'Radio'),
        ('text', 'Text')
    )
    title = models.TextField()
    is_active = models.BooleanField(default=False)
    question_type = models.CharField(max_length=8, choices=TYPE_CHOICES)

    def __str__(self):
        return self.title

    def get_extraanswers(self):
        return self.extraanswer_set.all()


class ExtraAnswer(models.Model):
    question = models.ForeignKey(ExtraQuestion, on_delete=models.CASCADE)
    answer = models.CharField(max_length=100)

    def __str__(self):
        return self.answer


class Result(models.Model):
    question = models.ForeignKey(ExtraQuestion, related_name='result_question', on_delete=models.CASCADE)
    answer = models.ForeignKey(ExtraAnswer, related_name='result_answer', on_delete=models.CASCADE)
    sent_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question.title
