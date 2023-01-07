from django.db import models


class Item(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='Название пункта меню',
    )
    slug = models.SlugField(
        max_length=50,
        verbose_name='слаг',
        unique=True,
    )
       
    def __str__(self):
        return self.title


class Menu(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='Название меню',
    )
    items = models.ManyToManyField(
        Item,
        through=('ItemMenu'),
        related_name='items_list'
    )
    submenu = models.ManyToManyField(
        'Menu',
        through=('MenuSub'),
        related_name='sub_menu'
    )
    
    def __str__(self):
        return self.title


class ItemMenu(models.Model):
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        related_name='item'
    )
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        related_name='menu'
    )
    
    def __str__(self):
        return f'{self.menu.title} {self.item.title}'
    
    
class MenuSub(models.Model):
    menu_1 = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        related_name='menu_1'
    )
    menu_2 = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        related_name='menu_2'
    )
    def __str__(self):
        return f'{self.menu_1.title} {self.menu_2.title}'