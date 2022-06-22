from django.db import models
import sklearn
import joblib

# Create your models here.
class Product(models.Model):
    title = models.CharField("Название запчасти",max_length = 200)
    content = models.TextField('Описание',blank = True)
    url = models.SlugField(max_length = 160)
    price = models.FloatField(null=True,blank=True,verbose_name='Стоимость')
    publish = models.DateTimeField(auto_now_add=True,db_index=True,verbose_name='Опубликовано')
    rubric = models.ForeignKey('Rubric',null = True,on_delete=models.PROTECT,verbose_name='Рубрика')
    image = models.ImageField(upload_to='bboard/',blank=True,null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('ad:ad_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])

    class Meta:
        verbose_name = "Название запчасти"
        verbose_name_plural = "Название запчастей"

class Rubric(models.Model):
    name = models.CharField(max_length = 20,db_index = True,verbose_name='Название')
    url = models.SlugField(max_length = 150,unique = True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Рубрика'
        verbose_name_plural ="Рубрики"
        ordering = ['name']

class RatingStar(models.Model):
    value = models.SmallIntegerField("Значение",default = 0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name='Звезда'
        verbose_name_plural ="Звезды"

class Rating(models.Model):
    ip = models.CharField("IP",max_length = 15)
    star = models.ForeignKey(RatingStar,on_delete = models.CASCADE,verbose_name = "звезда")
    product = models.ForeignKey(Product,on_delete = models.CASCADE,verbose_name = "Запчасть")

    def __str__(self):
        return f"{self.star} - {self.product}"

    class Meta:
        verbose_name='Рейтинг'
        verbose_name_plural ="Рейтинги"

class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField("Имя",max_length = 100)
    text = models.TextField("Текст",max_length = 100)
    parent = models.ForeignKey('self',verbose_name = "Родитель", on_delete = models.CASCADE,null = True)
    product = models.ForeignKey(Product,verbose_name="Запчасть",on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.product}"

    class Meta:
        verbose_name='Отзыв'
        verbose_name_plural ="Отзывы"

class Data(models.Model):
    name = models.CharField(max_length=100)
    power = models.PositiveIntegerField()
    drive = models.PositiveIntegerField()
    volume = models.FloatField()
    predictions = models.CharField(max_length=100,blank = True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date"]

    def save(self, *args, **kwargs):
        ml_model = joblib.load("ml_model/ml_cars_model.joblib")
        self.predictions = ml_model.predict([[self.power,self.drive,self.volume]])

        return super().save(*args,*kwargs)

    def __str__(self):
        return self.name
