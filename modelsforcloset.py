class UserProfile(models.Model):
	#This line is required. Links UserProfile to a User model instance.
	user = models.OneToOneField(User)

	#The additional attributes we wish to include.
	picture = models.ImageField(upload_to='profile_images', blank=True)
	bio = models.TextField(blank=True)

	def __unicode__(self):
		return self.user.username

class Category(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(max_length=128, unique=True)
	likes = models.IntegerField(default=0)
	slug = models.SlugField()

class Season(models.Model):
	category = models.ForeignKey(category)
	winter = models.CharField(max_length=128, unique=True)
	spring = models.CharField(max_length=128, unique=True)
	summer = models.CharField(max_length=128, unique=True)
	fall = models.CharField(max_length=128, unique=True)

class ClothingType(models.Model):
	user = models.ForeignKey(User)
	category = models.ForeignKey(Category)
	sweater = models.ImageField(auto_now=True)
	shirt = models.ImageField(auto_now=True)
	pants = models.ImageField(auto_now=True)
	dress = models.ImageField(auto_now=True)
	skirt = models.ImageField(auto_now=True)
	shoes = models.ImageField(auto_now=True)
	underwear = models.ImageField(auto_now=True)
	size = models.CharField(max_length=128, unique=True)
	colors = models.CharField(max_length= 128, unique=True)
	barcode = models.
	price = models.Inegerfield(dafault=0)
	picture = models.ImageField(auto_now=True)
	purchased_at = models.DateTimeField(auto_now=True)

class Accessory(models.Model):
	user = models.ForeignKey(User)
	category = models.ForeignKey(Category)
	earrings = models.ImageField(auto_now=True)
	necklace = models.ImageField(auto_now=True)
	glasses = models.ImageField(auto_now=True)
	rings = models.ImageField(auto_now=True)
	scarf = models.ImageField(auto_now=True)
	hat = models.ImageField(auto_now=True)
	belt = models.ImageField(auto_now=True)