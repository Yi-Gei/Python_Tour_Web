from django.db import models

# Create your models here.

class HotLine(models.Model):
	HLine        = models.CharField('热门线路名称',max_length=200);
	HLId         = models.IntegerField('线路编号(*数字)',default=-1);
	HL_PubDate   = models.DateTimeField('发布时间');
	HL_StartDate = models.DateTimeField('开团时间');
	HL_lp        = models.IntegerField('名额(*可缺省)',default=0); #名额
	HL_Img       = models.ImageField("上传图片",upload_to='photo',null=False,blank=False);
	HL_Type      = models.IntegerField("发布类型",default=0); #特价：0，组团：1，路线：2
	HL_description = models.TextField('简介(*200字以内,可缺省)',max_length=200,null=True,blank=True);

	def __str__(self):
		return self.HLine;


class HotCity(models.Model):
	HCity        = models.CharField('热门线路名称',max_length=200);
	HCId         = models.IntegerField('线路编号(*数字)',default=-1);
	HC_PubDate   = models.DateTimeField('发布时间');
	HC_StartDate = models.DateTimeField('开团时间');
	HC_lp        = models.IntegerField('名额(*可缺省)',default=0); #名额
	HC_Img       = models.ImageField("上传图片",upload_to='photo',null=False,blank=False);
	HC_Type      = models.IntegerField("发布类型",default=0); #特价：0，组团：1，路线：2
	HC_description = models.TextField('简介(*200字以内,可缺省)',max_length=200,null=True,blank=True);
	def __str__(self):
		return self.HCity;

class Group(models.Model):
	Gp           = models.CharField('热门线路名称',max_length=200);
	GpId         = models.IntegerField('线路编号(*数字)',default=-1);
	Gp_PubDate   = models.DateTimeField('发布时间');
	Gp_StartDate = models.DateTimeField('开团时间');
	Gp_lp        = models.IntegerField('名额(*可缺省)',default=0); #名额
	Gp_Img       = models.ImageField("上传图片",upload_to='photo',null=False,blank=False);
	Gp_Type      = models.IntegerField("发布类型",default=0); #特价：0，组团：1，路线：2
	Gp_description = models.TextField('简介(*200字以内,可缺省)',max_length=200,null=True,blank=True);

	def __str__(self):
		return self.Gp;


